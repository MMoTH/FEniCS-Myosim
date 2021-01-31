import numpy as np


## define heterogeneous parameters based on some rule
def assign_heterogeneous_params(sim_params,hs_params_list,passive_params_list,geo_options,fcn_list,no_of_int_points):

    # For fiber simulations, ends need to not contract, and may have different
    # stiffness than the contractile tissue
    if sim_params["simulation_geometry"][0] == "cylinder" or sim_params["simulation_geometry"][0] == "box_mesh" or sim_params["simulation_geometry"][0] == "gmesh_cylinder":

        end_marker_array = geo_options["end_marker_array"]

        fibrous_c  = geo_options["fibrous_c"]
        fibrous_c2 = geo_options["fibrous_c2"]
        fibrous_c3 = geo_options["fibrous_c3"]

        for jj in np.arange(no_of_int_points):
            #print "type" +str(end_marker_array[jj])

            if end_marker_array[jj] > 9.0 or end_marker_array[jj] < 1.0:
                hs_params_list[jj]["myofilament_parameters"]["k_3"][0] = 0.0
                passive_params_list[jj]["c"]  = fibrous_c[0]
                passive_params_list[jj]["c2"] = fibrous_c2[0]
                passive_params_list[jj]["c3"] = fibrous_c3[0]

                fcn_list[0].vector()[jj] = fibrous_c[0]
                fcn_list[1].vector()[jj] = fibrous_c2[0]
                fcn_list[2].vector()[jj] = fibrous_c3[0]
            else:

                #passive_params_list[jj]["c"] = passive_params_list[jj]["c"]
                #passive_params_list[jj]["c2"] = passive_params_list[jj]["c2"]
                #passive_params_list[jj]["c3"] = passive_params_list[jj]["c3"]
                fcn_list[0].vector()[jj] = passive_params_list[jj]["c"][0]
                fcn_list[1].vector()[jj] = passive_params_list[jj]["c2"][0]
                fcn_list[2].vector()[jj] = passive_params_list[jj]["c3"][0]

    else:

        for jj in np.arange(no_of_int_points):

            # assign them to be homogeneous until I put the option into the instruction files
            fcn_list[0].vector()[jj] = passive_params_list[0]["c"][0]
            fcn_list[1].vector()[jj] = passive_params_list[0]["c2"][0]
            fcn_list[2].vector()[jj] = passive_params_list[0]["c3"][0]


    return fcn_list,hs_params_list,passive_params_list
