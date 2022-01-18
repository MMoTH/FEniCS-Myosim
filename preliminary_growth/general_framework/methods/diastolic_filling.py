# @Author: charlesmann
# @Date:   2021-12-28T16:23:13-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-12T16:37:43-05:00

from dolfin import *
import numpy as np

def diastolic_filling(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, edv, output_object, n_load_steps, arrays_and_values, comm):

    #filling_file = File('./output/iter_'+str(iter_number)+'/load_disp.pvd')

    #n_load_steps = 10

    LVCavityvol = functions["LVCavityvol"]

    LVCavityvol.vol = uflforms.LVcavityvol()

    end_diastolic_volume = edv #mL
    total_vol_loading = end_diastolic_volume - LVCavityvol.vol
    volume_increment = total_vol_loading/n_load_steps

    w = functions["w"]

    for lmbda_value in range(0, n_load_steps):

        print "Diastolic loading step " + str(lmbda_value)

        LVCavityvol.vol += volume_increment

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        arrays_and_values["hsl_array_old"] = arrays_and_values["hsl_array"]

        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        arrays_and_values["hsl_array"] = project(functions["hsl"], fcn_spaces["quadrature_space"]).vector().get_local()[:]
        print "HALF SARCOMERE LENGTHS", arrays_and_values["hsl_array"][0:20]

        temp_DG = project(functions["Sff"], fcn_spaces["stimulusFS"], form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, fcn_spaces["quadrature_space"])
        arrays_and_values["p_f_array"] = p_f.vector().get_local()[:]

        for ii in range(np.shape(arrays_and_values["hsl_array"])[0]):
            if arrays_and_values["p_f_array"][ii] < 0.0:
                arrays_and_values["p_f_array"][ii] = 0.0

        arrays_and_values["delta_hsl_array"] = arrays_and_values["hsl_array"] - arrays_and_values["hsl_array_old"]


	    # Save displacement to check the loading
        #filling_file << w.sub(0)
        output_object.total_sol_file.save_pvd_object(w.sub(0))
        pk2_global, sff = uflforms.stress(functions["hsl"])
        temp_pf = project(inner(functions["f0"],pk2_global*functions["f0"]),fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
        temp_pf.rename("pf","pf")
        output_object.p_f_file.save_pvd_object(temp_pf)
        if(MPI.rank(comm) == 0):
            print >>output_object.fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, V_cav, 0.0, 0.0, 0.0

    functions["w"] = w

    return functions, arrays_and_values
