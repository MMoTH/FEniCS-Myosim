from dolfin import *
import numpy as np

def update_bcs(bcs,sim_geometry,Ftotal,geo_options,sim_protocol,expr,time,traction_switch_flag,x_dofs,test_marker_fcn,w,mesh,bcright,x_dir):

    output_dict = {}
    print "updating bcs"
    print sim_protocol["simulation_type"]
    # only really need to update if not ventricle simulation
    if (sim_geometry != "ventricle") and (sim_geometry != "ellipsoid"):

        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})

        for boundary_condition_i in np.arange(np.shape(bcs)[0]-1):
            bcs[boundary_condition_i].apply(b)


        if not geo_options:
            area = 1.0
        elif sim_geometry == "cylinder":
            area = 3.14*geo_options["end_radius"][0]**2 #assuming enough segments are used to approximate a circle
        elif sim_geometry == "gmesh_cylinder":
            area = 3.14
        elif sim_geometry == "box_mesh":
            area = 1.0

        f_int_total = b.copy()
        rxn_force=0.0
        for kk in x_dofs:
            rxn_force += f_int_total[kk]
        output_dict["rxn_force"] = rxn_force

    # If ramp and hold
        # u_D.u_D = whatever it's supposed to be

    if sim_protocol["simulation_type"][0] == "work_loop":
        print "in work loop updating bc"

        if traction_switch_flag < 1: # haven't switched bcs yet
            temp_stress = rxn_force/area

            if temp_stress[0] >= sim_protocol["traction_magnitude"][0]:
                print "switching to traction boundary condition"
                expr["Press"].P = sim_protocol["traction_magnitude"][0]
                if sim_geometry == "cylinder" or sim_geometry == "box_mesh" or sim_geometry == "gmesh_cylinder":
                   # bcs = [bcleft,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right]
		   bcs.pop() # remove bcright from boundary conditions
                if sim_geometry == "unit_cube": #bcleft and such are not passed in. Can probably use .pop() here too
                    bcs = [bcleft, bclower, bcfront,bcfix]
                traction_switch_flag = 1
                output_dict["traction_switch_flag"] = traction_switch_flag
                output_dict["bcs"] = bcs
                output_dict["expr"]=expr

            else:
                # still in the ramp and hold stage
                expr["u_D"].u_D = ramp_and_hold(time,sim_protocol,geo_options)
                output_dict["bcs"] = bcs
                output_dict["expr"]=expr
                output_dict["traction_switch_flag"] = traction_switch_flag
                #u_check = project(w.sub(0),VectorFunctionSpace(mesh,"CG",2))
                #File('u_check.pvd') << project(u_check, VectorFunctionSpace(mesh,"CG",2))
                u_x = inner(w.sub(0),x_dir)
                u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
                File('u_x.pvd') << u_x_projection
                print "test_marker shape"
                print np.shape(test_marker_fcn.vector())
                print "test marker vals"
                print test_marker_fcn.vector()[test_marker_fcn.vector()==1]
                print "u x proj shape"
                print np.shape(u_x_projection.vector())
                disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
                print "disp_value"
                print disp_value
                print "max of disp"
                print max(disp_value)

                
        elif traction_switch_flag == 1:
            # already switched to traction. Keep everything the same unless displacement is back to original value
            u_x = inner(w.sub(0),x_dir)
            u_x_projection = project(u_x,FunctionSpace(mesh,"CG",1))
            File('u_x.pvd') << u_x_projection
            print "test_marker shape"
            print np.shape(test_marker_fcn.vector())
            print "test marker vals"
            print test_marker_fcn.vector()[test_marker_fcn.vector()==1]
            print "u x proj shape"
            print np.shape(u_x_projection.vector())
            disp_value = u_x_projection.vector()[test_marker_fcn.vector()==1]
            print "disp_value"
            print disp_value
	    if max(disp_value) >= 0.90 and time > 172.0: # value of 1 is hard coded for now
                expr["u_D"].u_D = disp_value[0]
		traction_switch_flag = 2
		expr["Press"].P = 0.0
                bcs.append(bcright)
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
        
    elif sim_protocol["simulation_type"][0] == "ramp_and_hold":
        expr["u_D"].u_D = ramp_and_hold(time,sim_protocol,geo_options)
        output_dict["expr"] = expr
        output_dict["traction_switch_flag"] = traction_switch_flag
        print "assigning bcs"
        output_dict["bcs"] = bcs
        output_dict["rxn_force"] = rxn_force

    return output_dict

def ramp_and_hold(time,sim_protocol,geo_options):

    geo_check = not geo_options
    if geo_check:
        # unit cube
        length_scale = 1.0
    else:
        length_scale = geo_options["end_x"][0]
        print "length scale = " + str(length_scale)

    if time < sim_protocol["ramp_t_start"][0]:
        disp = 0.0
        print "displacement is " + str(disp)

    if time >= sim_protocol["ramp_t_end"][0]:
        disp = length_scale*sim_protocol["ramp_magnitude"][0]
        print "displacement is " + str(disp)
    else:
        slope = sim_protocol["ramp_magnitude"][0]/(sim_protocol["ramp_t_end"][0]-sim_protocol["ramp_t_start"][0])
        disp = length_scale*slope*time
        print "displacement is " + str(disp)

    return disp
