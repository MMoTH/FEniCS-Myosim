# @Author: charlesmann
# @Date:   2021-12-28T13:59:41-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T09:55:18-05:00

from dolfin import *
import sys
import numpy as np
from methods import load_mesh
from methods import simulation_state
from methods import initialize_spaces
from methods import initialize_functions
from methods import create_boundary_conditions
from methods import create_weak_form
from methods import full_cardiac_cycle
from methods import diastolic_unloading
from methods import calculate_stimulus_function
from methods import calculate_deviation_function
from methods import calculate_thetas
from methods import save_outputs


input_file = sys.argv[1]
load_flag = sys.argv[2]

print "load flag",load_flag

# Load in mesh, mesh file
mesh, f, input_parameters = load_mesh.load_mesh(input_file)

# communicator to run in parallel
comm = mesh.mpi_comm()


# save reference mesh
# KURTIS CONDENSE THIS INTO FILES DICTIONARY
print "Saving reference mesh"
File('./fc_output/reference_mesh.pvd') << mesh
total_sol_file = File('./fc_output/total_displacement.pvd')
p_f_file = File('./fc_output/passive_force.pvd')
dev_file = File('./fc_output/deviation.pvd')
theta_file = File('./fc_output/theta_ff.pvd')
dev_txt_file = open('./fc_output/average_deviation.txt','w')



print "Setting up function spaces"
# Set up elements and spaces for growth
fcn_spaces = initialize_spaces.initialize_spaces(mesh)

print "Initializing functions"
# Create functions, Fg (need f to load in fiber functions)
# This will include some other things besides strict fenics functions (like an expression, and mesh functions)
functions = initialize_functions.initialize_functions(mesh, fcn_spaces, f, input_parameters)

# Set up an initial simulation state
# Initialized from instruction file, updated after growth
sim_state = simulation_state.simulation_state(input_parameters)

print "Creating boundary conditions"
# Create boundary conditions
bcs, functions = create_boundary_conditions.create_boundary_conditions(mesh, fcn_spaces, functions)

print "Initializing weak form"
# Create weak form
Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive = create_weak_form.create_weak_form(mesh, fcn_spaces, functions)

# Get reference volume
ref_vol = uflforms.LVcavityvol()
functions["LVCavityvol"].vol = ref_vol

# Skipping this
print "check load flag", int(load_flag) >0
if int(load_flag) > 0:
    print "loading stimulus functions"
    stim_ff_array = np.load('stim_ff_array.npy')
    stim_ss_array = np.load('stim_ss_array.npy')
    stim_nn_array = np.load('stim_nn_array.npy')

    functions["set_point_ff"].vector()[:] = stim_ff_array
    # can't have set point of zero
    functions["set_point_ff"].vector()[:] = 1.0
    functions["set_point_ss"].vector()[:] = stim_ss_array
    functions["set_point_nn"].vector()[:] = stim_nn_array

    functions["stimulus_ff"].vector()[:] = stim_ff_array
    # force stimulus_ff to be 1.0, so deviation is zero
    functions["stimulus_ff"].vector()[:] = 1.0
    functions["stimulus_ss"].vector()[:] = stim_ss_array
    functions["stimulus_nn"].vector()[:] = stim_nn_array

else:

    # Load to ED, get stimulus, use as set point
    #functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, 0, total_sol_file, p_f_file)
    # Try to implement a full cardiac cycle, stimulus will be calculated within
    print "initial cycle"
    functions, functions["set_point_ff"], functions["set_point_ss"], functions["set_point_nn"] = full_cardiac_cycle.full_cycle(sim_state, fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, Pactive, comm, total_sol_file, p_f_file,0)

    # Go ahead and set the stimulus functions here before changing the set point
    functions["stimulus_ff"].assign(functions["set_point_ff"])
    functions["stimulus_ss"].assign(functions["set_point_ss"])
    functions["stimulus_nn"].assign(functions["set_point_nn"])

    # To save time for debugging, saving these stimulus functions
    stim_ff_array = functions["stimulus_ff"].vector().get_local()
    stim_ss_array = functions["stimulus_ss"].vector().get_local()
    stim_nn_array = functions["stimulus_nn"].vector().get_local()

    np.save("stim_ff_array.npy",stim_ff_array)
    np.save("stim_ss_array.npy",stim_ss_array)
    np.save("stim_nn_array.npy",stim_nn_array)

    # Unload the ventricle so we grow from the reference
    functions = diastolic_unloading.diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, ref_vol,0, total_sol_file, p_f_file)


# To force some growth, arbitrarily increasing the set point. In future, perturbations will come from somewhere else
#functions["set_point_ff"] *= Constant(0.8)
functions["set_point_ss"] *= Constant(0.8)
functions["set_point_nn"] *= Constant(0.8)

# While deviation < tol:
#    inflate to ED
#    calculate stimulus
#    calculate deviation
#    calculate theta_ff, theta_ss, theta_nn
#    with Fg updated, solve weak form
#    use solution from above to move mesh to new grown state



tol = 100
growth_iter_counter = 1
print "tolerance =",tol
print "current maximum deviation =",np.amax(functions["deviation_ss"].vector().get_local())
print "growth iteration ",growth_iter_counter

while np.average(functions["deviation_ss"].vector().get_local()) > tol:

    print "within while loop"
    print "CURRENT AVERAGE DEVIATION =",np.average(functions["deviation_ss"].vector().get_local())

    # Calculate deviation
    functions = calculate_deviation_function.calculate_deviation_function(fcn_spaces,functions)

    print "deviation_ff",functions["deviation_ff"].vector().get_local()

    # Calculate thetas
    functions = calculate_thetas.calculate_thetas(fcn_spaces,functions,input_parameters)

    # Move this to separate files/functions, but test here
    #-----------------------------------------------------
    # Solve a new weak form using a pressure boundary condition on the endo.
    # At this point, since we are back to the reference configuration, F = I,
    # and Fg has been calculated (no longer the identity in material coordinates).
    # Thus since Fe = F*inv(Fg), and stresses are calculated from Fe, a stress
    # state has been induced. Solving this weak form gives the displacement for
    # near zero stresses (no pressure on endo or epi, so weak form becomes
    # stress + rigid body constraint = 0. I think constraining LV volume causes non-convergence
    # in the case of non-uniform growth/lots of growth

    solve(Ftotal_growth == 0, functions["w"], bcs, J = Jac_growth, form_compiler_parameters={"representation":"uflacs"})

    (u,p,pendo,c11)   = split(functions["w"])

    # Move mesh to relieve residual stress
    # We need to project u which is in CG2 to CG1 to move the nodes of the tetrahedral mesh
    ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))

    # Save some outputs
    save_outputs.save(total_sol_file, p_f_file, theta_file, dev_file, mesh, functions, fcn_spaces, uflforms, growth_iter_counter)

    # Reset thetas so Fg is identity
    functions["theta_ff"].vector()[:] = 1.0
    functions["theta_ss"].vector()[:] = 1.0
    functions["theta_nn"].vector()[:] = 1.0

    # Try creating the weak form again. Something isn't updating correctly
    Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive = create_weak_form.create_weak_form(mesh, fcn_spaces, functions)

    # Now that growth has occurred (with LV cavity volume unconstrained), calculate LV cavity volume
    # and appropriately set the expression:
    ref_vol = uflforms.LVcavityvol()
    #functions["LVCavityvol"].vol = ref_vol

    # Reset solution to zero
    functions["w"].vector()[:] = 0.0


    print "uflforms",uflforms.LVcavityvol()
    # Simulate a full cycle again
    functions, functions["stimulus_ff"], functions["stimulus_ss"], functions["stimulus_nn"] = full_cardiac_cycle.full_cycle(sim_state, fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, Pactive, comm, total_sol_file, p_f_file,growth_iter_counter)


    # Calculate stimulus
    # Note! If functions["stimulus"] is used here, Fg will get prematurely updated, and there will be non-convergence
    # when trying to unload back to the reference
    #functions["stimulus_temp"] = calculate_stimulus_function.calculate_stimulus_function(fcn_spaces,functions,uflforms)

    # Unload back to reference
    functions = diastolic_unloading.diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, ref_vol, growth_iter_counter, total_sol_file, p_f_file)

    # Now, assign the stimulus function and proceed.
    # EDIT TO INCLUDE S0, N0
    #functions["stimulus"].assign(functions["stimulus_temp"])

    growth_iter_counter += 1

    print >> dev_txt_file, np.average(functions["deviation_ss"].vector().get_local())




print "done"
