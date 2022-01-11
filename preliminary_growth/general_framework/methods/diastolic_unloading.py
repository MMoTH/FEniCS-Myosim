# @Author: charlesmann
# @Date:   2021-12-29T15:26:09-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-10T22:04:50-05:00

from dolfin import *

def diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs,ref_vol,output_object, n_load_steps):

    #unloading_file = File('./output/iter_'+str(iter_number)+'/unload_disp.pvd')

    #n_load_steps = 10

    LVCavityvol = functions["LVCavityvol"]

    LVCavityvol.vol = uflforms.LVcavityvol()

    total_vol_loading = LVCavityvol.vol - ref_vol
    volume_increment = total_vol_loading/n_load_steps

    # Need to unload active stress as well
    unloading_stress_increment = functions["cbforce"].f/n_load_steps

    w = functions["w"]

    for lmbda_value in range(0, n_load_steps):

        print "Diastolic unloading step " + str(lmbda_value)

        LVCavityvol.vol -= volume_increment
        functions["cbforce"].f -= unloading_stress_increment

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        #hsl_array_old = hsl_array

        # ********************************************************
        # DO WE NEED PACTIVE TO BE SET TO ZERO FOR THIS???
        # ********************************************************

        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        # Save displacement to check the loading
        #unloading_file << w.sub(0)
        output_object.total_sol_file.save_pvd_object(w.sub(0))
        pk2_global, sff = uflforms.stress(functions["hsl"])
        temp_pf = project(inner(functions["f0"],pk2_global*functions["f0"]),fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
        temp_pf.rename("pf","pf")
        output_object.p_f_file.save_pvd_object(temp_pf)


    functions["w"] = w


    return functions
