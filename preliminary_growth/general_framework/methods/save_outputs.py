# @Author: charlesmann
# @Date:   2022-01-04T16:33:04-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-07T14:38:39-05:00

from dolfin import *

def save(total_sol_file, p_f_file, theta_file, dev_file, mesh, functions, fcn_spaces, uflforms, growth_iter_counter):

    # Want to check passive stress
    pk2_global, sff = uflforms.stress(functions["hsl"])

    # Save grown mesh
    grown_mesh_file = File("./fc_output/iter_"+str(growth_iter_counter)+"/"+"grown_mesh.pvd")
    grown_mesh_file << mesh

    # Save displacement
    total_sol_file << functions["w"].sub(0)
    temp_pf = project(inner(functions["f0"],pk2_global*functions["f0"]),fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    temp_pf.rename("pf","pf")
    p_f_file << temp_pf

    temp2 = project(functions["theta_ff"],fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    temp2.rename('theta_ff','theta_ff')
    theta_file << temp2

    temp = project(functions["deviation_ss"],fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    temp.rename('deviation_ss','deviation_ss')
    dev_file << temp

    # probably don't want to save this here. Save in diastolic filling?
    #p_cav = uflforms.LVcavitypressure()
    #print >> pv_file, p_cav*0.0075 , uflforms.LVcavityvol()
