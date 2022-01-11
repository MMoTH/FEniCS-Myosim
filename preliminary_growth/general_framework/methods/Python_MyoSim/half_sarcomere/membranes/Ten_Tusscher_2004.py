# Code generated from http://models.cellml.org/exposure/c7f7ced1e002d9f0af1b56b15a873736/tentusscher_noble_noble_panfilov_2004_a.cellml/@@cellml_codegen/Python
# Size of variable arrays:
sizeAlgebraic = 67
sizeStates = 17
sizeConstants = 46
from math import *
from numpy import *

from scipy.integrate import solve_ivp

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (joule_per_mole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_millimole)"
    legend_constants[3] = "Cm in component membrane (microF)"
    legend_constants[4] = "V_c in component membrane (micrometre3)"
    legend_algebraic[50] = "i_K1 in component inward_rectifier_potassium_current (picoA_per_picoF)"
    legend_algebraic[57] = "i_to in component transient_outward_current (picoA_per_picoF)"
    legend_algebraic[51] = "i_Kr in component rapid_time_dependent_potassium_current (picoA_per_picoF)"
    legend_algebraic[52] = "i_Ks in component slow_time_dependent_potassium_current (picoA_per_picoF)"
    legend_algebraic[55] = "i_CaL in component L_type_Ca_current (picoA_per_picoF)"
    legend_algebraic[58] = "i_NaK in component sodium_potassium_pump_current (picoA_per_picoF)"
    legend_algebraic[53] = "i_Na in component fast_sodium_current (picoA_per_picoF)"
    legend_algebraic[54] = "i_b_Na in component sodium_background_current (picoA_per_picoF)"
    legend_algebraic[59] = "i_NaCa in component sodium_calcium_exchanger_current (picoA_per_picoF)"
    legend_algebraic[56] = "i_b_Ca in component calcium_background_current (picoA_per_picoF)"
    legend_algebraic[61] = "i_p_K in component potassium_pump_current (picoA_per_picoF)"
    legend_algebraic[60] = "i_p_Ca in component calcium_pump_current (picoA_per_picoF)"
    legend_algebraic[0] = "i_Stim in component membrane (picoA_per_picoF)"
    legend_constants[5] = "stim_start in component membrane (millisecond)"
    legend_constants[6] = "stim_period in component membrane (millisecond)"
    legend_constants[7] = "stim_duration in component membrane (millisecond)"
    legend_constants[8] = "stim_amplitude in component membrane (picoA_per_picoF)"
    legend_algebraic[13] = "E_Na in component reversal_potentials (millivolt)"
    legend_algebraic[26] = "E_K in component reversal_potentials (millivolt)"
    legend_algebraic[35] = "E_Ks in component reversal_potentials (millivolt)"
    legend_algebraic[44] = "E_Ca in component reversal_potentials (millivolt)"
    legend_constants[9] = "P_kna in component reversal_potentials (dimensionless)"
    legend_constants[10] = "K_o in component potassium_dynamics (millimolar)"
    legend_constants[11] = "Na_o in component sodium_dynamics (millimolar)"
    legend_states[1] = "K_i in component potassium_dynamics (millimolar)"
    legend_states[2] = "Na_i in component sodium_dynamics (millimolar)"
    legend_constants[12] = "Ca_o in component calcium_dynamics (millimolar)"
    legend_states[3] = "Ca_i in component calcium_dynamics (millimolar)"
    legend_constants[13] = "g_K1 in component inward_rectifier_potassium_current (nanoS_per_picoF)"
    legend_algebraic[49] = "xK1_inf in component inward_rectifier_potassium_current (dimensionless)"
    legend_algebraic[47] = "alpha_K1 in component inward_rectifier_potassium_current (dimensionless)"
    legend_algebraic[48] = "beta_K1 in component inward_rectifier_potassium_current (dimensionless)"
    legend_constants[14] = "g_Kr in component rapid_time_dependent_potassium_current (nanoS_per_picoF)"
    legend_states[4] = "Xr1 in component rapid_time_dependent_potassium_current_Xr1_gate (dimensionless)"
    legend_states[5] = "Xr2 in component rapid_time_dependent_potassium_current_Xr2_gate (dimensionless)"
    legend_algebraic[1] = "xr1_inf in component rapid_time_dependent_potassium_current_Xr1_gate (dimensionless)"
    legend_algebraic[14] = "alpha_xr1 in component rapid_time_dependent_potassium_current_Xr1_gate (dimensionless)"
    legend_algebraic[27] = "beta_xr1 in component rapid_time_dependent_potassium_current_Xr1_gate (dimensionless)"
    legend_algebraic[36] = "tau_xr1 in component rapid_time_dependent_potassium_current_Xr1_gate (millisecond)"
    legend_algebraic[2] = "xr2_inf in component rapid_time_dependent_potassium_current_Xr2_gate (dimensionless)"
    legend_algebraic[15] = "alpha_xr2 in component rapid_time_dependent_potassium_current_Xr2_gate (dimensionless)"
    legend_algebraic[28] = "beta_xr2 in component rapid_time_dependent_potassium_current_Xr2_gate (dimensionless)"
    legend_algebraic[37] = "tau_xr2 in component rapid_time_dependent_potassium_current_Xr2_gate (millisecond)"
    legend_constants[15] = "g_Ks in component slow_time_dependent_potassium_current (nanoS_per_picoF)"
    legend_states[6] = "Xs in component slow_time_dependent_potassium_current_Xs_gate (dimensionless)"
    legend_algebraic[3] = "xs_inf in component slow_time_dependent_potassium_current_Xs_gate (dimensionless)"
    legend_algebraic[16] = "alpha_xs in component slow_time_dependent_potassium_current_Xs_gate (dimensionless)"
    legend_algebraic[29] = "beta_xs in component slow_time_dependent_potassium_current_Xs_gate (dimensionless)"
    legend_algebraic[38] = "tau_xs in component slow_time_dependent_potassium_current_Xs_gate (millisecond)"
    legend_constants[16] = "g_Na in component fast_sodium_current (nanoS_per_picoF)"
    legend_states[7] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[8] = "h in component fast_sodium_current_h_gate (dimensionless)"
    legend_states[9] = "j in component fast_sodium_current_j_gate (dimensionless)"
    legend_algebraic[4] = "m_inf in component fast_sodium_current_m_gate (dimensionless)"
    legend_algebraic[17] = "alpha_m in component fast_sodium_current_m_gate (dimensionless)"
    legend_algebraic[30] = "beta_m in component fast_sodium_current_m_gate (dimensionless)"
    legend_algebraic[39] = "tau_m in component fast_sodium_current_m_gate (millisecond)"
    legend_algebraic[5] = "h_inf in component fast_sodium_current_h_gate (dimensionless)"
    legend_algebraic[18] = "alpha_h in component fast_sodium_current_h_gate (per_millisecond)"
    legend_algebraic[31] = "beta_h in component fast_sodium_current_h_gate (per_millisecond)"
    legend_algebraic[40] = "tau_h in component fast_sodium_current_h_gate (millisecond)"
    legend_algebraic[6] = "j_inf in component fast_sodium_current_j_gate (dimensionless)"
    legend_algebraic[19] = "alpha_j in component fast_sodium_current_j_gate (per_millisecond)"
    legend_algebraic[32] = "beta_j in component fast_sodium_current_j_gate (per_millisecond)"
    legend_algebraic[41] = "tau_j in component fast_sodium_current_j_gate (millisecond)"
    legend_constants[17] = "g_bna in component sodium_background_current (nanoS_per_picoF)"
    legend_constants[18] = "g_CaL in component L_type_Ca_current (litre_per_farad_second)"
    legend_states[10] = "d in component L_type_Ca_current_d_gate (dimensionless)"
    legend_states[11] = "f in component L_type_Ca_current_f_gate (dimensionless)"
    legend_states[12] = "fCa in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_algebraic[7] = "d_inf in component L_type_Ca_current_d_gate (dimensionless)"
    legend_algebraic[20] = "alpha_d in component L_type_Ca_current_d_gate (dimensionless)"
    legend_algebraic[33] = "beta_d in component L_type_Ca_current_d_gate (dimensionless)"
    legend_algebraic[42] = "gamma_d in component L_type_Ca_current_d_gate (millisecond)"
    legend_algebraic[45] = "tau_d in component L_type_Ca_current_d_gate (millisecond)"
    legend_algebraic[8] = "f_inf in component L_type_Ca_current_f_gate (dimensionless)"
    legend_algebraic[21] = "tau_f in component L_type_Ca_current_f_gate (millisecond)"
    legend_algebraic[9] = "alpha_fCa in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_algebraic[22] = "beta_fCa in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_algebraic[34] = "gama_fCa in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_algebraic[43] = "fCa_inf in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_constants[45] = "tau_fCa in component L_type_Ca_current_fCa_gate (millisecond)"
    legend_algebraic[46] = "d_fCa in component L_type_Ca_current_fCa_gate (per_millisecond)"
    legend_constants[19] = "g_bca in component calcium_background_current (nanoS_per_picoF)"
    legend_constants[20] = "g_to in component transient_outward_current (nanoS_per_picoF)"
    legend_states[13] = "s in component transient_outward_current_s_gate (dimensionless)"
    legend_states[14] = "r in component transient_outward_current_r_gate (dimensionless)"
    legend_algebraic[10] = "s_inf in component transient_outward_current_s_gate (dimensionless)"
    legend_algebraic[23] = "tau_s in component transient_outward_current_s_gate (millisecond)"
    legend_algebraic[11] = "r_inf in component transient_outward_current_r_gate (dimensionless)"
    legend_algebraic[24] = "tau_r in component transient_outward_current_r_gate (millisecond)"
    legend_constants[21] = "P_NaK in component sodium_potassium_pump_current (picoA_per_picoF)"
    legend_constants[22] = "K_mk in component sodium_potassium_pump_current (millimolar)"
    legend_constants[23] = "K_mNa in component sodium_potassium_pump_current (millimolar)"
    legend_constants[24] = "K_NaCa in component sodium_calcium_exchanger_current (picoA_per_picoF)"
    legend_constants[25] = "K_sat in component sodium_calcium_exchanger_current (dimensionless)"
    legend_constants[26] = "alpha in component sodium_calcium_exchanger_current (dimensionless)"
    legend_constants[27] = "gamma in component sodium_calcium_exchanger_current (dimensionless)"
    legend_constants[28] = "Km_Ca in component sodium_calcium_exchanger_current (millimolar)"
    legend_constants[29] = "Km_Nai in component sodium_calcium_exchanger_current (millimolar)"
    legend_constants[30] = "g_pCa in component calcium_pump_current (picoA_per_picoF)"
    legend_constants[31] = "K_pCa in component calcium_pump_current (millimolar)"
    legend_constants[32] = "g_pK in component potassium_pump_current (nanoS_per_picoF)"
    legend_states[15] = "Ca_SR in component calcium_dynamics (millimolar)"
    legend_algebraic[62] = "i_rel in component calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[63] = "i_up in component calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[64] = "i_leak in component calcium_dynamics (millimolar_per_millisecond)"
    legend_states[16] = "g in component calcium_dynamics (dimensionless)"
    legend_constants[33] = "tau_g in component calcium_dynamics (millisecond)"
    legend_algebraic[12] = "g_inf in component calcium_dynamics (dimensionless)"
    legend_constants[34] = "a_rel in component calcium_dynamics (millimolar_per_millisecond)"
    legend_constants[35] = "b_rel in component calcium_dynamics (millimolar)"
    legend_constants[36] = "c_rel in component calcium_dynamics (millimolar_per_millisecond)"
    legend_constants[37] = "K_up in component calcium_dynamics (millimolar)"
    legend_constants[38] = "V_leak in component calcium_dynamics (per_millisecond)"
    legend_constants[39] = "Vmax_up in component calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[65] = "Ca_i_bufc in component calcium_dynamics (dimensionless)"
    legend_algebraic[66] = "Ca_sr_bufsr in component calcium_dynamics (dimensionless)"
    legend_constants[40] = "Buf_c in component calcium_dynamics (millimolar)"
    legend_constants[41] = "K_buf_c in component calcium_dynamics (millimolar)"
    legend_constants[42] = "Buf_sr in component calcium_dynamics (millimolar)"
    legend_constants[43] = "K_buf_sr in component calcium_dynamics (millimolar)"
    legend_constants[44] = "V_sr in component calcium_dynamics (micrometre3)"
    legend_algebraic[25] = "d_g in component calcium_dynamics (per_millisecond)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[4] = "d/dt Xr1 in component rapid_time_dependent_potassium_current_Xr1_gate (dimensionless)"
    legend_rates[5] = "d/dt Xr2 in component rapid_time_dependent_potassium_current_Xr2_gate (dimensionless)"
    legend_rates[6] = "d/dt Xs in component slow_time_dependent_potassium_current_Xs_gate (dimensionless)"
    legend_rates[7] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[8] = "d/dt h in component fast_sodium_current_h_gate (dimensionless)"
    legend_rates[9] = "d/dt j in component fast_sodium_current_j_gate (dimensionless)"
    legend_rates[10] = "d/dt d in component L_type_Ca_current_d_gate (dimensionless)"
    legend_rates[11] = "d/dt f in component L_type_Ca_current_f_gate (dimensionless)"
    legend_rates[12] = "d/dt fCa in component L_type_Ca_current_fCa_gate (dimensionless)"
    legend_rates[13] = "d/dt s in component transient_outward_current_s_gate (dimensionless)"
    legend_rates[14] = "d/dt r in component transient_outward_current_r_gate (dimensionless)"
    legend_rates[16] = "d/dt g in component calcium_dynamics (dimensionless)"
    legend_rates[3] = "d/dt Ca_i in component calcium_dynamics (millimolar)"
    legend_rates[15] = "d/dt Ca_SR in component calcium_dynamics (millimolar)"
    legend_rates[2] = "d/dt Na_i in component sodium_dynamics (millimolar)"
    legend_rates[1] = "d/dt K_i in component potassium_dynamics (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -86.2
    constants[0] = 8314.472
    constants[1] = 310
    constants[2] = 96485.3415
    constants[3] = 0.185
    constants[4] = 0.016404
    constants[5] = 10
    constants[6] = 1000
    constants[7] = 1
    constants[8] = 52
    constants[9] = 0.03
    constants[10] = 5.4
    constants[11] = 140
    states[1] = 138.3
    states[2] = 11.6
    constants[12] = 2
    states[3] = 0.0002
    constants[13] = 5.405
    constants[14] = 0.096
    states[4] = 0
    states[5] = 1
    constants[15] = 0.062
    states[6] = 0
    constants[16] = 14.838
    states[7] = 0
    states[8] = 0.75
    states[9] = 0.75
    constants[17] = 0.00029
    constants[18] = 0.000175
    states[10] = 0
    states[11] = 1
    states[12] = 1
    constants[19] = 0.000592
    constants[20] = 0.294
    states[13] = 1
    states[14] = 0
    constants[21] = 1.362
    constants[22] = 1
    constants[23] = 40
    constants[24] = 1000
    constants[25] = 0.1
    constants[26] = 2.5
    constants[27] = 0.35
    constants[28] = 1.38
    constants[29] = 87.5
    constants[30] = 0.825
    constants[31] = 0.0005
    constants[32] = 0.0146
    states[15] = 0.2
    states[16] = 1
    constants[33] = 2
    constants[34] = 0.016464
    constants[35] = 0.25
    constants[36] = 0.008232
    constants[37] = 0.00025
    constants[38] = 8e-5
    constants[39] = 0.000425
    constants[40] = 0.15
    constants[41] = 0.001
    constants[42] = 10
    constants[43] = 0.3
    constants[44] = 0.001094
    constants[45] = 2.00000
    return (states, constants)


def initConsts_with_adjustments(membrane_factors):
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -86.2
    constants[0] = 8314.472
    constants[1] = 310
    constants[2] = 96485.3415
    constants[3] = 0.185
    constants[4] = 0.016404
    constants[5] = 10
    constants[6] = 1000
    constants[7] = 1
    constants[8] = 52
    constants[9] = 0.03
    constants[10] = 5.4
    constants[11] = 140
    states[1] = 138.3
    states[2] = 11.6
    constants[12] = 2
    states[3] = 0.0002
    constants[13] = 5.405
    constants[14] = membrane_factors['g_Kr'] * 0.096
    states[4] = 0
    states[5] = 1
    constants[15] = membrane_factors['g_Ks'] * 0.062
    states[6] = 0
    constants[16] = 14.838
    states[7] = 0
    states[8] = 0.75
    states[9] = 0.75
    constants[17] = 0.00029
    constants[18] = membrane_factors['g_CaL'] * 0.000175
    states[10] = 0
    states[11] = 1
    states[12] = 1
    constants[19] = 0.000592
    constants[20] = membrane_factors['g_to'] * 0.294
    states[13] = 1
    states[14] = 0
    constants[21] = 1.362
    constants[22] = 1
    constants[23] = 40
    constants[24] = 1000
    constants[25] = 0.1
    constants[26] = 2.5
    constants[27] = 0.35
    constants[28] = 1.38
    constants[29] = 87.5
    constants[30] = 0.825
    constants[31] = 0.0005
    constants[32] = 0.0146
    states[15] = 0.2
    states[16] = 1
    constants[33] = 2
    constants[34] = membrane_factors['Ca_a_rel'] * 0.016464
    constants[35] = 0.25
    constants[36] = 0.008232
    constants[37] = 0.00025
    constants[38] = membrane_factors['Ca_V_leak'] * 8e-5
    constants[39] = membrane_factors['Ca_Vmax_up'] * 0.000425
    constants[40] = 0.15
    constants[41] = 0.001
    constants[42] = 10
    constants[43] = 0.3
    constants[44] = 0.001094
    constants[45] = 2.00000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+20.0000)/7.00000))
    algebraic[21] = 1125.00*exp(-(power(states[0]+27.0000, 2.00000))/240.000)+80.0000+165.000/(1.00000+exp((25.0000-states[0])/10.0000))
    rates[11] = (algebraic[8]-states[11])/algebraic[21]
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+20.0000)/5.00000))
    algebraic[23] = 85.0000*exp(-(power(states[0]+45.0000, 2.00000))/320.000)+5.00000/(1.00000+exp((states[0]-20.0000)/5.00000))+3.00000
    rates[13] = (algebraic[10]-states[13])/algebraic[23]
    algebraic[11] = 1.00000/(1.00000+exp((20.0000-states[0])/6.00000))
    algebraic[24] = 9.50000*exp(-(power(states[0]+40.0000, 2.00000))/1800.00)+0.800000
    rates[14] = (algebraic[11]-states[14])/algebraic[24]
    algebraic[12] = custom_piecewise([less(states[3] , 0.000350000), 1.00000/(1.00000+power(states[3]/0.000350000, 6.00000)) , True, 1.00000/(1.00000+power(states[3]/0.000350000, 16.0000))])
    algebraic[25] = (algebraic[12]-states[16])/constants[33]
    rates[16] = custom_piecewise([greater(algebraic[12] , states[16]) & greater(states[0] , -60.0000), 0.00000 , True, algebraic[25]])
    algebraic[1] = 1.00000/(1.00000+exp((-26.0000-states[0])/7.00000))
    algebraic[14] = 450.000/(1.00000+exp((-45.0000-states[0])/10.0000))
    algebraic[27] = 6.00000/(1.00000+exp((states[0]+30.0000)/11.5000))
    algebraic[36] = 1.00000*algebraic[14]*algebraic[27]
    rates[4] = (algebraic[1]-states[4])/algebraic[36]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+88.0000)/24.0000))
    algebraic[15] = 3.00000/(1.00000+exp((-60.0000-states[0])/20.0000))
    algebraic[28] = 1.12000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[37] = 1.00000*algebraic[15]*algebraic[28]
    rates[5] = (algebraic[2]-states[5])/algebraic[37]
    algebraic[3] = 1.00000/(1.00000+exp((-5.00000-states[0])/14.0000))
    algebraic[16] = 1100.00/(power(1.00000+exp((-10.0000-states[0])/6.00000), 1.0/2))
    algebraic[29] = 1.00000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[38] = 1.00000*algebraic[16]*algebraic[29]
    rates[6] = (algebraic[3]-states[6])/algebraic[38]
    algebraic[4] = 1.00000/(power(1.00000+exp((-56.8600-states[0])/9.03000), 2.00000))
    algebraic[17] = 1.00000/(1.00000+exp((-60.0000-states[0])/5.00000))
    algebraic[30] = 0.100000/(1.00000+exp((states[0]+35.0000)/5.00000))+0.100000/(1.00000+exp((states[0]-50.0000)/200.000))
    algebraic[39] = 1.00000*algebraic[17]*algebraic[30]
    rates[7] = (algebraic[4]-states[7])/algebraic[39]
    algebraic[5] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[18] = custom_piecewise([less(states[0] , -40.0000), 0.0570000*exp(-(states[0]+80.0000)/6.80000) , True, 0.00000])
    algebraic[31] = custom_piecewise([less(states[0] , -40.0000), 2.70000*exp(0.0790000*states[0])+310000.*exp(0.348500*states[0]) , True, 0.770000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[40] = 1.00000/(algebraic[18]+algebraic[31])
    rates[8] = (algebraic[5]-states[8])/algebraic[40]
    algebraic[6] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[19] = custom_piecewise([less(states[0] , -40.0000), (((-25428.0*exp(0.244400*states[0])-6.94800e-06*exp(-0.0439100*states[0]))*(states[0]+37.7800))/1.00000)/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[32] = custom_piecewise([less(states[0] , -40.0000), (0.0242400*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.600000*exp(0.0570000*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[41] = 1.00000/(algebraic[19]+algebraic[32])
    rates[9] = (algebraic[6]-states[9])/algebraic[41]
    algebraic[7] = 1.00000/(1.00000+exp((-5.00000-states[0])/7.50000))
    algebraic[20] = 1.40000/(1.00000+exp((-35.0000-states[0])/13.0000))+0.250000
    algebraic[33] = 1.40000/(1.00000+exp((states[0]+5.00000)/5.00000))
    algebraic[42] = 1.00000/(1.00000+exp((50.0000-states[0])/20.0000))
    algebraic[45] = 1.00000*algebraic[20]*algebraic[33]+algebraic[42]
    rates[10] = (algebraic[7]-states[10])/algebraic[45]
    algebraic[9] = 1.00000/(1.00000+power(states[3]/0.000325000, 8.00000))
    algebraic[22] = 0.100000/(1.00000+exp((states[3]-0.000500000)/0.000100000))
    algebraic[34] = 0.200000/(1.00000+exp((states[3]-0.000750000)/0.000800000))
    algebraic[43] = (algebraic[9]+algebraic[22]+algebraic[34]+0.230000)/1.46000
    algebraic[46] = (algebraic[43]-states[12])/constants[45]
    rates[12] = custom_piecewise([greater(algebraic[43] , states[12]) & greater(states[0] , -60.0000), 0.00000 , True, algebraic[46]])
    algebraic[58] = ((((constants[21]*constants[10])/(constants[10]+constants[22]))*states[2])/(states[2]+constants[23]))/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0353000*exp((-states[0]*constants[2])/(constants[0]*constants[1])))
    algebraic[13] = ((constants[0]*constants[1])/constants[2])*log(constants[11]/states[2])
    algebraic[53] = constants[16]*(power(states[7], 3.00000))*states[8]*states[9]*(states[0]-algebraic[13])
    algebraic[54] = constants[17]*(states[0]-algebraic[13])
    algebraic[59] = (constants[24]*(exp((constants[27]*states[0]*constants[2])/(constants[0]*constants[1]))*(power(states[2], 3.00000))*constants[12]-exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))*(power(constants[11], 3.00000))*states[3]*constants[26]))/((power(constants[29], 3.00000)+power(constants[11], 3.00000))*(constants[28]+constants[12])*(1.00000+constants[25]*exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))))
    rates[2] = (-1.00000*(algebraic[53]+algebraic[54]+3.00000*algebraic[58]+3.00000*algebraic[59])*constants[3])/(1.00000*constants[4]*constants[2])
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/states[1])
    algebraic[47] = 0.100000/(1.00000+exp(0.0600000*((states[0]-algebraic[26])-200.000)))
    algebraic[48] = (3.00000*exp(0.000200000*((states[0]-algebraic[26])+100.000))+exp(0.100000*((states[0]-algebraic[26])-10.0000)))/(1.00000+exp(-0.500000*(states[0]-algebraic[26])))
    algebraic[49] = algebraic[47]/(algebraic[47]+algebraic[48])
    algebraic[50] = constants[13]*algebraic[49]*(power(constants[10]/5.40000, 1.0/2))*(states[0]-algebraic[26])
    algebraic[57] = constants[20]*states[14]*states[13]*(states[0]-algebraic[26])
    algebraic[51] = constants[14]*(power(constants[10]/5.40000, 1.0/2))*states[4]*states[5]*(states[0]-algebraic[26])
    algebraic[35] = ((constants[0]*constants[1])/constants[2])*log((constants[10]+constants[9]*constants[11])/(states[1]+constants[9]*states[2]))
    algebraic[52] = constants[15]*(power(states[6], 2.00000))*(states[0]-algebraic[35])
    algebraic[55] = (((constants[18]*states[10]*states[11]*states[12]*4.00000*states[0]*(power(constants[2], 2.00000)))/(constants[0]*constants[1]))*(states[3]*exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-0.341000*constants[12]))/(exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[44] = ((0.500000*constants[0]*constants[1])/constants[2])*log(constants[12]/states[3])
    algebraic[56] = constants[19]*(states[0]-algebraic[44])
    algebraic[61] = (constants[32]*(states[0]-algebraic[26]))/(1.00000+exp((25.0000-states[0])/5.98000))
    algebraic[60] = (constants[30]*states[3])/(states[3]+constants[31])
    algebraic[0] = custom_piecewise([greater_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]) & less_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]+constants[7]), -constants[8] , True, 0.00000])
    rates[0] = (-1.00000/1.00000)*(algebraic[50]+algebraic[57]+algebraic[51]+algebraic[52]+algebraic[55]+algebraic[58]+algebraic[53]+algebraic[54]+algebraic[59]+algebraic[56]+algebraic[61]+algebraic[60]+algebraic[0])
    rates[1] = (-1.00000*((algebraic[50]+algebraic[57]+algebraic[51]+algebraic[52]+algebraic[61]+algebraic[0])-2.00000*algebraic[58])*constants[3])/(1.00000*constants[4]*constants[2])
    algebraic[62] = ((constants[34]*(power(states[15], 2.00000)))/(power(constants[35], 2.00000)+power(states[15], 2.00000))+constants[36])*states[10]*states[16]
    algebraic[63] = constants[39]/(1.00000+(power(constants[37], 2.00000))/(power(states[3], 2.00000)))
    algebraic[64] = constants[38]*(states[15]-states[3])
    algebraic[65] = 1.00000/(1.00000+(constants[40]*constants[41])/(power(states[3]+constants[41], 2.00000)))
    rates[3] = algebraic[65]*(((algebraic[64]-algebraic[63])+algebraic[62])-((1.00000*((algebraic[55]+algebraic[56]+algebraic[60])-2.00000*algebraic[59]))/(2.00000*1.00000*constants[4]*constants[2]))*constants[3])
    algebraic[66] = 1.00000/(1.00000+(constants[42]*constants[43])/(power(states[15]+constants[43], 2.00000)))
    rates[15] = ((algebraic[66]*constants[4])/constants[44])*(algebraic[63]-(algebraic[62]+algebraic[64]))
    return(rates)

def computeRates_with_activation(voi, states, constants, activation):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+20.0000)/7.00000))
    algebraic[21] = 1125.00*exp(-(power(states[0]+27.0000, 2.00000))/240.000)+80.0000+165.000/(1.00000+exp((25.0000-states[0])/10.0000))
    rates[11] = (algebraic[8]-states[11])/algebraic[21]
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+20.0000)/5.00000))
    algebraic[23] = 85.0000*exp(-(power(states[0]+45.0000, 2.00000))/320.000)+5.00000/(1.00000+exp((states[0]-20.0000)/5.00000))+3.00000
    rates[13] = (algebraic[10]-states[13])/algebraic[23]
    algebraic[11] = 1.00000/(1.00000+exp((20.0000-states[0])/6.00000))
    algebraic[24] = 9.50000*exp(-(power(states[0]+40.0000, 2.00000))/1800.00)+0.800000
    rates[14] = (algebraic[11]-states[14])/algebraic[24]
    algebraic[12] = custom_piecewise([less(states[3] , 0.000350000), 1.00000/(1.00000+power(states[3]/0.000350000, 6.00000)) , True, 1.00000/(1.00000+power(states[3]/0.000350000, 16.0000))])
    algebraic[25] = (algebraic[12]-states[16])/constants[33]
    rates[16] = custom_piecewise([greater(algebraic[12] , states[16]) & greater(states[0] , -60.0000), 0.00000 , True, algebraic[25]])
    algebraic[1] = 1.00000/(1.00000+exp((-26.0000-states[0])/7.00000))
    algebraic[14] = 450.000/(1.00000+exp((-45.0000-states[0])/10.0000))
    algebraic[27] = 6.00000/(1.00000+exp((states[0]+30.0000)/11.5000))
    algebraic[36] = 1.00000*algebraic[14]*algebraic[27]
    rates[4] = (algebraic[1]-states[4])/algebraic[36]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+88.0000)/24.0000))
    algebraic[15] = 3.00000/(1.00000+exp((-60.0000-states[0])/20.0000))
    algebraic[28] = 1.12000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[37] = 1.00000*algebraic[15]*algebraic[28]
    rates[5] = (algebraic[2]-states[5])/algebraic[37]
    algebraic[3] = 1.00000/(1.00000+exp((-5.00000-states[0])/14.0000))
    algebraic[16] = 1100.00/(power(1.00000+exp((-10.0000-states[0])/6.00000), 1.0/2))
    algebraic[29] = 1.00000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[38] = 1.00000*algebraic[16]*algebraic[29]
    rates[6] = (algebraic[3]-states[6])/algebraic[38]
    algebraic[4] = 1.00000/(power(1.00000+exp((-56.8600-states[0])/9.03000), 2.00000))
    algebraic[17] = 1.00000/(1.00000+exp((-60.0000-states[0])/5.00000))
    algebraic[30] = 0.100000/(1.00000+exp((states[0]+35.0000)/5.00000))+0.100000/(1.00000+exp((states[0]-50.0000)/200.000))
    algebraic[39] = 1.00000*algebraic[17]*algebraic[30]
    rates[7] = (algebraic[4]-states[7])/algebraic[39]
    algebraic[5] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[18] = custom_piecewise([less(states[0] , -40.0000), 0.0570000*exp(-(states[0]+80.0000)/6.80000) , True, 0.00000])
    algebraic[31] = custom_piecewise([less(states[0] , -40.0000), 2.70000*exp(0.0790000*states[0])+310000.*exp(0.348500*states[0]) , True, 0.770000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[40] = 1.00000/(algebraic[18]+algebraic[31])
    rates[8] = (algebraic[5]-states[8])/algebraic[40]
    algebraic[6] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[19] = custom_piecewise([less(states[0] , -40.0000), (((-25428.0*exp(0.244400*states[0])-6.94800e-06*exp(-0.0439100*states[0]))*(states[0]+37.7800))/1.00000)/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[32] = custom_piecewise([less(states[0] , -40.0000), (0.0242400*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.600000*exp(0.0570000*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[41] = 1.00000/(algebraic[19]+algebraic[32])
    rates[9] = (algebraic[6]-states[9])/algebraic[41]
    algebraic[7] = 1.00000/(1.00000+exp((-5.00000-states[0])/7.50000))
    algebraic[20] = 1.40000/(1.00000+exp((-35.0000-states[0])/13.0000))+0.250000
    algebraic[33] = 1.40000/(1.00000+exp((states[0]+5.00000)/5.00000))
    algebraic[42] = 1.00000/(1.00000+exp((50.0000-states[0])/20.0000))
    algebraic[45] = 1.00000*algebraic[20]*algebraic[33]+algebraic[42]
    rates[10] = (algebraic[7]-states[10])/algebraic[45]
    algebraic[9] = 1.00000/(1.00000+power(states[3]/0.000325000, 8.00000))
    algebraic[22] = 0.100000/(1.00000+exp((states[3]-0.000500000)/0.000100000))
    algebraic[34] = 0.200000/(1.00000+exp((states[3]-0.000750000)/0.000800000))
    algebraic[43] = (algebraic[9]+algebraic[22]+algebraic[34]+0.230000)/1.46000
    algebraic[46] = (algebraic[43]-states[12])/constants[45]
    rates[12] = custom_piecewise([greater(algebraic[43] , states[12]) & greater(states[0] , -60.0000), 0.00000 , True, algebraic[46]])
    algebraic[58] = ((((constants[21]*constants[10])/(constants[10]+constants[22]))*states[2])/(states[2]+constants[23]))/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0353000*exp((-states[0]*constants[2])/(constants[0]*constants[1])))
    algebraic[13] = ((constants[0]*constants[1])/constants[2])*log(constants[11]/states[2])
    algebraic[53] = constants[16]*(power(states[7], 3.00000))*states[8]*states[9]*(states[0]-algebraic[13])
    algebraic[54] = constants[17]*(states[0]-algebraic[13])
    algebraic[59] = (constants[24]*(exp((constants[27]*states[0]*constants[2])/(constants[0]*constants[1]))*(power(states[2], 3.00000))*constants[12]-exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))*(power(constants[11], 3.00000))*states[3]*constants[26]))/((power(constants[29], 3.00000)+power(constants[11], 3.00000))*(constants[28]+constants[12])*(1.00000+constants[25]*exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))))
    rates[2] = (-1.00000*(algebraic[53]+algebraic[54]+3.00000*algebraic[58]+3.00000*algebraic[59])*constants[3])/(1.00000*constants[4]*constants[2])
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/states[1])
    algebraic[47] = 0.100000/(1.00000+exp(0.0600000*((states[0]-algebraic[26])-200.000)))
    algebraic[48] = (3.00000*exp(0.000200000*((states[0]-algebraic[26])+100.000))+exp(0.100000*((states[0]-algebraic[26])-10.0000)))/(1.00000+exp(-0.500000*(states[0]-algebraic[26])))
    algebraic[49] = algebraic[47]/(algebraic[47]+algebraic[48])
    algebraic[50] = constants[13]*algebraic[49]*(power(constants[10]/5.40000, 1.0/2))*(states[0]-algebraic[26])
    algebraic[57] = constants[20]*states[14]*states[13]*(states[0]-algebraic[26])
    algebraic[51] = constants[14]*(power(constants[10]/5.40000, 1.0/2))*states[4]*states[5]*(states[0]-algebraic[26])
    algebraic[35] = ((constants[0]*constants[1])/constants[2])*log((constants[10]+constants[9]*constants[11])/(states[1]+constants[9]*states[2]))
    algebraic[52] = constants[15]*(power(states[6], 2.00000))*(states[0]-algebraic[35])
    algebraic[55] = (((constants[18]*states[10]*states[11]*states[12]*4.00000*states[0]*(power(constants[2], 2.00000)))/(constants[0]*constants[1]))*(states[3]*exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-0.341000*constants[12]))/(exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[44] = ((0.500000*constants[0]*constants[1])/constants[2])*log(constants[12]/states[3])
    algebraic[56] = constants[19]*(states[0]-algebraic[44])
    algebraic[61] = (constants[32]*(states[0]-algebraic[26]))/(1.00000+exp((25.0000-states[0])/5.98000))
    algebraic[60] = (constants[30]*states[3])/(states[3]+constants[31])
#    algebraic[0] = custom_piecewise([greater_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]) & less_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]+constants[7]), -constants[8] , True, 0.00000])
    algebraic[0] = activation * -52.0
    rates[0] = (-1.00000/1.00000)*(algebraic[50]+algebraic[57]+algebraic[51]+algebraic[52]+algebraic[55]+algebraic[58]+algebraic[53]+algebraic[54]+algebraic[59]+algebraic[56]+algebraic[61]+algebraic[60]+algebraic[0])
    rates[1] = (-1.00000*((algebraic[50]+algebraic[57]+algebraic[51]+algebraic[52]+algebraic[61]+algebraic[0])-2.00000*algebraic[58])*constants[3])/(1.00000*constants[4]*constants[2])
    algebraic[62] = ((constants[34]*(power(states[15], 2.00000)))/(power(constants[35], 2.00000)+power(states[15], 2.00000))+constants[36])*states[10]*states[16]
    algebraic[63] = constants[39]/(1.00000+(power(constants[37], 2.00000))/(power(states[3], 2.00000)))
    algebraic[64] = constants[38]*(states[15]-states[3])
    algebraic[65] = 1.00000/(1.00000+(constants[40]*constants[41])/(power(states[3]+constants[41], 2.00000)))
    rates[3] = algebraic[65]*(((algebraic[64]-algebraic[63])+algebraic[62])-((1.00000*((algebraic[55]+algebraic[56]+algebraic[60])-2.00000*algebraic[59]))/(2.00000*1.00000*constants[4]*constants[2]))*constants[3])
    algebraic[66] = 1.00000/(1.00000+(constants[42]*constants[43])/(power(states[15]+constants[43], 2.00000)))
    rates[15] = ((algebraic[66]*constants[4])/constants[44])*(algebraic[63]-(algebraic[62]+algebraic[64]))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+20.0000)/7.00000))
    algebraic[21] = 1125.00*exp(-(power(states[0]+27.0000, 2.00000))/240.000)+80.0000+165.000/(1.00000+exp((25.0000-states[0])/10.0000))
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+20.0000)/5.00000))
    algebraic[23] = 85.0000*exp(-(power(states[0]+45.0000, 2.00000))/320.000)+5.00000/(1.00000+exp((states[0]-20.0000)/5.00000))+3.00000
    algebraic[11] = 1.00000/(1.00000+exp((20.0000-states[0])/6.00000))
    algebraic[24] = 9.50000*exp(-(power(states[0]+40.0000, 2.00000))/1800.00)+0.800000
    algebraic[12] = custom_piecewise([less(states[3] , 0.000350000), 1.00000/(1.00000+power(states[3]/0.000350000, 6.00000)) , True, 1.00000/(1.00000+power(states[3]/0.000350000, 16.0000))])
    algebraic[25] = (algebraic[12]-states[16])/constants[33]
    algebraic[1] = 1.00000/(1.00000+exp((-26.0000-states[0])/7.00000))
    algebraic[14] = 450.000/(1.00000+exp((-45.0000-states[0])/10.0000))
    algebraic[27] = 6.00000/(1.00000+exp((states[0]+30.0000)/11.5000))
    algebraic[36] = 1.00000*algebraic[14]*algebraic[27]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+88.0000)/24.0000))
    algebraic[15] = 3.00000/(1.00000+exp((-60.0000-states[0])/20.0000))
    algebraic[28] = 1.12000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[37] = 1.00000*algebraic[15]*algebraic[28]
    algebraic[3] = 1.00000/(1.00000+exp((-5.00000-states[0])/14.0000))
    algebraic[16] = 1100.00/(power(1.00000+exp((-10.0000-states[0])/6.00000), 1.0/2))
    algebraic[29] = 1.00000/(1.00000+exp((states[0]-60.0000)/20.0000))
    algebraic[38] = 1.00000*algebraic[16]*algebraic[29]
    algebraic[4] = 1.00000/(power(1.00000+exp((-56.8600-states[0])/9.03000), 2.00000))
    algebraic[17] = 1.00000/(1.00000+exp((-60.0000-states[0])/5.00000))
    algebraic[30] = 0.100000/(1.00000+exp((states[0]+35.0000)/5.00000))+0.100000/(1.00000+exp((states[0]-50.0000)/200.000))
    algebraic[39] = 1.00000*algebraic[17]*algebraic[30]
    algebraic[5] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[18] = custom_piecewise([less(states[0] , -40.0000), 0.0570000*exp(-(states[0]+80.0000)/6.80000) , True, 0.00000])
    algebraic[31] = custom_piecewise([less(states[0] , -40.0000), 2.70000*exp(0.0790000*states[0])+310000.*exp(0.348500*states[0]) , True, 0.770000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[40] = 1.00000/(algebraic[18]+algebraic[31])
    algebraic[6] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[19] = custom_piecewise([less(states[0] , -40.0000), (((-25428.0*exp(0.244400*states[0])-6.94800e-06*exp(-0.0439100*states[0]))*(states[0]+37.7800))/1.00000)/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[32] = custom_piecewise([less(states[0] , -40.0000), (0.0242400*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.600000*exp(0.0570000*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[41] = 1.00000/(algebraic[19]+algebraic[32])
    algebraic[7] = 1.00000/(1.00000+exp((-5.00000-states[0])/7.50000))
    algebraic[20] = 1.40000/(1.00000+exp((-35.0000-states[0])/13.0000))+0.250000
    algebraic[33] = 1.40000/(1.00000+exp((states[0]+5.00000)/5.00000))
    algebraic[42] = 1.00000/(1.00000+exp((50.0000-states[0])/20.0000))
    algebraic[45] = 1.00000*algebraic[20]*algebraic[33]+algebraic[42]
    algebraic[9] = 1.00000/(1.00000+power(states[3]/0.000325000, 8.00000))
    algebraic[22] = 0.100000/(1.00000+exp((states[3]-0.000500000)/0.000100000))
    algebraic[34] = 0.200000/(1.00000+exp((states[3]-0.000750000)/0.000800000))
    algebraic[43] = (algebraic[9]+algebraic[22]+algebraic[34]+0.230000)/1.46000
    algebraic[46] = (algebraic[43]-states[12])/constants[45]
    algebraic[58] = ((((constants[21]*constants[10])/(constants[10]+constants[22]))*states[2])/(states[2]+constants[23]))/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0353000*exp((-states[0]*constants[2])/(constants[0]*constants[1])))
    algebraic[13] = ((constants[0]*constants[1])/constants[2])*log(constants[11]/states[2])
    algebraic[53] = constants[16]*(power(states[7], 3.00000))*states[8]*states[9]*(states[0]-algebraic[13])
    algebraic[54] = constants[17]*(states[0]-algebraic[13])
    algebraic[59] = (constants[24]*(exp((constants[27]*states[0]*constants[2])/(constants[0]*constants[1]))*(power(states[2], 3.00000))*constants[12]-exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))*(power(constants[11], 3.00000))*states[3]*constants[26]))/((power(constants[29], 3.00000)+power(constants[11], 3.00000))*(constants[28]+constants[12])*(1.00000+constants[25]*exp(((constants[27]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))))
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/states[1])
    algebraic[47] = 0.100000/(1.00000+exp(0.0600000*((states[0]-algebraic[26])-200.000)))
    algebraic[48] = (3.00000*exp(0.000200000*((states[0]-algebraic[26])+100.000))+exp(0.100000*((states[0]-algebraic[26])-10.0000)))/(1.00000+exp(-0.500000*(states[0]-algebraic[26])))
    algebraic[49] = algebraic[47]/(algebraic[47]+algebraic[48])
    algebraic[50] = constants[13]*algebraic[49]*(power(constants[10]/5.40000, 1.0/2))*(states[0]-algebraic[26])
    algebraic[57] = constants[20]*states[14]*states[13]*(states[0]-algebraic[26])
    algebraic[51] = constants[14]*(power(constants[10]/5.40000, 1.0/2))*states[4]*states[5]*(states[0]-algebraic[26])
    algebraic[35] = ((constants[0]*constants[1])/constants[2])*log((constants[10]+constants[9]*constants[11])/(states[1]+constants[9]*states[2]))
    algebraic[52] = constants[15]*(power(states[6], 2.00000))*(states[0]-algebraic[35])
    algebraic[55] = (((constants[18]*states[10]*states[11]*states[12]*4.00000*states[0]*(power(constants[2], 2.00000)))/(constants[0]*constants[1]))*(states[3]*exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-0.341000*constants[12]))/(exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[44] = ((0.500000*constants[0]*constants[1])/constants[2])*log(constants[12]/states[3])
    algebraic[56] = constants[19]*(states[0]-algebraic[44])
    algebraic[61] = (constants[32]*(states[0]-algebraic[26]))/(1.00000+exp((25.0000-states[0])/5.98000))
    algebraic[60] = (constants[30]*states[3])/(states[3]+constants[31])
    algebraic[0] = custom_piecewise([greater_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]) & less_equal(voi-floor(voi/constants[6])*constants[6] , constants[5]+constants[7]), -constants[8] , True, 0.00000])
    algebraic[62] = ((constants[34]*(power(states[15], 2.00000)))/(power(constants[35], 2.00000)+power(states[15], 2.00000))+constants[36])*states[10]*states[16]
    algebraic[63] = constants[39]/(1.00000+(power(constants[37], 2.00000))/(power(states[3], 2.00000)))
    algebraic[64] = constants[38]*(states[15]-states[3])
    algebraic[65] = 1.00000/(1.00000+(constants[40]*constants[41])/(power(states[3]+constants[41], 2.00000)))
    algebraic[66] = 1.00000/(1.00000+(constants[42]*constants[43])/(power(states[15]+constants[43], 2.00000)))
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    # This code has been adapted by Ken to work with modern Python scipy
    from scipy.integrate import ode
    from scipy.integrate import solve_ivp
    import numpy as np
    from functools import partial
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    if (0):
        dt = 1
        voi = np.arange(0,200,dt)
        states = array([[0.0] * len(voi)] * sizeStates)
        states[:,0] = init_states
        for (i,t) in enumerate(voi[1:]):
            print('%d %f' % (i,t))
            sol = solve_ivp(partial(computeRates, constants=constants),
                            voi[i]+[0, dt], states[:,i],
                            method='Radau')
            if (i<(len(voi)-1)):
                states[:,i+1] = sol.y[:,-1]
            
        algebraic = computeAlgebraic(constants, states, voi)
        
        return (voi, states, algebraic)


    if (1):
        dt = 1
        voi = np.arange(0,1000,dt)
        states = array([[0.0] * len(voi)] * sizeStates)
        states[:,0] = init_states
        for (i,t) in enumerate(voi[1:]):
            print('%d %f' % (i,t))
            if ((i>100)&(i<110)):
                activation = 1.0
            else:
                activation = 0.0
            sol = solve_ivp(partial(computeRates_with_activation,
                                    constants=constants,
                                    activation = activation),
                            0*voi[i]+[0, dt], states[:,i],
                            method='BDF')
#            print("t_points:")
#            print(sol.t)
#            print("nfev:")
#            print(sol.nfev)
                
            if (i<(len(voi)-1)):
                states[:,i+1] = sol.y[:,-1]
            
#        algebraic = computeAlgebraic(constants, states, voi)
        algebraic = 0*states
        
    if (0):
        dt = 0.1
             # Set timespan to solve over
        voi = np.arange(0,10,dt)
    
        # Construct ODE object to solve
        r = ode(computeRates)
        r.set_integrator('vode', method='bdf', atol=1e-03, rtol=1e-03, max_step=1)
        r.set_initial_value(init_states, voi[0])
        r.set_f_params(constants)
    
        # Solve model
        states = array([[0.0] * len(voi)] * sizeStates)
        states[:,0] = init_states
        for (i,t) in enumerate(voi[1:]):
            print(i)
            if r.successful():
                r.integrate(t)
                states[:,i+1] = r.y
            else:
                break
    
        # Compute algebraic variables
        algebraic = computeAlgebraic(constants, states, voi)
        return (voi, states, algebraic)
        
    return (voi, states, algebraic)


def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
#    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()
    
    print(voi)
    print(states)
    pylab.figure(2)
    pylab.plot(voi,states[3, :],'b-')


if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
#    plot_model(voi, states, algebraic)
