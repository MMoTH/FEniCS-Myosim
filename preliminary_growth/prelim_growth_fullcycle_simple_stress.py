# @Author: charlesmann
# @Date:   2021-12-28T13:59:41-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-05T13:53:06-05:00

from dolfin import *
import sys
import numpy as np
from methods import load_mesh
from methods import initialize_spaces
from methods import initialize_functions
from methods import create_boundary_conditions
from methods import create_weak_form
from methods import full_cardiac_cycle
from methods import calculate_stimulus_function
from methods import calculate_deviation_function
from methods import calculate_thetas
from methods import save_outputs


input_file = sys.argv[1]

# Load in mesh, mesh file
mesh, f, input_parameters = load_mesh.load_mesh(input_file)

# save reference mesh
# KURTIS CONDENSE THIS INTO FILES DICTIONARY
print "Saving reference mesh"
File('./fc_output/reference_mesh.pvd') << mesh
total_sol_file = File('./fc_output/total_displacement.pvd')
p_f_file = File('./fc_output/passive_force.pvd')
dev_file = File('./fc_output/deviation.pvd')
theta_file = File('./fc_output/theta_ff.pvd')
fdataPV = open('./fc_output/PV_.txt', "w", 0)

print "Setting up function spaces"
# Set up elements and spaces for growth
fcn_spaces = initialize_spaces.initialize_spaces(mesh)

print "Initializing functions"
# Create functions, Fg (need f to load in fiber functions)
# This will include some other things besides strict fenics functions (like an expression, and mesh functions)
functions = initialize_functions.initialize_functions(mesh, fcn_spaces, f, input_parameters)

print "Creating boundary conditions"
# Create boundary conditions
bcs, functions = create_boundary_conditions.create_boundary_conditions(mesh, fcn_spaces, functions)

print "Initializing weak form"
# Create weak form
Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions = create_weak_form.create_weak_form(mesh, fcn_spaces, functions)

# Get reference volume
ref_vol = uflforms.LVcavityvol()
functions["LVCavityvol"].vol = ref_vol

# Load to ED, get stimulus, use as set point
#functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, 0, total_sol_file, p_f_file)
# Try to implement a full cardiac cycle, stimulus will be calculated within
functions = full_cardiac_cycle.full_cycle()

# Calculate the stimulus value. Without any perturbation, the stimulus value is the set point
#functions["set_point"] = calculate_stimulus_function.calculate_stimulus_function(fcn_spaces,functions,uflforms)

# Unload the ventricle so we grow from the reference
functions = diastolic_unloading.diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, ref_vol,0, total_sol_file, p_f_file)


# To force some growth, arbitrarily increasing the set point. In future, perturbations will come from somewhere else
functions["set_point"] *= Constant(0.8)

# While deviation < tol:
#    inflate to ED
#    calculate stimulus
#    calculate deviation
#    calculate theta_ff, theta_ss, theta_nn
#    with Fg updated, solve weak form
#    use solution from above to move mesh to new grown state

# Set up a simulation state class/dictionary. If we are going to grow in
# the middle of cardiac simulations and continue on, we need to be able to
# save things like windkessel volumes and pressures
sim_state = 


tol = 100
growth_iter_counter = 1
print "tolerance =",tol
print "current maximum deviation =",np.amax(functions["deviation"].vector().get_local())
print "growth iteration ",growth_iter_counter
stop
while np.average(functions["deviation"].vector().get_local()) > tol:

    print "within while loop"
    print "CURRENT AVERAGE DEVIATION =",np.average(functions["deviation"].vector().get_local())

    # Reset solution to zero
    functions["w"].vector()[:] = 0.0

    # Load to ED
    #functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, growth_iter_counter, total_sol_file, p_f_file)
    # Full cycle here, including stimulus_temp


    # Calculate stimulus
    # Note! If functions["stimulus"] is used here, Fg will get prematurely updated, and there will be non-convergence
    # when trying to unload back to the reference
    #functions["stimulus_temp"] = calculate_stimulus_function.calculate_stimulus_function(fcn_spaces,functions,uflforms)

    # Unload back to reference
    functions = diastolic_unloading.diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, ref_vol, growth_iter_counter, total_sol_file, p_f_file)

    # Now, assign the stimulus function and proceed.
    # EDIT TO INCLUDE S0, N0
    functions["stimulus"].assign(functions["stimulus_temp"])

    # Calculate deviation
    # EDIT TO INCLUDE S0, N0
    functions["deviation"] = calculate_deviation_function.calculate_deviation_function(fcn_spaces,functions)

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
    save_outputs.save(total_sol_file, p_f_file, theta_file, dev_file, mesh, functions, fcn_spaces, uflforms, fdataPV, growth_iter_counter)

    # Reset thetas so Fg is identity
    functions["theta_ff"].vector()[:] = 1.0
    functions["theta_ss"].vector()[:] = 1.0
    functions["theta_nn"].vector()[:] = 1.0

    # Now that growth has occurred (with LV cavity volume unconstrained), calculate LV cavity volume
    # and appropriately set the expression:
    functions["LVCavityvol"].vol = uflforms.LVcavityvol()
    ref_vol = uflforms.LVcavityvol()

    growth_iter_counter += 1


print "done"
