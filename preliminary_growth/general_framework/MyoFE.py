# @Author: charlesmann
# @Date:   2022-01-10T16:46:33-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T13:51:36-05:00

from dolfin import *
import sys
import numpy as np
from methods import load_mesh
from methods import OutputData
from methods import SimulationState
from methods import initialize_spaces
from methods import initialize_functions
from methods import create_boundary_conditions
from methods import create_weak_form
from methods import diastolic_unloading
from methods import diastolic_filling
from methods import CirculatorySystem
from methods import calculate_stimulus_function
from methods import calculate_deviation_function
from methods import calculate_thetas
from methods import grow_mesh
from methods import save_outputs


# Attempting a more general framework that works in the absence of growth
input_file = sys.argv[1]

# Load in mesh, instruction file
#------------------------
mesh, f, input_parameters = load_mesh.load_mesh(input_file)

# communicator to run in parallel
# it appears something weird happens when trying to work directly with function
# vectors in parallel. Will need to investigate. Seems to run normal simulation
# (without myosim) fine
comm = mesh.mpi_comm()


# Let's go ahead and figure out if growth will be occurring
#----------------------------------------------------------
if "growth_and_remodeling" in input_parameters.keys():

    if(MPI.rank(comm) == 0):

        print "Growth parameters detected. Setting growth flag to 1"

    # Growth is desired. Note, Fg and all quantities will still be initialized. It just won't be updated
    growth_flag = 1
    tol = input_parameters["growth_and_remodeling"]["tolerance"][0]

else:

    growth_flag = 0

# Output stuff, need to clean this up
#------------------------------------
output_object = OutputData.OutputData(input_parameters["output_options"])
output_object.ref_mesh_file.save_pvd_object(mesh)


# Set up elements and function spaces
#------------------------------------
if(MPI.rank(comm) == 0):
    print "Setting up function spaces"
fcn_spaces = initialize_spaces.initialize_spaces(mesh)


# Create functions, Fg (need f to load in fiber functions)
# This will include some other things besides strict fenics functions (like an expression, and mesh functions)
#-------------------------------------------------------------------------------------------------------------
if(MPI.rank(comm) == 0):
    print "Initializing functions"
functions = initialize_functions.initialize_functions(mesh, fcn_spaces, f, input_parameters)


# Set up an initial simulation state
# Initialized from instruction file, updated after growth
#---------------------------------------------------------
sim_state = SimulationState.SimulationState(input_parameters)


# Create boundary conditions
#----------------------------
if(MPI.rank(comm) == 0):
    print "Creating boundary conditions"
bcs, functions = create_boundary_conditions.create_boundary_conditions(mesh, fcn_spaces, functions)


# Create weak form
#-----------------
if(MPI.rank(comm) == 0):
    print "Initializing weak form"
Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive = create_weak_form.create_weak_form(mesh, fcn_spaces, functions)


# Get reference volume
ref_vol = uflforms.LVcavityvol()
functions["LVCavityvol"].vol = ref_vol

# Start setting up the stuff for the time loop
#---------------------------------------------
# Set up time step
num_cycles_to_steady_state = 1
no_of_time_steps = int(sim_state.sim_duration/sim_state.timestep)
t = np.linspace(sim_state.timestep,sim_state.sim_duration,no_of_time_steps) # does this work for growth?


# Initialize calcium object (eventually)


# Initialize windkessel
# Going to save pressure and volume of LV
Pcav_array = np.zeros(no_of_time_steps)
LVcav_array = np.zeros(no_of_time_steps)
windkessel_params = sim_state.wk_params
circ_system = CirculatorySystem.CirculatorySystem(windkessel_params)

# solution function
w = functions["w"]



# Initialize half-sarcomere object (eventually), for now load in cb_force
cb_force_loaded = np.load('/home/fenics/shared/preliminary_growth/general_framework/prescribed_cb_force_refined.npy')
cb_force = np.nan*np.ones(int(sim_state.cardiac_period/sim_state.timestep))
cb_force[0:np.shape(cb_force_loaded)[0]] = cb_force_loaded
cb_force[np.shape(cb_force_loaded)[0]:] = cb_force_loaded[-1]
cb_force = np.tile(cb_force,sim_state.max_cycles)

sim_state.termination_flag = False
growth_iter_counter = 0 # only updated if there's growth




#      Diastolic loading
# diastolic loading to a prescribed EDV (keeping it the same as the last
# cycle from previous simulation, or the initial prescribed. Assumption is
# the total blood volume is constant)
functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, sim_state.edv, output_object, sim_state.reference_load_steps)


#      "Load" Myosim

while sim_state.termination_flag == False:

    #   Go forward in time, get stimulus if growth is desired
    for l in np.arange(no_of_time_steps):


        if(MPI.rank(comm) == 0):
            print "Current time step: ", t[l]

        # Update Calcium
        #---------------


        # Update windkessel
        #------------------
        #update wk compartments, return end_diastole or end_systole

        # Get current cavity pressure
        p_cav = uflforms.LVcavitypressure()

        # Get current cavity volume using divergence theorem
        V_cav = uflforms.LVcavityvol()
        if(MPI.rank(comm) == 0):
            print "forms vol before solve",V_cav

        # pass these into the windkessel model
        circ_dict = circ_system.update_compartments(p_cav,V_cav,sim_state.timestep)

        # Assign volume constraint expression to volume calculated by windkessel
        functions["LVCavityvol"].vol = circ_dict["V_cav"]
        LVcav_array[l] = circ_dict["V_cav"]
        end_systole = circ_dict["end_systole"]
        end_diastole = circ_dict["end_diastole"]
        LVcav_array[l] = circ_dict["V_cav"]
        Pcav_array[l] = p_cav*0.0075

        # Now print out volumes, pressures
        if(MPI.rank(comm) == 0):
            print >>output_object.fdataPV, t[l], circ_dict["p_cav"]*0.0075 , circ_dict["Part"]*.0075, circ_dict["Pven"]*.0075, circ_dict["V_cav"], circ_dict["V_ven"], circ_dict["V_art"]

    #       Update Myosim/cb_force expression
        #---------------------------------
        functions["cbforce"].f = 2.2*cb_force[l]

    #       Solve cardiac mechanics weak form
        #--------------------------------
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    #       Update quantities (mostly for myosim)
        #------------------------------------


    #       Hard coding stimuli for now
        if growth_flag > 0:
            # check to calculate stimulus

            end_of_cycle = t[l]%sim_state.cardiac_period

            if(MPI.rank(comm) == 0):
                print "end of cycle?", end_of_cycle == 0

            if circ_dict["end_systole"]:

                if growth_iter_counter < 1:

                    # first cycle, set as set-point
                    functions["set_point_ff"],functions["set_point_ss"],functions["set_point_nn"] = calculate_stimulus_function.calculate_stimulus_function(fcn_spaces, functions, uflforms, Pactive)
                    # set stimulus to be equal to the set point. No perturbations yet
                    functions["stimulus_ff_temp"].vector()[:] = 1.0
                    functions["stimulus_ss_temp"].assign(functions["set_point_ss"])
                    functions["stimulus_nn_temp"].assign(functions["set_point_nn"])

                    # To trigger growth, forcing set point down
                    functions["set_point_ss"] *= Constant(0.8)
                    functions["set_point_nn"] *= Constant(0.8)

                else:
                    # set stimulus
                    functions["stimulus_ff_temp"],functions["stimulus_ss_temp"],functions["stimulus_nn_temp"] = calculate_stimulus_function.calculate_stimulus_function(fcn_spaces, functions, uflforms, Pactive)


           #if end-diastole:
    #               calculate eccentric growth stimulus
    #
            if end_of_cycle == 0:
                print "reached end of cardiac cycle"
    #               # for now, termination condition for growth is average deviation < tol
                if np.average(functions["deviation_ss"].vector().get_local()) > tol:
                    # grow

                    functions, mesh, growth_iter_counter = grow_mesh.grow_mesh(fcn_spaces, functions, uflforms, Ftotal, Jac, Ftotal_growth, Jac_growth, bcs, ref_vol, output_object, sim_state, mesh, input_parameters, growth_iter_counter)

                    # Try creating the weak form again. Something isn't updating correctly
                    Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive = create_weak_form.create_weak_form(mesh, fcn_spaces, functions)

                    # Now that growth has occurred (with LV cavity volume unconstrained), calculate LV cavity volume
                    # and appropriately set the expression:
                    ref_vol = uflforms.LVcavityvol()
                    #functions["LVCavityvol"].vol = ref_vol

                    # Reset solution to zero
                    functions["w"].vector()[:] = 0.0

                    # Reload to EDV
                    functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, sim_state.edv, output_object, sim_state.reference_load_steps)



                else:
                    if(MPI.rank(comm) == 0):
                        print "Average deviation within tolerance. Finished growing"
                    # within tolerance, growth stopping
                    sim_state.termination_flag = True
                    break




    #   save outputs
        output_object.total_sol_file.save_pvd_object(w.sub(0))

        if l+1 ==  no_of_time_steps: # either simulated desired number of cycles or growth has converged
            if(MPI.rank(comm) == 0):
                print "Reached end of simulation duration"
            sim_state.termination_flag = True
