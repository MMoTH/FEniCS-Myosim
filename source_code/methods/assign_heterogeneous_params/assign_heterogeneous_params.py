from dolfin import *
import numpy as np
import numpy.random as r


## define heterogeneous parameters based on some rule
def assign_heterogeneous_params(sim_params,hs_params_template,hs_params_list,dolfin_functions,geo_options,no_of_int_points,no_of_cells):

    # Going to directly go through hs_params_list and then dolfin_functions and check for heterogeneity
    # hs_params_template is the base copy of myosim parameters, loop through this
    seed = sim_params["rseed"][0]
    r.seed(seed)

    # create empty dictionary that will hold keys for heterogeneous hs parameters
    het_hs_dict = {}

    # fill het_hs_dict with any keys that are flagged as heterogeneous
    het_hs_dict = iterate_hs_keys(hs_params_template,het_hs_dict)

    # assign heterogeneous parameters based on the desired law
    hs_params_list = assign_hs_values(het_hs_dict,hs_params_list,no_of_int_points,geo_options) #geo_options will contain information for specific spatial variations

    # create empty dictionary to hold keys for heterogeneous dolfin functions
    het_dolfin_dict = {}

    # fill het_dolfin_dict with any keys that are flagged as heterogeneous
    #print "dolfin functions"
    #rint dolfin_functions
    het_dolfin_dict = iterate_dolfin_keys(dolfin_functions,het_dolfin_dict)

    # assign heterogeneous parametrs based on the desired law
    dolfin_functions = assign_dolfin_functions(dolfin_functions,het_dolfin_dict,no_of_int_points,no_of_cells,geo_options)

    # Kurtis needs to update this
    #--------------------------------------------------------
    # For fiber simulations, ends need to not contract, and may have different
    # stiffness than the contractile tissue
    """if sim_params["simulation_geometry"][0] == "cylinder" or sim_params["simulation_geometry"][0] == "box_mesh" or sim_params["simulation_geometry"][0] == "gmesh_cylinder":

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
            fcn_list[2].vector()[jj] = passive_params_list[0]["c3"][0]"""


    return hs_params_list,dolfin_functions

def iterate_hs_keys(hs_template,het_hs_dict):

    for k, v in hs_template.items():

        if isinstance(v,dict):
            iterate_hs_keys(v,het_hs_dict)

        else:
            # got actual parameter value list, not another dictionary
            for j in v:
                if isinstance(j,dict):
                    if k == "cb_number_density":
                        print "something"
                    else:
                        check = j["heterogeneous"]
                        if (check=="true") or (check =="True"):
                            # this parameters should be homogeneous
                            temp_law = j["law"]
                            base_value = v[0] #first entry is base value
                            het_hs_dict[k]=[base_value,temp_law]
                            if temp_law == "gaussian":
                                if "width" in j:
                                    width = j["width"]
                                else:
                                    width = 0
                                het_hs_dict[k].append(width)
                            if temp_law == "percent_fibrosis":
                                if "percent" in j:
                                    percent = j["percent"]
                                else:
                                    percent = 0.33
                                if "scaling_factor" in j:
                                    scaling_factor = j["scaling_factor"]
                                else:
                                    scaling_factor = 20
                                het_hs_dict[k].append(percent)
                                het_hs_dict[k].append(scaling_factor)
                            if temp_law == "fiber_w_compliance":
                                if "fiber_value" in j:
                                    fiber_value = j["fiber_value"]
                                else:
                                    fiber_value = base_value
                                het_hs_dict[k].append(fiber_value)

    return het_hs_dict

def assign_hs_values(het_hs_dict,hs_params_list,no_of_int_points,geo_options):

    for k in het_hs_dict.keys():
        base_value = het_hs_dict[k][0]
        hetero_law = het_hs_dict[k][1]
        if hetero_law == "gaussian":
            hs_params_list = scalar_gaussian_law(hs_params_list,base_value,k,het_hs_dict[k][-1],no_of_int_points)

        if hetero_law == "percent_fibrosis":
            hs_params_list = scalar_fibrosis_law(hs_params_list,base_value,k,het_hs_dict[k][-2],het_hs_dict[k][-1],no_of_int_points)
        if hetero_law == "fiber_w_compliance":
            hs_params_list = scalar_fiber_w_compliance_law(hs_params_list,base_value,k,het_hs_dict[k][-1],no_of_int_points,geo_options)

        else:
            print "instruction file law is",hetero_law
            print "invalid law. Please choose from `gaussian` or `percent_fibrosis`, or 'fiber_w_compliance'"

    return hs_params_list

def iterate_dolfin_keys(dolfin_functions,het_dolfin_dict):
    #print "dolfin function"
    #print dolfin_functions
    for k, v in dolfin_functions.items():

        if isinstance(v,dict):
            iterate_dolfin_keys(v,het_dolfin_dict)

        else:
            # got actual parameter value list, not another dictionary
            for j in v:
                if isinstance(j,dict):
                    check = j["heterogeneous"]
                    if (check=="true") or (check=="True"):
                        #print "there is a hetero dict"
                        #print k
                        # this parameter should be homogeneous
                        temp_law = j["law"]
                        base_value = v[0] #first entry is base value
                        het_dolfin_dict[k]=[base_value,temp_law]
                        #print "het_dolfin_dict"
                        #print het_dolfin_dict
                        if temp_law == "gaussian":
                            if "width" in j:
                                width = j["width"]
                            else:
                                width = 1
                            het_dolfin_dict[k].append(width)
                        if temp_law == "percent_fibrosis":
                            if "percent" in j:
                                percent = j["percent"]
                            else:
                                percent = 0.33
                            if "scaling_factor" in j:
                                scaling_factor = j["scaling_factor"]
                            else:
                                scaling_factor = 20
                            if "material_properties" in j:
                                mat_prop = j["material_properties"]
                            else:
                                mat_prop = "transversely_isotropic"
                            het_dolfin_dict[k].append(percent)
                            het_dolfin_dict[k].append(scaling_factor)
                            het_dolfin_dict[k].append(mat_prop)
                        if temp_law == "fiber_w_compliance":
                            if "fiber_value" in j:
                                fiber_value = j["fiber_value"]
                            else:
                                fiber_value = base_value
                            het_dolfin_dict[k].append(fiber_value)
			if temp_law == "fibrosis_w_compliance":
			    if "compliance_value" in j:
				compliance_value = j["compliance_value"]
			    else:
				compliance_value = base_value
			    if "percent" in j:
				percent = j["percent"]
			    else:
				percent = 0.33
			    if "scaling_factor" in j:
				scaling_factor = j["scaling_factor"]
			    else:
				scaling_factor = 20
			    if "material_properties" in j:
				mat_prop = j["material_properties"]
			    else:
				mat_prop = "transversely_isotropic"
			    het_dolfin_dict[k].append(compliance_value)
                            het_dolfin_dict[k].append(percent)
                            het_dolfin_dict[k].append(scaling_factor)
                            het_dolfin_dict[k].append(mat_prop)
                        if temp_law == "fiber_w_compliance_boxmesh":
                            if "fiber_value" in j:
                                fiber_value = j["fiber_value"]
                            else:
                                fiber_value = base_value
                            het_dolfin_dict[k].append(fiber_value)
                        if temp_law == "inclusion":
                            if "scaling_factor" in j:
                                scaling_factor = j["scaling_factor"]
                            else:
                                scaling_factor = 20
                            if "material_properties" in j:
                                mat_prop = j["material_properties"]
                            else:
                                mat_prop = "transversely_isotropic"
                            het_dolfin_dict[k].append(scaling_factor)
                            het_dolfin_dict[k].append(mat_prop)
                        if temp_law == "biphasic":
                            if "normal" in j:
                                normal = j["normal"]
                            else:
                                normal = "y"
                            if "scaling_factor" in j:
                                scaling_factor = j["scaling_factor"]
                            else:
                                scaling_factor = 20
                            if "material_properties" in j:
                                mat_prop = j["material_properties"]
                            else:
                                mat_prop = "transversely_isotropic"
                            het_dolfin_dict[k].append(normal)
                            het_dolfin_dict[k].append(scaling_factor)
                            het_dolfin_dict[k].append(mat_prop)
                        if temp_law == "percent_contractile":
                            if "percent" in j:
                                percent = j["percent"]
                            else:
                                percent = 0.33
                            if "width" in j:
                                width = j["width"]
                            else:
                                width = 1
                            if "scaling_factor" in j:
                                scaling_factor = j["scaling_factor"]
                            else:
                                scaling_factor = 1.0
                            if "contract_option" in j:
                                contract_option = "no_contract"
                            else:
                                contract_option = "gauss_contract"
                            het_dolfin_dict[k].append(percent)
                            het_dolfin_dict[k].append(width)
                            het_dolfin_dict[k].append(scaling_factor)
                            het_dolfin_dict[k].append(contract_option)
                        if temp_law == "rat_ellipsoid_infarct":
                            if "scaling_factor" in j:
                                scaling_factor = j["scaling_factor"]
                                het_dolfin_dict[k].append(scaling_factor)

    return het_dolfin_dict

def assign_dolfin_functions(dolfin_functions,het_dolfin_dict,no_of_int_points,no_of_cells,geo_options):

    for k in het_dolfin_dict.keys():
        #print "het_dolfin_dict"
        #print k
        #print "assigning functions"
        #print het_dolfin_dict
        #print k
        base_value = het_dolfin_dict[k][0]
        hetero_law = het_dolfin_dict[k][1]

        if hetero_law == "gaussian":
            dolfin_functions = df_gaussian_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-1],no_of_int_points)

        if hetero_law == "percent_fibrosis":
            dolfin_functions = df_fibrosis_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-3],het_dolfin_dict[k][-2],het_dolfin_dict[k][-1],no_of_cells)

        if hetero_law == "fiber_w_compliance":
            dolfin_functions = df_fiber_w_compliance_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-1],no_of_cells,no_of_int_points,geo_options)
        """if hetero_law == "fiber_w_compliance_boxmesh":
            dolfin_functions = df_fiber_w_compliance_law_boxmesh(dolfin_functions,base_value,k,het_dolfin_dict[k][-1],no_of_int_points,geo_options)"""

	if hetero_law == "fibrosis_w_compliance":
            dolfin_functions = df_fibrosis_w_compliance_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-4],het_dolfin_dict[k][-3],het_dolfin_dict[k][-2],het_dolfin_dict[k][-1],no_of_cells,geo_options)

        if hetero_law == "inclusion":
            dolfin_functions = df_inclusion_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-2],het_dolfin_dict[k][-1],no_of_cells,geo_options)

        if hetero_law == "biphasic":
            dolfin_functions = df_biphasic_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-3],het_dolfin_dict[k][-2],het_dolfin_dict[k][-1],no_of_cells,geo_options)

        if hetero_law == "percent_contractile":
            dolfin_functions = df_contractile_law(dolfin_functions,base_value,k,het_dolfin_dict[k][-4],het_dolfin_dict[k][-3],het_dolfin_dict[k][-2],het_dolfin_dict[k][-1],no_of_cells,geo_options)

        if hetero_law == "rat_ellipsoid_infarct":
            dolfin_functions = df_rat_ellipsoid_infarct(dolfin_functions,base_value,k,het_dolfin_dict[k][-1],no_of_int_points,geo_options)

    return dolfin_functions

def scalar_gaussian_law(hs_params_list,base_value,k,width,no_of_int_points):

    # generate random values for parameter k using gaussian distribution centered at base_value
    # with width specified by user
    values_array = r.normal(base_value,width,no_of_int_points)

    for jj in np.arange(no_of_int_points):
        # right now, assuming that only myofilmaent parameters change
        hs_params_list[jj]["myofilament_parameters"][k][0] = values_array[jj]

    return hs_params_list

def df_gaussian_law(dolfin_functions,base_value,k,width,no_of_int_points):

    values_array = r.normal(base_value,width,no_of_int_points)

    #print "gauss law"
    #print dolfin_functions["passive_params"][k]

    if k == "cb_number_density":
        dolfin_functions[k][-1].vector()[:] = values_array #last element in list is the initialized function
    else:
        dolfin_functions["passive_params"][k][-1].vector()[:] = values_array #last element in list is the initialized function

    return dolfin_functions

def scalar_fibrosis_law(hs_params_list,base_value,k,percent,scaling_factor,no_of_int_points):

    sample_indices = r.choice(no_of_int_points,int(percent*no_of_int_points), replace=False)

    for jj in np.arange(no_of_int_points):

        if jj in sample_indices:

            hs_params_list[jj]["myofilament_parameters"][k][0] == base_value*scaling_factor

    return hs_params_list

def df_fibrosis_law(dolfin_functions,base_value,k,percent,scaling_factor,mat_prop,no_of_cells):

    sample_indices = r.choice(no_of_cells,int(percent*no_of_cells), replace=False)
    #print "sample indices"
    #print sample_indices

    for jj in np.arange(no_of_cells):

        if mat_prop == "isotropic":

            if jj in sample_indices:

                if k == "cb_number_density":
                    dolfin_functions[k][-1].vector()[jj] = base_value*scaling_factor #make 20 specified by user
                else:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = 11750
                    dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
                    dolfin_functions["cb_number_density"][-1].vector()[jj] = 0

        else:

            if jj in sample_indices:

                if k == "cb_number_density":
                    dolfin_functions[k][-1].vector()[jj] = base_value*scaling_factor #make 20 specified by user
                else:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor

    return dolfin_functions

def scalar_fiber_w_compliance_law(hs_params_list,base_value,k,fiber_value,no_of_int_points,geo_options):

    end_marker_array = geo_options["end_marker_array"]
    for jj in np.arange(no_of_int_points):

        if end_marker_array[jj] > 9.0 or end_marker_array[jj] < 1.0:
            hs_params_list[jj]["myofilament_parameters"][k][0] = fiber_value

    return hs_params_list

def df_fiber_w_compliance_law(dolfin_functions,base_value,k,fiber_value,no_of_cells,no_of_int_points,geo_options):

    end_marker_array = geo_options["end_marker_array"]
    fiberFS = geo_options["fiberFS"] # used quad, not fiberFS. Quad is scalar, so just divide this by 3
    dm = fiberFS.dofmap()
    local_range = dm.ownership_range()
    local_dim = local_range[1] - local_range[0]
    local_dim /= 3
    # make array to hold values
    assign_array = base_value*np.ones(int(local_dim))
    #print "base value", base_value
    for jj in np.arange(int(local_dim)):
    #for jj in np.arange(no_of_cells):

        if (end_marker_array[jj] > 9.0) or (end_marker_array[jj] < geo_options["compliance_first_bdry_end"][0]):
            if k == "cb_number_density":
                #print "ASSIGNING CROSSBRIDGE DENSITY", fiber_value
                #dolfin_functions[k][-1].vector()[jj] = fiber_value
                assign_array[jj] = fiber_value
            else:
                #dolfin_functions["passive_params"][k][-1].vector()[jj] = fiber_value
                assign_array[jj] = fiber_value
    if k == "cb_number_density":
        dolfin_functions[k][-1].vector().set_local(assign_array)
        as_backend_type(dolfin_functions[k][-1].vector()).update_ghost_values()
    else:
        dolfin_functions["passive_params"][k][-1].vector().set_local(assign_array)
        as_backend_type(dolfin_functions["passive_params"][k][-1].vector()).update_ghost_values()

    return dolfin_functions

def df_fibrosis_w_compliance_law(dolfin_functions,base_value,k,fiber_value,percent,scaling_factor,mat_prop,no_of_cells,geo_options):

    end_marker_array = geo_options["x_marker_array"]
    compliant_cell_array = []
    remaining_cell_array = []
    total_cell_array = np.arange(no_of_cells)

    for jj in total_cell_array:

        if end_marker_array[jj] < 0.5:
            compliant_cell_array.append(jj)
            """if k == "cb_number_density":
                print "ASSIGNING CROSSBRIDGE DENSITY TO ", fiber_value
                dolfin_functions[k][-1].vector()[jj] = fiber_value
            else:"""
            dolfin_functions["passive_params"][k][-1].vector()[jj] = fiber_value
	    dolfin_functions["cb_number_density"][-1].vector()[jj] = 0

    for index in total_cell_array:
        if index not in compliant_cell_array:
            remaining_cell_array.append(index)
    remaining_no_of_cells = len(remaining_cell_array)
    #print "remaining_cell_array: ", remaining_cell_array
    sample_indices = r.choice(remaining_cell_array,int(percent*remaining_no_of_cells), replace=False)
    #print "sample indices: ", sample_indices

    for jj in remaining_cell_array:

        if mat_prop == "isotropic":

            if jj in sample_indices:

                if k == "cb_number_density":
                    #dolfin_functions[k][-1].vector()[jj] = base_value*scaling_factor #make 20 specified by user
                    #print "don't want to touch density for remaining elements!!!!!"
		    pass
                else:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = 3130 
                    dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
                    dolfin_functions["cb_number_density"][-1].vector()[jj] = 0

        else:

            if jj in sample_indices:

                if k == "cb_number_density":
                    #print "don't want to mess with density here!!!!!"
                    #dolfin_functions[k][-1].vector()[jj] = base_value*scaling_factor #make 20 specified by user
		    pass
                else:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor

    return dolfin_functions

def df_inclusion_law(dolfin_functions,base_value,k,scaling_factor,mat_prop,no_of_cells,geo_options):
    x_marker_array = geo_options["x_marker_array"]
    y_marker_array = geo_options["y_marker_array"]
    z_marker_array = geo_options["z_marker_array"]

    for jj in np.arange(no_of_cells):

        if mat_prop == "isotropic":

            if x_marker_array[jj] > 1.0 and x_marker_array[jj] <= 2.0 and y_marker_array[jj] > 1.0 and y_marker_array[jj] <= 2.0 and z_marker_array[jj] > 1.0 and z_marker_array[jj] <= 2.0:
                dolfin_functions["passive_params"][k][-1].vector()[jj] = 3130 
                dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
        else:

            if x_marker_array[jj] > 1.0 and x_marker_array[jj] <= 2.0 and y_marker_array[jj] > 1.0 and y_marker_array[jj] <= 2.0 and z_marker_array[jj] > 1.0 and z_marker_array[jj] <= 2.0:
                dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor

    return dolfin_functions

def df_biphasic_law(dolfin_functions,base_value,k,normal,scaling_factor,mat_prop,no_of_cells,geo_options):
    x_marker_array = geo_options["x_marker_array"]
    y_marker_array = geo_options["y_marker_array"]
    z_marker_array = geo_options["z_marker_array"]

    x_length = geo_options["end_x"][0] - geo_options["base_corner_x"][0]
    y_length = geo_options["end_y"][0] - geo_options["base_corner_y"][0]
    z_length = geo_options["end_z"][0] - geo_options["base_corner_z"][0]

    for jj in np.arange(no_of_cells):

        if mat_prop == "isotropic":

            if normal == "x":
                if x_marker_array[jj] <= x_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = 3130
                    dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
            elif normal == "y":
                if y_marker_array[jj] <= y_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = 3130
                    dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
            elif normal == "z":
                if z_marker_array[jj] <= z_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = 3130
                    dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                    dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10

        else:

            if normal == "x":
                if x_marker_array[jj] <= x_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor
            elif normal == "y":
                if y_marker_array[jj] <= y_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor
            elif normal == "z":
                if z_marker_array[jj] <= z_length/2:
                    dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor


    return dolfin_functions

def df_contractile_law(dolfin_functions,base_value,k,percent,width,scaling_factor,act_option,no_of_cells,geo_options):

    end_marker_array = geo_options["x_marker_array"]
    
    compliant_cell_array = []
    remaining_cell_array = []
    total_cell_array = np.arange(no_of_cells)

    for jj in total_cell_array:

	# create compliant, non-contracting end and track corresponding indices
        if end_marker_array[jj] < 0.5:
            compliant_cell_array.append(jj)
            dolfin_functions["passive_params"]["c"][-1].vector()[jj] = 26.6 
	    dolfin_functions["cb_number_density"][-1].vector()[jj] = 0

    for index in total_cell_array:
        if index not in compliant_cell_array:
            remaining_cell_array.append(index)
    remaining_no_of_cells = len(remaining_cell_array)
    #print "remaining_cell_array: ", remaining_cell_array
    sample_indices = r.choice(remaining_cell_array,int(percent*remaining_no_of_cells), replace=False)

    values_array = r.normal(0.0,width,int(percent*remaining_no_of_cells))
    value_index_dict = dict(zip(sample_indices,values_array))

    for jj in remaining_cell_array:

        if jj in value_index_dict.keys():

            if act_option == "no_contract":
                dolfin_functions[k][-1].vector()[jj] = 0.0
            else:
                dolfin_functions[k][-1].vector()[jj] = scaling_factor*base_value*(1.0 + value_index_dict[jj])

    return dolfin_functions

def df_rat_ellipsoid_infarct(dolfin_functions,base_value,k,scaling_factor,no_of_int_points,geo_options):
    xq = geo_options["xq"] # coordinate of quadrature points
    for jj in np.arange(no_of_int_points):
    
        r = np.sqrt(xq[jj][1]**2 + (xq[jj][2]+.44089)**2)

        if xq[jj][0] > 0 and (r < .2044):
            dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor
            dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
            dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
            dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
            dolfin_functions["cb_number_density"][-1].vector()[jj] = 0

        if xq[jj][0] > 0 and (r >= .2044):
            if r < (0.25):
                #dolfin_functions["passive_params"][k][-1].vector()[jj] = base_value*scaling_factor
                #dolfin_functions["passive_params"]["bt"][-1].vector()[jj] = 10
                #dolfin_functions["passive_params"]["bf"][-1].vector()[jj] = 10
                #dolfin_functions["passive_params"]["bfs"][-1].vector()[jj] = 10
                dolfin_functions["cb_number_density"][-1].vector()[jj] = 1.513157e18*(r-.2044)    
    return dolfin_functions
