from dolfin import *
import numpy as np
import pandas as pd


def save_solution(output_path,mesh,f0,n0,s0,facetboundaries,edgeboundaries,subdomains,LVCavityvol,u_D,u_top,u_front,Press,hs_params_list,dolfin_functions,W,w,hsl,y_vec,bcs,concentric_growth_stimulus,eccentric_growth_stimulus,cb_f_array,p_f_array):

    print "saving solution"
    f = HDF5File(mpi_comm_world(), output_path+"solution.hdf5",'w')
    columns = ['LVCavityvol','u_D','u_top','u_front','Press']
    sol_df = pd.DataFrame(columns=columns)

    # save mesh
    f.write(mesh,"/mesh")

    # save local coordinate system
    f.write(f0,"/f0")
    f.write(n0,"/n0")
    f.write(s0,"/s0")

    # Save other mesh information
    f.write(facetboundaries,"/facetboundaries")
    f.write(edgeboundaries,"/edgeboundaries")
    f.write(subdomains,"/subdomains")

    f.write(concentric_growth_stimulus,"/concentric_growth_stimulus")
    f.write(eccentric_growth_stimulus,"/eccentric_growth_stimulus")

    # Save expressions
    # Save as numpy?

    #f.write(temp,"/LVCavityvol")
    row = {'LVCavityvol':[LVCavityvol.vol],'u_D':[u_D.u_D],'u_top':[u_top.u_top],'u_front':[u_front.u_front],'Press':[Press.P]}
    sol_df = pd.DataFrame(data=row)

    np.save(output_path+'cb_f_array',cb_f_array)
    np.save(output_path+'p_f_array',p_f_array)


    #f.write(W,"W")

    # Save solution
    f.write(w,"w")

    # Save hsl0
    f.write(hsl,"hsl")

    # Save growth stimuli
    # Using end diastolic stress and end systolic stress for now.

    # Save myosim populations
    f.write(y_vec,"y_vec")

    """if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):

        # save windkessel stuff
        columns_wk = ['V_ven','V_art','Part','PLV','Pven']
        sol_df_wk = pd.DataFrame(columns=columns)
        row_wk = {'V_ven':wk_params["V_ven"],'V_art':wk_params["V_art"],'Part':wk_params["Part"],'PLV':wk_params["PLV"],'Pven':wk_params["Pven"]}
        sol_df_wk = pd.DataFrame(data=row)
        sol_df_wk.to_csv(output_path+'sol_df_wk.csv')"""







    # Maybe we can just get these set up like the original simulation
    # Save all initialized dolfin functions
    #f.write(dolfin_functions,"dolfin_functions")


    # Save list of half-sarcomere params. hs_params_list[i] is the full set of params for integration point i
    #f.write(hs_params_list,"hs_params_list")




    # Save boundary conditions
    #f.write(bcs,"bcs")

    f.close()
    sol_df.to_csv(output_path+'sol_df.csv')

    return()
