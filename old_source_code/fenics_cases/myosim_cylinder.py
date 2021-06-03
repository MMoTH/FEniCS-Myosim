from __future__ import division
import sys
sys.path.append("/home/fenics/shared/source_code/dependencies/")
import os as os
from dolfin import *
import numpy as np
from matplotlib import pylab as plt
#from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver
import math
import Python_MyoSim.half_sarcomere.half_sarcomere as half_sarcomere
import Python_MyoSim.half_sarcomere.implement as implement
from cell_ion_module import cell_ion_driver
import vtk
import vtk_py
import mshr
from numpy import random as r
import copy
import pandas as pd


def fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,pso):

    # marking these as indices because this is a function called from fenics_driver
    i,j = indices(2)

    #------------------## Load in all information and set up simulation --------
    output_path = output_params["output_path"][0]
    displacementfile = File(output_path + "u_disp.pvd")
    save_output = sim_params["save_output"][0]

    filament_compliance_factor = hs_params["myofilament_parameters"]["filament_compliance_factor"][0]
    no_of_states = hs_params["myofilament_parameters"]["num_states"][0]
    no_of_attached_states = hs_params["myofilament_parameters"]["num_attached_states"][0]
    no_of_detached_states = no_of_states-no_of_attached_states
    no_of_transitions = hs_params["myofilament_parameters"]["num_transitions"][0]
    state_attached = hs_params["myofilament_parameters"]["state_attached"][0]
    cb_extensions = hs_params["myofilament_parameters"]["cb_extensions"][0]
    k_cb_multiplier = hs_params["myofilament_parameters"]["k_cb_multiplier"][0]
    k_cb_pos = hs_params["myofilament_parameters"]["k_cb_pos"][0]
    k_cb_neg = hs_params["myofilament_parameters"]["k_cb_neg"][0]
    cb_number_density = hs_params["cb_number_density"][0]
    alpha_value = hs_params["myofilament_parameters"]["alpha"][0]
    x_bin_min = hs_params["myofilament_parameters"]["bin_min"][0]
    x_bin_max = hs_params["myofilament_parameters"]["bin_max"][0]
    x_bin_increment = hs_params["myofilament_parameters"]["bin_width"][0]
    work_loop = sim_params["work_loop"][0]

## ---------  Set up information for active force calculation ------------------

    # Create x interval for cross-bridges
    xx = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)

    # Define number of intervals cross-bridges are defined over
    no_of_x_bins = np.shape(xx)[0]

    # Define the length of the populations vector
    n_array_length = no_of_attached_states * no_of_x_bins + no_of_detached_states + 2
    print "n array length = " + str(n_array_length)
    n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1]]

    hsl0 = hs_params["initial_hs_length"][0]
    step_size = sim_params["sim_timestep"][0]
    sim_duration = sim_params["sim_duration"][0]
    time_steps = int(sim_duration/step_size +1)
    Ca_flag = 4
    constant_pCa = 6.5

    fdataCa = open(output_path + "calcium_.txt", "w", 0)
    pk1file = File(output_path + "pk1_act_on_f0.pvd")
    hsl_file = File(output_path + "hsl_mesh.pvd")


    # holder for reaction force at right end
    fx_rxn = np.zeros((time_steps))

    shorten_flag = 0 # switches to one if shortening begins

    # Define the cylinder
    x = 10.0
    y = 0.0
    z = 0.0
    cyl_top = Point(x,y,z)
    cyl_bottom = Point(0,0,0)
    top_radius = 1.0
    bottom_radius = 1.0
    segments = 4
    geometry = mshr.Cylinder(cyl_top,cyl_bottom,top_radius,bottom_radius,segments)

    # Create the mesh
    mesh = mshr.generate_mesh(geometry,20)
    # Save the mesh
    File('cylinder_3.pvd') << mesh

    no_of_int_points = 4 * np.shape(mesh.cells())[0]

    # General quadrature element whose points we will evaluate myosim at
    Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
    Quadelem._quad_scheme = 'default'

    # Vector element at gauss points (for fibers)
    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'

    # Real element for rigid body motion boundary condition
    Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
    Relem._quad_scheme = 'default'

    # Quadrature space for information needed at gauss points, such as
    # hsl, cb_force, passive forces, etc.
    Quad = FunctionSpace(mesh, Quadelem)

    # Initialize the half-sarcomere class. Its methods will be used to solve for cell populations
    hs = half_sarcomere.half_sarcomere(hs_params,1)

    # Need to create a list of dictionaries for parameters for each gauss point
    hs_params_list = [{}]*no_of_int_points
    passive_params_list = [{}]*no_of_int_points

    # Initialize ion class (get calcium transient from here)
    cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params)
    calcium = np.zeros(time_steps)
    calcium[0] = cell_ion.calculate_concentrations(0,0)

    for jj in np.arange(np.shape(hs_params_list)[0]):
        hs_params_list[jj] = copy.deepcopy(hs_params)
        passive_params_list[jj] = copy.deepcopy(passive_params)

    # Create a simple expression to test if x_coord is > 9.0
    # making last 10% of cylinder spring elements
    tester = Expression("x[0]",degree=1)
    digitation = Expression("pow(x[1],2) + pow(x[2],2) + 0.5",degree=1)
    point_radius = Expression("sqrt(pow(x[1],2)+pow(x[2],2))",degree=1)

    # Project the expression onto the mesh
    temp_tester_values = project(tester,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
    dig_values = project(digitation,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
    point_rad_values = project(point_radius,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})

    # Interpolate onto the FunctionSpace for quadrature points
    temp_tester = interpolate(temp_tester_values,Quad)
    dig = interpolate(dig_values,Quad)
    point_rad = interpolate(point_rad_values,Quad)

    # Create array of the expression values
    temp_tester_array = temp_tester.vector().get_local()
    dig_array = dig.vector().get_local()
    point_rad_array = point_rad.vector().get_local()

    parameters["form_compiler"]["quadrature_degree"]=2
    parameters["form_compiler"]["representation"] = "quadrature"

    # defining parts of the model where the boundary condition should be applied later
    #  where x[0] = 0
    class Left(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[0]) < tol
    #  where x[0] = 10
    class Right(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[0]-10.0) < tol
    class Fix_y(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-1
            return near(x[0],0.0,tol) and near(x[1],0.0,tol)
    class Fix_y_right(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return near(x[0],10.0,tol) and near(x[1],0.0,tol)
    class Fix_z_right(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return near(x[0],10.0,tol) and near(x[2],0.0,tol)
    class Fix_z(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return (near(x[0],0.0,tol) and near(x[2],0.0,tol))




    # now test_marker_fcn has value of 1 on right boundary always


    # Define spatial coordinate system used in rigid motion constraint
    X = SpatialCoordinate (mesh)
    facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
    edgeboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-2)

    facetboundaries.set_all(0)
    left = Left()
    right = Right()
    fix_y = Fix_y()
    fix_y_right = Fix_y_right()
    fix_z = Fix_z()
    fix_z_right = Fix_z_right()
    #horizontal = Horizontal()
    #lower = Lower()
    #front = Front()
    #
    left.mark(facetboundaries, 1)
    right.mark(facetboundaries, 2)
    fix_y.mark(facetboundaries, 3)
    #horizontal.mark(facetboundaries,4)
    fix_z.mark(facetboundaries,5)

    marker_space = FunctionSpace(mesh,'CG',1)
    bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
    test_marker_fcn = Function(marker_space)
    bc_right_test.apply(test_marker_fcn.vector())

    File(output_path + "facetboundaries.pvd") << facetboundaries

    #lower.mark(facetboundaries, 4)
    #front.mark(facetboundaries, 5)
    #
    ds = dolfin.ds(subdomain_data = facetboundaries)

    #
    ###############################################################################
    isincomp = True#False
    N = FacetNormal (mesh)
    #Cparam = Constant(1.0e2)


    TF = TensorFunctionSpace(mesh, 'DG', 1)

    Velem = VectorElement("Lagrange", tetrahedron, 2, quad_scheme="default")
    Velem._quad_scheme = 'default'
    Qelem = FiniteElement("Lagrange", tetrahedron, 1, quad_scheme="default")
    Qelem._quad_scheme = 'default'
    # Mixed element for rigid body motion. One each for x, y displacement. One each for
    # x, y, z rotation
    VRelem = MixedElement([Relem, Relem, Relem, Relem, Relem])


    W = FunctionSpace(mesh, MixedElement([Velem,Qelem,VRelem]))
    x_dofs = W.sub(0).sub(0).dofmap().dofs()

    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))


    # Kurtis trying to initialize vectors
    fiberFS = FunctionSpace(mesh, VQuadelem)
    f0 = Function(fiberFS)
    s0 = Function(fiberFS)
    n0 = Function(fiberFS)
    f0_diff = Function(fiberFS)

    c_param = Function(Quad)
    c2_param = Function(Quad)
    c3_param = Function(Quad)

    File(output_path + "fiber1.pvd") << project(f0, VectorFunctionSpace(mesh, "DG", 0))

    m_x = 1.0
    m_y = 0.0
    m_z = 0.0
    width = sim_params["width"][0]
    #x_comps = r.normal(m_x,width,no_of_int_points)
    #y_comps = r.normal(m_y,width,no_of_int_points)
    #z_comps = r.normal(m_z,width,no_of_int_points)
    for jj in np.arange(no_of_int_points):

        #if (temp_tester_array[jj] < dig_array[jj]) or (temp_tester_array[jj] > -dig_array[jj] + 10.0):
        if (temp_tester_array[jj] > 9.0) or (temp_tester_array[jj] < 1.0):
            # inside left end
            f0.vector()[jj*3] = 1.0
            f0.vector()[jj*3+1] = 0.0
            f0.vector()[jj*3+2] = 0.0
            hs_params_list[jj]["myofilament_parameters"]["k_3"][0] = 0.0
            #passive_params_list[jj]["c"][0] = 2000
            c_param.vector()[jj] = 400
            c2_param.vector()[jj] = 250
            c3_param.vector()[jj] = 10


        else:

            # In middle region, assign fiber vector
            # find radius of point
            temp_radius = point_rad_array[jj]
            if np.abs(temp_radius - top_radius) < 0.01:
                temp_width = 0.0
            else:
                temp_width = width*(1.0-(temp_radius*temp_radius/(top_radius*top_radius)))
            f0.vector()[jj*3] = r.normal(m_x,temp_width,1)[0]
            f0.vector()[jj*3+1] = r.normal(m_y,temp_width,1)[0]
            f0.vector()[jj*3+2] = r.normal(m_z,temp_width,1)[0]
            c_param.vector()[jj] = 1000
            c2_param.vector()[jj] = 250
            c3_param.vector()[jj] = 15
        """f0.vector()[kk*3] = x_comps[kk]
        # assign y component
        f0.vector()[kk*3+1] = y_comps[kk]
        # z component would look like
        f0.vector()[kk*3+2] = z_comps[kk]"""

    f0 = f0/sqrt(inner(f0,f0))

    #f0_norm = project(sqrt(inner(f0,f0)),FunctionSpace(mesh,"CG",1))
    #print "norm is " + str(f0_norm.vector().array())
    #stop

    f0_diff = f0 - Constant((1.,0.,0.))
    long_axis = Function(fiberFS)

    for nn in np.arange(no_of_int_points):
        long_axis.vector()[nn*3] = 0.0
        long_axis.vector()[nn*3+1] = 0.0
        long_axis.vector()[nn*3+2] = 1.0

    #s0 = f0 + f0_diff # sum object
    #n0 = cross(f0,s0) # cross object

    #s0  = project(Constant((0,1,0))+f0_diff,VectorFunctionSpace(mesh, "DG", 0))
    s0 = cross(long_axis,f0)
    s0 = s0/sqrt(inner(s0,s0))
    File(output_path + "sheet.pvd") << project(s0,VectorFunctionSpace(mesh, "DG", 0))

    n0 = project(cross(f0,s0),VectorFunctionSpace(mesh, "DG", 0))
    n0 = n0/sqrt(inner(n0,n0))
    File(output_path + "sheet_normal.pvd") << project(n0,VectorFunctionSpace(mesh, "DG", 0))
    File(output_path + "fiber.pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))
    #test_tensor = as_tensor(f0*f0)

    # assigning BCs
    u_D = Expression(("u_D"), u_D = 0.0, degree = 2)
    bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
    bcright= DirichletBC(W.sub(0).sub(0), u_D, facetboundaries, 2)
    bcfix_y = DirichletBC(W.sub(0).sub(1), Constant((0.0)), fix_y, method="pointwise")
    bcfix_z = DirichletBC(W.sub(0).sub(2), Constant((0.0)), fix_z, method="pointwise") # at one vertex u = v = w = 0
    bcfix_y_right = DirichletBC(W.sub(0).sub(1), Constant((0.0)),fix_y_right, method="pointwise")
    bcfix_z_right = DirichletBC(W.sub(0).sub(2), Constant((0.0)),fix_z_right, method="pointwise")
    #bchorizontal = DirichletBC(W.sub(0).sub(1), Constant((0.0)), horizontal, method="pointwise")
    #bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
    #bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)        # u2 = 0 on front face
    #bcs = [bcleft, bclower, bcfront, bcright,bcfix]

    bcs = [bcleft, bcright,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right]

    du,dp,dc11 = TrialFunctions(W)
    w = Function(W)
    dw = TrialFunction(W)
    (u,p,c11) = split(w)
    (v,q,v11) = TestFunctions(W)
    wtest = TestFunction(W)

    params= {"mesh": mesh,
         "facetboundaries": facetboundaries,
         "facet_normal": N,
    	 "mixedfunctionspace": W,
    	 "mixedfunction": w,
         "displacement_variable": u,
         "pressure_variable": p,
    	 "fiber": f0,
         "sheet": s0,
         "sheet-normal": n0,
         #"C_param": Cparam,
    	 "incompressible": isincomp,
    	 "Kappa":Constant(1e5)}
    params.update(passive_params)
    params["c"] = c_param
    params["c2"] = c2_param
    params["c3"] = c3_param

    uflforms = Forms(params)


    Fmat = uflforms.Fmat()
    Cmat = (Fmat.T*Fmat)
    Emat = uflforms.Emat()
    J = uflforms.J()

    n = J*inv(Fmat.T)*N
    dx = dolfin.dx(mesh,metadata = {"integration_order":2})

    #Ematrix = project(Emat, TF)
    Wp = uflforms.PassiveMatSEF()

    #Active force calculation------------------------------------------------------
    y_vec = Function(Quad_vectorized_Fspace)
    hsl = sqrt(dot(f0, Cmat*f0))*hsl0
    hsl_old = Function(Quad)
    #hsl_old = hsl
    delta_hsl = hsl - hsl_old
    #delta_hsl = 0.0

    #f_holder = Constant(0.0)
    cb_force = Constant(0.0)

    y_vec_split = split(y_vec)
    #print "shape of yvecsplit " + str(np.shape(y_vec_split))

    for jj in range(no_of_states):

        f_holder = Constant(0.0)
        temp_holder = Constant(0.0)

        if state_attached[jj] == 1:

            cb_ext = cb_extensions[jj]

            for kk in range(no_of_x_bins):

                dxx = xx[kk] + delta_hsl * filament_compliance_factor

                n_pop = y_vec_split[n_vector_indices[jj][0] + kk]

                temp_holder = n_pop * k_cb_multiplier[jj] * (dxx + cb_ext) * conditional(gt(dxx + cb_ext,0.0), k_cb_pos, k_cb_neg)
                #temp_holder = temp_holder*conditional(gt(abs(dxx),x_bin_max),0.0,1.0)
                #f_holder = f_holder + conditional(gt(temp_holder,0.0),temp_holder,0.0)
                f_holder = f_holder + temp_holder

            f_holder = f_holder * cb_number_density * 1e-9

            f_holder = f_holder * alpha_value

        cb_force = cb_force + f_holder

    #print "rank" + str(f0.rank())
    Pactive = cb_force * as_tensor(f0[i]*f0[j], (i,j))
    Press = Expression(("P"), P=0.0, degree=0)
    # Automatic differentiation  #####################################################################################################
    F1 = derivative(Wp, w, wtest)*dx
    F2 = inner(Fmat*Pactive, grad(v))*dx
    F3 = inner(Press*N, v)*ds(2, domain=mesh)
    # constrain rigid body motion
    """L4 = inner(as_vector([c11[0], c11[1], 0.0]), u)*dx + \
    	 inner(as_vector([0.0, 0.0, c11[2]]), cross(X, u))*dx + \
    	 inner(as_vector([c11[3], 0.0, 0.0]), cross(X, u))*dx + \
    	 inner(as_vector([0.0, c11[4], 0.0]), cross(X, u))*dx
    F4 = derivative(L4, w, wtest)"""
    Ftotal = F1 + F2 - F3 #+ F4

    Jac1 = derivative(F1, w, dw)
    Jac2 = derivative(F2, w, dw)
    Jac3 = derivative(F3, w, dw)
    #Jac4 = derivative(F4, w, dw)
    Jac = Jac1 + Jac2 - Jac3 #+ Jac4
    ##################################################################################################################################


    darray = []
    """hslarray = np.zeros((time_steps+1,no_of_int_points))
    calarray = []
    strarray = np.zeros((time_steps+1,no_of_int_points))
    pstrarray = np.zeros((time_steps+1,no_of_int_points))
    overlaparray = np.zeros((time_steps+1,no_of_int_points))"""

    calcium_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    calcium_ds = calcium_ds.transpose()
    calcium = np.zeros(time_steps)

    active_stress_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    active_stress_ds = active_stress_ds.transpose()

    dumped_populations_ds = pd.DataFrame(np.zeros((no_of_int_points,n_array_length)))

    tarray_ds = pd.DataFrame(np.zeros(time_steps+1),index=None)
    tarray_ds = tarray_ds.transpose()
    tarray = np.zeros(time_steps)

    p_f_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    p_f_array_ds = p_f_array_ds.transpose()

    pgf_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgf_array_ds = pgf_array_ds.transpose()

    pgt_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgt_array_ds = pgt_array_ds.transpose()

    pgs_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgs_array_ds = pgs_array_ds.transpose()

    temp_overlap_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    temp_overlap_ds = temp_overlap_ds.transpose()

    alpha_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    alpha_array_ds = alpha_array_ds.transpose()

    hsl_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
    hsl_array_ds = hsl_array_ds.transpose()

    delta_hsl_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    delta_hsl_array_ds = delta_hsl_array_ds.transpose()

    y_vec_array = y_vec.vector().get_local()[:]

    hsl_array = project(hsl, Quad).vector().get_local()[:]

    #hsl_array = np.ones(no_of_int_points)*hsl0
    delta_hsl_array = np.zeros(no_of_int_points)

    for counter in range(0,n_array_length * no_of_int_points,n_array_length):
        y_vec_array[counter] = 1
        y_vec_array[counter-2] = 1

    Pg, Pff, alpha = uflforms.stress()

    # Magnitude of bulk passive stress in fiber direction
    Pg_fiber = inner(f0,Pg*f0)
    Pg_transverse = inner(n0,Pg*n0)
    Pg_shear = inner(n0,Pg*f0)

    temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]

    temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    alphas = interpolate(temp_DG_1, Quad)
    alpha_array = alphas.vector().get_local()[:]

    cb_f_array = project(cb_force, Quad).vector().get_local()[:]

    dumped_populations = np.zeros((no_of_int_points, n_array_length))
    y_interp = np.zeros((no_of_int_points)*n_array_length)

    x_dofs = W.sub(0).sub(0).dofmap().dofs()

    temp_overlap = np.zeros((no_of_int_points))
    y_vec_array_new = np.zeros(((no_of_int_points)*n_array_length))
    j3_fluxes = np.zeros((no_of_int_points,time_steps))
    j4_fluxes = np.zeros((no_of_int_points,time_steps))
    #print "shapes of stuff"
    #print np.shape(temp_overlap)
    #print np.shape(y_vec_array_new)
    temp_astress = np.ones(no_of_int_points)
    t = 0.0
    #delta_hsls = np.zeros((time_steps,24))
    for l in range(time_steps):



        tarray[l]=(t)





        # Right now, not general. The calcium depends on cycle number, just saying 0
        cycle = 0
        #calcium[l] = cell_ion.model_class.calculate_concentrations(cycle,t)
        calcium[l] = cell_ion.calculate_concentrations(step_size,l)

        #calcium[l] = cell_ion.model.calculate_concentrations(0,t)

        # Looping through integration points within Python Myosim, not here

        # Quick hack
        if l == 0:
            overlap_counter = 1
        else:
            overlap_counter = l

        # Because we want to be able to change contractility parameters for each
        # gauss point, we need to loop through the gauss points here

        #temp_overlap, y_interp, y_vec_array_new = implement.update_simulation(hs, step_size, delta_hsl_array, hsl_array, y_vec_array, p_f_array, cb_f_array, calcium[l], n_array_length, t,overlaparray[overlap_counter,:])
        #print "hs list dict " + str(hs_params_list
        #print "y_vec_new " + str(y_vec_array_new)
        for mm in np.arange(no_of_int_points):
            #print hsl_array[mm]
            temp_overlap[mm], y_interp[mm*n_array_length:(mm+1)*n_array_length], y_vec_array_new[mm*n_array_length:(mm+1)*n_array_length] = implement.update_simulation(hs, step_size, delta_hsl_array[mm], hsl_array[mm], y_vec_array[mm*n_array_length:(mm+1)*n_array_length], p_f_array[mm], cb_f_array[mm], calcium[l], n_array_length, t,hs_params_list[mm])
            temp_flux_dict, temp_rate_dict = implement.return_rates_fenics(hs)
            #print temp_flux_dict["J3"]
            j3_fluxes[mm,l] = sum(temp_flux_dict["J3"])
            j4_fluxes[mm,l] = sum(temp_flux_dict["J4"])
    #    print y_vec_array_new[0:53]
        y_vec_array = y_vec_array_new # for Myosim
        print " num gauss points " + str(no_of_int_points)
        print "y_vec shape" + str(np.shape(y_vec_array))
        print "y_interp shape"  + str(np.shape(y_interp))

        for  m in range(no_of_int_points):

            for k in range(n_array_length):

                dumped_populations[m, k] = y_interp[m * n_array_length + k]


        #print "shapes of stuff"
        #print np.shape(y_vec.vector())
        #print np.shape(y_vec_array)
        y_vec.vector()[:] = y_vec_array # for PDE

    #    print y_vec_array[0:53]
        hsl_array_old = hsl_array

        # trying to implement a work loop

        if work_loop:

            if l>0:
                temp_astress = cb_f_array[:]
                temp_astress = temp_astress[temp_astress > 0.0]
                if np.shape(temp_astress)[0] == 0:
                    temp_astress=0.0
            """if l > 2:
                u_check = project(u,VectorFunctionSpace(mesh,"CG",2))
                disp_value = u_check.vector()[test_marker_fcn.vector()==1]
                print "displacement after shortening on right is = " + str(disp_value[0])
                u_D.u_D=disp_value[0]"""
            if np.average(temp_astress>=50000):
                Press.P=50000
                bcs = [bcleft,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right]
                shorten_flag = 1
            else:
                if shorten_flag < 0:
                    u_D.u_D = u_D.u_D
                    Press.P=0.0

                if shorten_flag > 0:
                    u_check = project(u,VectorFunctionSpace(mesh,"CG",2))
                    disp_value = u_check.vector()[test_marker_fcn.vector()==1]
                    print "displacement after shortening on right is = " + str(disp_value[0])
                    u_D.u_D=disp_value[0]
                    shorten_flag = -1

                bcs = [bcleft,bcright,bcfix_y,bcfix_z,bcfix_y_right,bcfix_z_right]



        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})

        """np.save(output_path +"dumped_populations", dumped_populations)
        np.save(output_path + "tarray", tarray)
        np.save(output_path + "stress_array", strarray)
        np.save(output_path + "hsl", hslarray)
        np.save(output_path + "overlap", overlaparray)
        np.save(output_path + "pstress_array",pstrarray)
        #np.save(output_path + "alpha_array",alphaarray)
        np.save(output_path + "calcium",calarray)"""

        displacementfile << w.sub(0)
        pk1temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'CG',1))
        pk1temp.rename("pk1temp","pk1temp")
        pk1file << pk1temp
        hsl_temp = project(hsl,FunctionSpace(mesh,'DG',1))
        hsl_temp.rename("hsl_temp","hsl")
        #hsl_file << hsl_temp

        hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for PDE

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim

        delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim

        #delta_hsls[l] = delta_hsl_array
        temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)
        pgf_array = pgf.vector().get_local()[:]
        temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgt = interpolate(temp_DG_3, Quad)
        pgt_array = pgt.vector().get_local()[:]
        temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgs = interpolate(temp_DG_4, Quad)
        pgs_array = pgs.vector().get_local()[:]

        cb_f_array = project(cb_force, Quad).vector().get_local()[:]
        #strarray.append(cb_f_array[0])
        #strarray[l,:] = cb_f_array[:]
        #pstrarray[l,:] = p_f_array[:]
        #hslarray.append(hsl_array[0]+delta_hsl_array[0])
        #hslarray[l,:] = hsl_array[:] + delta_hsl_array[:]
        #overlaparray[l,:] = temp_overlap

        # Calculate reaction force at right end
        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})
        bcleft.apply(b)
        bcfix_y.apply(b)
        bcfix_z.apply(b)
        bcfix_y_right.apply(b)
        bcfix_z_right.apply(b)

        f_int_total = b.copy()
        for kk in x_dofs:
            fx_rxn[l] += f_int_total[kk]
        #bcleft.apply(f_int_total)
        #FX = 0
        #for kk in x_dofs:
        #    FX += f_int_total[i]

        #fx_rxn[l] = Fx
        np.save(output_path + "fx",fx_rxn)

        if t <= 5:
            u_D.u_D += .14
        else:
            u_D.u_D = u_D.u_D

        #print(cb_f_array)

        """if t <= 100: # stretch to 1300
            u_D.u_D += .003
        if t < 500 and t > 100:
            u_D.u_D =u_D.u_D
        if t < 600 and t >= 500:
            u_D.u_D += .0005
        if t < 800 and t >=600:
            u_D.u_D = u_D.u_D
        if t < 900 and t >= 800:
            u_D.u_D -= .0005
        if t >= 900:
            u_D.u_D = u_D.u_D"""
        """if t < 170 and t > 150:
            u_D.u_D -= 0.005
        else:
            u_D.u_D = u_D.u_D"""
        """if t < 5:
            u_D.u_D += 0.03
        else:
            u_D.u_D = u_D.u_D"""
        t = t + step_size

        #calarray.append(hs.Ca_conc*np.ones(no_of_int_points))
        #calcium[] = hs.Ca_conc*
        if save_output:

            active_stress_ds.iloc[0,:] = cb_f_array[:]
            active_stress_ds.to_csv(output_path + 'active_stress.csv',mode='a',header=False)

            #active_stress_ds = active_stress_ds.transpose()
            #hsl_array_ds.iloc[0,:] = hsl_array[:]
            #hsl_array_ds.to_csv(output_path + 'half_sarcomere_lengths.csv',mode='a',header=False)

            calcium_ds.iloc[0,:] = calcium[l]
            calcium_ds.to_csv(output_path + 'calcium.csv',mode='a',header=False)

            #for i in range(no_of_int_points):
            #    dumped_populations_ds.iloc[i,:] = dumped_populations[i,:]
            #dumped_populations_ds.to_csv(output_path + 'populations.csv',mode='a',header=False)

            tarray_ds[l] = tarray[l]
            tarray_ds.to_csv(output_path + 'time.csv',mode='a',header=False)

            #p_f_array_ds.iloc[0,:] = p_f_array[:]
            #p_f_array_ds.to_csv(output_path + 'myofiber_passive.csv',mode='a',header=False)

            #pgf_array_ds.iloc[0,:] = pgf_array[:]
            #pgf_array_ds.to_csv(output_path + 'gucc_fiber_pstress.csv',mode='a',header=False)

            #pgt_array_ds.iloc[0,:] = pgt_array[:]
            #pgt_array_ds.to_csv(output_path + 'gucc_trans_pstress.csv',mode='a',header=False)

            #pgs_array_ds.iloc[0,:] = pgs_array[:]
            #pgs_array_ds.to_csv(output_path + 'gucc_shear_pstress.csv',mode='a',header=False)

            #temp_overlap_ds.iloc[0,:] = temp_overlap[:]
            #temp_overlap_ds.to_csv(output_path + 'overlap.csv',mode='a',header=False)

            #alpha_array_ds.iloc[0,:] = alpha_array[:]
            #alpha_array_ds.to_csv(output_path + 'alpha.csv',mode='a',header=False)

            #delta_hsl_array_ds.iloc[0,:] = delta_hsl_array[:]
            #delta_hsl_array_ds.to_csv(output_path + 'delta_hsl.csv',mode='a',header=False)

        # Update Fiber orientation
        #f0 = f0+step_size*(Cmat*f0-f0)/sqrt(inner(Cmat*f0-f0,Cmat*f0-f0))
        #target_vec = Cmat*f0
        #print target_vec.type()
        #target_diff = target_vec - f0
        #target_diff = target_diff/sqrt(inner(target_diff,target_diff))
        #f0 = f0 + step_size*target_diff
        #File(output_path + "fiber_" +str(t)+ ".pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))


        """for  m in range(no_of_int_points):

            for k in range(n_array_length):

                dumped_populations[l, m, k] = y_vec_array[m * n_array_length + k]"""

    rate_constants = np.zeros((no_of_x_bins,no_of_transitions + 1))

    #for l in range(no_of_x_bins):

    #    for m in range(no_of_transitions + 1):

    #        rate_constants[l,m] = Myosim.dump_rate_constants(l, m, 0)
    fluxes, rates = implement.return_rates_fenics(hs)



    #np.save("/home/fenics/shared/python_dev/test_10_pm/rates",rates)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/dumped_populations",dumped_populations)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/tarray",tarray)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/stress_array",strarray)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/pstress_array",p_f)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/calcium",calarray)

    #np.save("/home/fenics/shared/test_10/displacements",darray)

    #np.save("/home/fenics/shared/python_dev/test_10_pm/HSL",hslarray)

    #np.save("/home/fenics/shared/test_10/DHSL",delta_hsls)
    """outputs = {
    "rates": rates,
    "dumped_populations": dumped_populations,
    "tarray": tarray,
    "strarray": strarray,
    "pstrarray": pstrarray,
    "alphaarray": darray,
    "calarray": calarray,
    "hsl": hslarray,
    #"overlap": overlaparray

    }"""
    outputs = {}

    """np.save(output_path +"dumped_populations", dumped_populations)
    np.save(output_path + "tarray", tarray)
    np.save(output_path + "stress_array", strarray)
    np.save(output_path + "hsl", hslarray)
    np.save(output_path + "overlap", overlaparray)
    np.save(output_path + "pstress_array",pstrarray)
    np.save(output_path + "j3",j3_fluxes)
    np.save(output_path + "j4",j4_fluxes)
    #np.save(output_path + "alpha_array",alphaarray)
    np.save(output_path + "calcium",calarray)"""
    fdataCa.close()

    return(outputs)
