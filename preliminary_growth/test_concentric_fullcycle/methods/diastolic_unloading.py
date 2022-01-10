# @Author: charlesmann
# @Date:   2021-12-29T15:26:09-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-03T16:00:23-05:00

from dolfin import *

def diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs,ref_vol,iter_number,total_sol_file,p_f_file):

    unloading_file = File('./output/iter_'+str(iter_number)+'/unload_disp.pvd')

    n_load_steps = 10

    LVCavityvol = functions["LVCavityvol"]

    LVCavityvol.vol = uflforms.LVcavityvol()

    total_vol_loading = LVCavityvol.vol - ref_vol
    volume_increment = total_vol_loading/n_load_steps

    w = functions["w"]

    for lmbda_value in range(0, n_load_steps):

        print "Diastolic unloading step " + str(lmbda_value)

        LVCavityvol.vol -= volume_increment

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        #hsl_array_old = hsl_array

        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        # Save displacement to check the loading
        unloading_file << w.sub(0)
        total_sol_file << w.sub(0)
        pk2_global, sff = uflforms.stress(functions["hsl"])
        temp_pf = project(inner(functions["f0"],pk2_global*functions["f0"]),fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
        temp_pf.rename("pf","pf")
        p_f_file << temp_pf


    functions["w"] = w


    return functions
