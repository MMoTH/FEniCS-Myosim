from dolfin import *
import numpy as np

## set boundary conditions

def set_bcs(sim_geometry,protocol,geo_options,mesh,W,facetboundaries,expr):

    output = {}

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):

        # if ventricle or ellipsoid simulation, constrain base in longitudinal direction,
        # and other constraints are in weak form
        topid = 4
        LVendoid = 2
        epiid = 1
        bctop = DirichletBC(W.sub(0).sub(2), Expression(("0.0"), degree = 2), facetboundaries, topid)
        bcs = [bctop]

    elif (sim_geometry == "cylinder") or sim_geometry == "gmesh_cylinder":
        sim_type = protocol["simulation_type"][0]

        if sim_geometry == "cylinder" or sim_geometry == "gmesh_cylinder":
            center = 0.0
            radius = 1.0
            length = 10.0
        else:
            center = 0.5
            radius = 0.5
            # hard coding in length for simple case
            length = 1.0



        # defining parts of the model where the boundary condition should be applied later
        class Left(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]) < tol
        #  where x[0] = 10
        class Right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]-length) < tol
        class Fix_y(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],0.0,tol) and near(x[1],center,tol)
        class Fix_y_right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],10.0,tol) and near(x[1],center,tol)
        class Fix_z_right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],10.0,tol) and near(x[2],center,tol)
        class Fix_z(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[2],center,tol))

        # Appropriately mark all facetboundaries
        facetboundaries.set_all(0)
        left = Left()
        right = Right()
        fix_y = Fix_y()
        fix_y_right = Fix_y_right()
        fix_z = Fix_z()
        fix_z_right = Fix_z_right()

        left.mark(facetboundaries, 1)
        right.mark(facetboundaries, 2)
        fix_y.mark(facetboundaries, 3)
        fix_z.mark(facetboundaries,5)



        # fix left face in x, right face is displacement (until traction bc may be triggered)
        bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)
        bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
        bcfix_y = DirichletBC(W.sub(0).sub(1), Constant((0.0)), fix_y, method="pointwise")
        bcfix_z = DirichletBC(W.sub(0).sub(2), Constant((0.0)), fix_z, method="pointwise")
        bcfix_y_right = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix_y_right, method="pointwise")
        bcfix_z_right = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix_z_right, method="pointwise")
        #bcright_after_switch = DirichletBC(W.sub(0).sub(0), disp_holder, facetboundaries, 2)

        bcs = [bcleft,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right,bcright] # order matters!

        #if sim_type == "work_loop":
        marker_space = FunctionSpace(mesh,'CG',1)
        bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
        test_marker_fcn = Function(marker_space) # this is what we need to grab the displacement after potential shortening
        bc_right_test.apply(test_marker_fcn.vector())
        output["test_marker_fcn"] = test_marker_fcn
        print "KURTIS LOOK HERE, ASSIGNING PROTOCOL ARRAY"
        protocol["end_disp_array"] = np.zeros(int(protocol["simulation_duration"][0]/protocol["simulation_timestep"][0]))
        # storing this bc in the protocol dictionary bc it's already passed into update bcs
        #protocol["bcright_after"] = bcright_after_switch


    elif sim_geometry == "box_mesh":
        sim_type = protocol["simulation_type"][0]

        x_end = geo_options["end_x"][0]
        y_end = geo_options["end_y"][0]
        z_end = geo_options["end_z"][0]
        y_center = y_end/2.
        z_center = z_end/2.

        class Left(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]) < tol
        #  where x[0] = 10
        class Right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]-x_end) < tol
        class Fix_y(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],0.0,tol) and near(x[1],y_center,tol)
        class Fix_y_right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],x_end,tol) and near(x[1],y_center,tol)
        class Fix_z_right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return near(x[0],x_end,tol) and near(x[2],z_center,tol)
        class Fix_z(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[2],z_center,tol))
        class Fix(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                #return on_boundary and abs(x[0]) < tol and abs(x[1]) < tol and abs(x[2]) < tol
                return (near(x[0],0.0,tol) and near(x[1],0.0,tol) and near(x[2],0.0,tol))
        class Fix2(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],0.0,tol) and near(x[2],z_end,tol))
        class Fix3(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],y_end,tol) and near(x[2],0.0,tol))
        class Fix_y_points_at_right_face(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-3
                return (near(x[0],x_end,tol) and near(x[1],y_center,tol))
        class Fix_z_points_at_right_face(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-3
                return (near(x[0],x_end,tol) and near(x[2],z_center,tol))
	class Fix_y_points_at_left_face(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-3
                return (near(x[0],0.0,tol) and near(x[1],y_center,tol))
        class Fix_z_points_at_left_face(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-3
                return (near(x[0],0.0,tol) and near(x[2],z_center,tol))
	class Left_back_midpoint(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],y_center,tol) and near(x[2],0.0,tol))
        class Left_top_midpoint(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],y_end,tol) and near(x[2],z_center,tol))
        class Left_front_midpoint(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],y_center,tol) and near(x[2],z_end,tol))
        class Left_bottom_midpoint(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],0.0,tol) and near(x[2],z_center,tol))

        # Appropriately mark all facetboundaries
        facetboundaries.set_all(0)
        left = Left()
        right = Right()
        fix_y = Fix_y()
        fix_y_right = Fix_y_right()
        fix_z = Fix_z()
        fix_z_right = Fix_z_right()
        fix = Fix()
        fix2 = Fix2()
        fix3 = Fix3()
        fix_y_points_at_right_face = Fix_y_points_at_right_face()
	fix_z_points_at_right_face = Fix_z_points_at_right_face()
        fix_y_points_at_left_face = Fix_y_points_at_left_face()
        fix_z_points_at_left_face = Fix_z_points_at_left_face()
	left_back_midpoint = Left_back_midpoint()
        left_top_midpoint = Left_top_midpoint()
        left_front_midpoint = Left_front_midpoint()
        left_bottom_midpoint = Left_bottom_midpoint()

        left.mark(facetboundaries, 1)
        right.mark(facetboundaries, 2)
        fix_y.mark(facetboundaries, 3)
        fix_z.mark(facetboundaries,5)

        # fix left face in x, right face is displacement (until traction bc may be triggered)
        if sim_type == "ramp_and_hold" or sim_type == "custom":

            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)

            bcfix_y = DirichletBC(W.sub(0).sub(1), Constant((0.0)), fix_y, method="pointwise")
            bcfix_z = DirichletBC(W.sub(0).sub(2), Constant((0.0)), fix_z, method="pointwise")
            bcfix_y_right = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix_y_right, method="pointwise")
            bcfix_z_right = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix_z_right, method="pointwise")

            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise")
            bcfix2 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix2,method="pointwise")
            bcfix22 = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix2,method="pointwise")
            bcfix3 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix3,method="pointwise")
            bcfix33 = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix3,method="pointwise")

            #bcs = [bcleft,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right,bcright] # order matters!
            bcs = [bcleft,bcfix,bcfix2,bcfix22,bcfix3,bcfix33,bcright]

        if sim_type == "traction_hold":
            print "traction simulation"
            # Similar to cylinder but without fixing displacement along y and z axes to prevent rotation
            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)

            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
            bcfix2 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix2,method="pointwise")
            bcfix22 = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix2,method="pointwise")
            bcfix3 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix3,method="pointwise")
            bcfix33 = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix3,method="pointwise")
            bcs = [bcleft,bcfix,bcfix22,bcfix33] #order matters!

        if sim_type == "stress_strain_loop":

            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)

            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
            bcfix2 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix2,method="pointwise")
            bcfix22 = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix2,method="pointwise")
            bcfix3 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix3,method="pointwise")
            bcfix33 = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix3,method="pointwise")
            bc_fix_y_rf = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix_y_points_at_right_face,method="pointwise")
            bc_fix_z_rf = DirichletBC(W.sub(0).sub(2), Constant((0.0)), fix_z_points_at_right_face,method="pointwise")
	    bc_fix_y_lf = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix_y_points_at_left_face,method="pointwise")
            bc_fix_z_lf = DirichletBC(W.sub(0).sub(2), Constant((0.0)), fix_z_points_at_left_face,method="pointwise")
            bcleft_back_mp = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), left_back_midpoint,method="pointwise")
            bcleft_top_mp = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), left_top_midpoint,method="pointwise")
            bcleft_front_mp = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), left_front_midpoint,method="pointwise")
            bcleft_bottom_mp = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), left_bottom_midpoint,method="pointwise")
	    #bcs = [bcleft,bcleft_back_mp,bcleft_top_mp,bcleft_front_mp,bcleft_bottom_mp,bc_fix_yz_rf1,bc_fix_yz_rf2,bcfix_yz_lf1,bcfix_yz_lf2]
	    #bcs = [bcleft, bc_fix_y_rf, bc_fix_z_rf, bc_fix_y_lf, bc_fix_z_lf]
            bcs = [bcleft,bcfix,bcfix22,bcfix33,bc_fix_y_rf,bc_fix_z_rf]
	    #print "KURTIS LOOK HERE, ASSIGNING PROTOCOL ARRAY"
            protocol["previous_end_disp"] = 0.0
            protocol["diastole"] = 1
            protocol["isovolumic"] = 0
            protocol["ejection"] = 0

        #if sim_type == "work_loop":
        marker_space = FunctionSpace(mesh,'CG',1)
        bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
        test_marker_fcn = Function(marker_space) # this is what we need to grab the displacement after potential shortening
        bc_right_test.apply(test_marker_fcn.vector())
        output["test_marker_fcn"] = test_marker_fcn

    elif sim_geometry == "unit_cube":
        sim_type = protocol["simulation_type"][0]
        print "sim type = " + sim_type
        output["test_marker_fcn"] = 0

        class Left(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]) < tol
        #  where x[0] = 10
        class Right(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[0]-1.0) < tol
        #  where x[2] = 0
        class Lower(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[2]) < tol
        class Top(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[2]-1.0) < tol
        #  where x[1] = 0
        class Front(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[1]) < tol
        class Back(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return on_boundary and abs(x[1]-1.) < tol
        #  where x[0], x[1] and x[2] = 0
        class Fix(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                #return on_boundary and abs(x[0]) < tol and abs(x[1]) < tol and abs(x[2]) < tol
                return (near(x[0],0.0,tol) and near(x[1],0.0,tol) and near(x[2],0.0,tol))
        class Fix2(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],0.0,tol) and near(x[2],1.0,tol))
        class Fix3(SubDomain):
            def inside(self, x, on_boundary):
                tol = 1E-14
                return (near(x[0],0.0,tol) and near(x[1],1.0,tol) and near(x[2],0.0,tol))

        facetboundaries.set_all(0)
        left = Left()
        right = Right()
        fix = Fix()
        fix2 = Fix2()
        fix3 = Fix3()
        lower = Lower()
        front = Front()
        top = Top()
        back = Back()
        #
        left.mark(facetboundaries, 1)
        right.mark(facetboundaries, 2)
        fix.mark(facetboundaries, 3)
        lower.mark(facetboundaries, 4)
        front.mark(facetboundaries, 5)
        top.mark(facetboundaries, 6)
        back.mark(facetboundaries, 7)

        if sim_type == "ramp_and_hold" or sim_type == "custom":
            print "checking expression",expr["u_D"].u_D
            # Similar to cylinder but without fixing displacement along y and z axes to prevent rotation
            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
            bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
            bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)        # u2 = 0 on front face
            bcfix2 = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)),fix2,method="pointwise")
            #bcfix22 = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix2,method="pointwise")
            bcfix3 = DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)),fix3,method="pointwise")
            #bcfix33 = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix3,method="pointwise")
            bcs = [bcleft,bcfix3,bclower,bcright] #order matters!
            # Trying shear
            """bcleft= DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcleft2 = DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 1)
            bcright= DirichletBC(W.sub(0).sub(1), u_D, facetboundaries, 2)
            bcright2 = DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 2)
            bcright3 = DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 2)
            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
            bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
            #bcs = [bcleft, bclower, bcfront,bcfix, bcright] #order matters!
            bcs = [bcleft, bcright,bcright2,bcright3]"""

        if sim_type == "ramp_and_hold_simple_shear":
            print "in simple shear bcs"
            bcleft= DirichletBC(W.sub(0), Constant((0.0,0.0,0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(1), expr["u_D"], facetboundaries, 2)
            bcright_x = DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 2)
            bcright_z = DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 2)
            bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
            bctop = DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 6)
            bcs = [bcleft, bcright, bcright_x,bclower]

        if sim_type == "ramp_and_hold_biaxial":
            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
            bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
            bctop = DirichletBC(W.sub(0).sub(2), expr["u_front"], facetboundaries, 6)
            bcback = DirichletBC(W.sub(0).sub(1), expr["u_D"], facetboundaries, 7)
            bcfront = DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries,5)
            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0

            bcs = [bcleft, bcfront,bcback,bctop,bcright]

        if sim_type == "traction_hold":
            print "traction simulation"
            # Similar to cylinder but without fixing displacement along y and z axes to prevent rotation
            bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
            bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
            bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
            bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
            bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)        # u2 = 0 on front face
            bcfix2 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix2,method="pointwise")
            bcfix22 = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix2,method="pointwise")
            bcfix3 = DirichletBC(W.sub(0).sub(0), Constant((0.0)),fix3,method="pointwise")
            bcfix33 = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix3,method="pointwise")
            bcs = [bcleft,bcfix,bcfix22,bcfix33] #order matters!


        if sim_type == "work_loop":

            marker_space = FunctionSpace(mesh,'CG',1)
            bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
            test_marker_fcn = Function(marker_space) # this is what we need to grab the displacement after potential shortening
            bc_right_test.apply(test_marker_fcn.vector())
            output["test_marker_fcn"] = test_marker_fcn
            #print "KURTIS LOOK HERE, ASSIGNING PROTOCOL ARRAY"
            protocol["end_disp_array"] = np.zeros(int(protocol["simulation_duration"][0]/protocol["simulation_timestep"][0]))

            if sim_geometry == "unit_cube":
                bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
                bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
                bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
                bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
                bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)
                bcs = [bcleft,bcfix,bclower,bcright]

        if sim_type == "stress_strain_loop":

            marker_space = FunctionSpace(mesh,'CG',1)
            bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
            test_marker_fcn = Function(marker_space) # this is what we need to grab the displacement after potential shortening
            bc_right_test.apply(test_marker_fcn.vector())
            output["test_marker_fcn"] = test_marker_fcn
            #print "KURTIS LOOK HERE, ASSIGNING PROTOCOL ARRAY"
            protocol["previous_end_disp"] = 0.0
            protocol["diastole"] = 1
            protocol["isovolumic"] = 0
            protocol["ejection"] = 0

            if sim_geometry == "unit_cube":
                bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
                bcright= DirichletBC(W.sub(0).sub(0), expr["u_D"], facetboundaries, 2)
                bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
                bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
                bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)
                bcs = [bcleft,bcfix,bclower]

    output["bcs"] = bcs
    return output
