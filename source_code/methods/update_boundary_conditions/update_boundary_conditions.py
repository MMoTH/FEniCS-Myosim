from dolfin import *
import numpy as np

def update_bcs(bcs,sim_geometry,Ftotal,geo_options,sim_protocol,expr,time,traction_switch_flag,x_dofs,test_marker_fcn,w,mesh,bcright,x_dir,l,W,facetboundaries,custom_disp,comm):
    print "x_dofs",x_dofs 
    dm = W.sub(0).dofmap()
    local_range = dm.ownership_range()
    local_dim = local_range[1] - local_range[0]
    x_dofs_local = x_dofs - local_range[0] 
    output_dict = {}
    #print "updating bcs"
    # only really need to update if not ventricle simulation
    if (sim_geometry != "ventricle") and (sim_geometry != "ellipsoid"):

        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})

        for boundary_condition_i in np.arange(np.shape(bcs)[0]-1):
            bcs[boundary_condition_i+1].apply(b)

        if sim_geometry == "unit_cube":
            area = 1.0
        elif sim_geometry == "cylinder":
            area = 3.14*geo_options["end_radius"][0]**2 #assuming enough segments are used to approximate a circle
        elif sim_geometry == "gmesh_cylinder":
            area = 3.05304
        elif sim_geometry == "box_mesh":
            area = 1.0

        f_int_total = b.copy()
        print "f int local size", f_int_total.local_size()
        #print f_int_total[0]
        #f_int_global = Vector()
        #f_int_total.vec().gather(f_int_global, np.array(range(VectorFunctionSpace(mesh,"CG",2).dim())), "intc")
        #print "f int total",f_int_total
        rxn_force=0.0
        #V2 = VectorFunctionSpace(mesh,"CG",2)
        #dm = V2.dofmap()
        #local_range = dm.ownership_range()
        #x_dofs = V2.sub(0).dofmap().dofs()-local_range[0]
        #print("x dofs 2",x_dofs)
        for kk in x_dofs_local:
            rxn_force += f_int_total[kk]
            #rxn_force += f_int_global[kk] 
        print("rxn force",rxn_force)
        global_rxn_force = comm.reduce(rxn_force)
        global_rxn_force = comm.bcast(global_rxn_force)
        print("global rxn",global_rxn_force)
        output_dict["rxn_force"] = global_rxn_force
        print("dictionary value", output_dict["rxn_force"][0])

        #expr["P"].P = temp_traction # trying to remove traction, calculate rxn force, then re-apply traction

    # If ramp and hold
        # u_D.u_D = whatever it's supposed to be

    if sim_protocol["simulation_type"][0] == "work_loop":
        #print "in work loop updating bc"

        if traction_switch_flag < 1: # haven't switched bcs yet
            temp_stress = global_rxn_force/area
            #print 'rxn_force: ', rxn_force
            #print 'temp_stress: ', temp_stress

            if -1*temp_stress[0] >= sim_protocol["traction_magnitude"][0]:
                #print "switching to traction boundary condition"
                expr["Press"].P = sim_protocol["traction_magnitude"][0]
                if sim_geometry == "cylinder" or sim_geometry == "box_mesh" or sim_geometry == "gmesh_cylinder":
                   # bcs = [bcleft,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right]
		            bcs.pop() # remove bcright from boundary conditions
                if sim_geometry == "unit_cube": #bcleft and such are not passed in. Can probably use .pop() here too
                    bcs.pop()
                traction_switch_flag = 1
                sim_protocol["traction_switch_index"] = l
                output_dict["traction_switch_flag"] = traction_switch_flag
                output_dict["bcs"] = bcs
                output_dict["expr"]=expr

            else:
                # still in the ramp and hold stage
                expr["u_D"].u_D = ramp_and_hold(time,sim_protocol,geo_options,expr["u_D"].u_D)
                output_dict["bcs"] = bcs
                output_dict["expr"]=expr
                output_dict["traction_switch_flag"] = traction_switch_flag
                #u_check = project(w.sub(0),VectorFunctionSpace(mesh,"CG",2))
                #File('u_check.pvd') << project(u_check, VectorFunctionSpace(mesh,"CG",2))
                u_x = inner(w.sub(0),x_dir)
                u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
                File('u_x.pvd') << u_x_projection
                u_temp,p_temp = w.split(True)
                #print "u temp evaluated at right face?"
                ux = inner(u_temp,x_dir)
                ux_proj = project(ux,FunctionSpace(mesh,"CG",1))
                #print ux_proj.vector()[test_marker_fcn.vector()==1]
                #print u_temp.vector()[test_marker_fcn.vector()==1]
                #print "test_marker shape: ", np.shape(test_marker_fcn.vector())
                #print "test marker vals: ",test_marker_fcn.vector()[test_marker_fcn.vector()==1]
                #print "u x proj shape: " , np.shape(u_x_projection.vector())
                disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
                #print "disp_value: ", disp_value
                #print "max of disp: ", max(disp_value)


        elif traction_switch_flag == 1:
            # already switched to traction. Keep everything the same unless displacement is back to original value
            u_x = inner(w.sub(0),x_dir)
            u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
            File('u_x.pvd') << u_x_projection
            #print "test_marker shape: ",np.shape(test_marker_fcn.vector())
            #print "test marker vals: ",test_marker_fcn.vector()[test_marker_fcn.vector()==1]
            #print "u x proj shape: ",np.shape(u_x_projection.vector())
            disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
            #print "disp_value: ",disp_value
            if len(disp_value) > 0:
                sim_protocol["end_disp_array"][l] = max(disp_value)
            #if max(disp_value) >= 0.99 and time > 194.0: # value of 1 is hard coded for now
            if ((sim_protocol["end_disp_array"][l] - sim_protocol["end_disp_array"][l-1])>=0.0) and (l > sim_protocol["traction_switch_index"] + 2):
                #expr["u_D"].u_D = (sim_protocol["end_disp_array"][l]+min(disp_value))/2.
                temp_V = VectorFunctionSpace(mesh,"CG",2)
                temp_fcn = Function(temp_V)
                u,p = w.split(True)
                temp_fcn.assign(u)
                bcright_2 = DirichletBC(W.sub(0),temp_fcn,facetboundaries, 2)
                traction_switch_flag = 2
                expr["Press"].P = 0.0
                #bcs.append(bcright)
                bcs.append(bcright_2)
                #bcright.apply(w.sub(0).vector())
                #bcs.append(sim_protocol["bcright_after"])
            expr["Press"].P = expr["Press"].P
            bcs = bcs
            output_dict["traction_switch_flag"] = traction_switch_flag
            output_dict["bcs"] = bcs
            output_dict["expr"]=expr

        elif traction_switch_flag == 2:
            # switched back to displacement bdry, don't do anything
        	expr["Press"].P = 0.0
        	expr["u_D"].u_D = expr["u_D"].u_D
        	output_dict["traction_switch_flag"] = traction_switch_flag
        	output_dict["bcs"] = bcs
        	output_dict["expr"] = expr

        output_dict["previous_rxn_force"] = global_rxn_force

    elif sim_protocol["simulation_type"][0] == "stress_strain_loop":

        diastole = sim_protocol["diastole"]
        isovolumic = sim_protocol["isovolumic"]
        ejection = sim_protocol["ejection"]

        print "diastole: ", diastole
        print "isovolumic: ", isovolumic
        print "ejection: ", ejection

        #Diastolic Loading/Lengthening
        if diastole == 1:

            cycle_time = sim_protocol["track_and_update"]["cycle_time"][0]

            expr["Press"].P = traction_ramp_and_hold(cycle_time,sim_protocol,geo_options)
            #print "traction (diastole): ", expr["Press"].P

            if cycle_time == sim_protocol["end_diastolic_time"][0]:
                temp_V = VectorFunctionSpace(mesh,"CG",2)
                temp_fcn = Function(temp_V)
                u,p = w.split(True)
                temp_fcn.assign(u)
                bcright_2 = DirichletBC(W.sub(0),temp_fcn,facetboundaries, 2)
                bcs.append(bcright_2)
                expr["Press"].P = 0.0
                expr["u_D"].u_D = expr["u_D"].u_D
                sim_protocol["diastole"] = 0
                sim_protocol["isovolumic"] = 1

            output_dict["bcs"] = bcs
            output_dict["expr"] = expr

        # Isovolumic Contraction
        if isovolumic == 1:

            fx_press = rxn_force/area

            if -1*fx_press[0] <= sim_protocol["afterload"][0]:
                #fix displacement
                expr["u_D"].u_D = expr["u_D"].u_D
                #print "current displacement: ", expr["u_D"].u_D

            else:
                sim_protocol["isovolumic"] = 0
                sim_protocol["ejection"] = 1
                sim_protocol["traction_switch_index"] = sim_protocol["track_and_update"]["cycle_time"][0]
                bcs.pop()
                expr["Press"].P = sim_protocol["afterload"][0]
                # Storing previous end disp for ejection phase
                u_x = inner(w.sub(0),x_dir)
                u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
                disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
                sim_protocol["previous_end_disp"] = disp_value
                #print 'previous_end_disp: ', sim_protocol["previous_end_disp"]

            output_dict["bcs"] = bcs
            output_dict["expr"] = expr

        if ejection == 1:

            u_x = inner(w.sub(0),x_dir)
            u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
            File('u_x.pvd') << u_x_projection
            u_temp,p_temp = w.split(True)
            ux = inner(u_temp,x_dir)
            ux_proj = project(ux,FunctionSpace(mesh,"CG",1))
            disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
            #print "disp_value: ", disp_value
            #print "previous end disp: ", sim_protocol["previous_end_disp"]
            #print "max of disp: ", max(disp_value)

            if ((disp_value[0] - sim_protocol["previous_end_disp"][0]) >= 0.0) and (sim_protocol["track_and_update"]["cycle_time"][0] > sim_protocol["traction_switch_index"] + 2):
                sim_protocol["ejection"] = 0
                sim_protocol["isovolumic"] = 2
                temp_V = VectorFunctionSpace(mesh,"CG",2)
                temp_fcn = Function(temp_V)
                u,p = w.split(True)
                temp_fcn.assign(u)
                bcright_2 = DirichletBC(W.sub(0),temp_fcn,facetboundaries, 2)
                bcs.append(bcright_2)
                expr["Press"].P = 0.0
                expr["u_D"].u_D = expr["u_D"].u_D
                sim_protocol["previous_rxn_force"] = rxn_force
                #print 'rxn_force: ', sim_protocol["previous_rxn_force"]

            sim_protocol["previous_end_disp"] = disp_value
            output_dict["bcs"] = bcs
            output_dict["expr"] = expr

        if isovolumic == 2:
            #print 'previous rxn force: ', sim_protocol["previous_rxn_force"]
            #print 'current rxn force: ', rxn_force
            if abs(rxn_force[0] - sim_protocol["previous_rxn_force"][0]) >= 5:
                expr["u_D"].u_D = expr["u_D"].u_D
                #print "current displacement: ", expr["u_D"].u_D
            else:
		bcs.pop()
                press_rxn = rxn_force/area
		#print 'press_rxn: ',press_rxn
                expr["Press"].P = -1*press_rxn[0]
                sim_protocol["start_diastolic_pressure"] = -1*press_rxn[0]
                #expr["Press"].P = 0.0
                sim_protocol["isovolumic"] = 0
                sim_protocol["diastole"] = 1
                #print "cycle period: ", sim_protocol["track_and_update"]["cycle_time"][0]
                sim_protocol["track_and_update"]["cycle_time"][0] = -1*sim_protocol["simulation_timestep"][0]
                sim_protocol["track_and_update"]["cycle_l"][0] = -1

            output_dict["bcs"] = bcs
            output_dict["expr"] = expr

        sim_protocol["previous_rxn_force"] = rxn_force
        output_dict["traction_switch_flag"] = traction_switch_flag
        sim_protocol["track_and_update"]["cycle_time"][0] += sim_protocol["simulation_timestep"][0]
        #print "next cycle_time",sim_protocol["track_and_update"]["cycle_time"][0]
        sim_protocol["track_and_update"]["cycle_l"][0] += 1
        #print "next cycle_l",sim_protocol["track_and_update"]["cycle_l"][0]


    elif sim_protocol["simulation_type"][0] == "ramp_and_hold" or sim_protocol["simulation_type"][0] == "ramp_and_hold_simple_shear" or sim_protocol["simulation_type"][0] == "ramp_and_hold_biaxial":
        expr["u_D"].u_D = ramp_and_hold(time,sim_protocol,geo_options,expr["u_D"].u_D)
        #print "u_D: ",expr["u_D"].u_D
        expr["u_front"].u_front = (1./((1.+expr["u_D"].u_D)*(1.+expr["u_D"].u_D))-1.)

        #print "u_front",expr["u_front"].u_front
        output_dict["expr"] = expr
        output_dict["traction_switch_flag"] = traction_switch_flag
        #print "assigning bcs"
        output_dict["bcs"] = bcs
        output_dict["rxn_force"] = global_rxn_force

    elif sim_protocol["simulation_type"][0] == "traction_hold":
        expr["Press"].P = traction_hold(time,sim_protocol,geo_options,expr["Press"].P)
        output_dict["expr"] = expr
        output_dict["traction_switch_flag"] = traction_switch_flag
        #print "assigning bcs"
        output_dict["bcs"] = bcs
        output_dict["rxn_force"] = global_rxn_force


    elif sim_protocol["simulation_type"][0] == "custom":
        expr["u_D"].u_D = custom_disp[l+1]
        #print "u_D: ",expr["u_D"].u_D
        output_dict["expr"] = expr
        output_dict["traction_switch_flag"] = traction_switch_flag
        #print "assigning bcs"
        output_dict["bcs"] = bcs
        output_dict["rxn_force"] = rxn_force

    if sim_geometry == "ventricle" or sim_geometry == "ellipsoid":
        #don't change bcs
        output_dict["bcs"] = bcs


    return output_dict

def traction_hold(time,sim_protocol,geo_options,cur_disp):

    """geo_check = not geo_options
    if geo_check:
        # unit cube
        length_scale = 1.0
    else:
        length_scale = geo_options["end_x"][0]
        print "length scale = " + str(length_scale)"""

    length_scale = 1.0

    if time < sim_protocol["tract_t_start"][0]:
        disp = cur_disp
        #print "Traction magnitude is " + str(disp)

    elif time >= sim_protocol["tract_t_end"][0]:
        disp = length_scale*sim_protocol["tract_magnitude"][0]
        #print "Traction magnitude is " + str(disp)
    else:
        slope = sim_protocol["tract_magnitude"][0]/(sim_protocol["tract_t_end"][0]-sim_protocol["tract_t_start"][0])
        disp = length_scale*slope*time
        #print "Traction magnitude is " + str(disp)

    return disp

def ramp_and_hold(time,sim_protocol,geo_options,cur_disp):

    geo_check = not geo_options
    #print("CHECKING GEO OPTIONS")
    #print(geo_options)
    if geo_check:
        # unit cube
        length_scale = 1.0
    else:
        length_scale = geo_options["end_x"][0]
        #print "length scale = " + str(length_scale)

    if time < sim_protocol["ramp_t_start"][0]:
        disp = cur_disp
        #print "time < t start"
        #print "displacement is " + str(disp)

    elif time >= sim_protocol["ramp_t_end"][0]:
        disp = length_scale*sim_protocol["ramp_magnitude"][0]
        #print "time > t_end"
        #print "displacement is " + str(disp)
    else:
        slope = sim_protocol["ramp_magnitude"][0]/(sim_protocol["ramp_t_end"][0]-sim_protocol["ramp_t_start"][0])
        disp = length_scale*slope*time
        #print "time in the middle"
        #print "displacement is " + str(disp)

    return disp

"""def traction_ramp_and_hold(cycle_time,sim_protocol,geo_options):

    # created for stress_strain_loop protocol

    length_scale = 1.0

    if cycle_time >= sim_protocol["end_diastolic_time"][0]:
        traction = length_scale*sim_protocol["end_diastolic_stress"][0]
        print "Traction magnitude is " + str(traction)
    else:
        slope = (sim_protocol["end_diastolic_stress"][0])/(sim_protocol["end_diastolic_time"][0])
        traction = length_scale*slope*cycle_time
        print "Traction magnitude is " + str(traction)

    return traction
"""
def traction_ramp_and_hold(time,sim_protocol,geo_options):
    # use if reaction stress at end systole nonzero in simulation

    length_scale = 1.0

    if time >= sim_protocol["end_diastolic_time"][0]:
        traction = length_scale*sim_protocol["end_diastolic_stress"][0]
        #print "Traction magnitude is " + str(traction)
    else:
        slope = (sim_protocol["end_diastolic_stress"][0] - sim_protocol["start_diastolic_pressure"])/(sim_protocol["end_diastolic_time"][0])
        traction = length_scale*slope*time + sim_protocol["start_diastolic_pressure"]
        #print "Traction magnitude is " + str(traction)

    return traction
