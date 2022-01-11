# @Author: charlesmann
# @Date:   2022-01-05T12:39:33-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-10T20:56:53-05:00
from dolfin import *
from methods import diastolic_filling
from methods import circulatory_system
import numpy as np
import os


def full_cycle(sim_state,fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, Pactive, comm, total_sol_file, p_f_file, growth_iter):

    # initialize things from the simulation state
    edv = sim_state.edv
    sim_timestep = sim_state.timestep
    print "time step", sim_timestep
    sim_duration = sim_state.duration
    no_of_time_steps = int(sim_duration/sim_timestep)
    t = np.linspace(0,sim_duration,no_of_time_steps)


    # checking volumes
    temp_vol = uflforms.LVcavityvol()
    functions["LVCavityvol"].vol = temp_vol
    print "expr",functions["LVCavityvol"].vol

    #ref_vol = uflforms.LVcavityvol()
    #functions["LVCavityvol"].vol = ref_vol


    # PV file
    if (MPI.rank(comm)==0):
        if growth_iter < 1:
            os.mkdir("/home/fenics/shared/preliminary_growth/test_concentric_fullcycle/fc_output/iter_"+str(growth_iter))
        fdataPV = open("/home/fenics/shared/preliminary_growth/test_concentric_fullcycle/fc_output/iter_"+str(growth_iter)+"/"+"PV_.txt", "w+", 0)


    # Initialize return objects
    temp_stim_ff = Function(fcn_spaces["stimulusFS"])
    temp_stim_ss = Function(fcn_spaces["stimulusFS"])
    temp_stim_nn = Function(fcn_spaces["stimulusFS"])

    # Loading in a custom cb force
    cb_force_loaded = np.load('/home/fenics/shared/preliminary_growth/test_concentric_fullcycle/prescribed_cb_force_refined.npy')
    cb_force = np.nan*np.ones(no_of_time_steps)
    cb_force[0:np.shape(cb_force_loaded)[0]] = cb_force_loaded
    cb_force[np.shape(cb_force_loaded)[0]:] = cb_force_loaded[-1]
    np.save('./fc_output/loaded_cbforce.npy',cb_force)

    # Going to save pressure and volume of LV
    Pcav_array = np.zeros(no_of_time_steps)
    LVcav_array = np.zeros(no_of_time_steps)


    # solution function
    w = functions["w"]

    # initialize circulatory system
    windkessel_params = sim_state.wk_params
    circ_system = circulatory_system.circulatory_system(windkessel_params)

    # diastolic loading to a prescribed EDV (keeping it the same as the last
    # cycle from previous simulation, or the initial prescribed. Assumption is
    # the total blood volume is constant)
    functions = diastolic_filling.diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, edv, 0, total_sol_file, p_f_file)

    # cycle through time
    # Right now, assuming constant heart rate and running for 5 cycles
    for l in np.arange(no_of_time_steps):

    #   update wk compartments, return end_diastole or end_systole
        # Get current cavity pressure
        p_cav = uflforms.LVcavitypressure()

        # Get current cavity volume using divergence theorem
        V_cav = uflforms.LVcavityvol()
        print "forms vol before solve",V_cav

        # pass these into the windkessel model
        circ_dict = circ_system.update_compartments(p_cav,V_cav,sim_timestep)

        # Assign volume constraint expression to volume calculated by windkessel
        functions["LVCavityvol"].vol = circ_dict["V_cav"]
        LVcav_array[l] = circ_dict["V_cav"]
        end_systole = circ_dict["end_systole"]
        end_diastole = circ_dict["end_diastole"]
        #LVCavityvol.vol = V_cav
        LVcav_array[l] = circ_dict["V_cav"]
        Pcav_array[l] = p_cav*0.0075

        # Now print out volumes, pressures
        if(MPI.rank(comm) == 0):
            print >>fdataPV, t[l], circ_dict["p_cav"]*0.0075 , circ_dict["Part"]*.0075, circ_dict["Pven"]*.0075, circ_dict["V_cav"], circ_dict["V_ven"], circ_dict["V_art"]

    #   update active stress
        functions["cbforce"].f = 2.2*cb_force[l]

    #   solve weak form
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        # After solving, check current LV volume and constraint volume
        print "LV vol expression,", functions["LVCavityvol"].vol
        print "Actual calculated LVV,",uflforms.LVcavityvol()


        total_sol_file << w.sub(0)


    #   update necessary quantities

    #   calculate stimulus
    #   just concentric for now
        if end_systole > 0:
            total_passive_PK2, Sff = uflforms.stress(functions["hsl"])
            end_systolic_stress_calc = inner(functions["f0"],(total_passive_PK2 + Pactive)*functions["f0"])
            concentric_growth_stimulus = project(end_systolic_stress_calc,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
            temp_stim_ss.assign(concentric_growth_stimulus)
            temp_stim_nn.assign(concentric_growth_stimulus)

    if(MPI.rank(comm) == 0):
        fdataPV.close()

    return functions, temp_stim_ff, temp_stim_ss, temp_stim_nn
