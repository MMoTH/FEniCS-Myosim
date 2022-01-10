# @Author: charlesmann
# @Date:   2022-01-05T12:39:33-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-07T14:31:00-05:00
from dolfin import *
from methods import diastolic_filling
from methods import circulatory_system
import numpy as np


def full_cycle(sim_state,fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, Pactive, comm, total_sol_file, p_f_file, growth_iter):

    # initialize things from the simulation state
    edv = sim_state.edv
    sim_timestep = sim_state.timestep
    sim_duration = sim_state.duration
    no_of_time_steps = int(sim_duration/sim_timestep)
    t = np.linspace(0,sim_duration,no_of_time_steps)

    # PV file
    if (MPI.rank(comm)==0):
        fdataPV = open('./fc_output/'+str(growth_iter)+'PV_.txt', "w", 0)


    # Initialize return objects
    temp_stim_ff = Function(fcn_spaces["stimulusFS"])
    temp_stim_ss = Function(fcn_spaces["stimulusFS"])
    temp_stim_nn = Function(fcn_spaces["stimulusFS"])

    # Loading in a custom cb force
    cb_force_loaded = np.load('/home/fenics/shared/preliminary_growth/prescribed_cb_force_refined.npy')
    cb_force = np.nan*np.ones(no_of_time_steps)
    cb_force[0:np.shape(cb_force_loaded)[0]] = cb_force_loaded
    cb_force[np.shape(cb_force_loaded)[0]:] = cb_force_loaded[-1]

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
        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()
        print "Volume of LV = ",V_cav
        circ_dict = circ_system.update_compartments(p_cav,V_cav,sim_timestep)
        functions["LVCavityvol"].vol = circ_dict["V_cav"]
        LVcav_array[l] = circ_dict["V_cav"]
        end_systole = circ_dict["end_systole"]
        end_diastole = circ_dict["end_diastole"]
        #LVCavityvol.vol = V_cav
        #LVcav_array[l] = V_cav
        Pcav_array[l] = p_cav*0.0075

        # Now print out volumes, pressures
        if(MPI.rank(comm) == 0):
            print >>fdataPV, t[l], circ_dict["p_cav"]*0.0075 , circ_dict["Part"]*.0075, circ_dict["Pven"]*.0075, circ_dict["V_cav"], circ_dict["V_ven"], circ_dict["V_art"]

    #   update active stress
        functions["cbforce"].f = 2.2*cb_force[l]

    #   solve weak form
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

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
