# @Author: charlesmann
# @Date:   2022-01-10T16:46:33-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T17:28:28-05:00

from dolfin import *
import sys
#sys.path.append('/home/fenics/shared/preliminary_growth/general_framework/methods/')
sys.path.append('/mnt/home/f0101140/Desktop/test_myosim_growth/FEniCS-Myosim/preliminary_growth/general_framework/methods/')
import numpy as np
from methods import load_mesh
from methods import OutputData
from methods import SimulationState
from methods import initialize_spaces
from methods import initialize_functions
from methods import create_boundary_conditions
from methods import create_weak_form
import Python_MyoSim.half_sarcomere.half_sarcomere as half_sarcomere
import Python_MyoSim.half_sarcomere.implement as implement
from cell_ion_module import cell_ion_driver
from methods import diastolic_unloading
from methods import diastolic_filling
from methods import CirculatorySystem
from methods import calculate_stimulus_function
from methods import calculate_deviation_function
from methods import calculate_thetas
from methods import grow_mesh
from methods import save_outputs
import copy

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


# Creating a dictionary "arrays_and_values" to hold some of the more miscellaneous things
# Things needed for other functions will be put into this dictionary
arrays_and_values = {}

# We need to set up some of the Myosim stuff to correctly define some of the funtions
# and function spaces. Let's go ahead and get it all from the instruction file
arrays_and_values["k_myo_damp"] = 0.0
hs_params = input_parameters["myosim_parameters"]

arrays_and_values["filament_compliance_factor"] = hs_params["myofilament_parameters"]["filament_compliance_factor"][0]
arrays_and_values["no_of_states"] = hs_params["myofilament_parameters"]["num_states"][0]
no_of_attached_states = hs_params["myofilament_parameters"]["num_attached_states"][0]
no_of_detached_states = arrays_and_values["no_of_states"]-no_of_attached_states
no_of_transitions = hs_params["myofilament_parameters"]["num_transitions"][0]
arrays_and_values["state_attached"] = hs_params["myofilament_parameters"]["state_attached"][0]
arrays_and_values["cb_extensions"] = hs_params["myofilament_parameters"]["cb_extensions"][0]
arrays_and_values["k_cb_multiplier"] = hs_params["myofilament_parameters"]["k_cb_multiplier"][0]
arrays_and_values["k_cb_pos"] = hs_params["myofilament_parameters"]["k_cb_pos"][0]
arrays_and_values["k_cb_neg"] = hs_params["myofilament_parameters"]["k_cb_neg"][0]
cb_number_density = hs_params["cb_number_density"][0]
arrays_and_values["alpha_value"] = hs_params["myofilament_parameters"]["alpha"][0]
x_bin_min = hs_params["myofilament_parameters"]["bin_min"][0]
x_bin_max = hs_params["myofilament_parameters"]["bin_max"][0]
x_bin_increment = hs_params["myofilament_parameters"]["bin_width"][0]
arrays_and_values["xfiber_fraction"] = hs_params["myofilament_parameters"]["xfiber_fraction"][0]

# Create x interval for cross-bridges
arrays_and_values["xx"] = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)
# Define number of intervals cross-bridges are defined over
arrays_and_values["no_of_x_bins"] = np.shape(arrays_and_values["xx"])[0]
# Define the length of the populations vector
n_array_length = no_of_attached_states * arrays_and_values["no_of_x_bins"] + no_of_detached_states + 2

# need to generalize this
if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "3state_with_SRX":
    arrays_and_values["n_vector_indices"] = [[0,0], [1,1], [2,2+arrays_and_values["no_of_x_bins"]-1]]
if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "4state_with_SRX":
    arrays_and_values["n_vector_indices"] = [[0,0], [1,1], [2,2+arrays_and_values["no_of_x_bins"]-1], [(2+arrays_and_values["no_of_x_bins"]), (2+arrays_and_values["no_of_x_bins"])+arrays_and_values["no_of_x_bins"]-1]]



# Set up elements and function spaces
#------------------------------------
if(MPI.rank(comm) == 0):
    print "Setting up function spaces"
fcn_spaces, no_of_int_points = initialize_spaces.initialize_spaces(mesh, n_array_length)


# Doing this allows us to introduce heterogeneity in the half-sarcomere parameters
hs_params_list = [{}]*no_of_int_points
for jj in np.arange(np.shape(hs_params_list)[0]):
    hs_params_list[jj] = copy.deepcopy(hs_params) # because this is a copy, everything is initialized


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
Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive, arrays_and_values = create_weak_form.create_weak_form(mesh, fcn_spaces, functions, arrays_and_values)


# Get reference volume
ref_vol = uflforms.LVcavityvol()
functions["LVCavityvol"].vol = ref_vol

# Start setting up the stuff for the time loop
#---------------------------------------------
# Set up time step
num_cycles_to_steady_state = 1
no_of_time_steps = int(sim_state.sim_duration/sim_state.timestep)
t = np.linspace(sim_state.timestep,sim_state.sim_duration,no_of_time_steps) # does this work for growth?

arrays_and_values["temp_overlap"] = np.zeros((no_of_int_points))
arrays_and_values["y_vec_array_new"] = np.zeros(((no_of_int_points)*n_array_length))
arrays_and_values["j3_fluxes"] = np.zeros((no_of_int_points,no_of_time_steps))
arrays_and_values["j4_fluxes"] = np.zeros((no_of_int_points,no_of_time_steps))
arrays_and_values["j7_fluxes"] = np.zeros((no_of_int_points,no_of_time_steps))
arrays_and_values["y_interp"] = np.zeros((no_of_int_points)*n_array_length)
arrays_and_values["calcium"] = np.zeros(no_of_time_steps)
arrays_and_values["delta_hsl_array"] = np.zeros(no_of_int_points)

# Initialize calcium object (eventually)
# Initialize cell ion module
cell_ion_params = input_parameters["electrophys_parameters"]["cell_ion_parameters"]
cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params,sim_state.timestep,sim_state.sim_duration)

# Initialize calcium concentration from cell_ion module
arrays_and_values["calcium"][0] = cell_ion.calculate_concentrations(sim_state.timestep,0,0)

# Initialize windkessel
# Going to save pressure and volume of LV
Pcav_array = np.zeros(no_of_time_steps)
LVcav_array = np.zeros(no_of_time_steps)
windkessel_params = sim_state.wk_params
circ_system = CirculatorySystem.CirculatorySystem(windkessel_params)

# solution function
w = functions["w"]



# Initialize half-sarcomere object
# -----------------------------------------------------------------------
# create lists of dictionaries that hold parameters for each gauss point
# These will remain scalars for now. Each parameter could be set up on the
# Quad space, but that would require re-working myosim to be more FEniCS friendly.
# Don't know if it's worth doing.

arrays_and_values["y_vec_array"] = functions["y_vec"].vector().get_local()[:]

# Initialize half-sarcomere class. Methods used to calculate cross-bridges
# at gauss points
hs = half_sarcomere.half_sarcomere(hs_params,1)

# putting this here to show that it exists
#hs_params_list,dolfin_functions = assign_params.assign_heterogeneous_params(sim_params,hs_params,hs_params_list,dolfin_functions,geo_options,no_of_int_points,no_of_cells)



"""cb_force_loaded = np.load('/home/fenics/shared/preliminary_growth/general_framework/prescribed_cb_force_refined.npy')
cb_force = np.nan*np.ones(int(sim_state.cardiac_period/sim_state.timestep))
cb_force[0:np.shape(cb_force_loaded)[0]] = cb_force_loaded
cb_force[np.shape(cb_force_loaded)[0]:] = cb_force_loaded[-1]
cb_force = np.tile(cb_force,sim_state.max_cycles)"""


sim_state.termination_flag = False
growth_iter_counter = 0 # only updated if there's growth




#      Diastolic loading
# diastolic loading to a prescribed EDV (keeping it the same as the last
# cycle from previous simulation, or the initial prescribed. Assumption is
# the total blood volume is constant)
functions, arrays_and_values = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, sim_state.edv, output_object, sim_state.reference_load_steps, arrays_and_values)


#      "Load" Myosim

while sim_state.termination_flag == False:

    #   Go forward in time, get stimulus if growth is desired
    for l in np.arange(no_of_time_steps):


        if(MPI.rank(comm) == 0):
            print "Current time step: ", t[l]

        # Update Calcium
        #---------------
        arrays_and_values["calcium"][l] = cell_ion.calculate_concentrations(sim_state.timestep,t[l],l)

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


        # Quick hack
        if l == 0:
            overlap_counter = 1
        else:
            overlap_counter = l

    #   Update Myosim/cb_force expression
        #---------------------------------
        #functions["cbforce"].f = 2.2*cb_force[l]
        # At each gauss point, solve for cross-bridge distributions using myosim
        print "calling myosim"
        for mm in np.arange(no_of_int_points):
            arrays_and_values["temp_overlap"][mm], arrays_and_values["y_interp"][mm*n_array_length:(mm+1)*n_array_length], \
               arrays_and_values["y_vec_array_new"][mm*n_array_length:(mm+1)*n_array_length] = implement.update_simulation(hs,  \
               sim_state.timestep, arrays_and_values["delta_hsl_array"][mm], arrays_and_values["hsl_array"][mm], arrays_and_values["y_vec_array"][mm*n_array_length:(mm+1)*n_array_length], \
               arrays_and_values["p_f_array"][mm], arrays_and_values["cb_f_array"][mm], arrays_and_values["calcium"][l], n_array_length, t,hs_params_list[mm])

            temp_flux_dict, temp_rate_dict = implement.return_rates_fenics(hs)
            arrays_and_values["j3_fluxes"][mm,l] = sum(temp_flux_dict["J3"])
            arrays_and_values["j4_fluxes"][mm,l] = sum(temp_flux_dict["J4"])
            if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "4state_with_SRX":
              arrays_and_values["j7_fluxes"][mm,l] = sum(temp_flux_dict["J7"])

        # Update the populations
        arrays_and_values["y_vec_array"] = arrays_and_values["y_vec_array_new"] # for Myosim

        # Update the population function for fenics
        functions["y_vec"].vector()[:] = arrays_and_values["y_vec_array"] # for PDE

        # Update the array for myosim
        arrays_and_values["hsl_array_old"] = arrays_and_values["hsl_array"]

        # Update the hsl_old function for fenics
        functions["hsl_old"].vector()[:] = arrays_and_values["hsl_array_old"][:]

    #   Solve cardiac mechanics weak form
        #--------------------------------
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    #   Update quantities (mostly for myosim)
        #------------------------------------
        arrays_and_values["cb_f_array"][:] = project(functions["cb_force"], fcn_spaces["quadrature_space"]).vector().get_local()[:]
        functions["hsl_old"].vector()[:] = project(functions["hsl"], fcn_spaces["quadrature_space"]).vector().get_local()[:] # for PDE
        functions["pseudo_old"].vector()[:] = project(functions["pseudo_alpha"], fcn_spaces["quadrature_space"]).vector().get_local()[:]
        arrays_and_values["hsl_array"] = project(functions["hsl"], fcn_spaces["quadrature_space"]).vector().get_local()[:]           # for Myosim
        arrays_and_values["delta_hsl_array"] = project(sqrt(dot(functions["f0"], uflforms.Cmat()*functions["f0"]))*functions["hsl0"], fcn_spaces["quadrature_space"]).vector().get_local()[:] - arrays_and_values["hsl_array_old"] # for Myosim

        temp_DG = project(functions["Sff"], FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, fcn_spaces["quadrature_space"])
        arrays_and_values["p_f_array"] = p_f.vector().get_local()[:]

        for ii in range(np.shape(arrays_and_values["hsl_array"])[0]):
            if arrays_and_values["p_f_array"][ii] < 0.0:
                arrays_and_values["p_f_array"][ii] = 0.0

    #   Hard coding stimuli for now
        #--------------------------
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
                    Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive, arrays_and_values = create_weak_form.create_weak_form(mesh, fcn_spaces, functions, arrays_and_values)

                    # Now that growth has occurred (with LV cavity volume unconstrained), calculate LV cavity volume
                    # and appropriately set the expression:
                    ref_vol = uflforms.LVcavityvol()
                    functions["LVCavityvol"].vol = ref_vol

                    # Reset solution to zero
                    functions["w"].vector()[:] = 0.0

                    # Reload to EDV
                    functions, arrays_and_values = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, sim_state.edv, output_object, sim_state.reference_load_steps, arrays_and_values)



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
