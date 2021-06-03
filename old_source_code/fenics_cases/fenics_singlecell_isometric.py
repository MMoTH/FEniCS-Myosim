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
import copy
import timeit


def fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,pso):
    global i
    global j

    # forcing hsl from other simulation
    """hsl_template = np.zeros(701)
    hsl_template[0:700] = np.load('hsl_template_altered.npy')
    hsl_template[700] = hsl_template[699]
    print "hsl template " + str(np.shape(hsl_template))"""
    output_path = output_params["output_path"][0]
    displacementfile = File(output_path + "u_disp.pvd")
    pk1_file = File(output_path + "active_stress.pvd")
    fiber_file = File(output_path + "f0_direction.pvd")


    filament_compliance_factor = hs_params["myofilament_parameters"]["filament_compliance_factor"][0]
#    filament_compliance_factor = 0.5

    no_of_states = hs_params["myofilament_parameters"]["num_states"][0]
    #no_of_states = 3
    #no_of_attached_states = 1
    #no_of_detached_states = 2
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
    kappa_kroon = sim_params["kroon_rate"][0]
    shorten_flag = 0

    #no_of_transitions = 4
    #state_attached = [0, 0, 1]
    #cb_extensions = [ 0, 0, 4.75642]
    #k_cb_multiplier = [ 1.0, 1.0, 1.0]
    #k_cb_pos = 0.001
    #k_cb_neg = 0.001
    #cb_number_density = 7.67e16
    #alpha_value = 1.0

    #x_bin_min = -12
    #x_bin_max = +12
    #x_bin_increment = 0.5
    xx = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)
    no_of_x_bins = np.shape(xx)[0]
    n_array_length = no_of_attached_states * no_of_x_bins + no_of_detached_states + 2
    n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1]]

    #hsl0 = 1000
    hsl0 = hs_params["initial_hs_length"][0]
    #time_steps = 401
    #time_steps = 2
    #step_size = 0.5
    step_size = sim_params["sim_timestep"][0]
    sim_duration = sim_params["sim_duration"][0]
    time_steps = int(sim_duration/step_size +1)
    Ca_flag = 4
    constant_pCa = 6.5

    fdataCa = open(output_path + "calcium_.txt", "w", 0)

    fx_rxn = np.zeros((time_steps))


    #prev_ca = np.load("calcium_10.npy")
    #prev_ca = prev_ca[:,0]

    #xml_struct = ut.parse('pm_test10.xml')
    #hs_params = xml_struct.single_circulation_simulation.half_sarcomere
    hs = half_sarcomere.half_sarcomere(hs_params,1)

    cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params)
    calcium = np.zeros(time_steps)
    calcium[0] = cell_ion.calculate_concentrations(0,0)
    parameters["form_compiler"]["quadrature_degree"]=2
    parameters["form_compiler"]["representation"] = "quadrature"
    #
    #os.system("rm *.pvd")
    #os.system("rm *.vtu")
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
            return on_boundary and abs(x[0]-1.0) < tol
    #  where x[2] = 0
    class Lower(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[2]) < tol
    #  where x[1] = 0
    class Front(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[1]) < tol
    #  where x[0], x[1] and x[2] = 0
    class Fix(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[0]) < tol and abs(x[1]) < tol and abs(x[2]) < tol
    #
    #
    mesh = UnitCubeMesh(1,1,1)
    #mesh.cells()
    no_of_int_points = 4 * np.shape(mesh.cells())[0]
    temp_overlap = np.zeros((no_of_int_points))
    y_vec_array_new = np.zeros(((no_of_int_points)*n_array_length))
    j3_fluxes = np.zeros((no_of_int_points,time_steps))
    j4_fluxes = np.zeros((no_of_int_points,time_steps))

    hs_params_list = [{}]*no_of_int_points
    for jj in np.arange(np.shape(hs_params_list)[0]):
        hs_params_list[jj] = copy.deepcopy(hs_params)
    #plot(mesh)
    #plt.show()

    #f0 = Constant((1.0, 0.0, 0.0))
    # Vector element at gauss points (for fibers)
    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'
    fiberFS = FunctionSpace(mesh, VQuadelem)
    f0 = Function(fiberFS)
    temp_f = Function(fiberFS)
    f = Function(fiberFS)
    f_diff = Function(fiberFS)
    scaled_fdiff = Function(fiberFS)

    if kappa_kroon > 0.0:
        # initialize fibers away from long axis
        for ff in np.arange(no_of_int_points):
            f0.vector()[ff*3] = 1.0/sqrt(2)
            f0.vector()[ff*3+1] = 1.0/sqrt(2)
            f0.vector()[ff*3+2] = 0.0
    for jj in np.arange(no_of_int_points):
        f0.vector()[jj*3] = 1.0
    File(output_path + "fiber.pvd") << project(f0,VectorFunctionSpace(mesh, "DG", 0))

    s0 = Constant((0.0, 1.0, 0.0))
    n0 = Constant((0.0, 0.0, 1.0))

    facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
    facetboundaries.set_all(0)
    left = Left()
    right = Right()
    fix = Fix()
    lower = Lower()
    front = Front()
    #
    left.mark(facetboundaries, 1)
    right.mark(facetboundaries, 2)
    fix.mark(facetboundaries, 3)
    lower.mark(facetboundaries, 4)
    front.mark(facetboundaries, 5)

    File(output_path + "facetboundaries.pvd") << facetboundaries

    #
    ds = dolfin.ds(subdomain_data = facetboundaries)
    #
    ###############################################################################
    #
    #
    isincomp = True#False
    N = FacetNormal (mesh)
    #Cparam = Constant(1.0e2)                                                        #??


    TF = TensorFunctionSpace(mesh, 'DG', 1)

    Velem = VectorElement("Lagrange", tetrahedron, 2, quad_scheme="default")
    Velem._quad_scheme = 'default'
    Qelem = FiniteElement("Lagrange", tetrahedron, 1, quad_scheme="default")
    Qelem._quad_scheme = 'default'
    Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
    Quadelem._quad_scheme = 'default'

    W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
    x_dofs = W.sub(0).sub(0).dofmap().dofs()

    Quad = FunctionSpace(mesh, Quadelem)
    # making these functions so they no longer have to be uniform
    c_param = Function(Quad)
    c2_param = Function(Quad)
    c3_param = Function(Quad)

    c_param.vector()[:] = passive_params["c"][0]
    c2_param.vector()[:] = passive_params["c2"][0]
    c3_param.vector()[:] = passive_params["c3"][0]


    # Putting them back in the "passive_params" dictionary so that when
    # the dictionary is updated below, it reflects these changes
    passive_params["c"] = c_param
    passive_params["c2"] = c2_param
    passive_params["c3"] = c3_param

    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))

    # assigning BCs
    u_D = Expression(("u_D"), u_D = 0.0, degree = 2)
    bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
    bcright= DirichletBC(W.sub(0).sub(0), u_D, facetboundaries, 2)
    bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
    bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
    bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)        # u2 = 0 on front face
    bcs = [bcleft, bclower, bcfront, bcright,bcfix]

    du,dp = TrialFunctions(W)
    w = Function(W)
    dw = TrialFunction(W)
    (u,p) = split(w)
    (v,q) = TestFunctions(W)
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
         "hsl0": hsl0,
    	 "Kappa":Constant(1e5)}
    params.update(passive_params)

    uflforms = Forms(params)


    Fmat = uflforms.Fmat()
    Cmat = (Fmat.T*Fmat)
    Emat = uflforms.Emat()
    Umat = uflforms.Umat()
    J = uflforms.J()

    n = J*inv(Fmat.T)*N
    dx = dolfin.dx(mesh,metadata = {"integration_order":2})
    hsl = sqrt(dot(f0, Cmat*f0))*hsl0

    #Ematrix = project(Emat, TF)
    Wp = uflforms.PassiveMatSEF(hsl)

    #Active force calculation------------------------------------------------------
    y_vec = Function(Quad_vectorized_Fspace)
    hsl_old = Function(Quad)
    #hsl_old = hsl
    delta_hsl = hsl - hsl_old
    #delta_hsl = 0.0

    #f_holder = Constant(0.0)
    cb_force = Constant(0.0)

    y_vec_split = split(y_vec)

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

    Pactive = cb_force * as_tensor(f0[i]*f0[j], (i,j))
    Press = Expression(("P"), P=0.0, degree=0)
    # Automatic differentiation  #####################################################################################################
    F1 = derivative(Wp, w, wtest)*dx
    F2 = inner(Fmat*Pactive, grad(v))*dx
    F3 = inner(Press*N, v)*ds(2, domain=mesh)
    Ftotal = F1 + F2 - F3

    Jac1 = derivative(F1, w, dw)
    Jac2 = derivative(F2, w, dw)
    Jac3 = derivative(F3, w, dw)
    Jac = Jac1 + Jac2 - Jac3
    ##################################################################################################################################

    # Contraction phase
    '''header_file = open("./C++/hs.h","r")
    code = header_file.read()
    header_file.close()

    ext_module = compile_extension_module(code=code, source_directory="C++", sources=["hs.cpp", "mf.cpp", "Ca.cpp", "base_parameters.cpp"],
         additional_system_headers=["petscvec.h"],
         include_dirs=[".", os.path.abspath("C++"),"/usr/include", "./C++"],
         library_dirs = ['/usr/lib/x86_64-linux-gnu'],
         libraries = ['libgsl.a'])

    Myosim = ext_module.hs()

    _FE_params = {"step_size": step_size};
    Myosim.FE_params.update(_FE_params)

    _Ca_params = {"Ca_flag": Ca_flag};
    Myosim.Ca_params.update(_Ca_params)

    _Ca_params = {"constant_pCa": constant_pCa};
    Myosim.Ca_params.update(_Ca_params)'''


    darray = []
    tarray = []
    hslarray = np.zeros((time_steps+1,no_of_int_points))
    calarray = []
    strarray = np.zeros((time_steps+1,no_of_int_points))
    pstrarray = np.zeros((time_steps+1,no_of_int_points))
    overlaparray = np.zeros((time_steps+1,no_of_int_points))

    y_vec_array = y_vec.vector().get_local()[:]

    hsl_array = project(hsl, Quad).vector().get_local()[:]

    #hsl_array = np.ones(no_of_int_points)*hsl0
    delta_hsl_array = np.zeros(no_of_int_points)

    for counter in range(0,n_array_length * no_of_int_points,n_array_length):
        #y_vec_array[counter] = 1
        # Starting all in on state for Debugging
        y_vec_array[counter] = 1
        y_vec_array[counter-2] = 1

    Pg, Pff, alpha = uflforms.stress(hsl)

    temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]

    temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    alphas = interpolate(temp_DG_1, Quad)
    alpha_array = alphas.vector().get_local()[:]

    '''P,S,T = uflforms.stress()
    Pff =  inner(f0,P*f0)
    p_f = project(Pff, Quad)
    p_f_array = p_f.vector().get_local()[:]'''

    #p_f = np.load("/home/fenics/shared/python_dev/test_10/passive_forces.npy")

    cb_f_array = project(cb_force, Quad).vector().get_local()[:]

    dumped_populations = np.zeros((time_steps, no_of_int_points, n_array_length))
    y_interp = np.zeros(no_of_int_points*n_array_length)

    """marker_space = FunctionSpace(mesh,'CG',1)
    bc_right_test = DirichletBC(marker_space,Constant(1),facetboundaries,2)
    test_marker_fcn = Function(marker_space)
    bc_right_test.apply(test_marker_fcn.vector())"""

    t = 0.0
    #delta_hsls = np.zeros((time_steps,24))
    for l in range(time_steps):
        start_time = timeit.default_timer()



        tarray.append(t)


        #hslarray.append(hsl_array[0])
        #strarray.append(cb_f_array[0])
        #pstrarray.append(p_f_array[0])

    #    _Ca_params = {"time_point": l};
    #    Myosim.Ca_params.update(_Ca_params)


        #print p_f[l]

        #for k in range(no_of_int_points):
        #    pop_holder = implement.update_simulation(hs, step_size, delta_hsl_array[k], hsl_array[k], y_vec_array[k*n_array_length:(k+1)*n_array_length],p_f_array[k], cb_f_array[k], prev_ca[l])
    #    y_vec_array_new = Myosim.apply_time_step(y_vec_array, delta_hsl_array, hsl_array, p_f_array, cb_f_array)
        #y_vec_array_new[k*n_array_length:(k+1)*n_array_length] = pop_holder

        # Right now, not general. The calcium depends on cycle number, just saying 0
        cycle = 0
        calcium[l] = cell_ion.calculate_concentrations(step_size,l)

        #calcium[l] = cell_ion.model.calculate_concentrations(0,t)

        # Looping through integration points within Python Myosim, not here
        # Debugging, checking if y_input matches y_output between steps
        #print y_vec_array[0:53]
        # Quick hack
        if l == 0:
            overlap_counter = 1
        else:
            overlap_counter = l

        for mm in np.arange(no_of_int_points):
            #print hsl_array[mm]
            temp_overlap[mm], y_interp[mm*n_array_length:(mm+1)*n_array_length], y_vec_array_new[mm*n_array_length:(mm+1)*n_array_length] = implement.update_simulation(hs, step_size, delta_hsl_array[mm], hsl_array[mm], y_vec_array[mm*n_array_length:(mm+1)*n_array_length], p_f_array[mm], cb_f_array[mm], calcium[l], n_array_length, t,hs_params_list[mm])
            temp_flux_dict, temp_rate_dict = implement.return_rates_fenics(hs)
            #print temp_flux_dict["J3"]
            j3_fluxes[mm,l] = sum(temp_flux_dict["J3"])
            j4_fluxes[mm,l] = sum(temp_flux_dict["J4"])
        y_vec_array = y_vec_array_new # for Myosim
        for  m in range(no_of_int_points):

            for k in range(n_array_length):

                dumped_populations[l, m, k] = y_interp[m * n_array_length + k]

        y_vec.vector()[:] = y_vec_array # for PDE

    #    print y_vec_array[0:53]
        hsl_array_old = hsl_array

        if work_loop:
            if l > 12:
                Press.P = fx_rxn[11]
                bcs = [bcleft, bclower, bcfront,bcfix]


        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})

        np.save(output_path +"dumped_populations", dumped_populations)
        np.save(output_path + "tarray", tarray)
        np.save(output_path + "stress_array", strarray)
        np.save(output_path + "hsl", hslarray)
        np.save(output_path + "overlap", overlaparray)
        np.save(output_path + "pstress_array",pstrarray)
        #np.save(output_path + "alpha_array",alphaarray)
        np.save(output_path + "calcium",calarray)

        displacementfile << w.sub(0)
        pk1temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'CG',1))
        pk1temp.rename("active_stress","active_stress")
        pk1_file << pk1temp

        hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for PDE

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim

        delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim

        #delta_hsls[l] = delta_hsl_array
        temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        cb_f_array = project(cb_force, Quad).vector().get_local()[:]
        #strarray.append(cb_f_array[0])
        strarray[l,:] = cb_f_array[:]
        pstrarray[l,:] = p_f_array[:]
        #hslarray.append(hsl_array[0]+delta_hsl_array[0])
        hslarray[l,:] = hsl_array[:] #+ delta_hsl_array[:]
        overlaparray[l,:] = temp_overlap

        if kappa_kroon>0.0:
            if t >= 15:
                temp_f = Umat*f0
                f_mag = sqrt(inner(temp_f,temp_f))
                f = temp_f/f_mag
                f_diff = f-f0
                scaled_fdiff = f_diff * (step_size/kappa_kroon)
                scaled_f_assign = project(scaled_fdiff,VectorFunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
                scaled_f_2 = interpolate(scaled_f_assign, fiberFS)
                #print temp_f.type()

                f0.vector()[:] += scaled_f_2.vector()[:]
                f0_temp = project(f0, VectorFunctionSpace(mesh, "DG", 0))
                f0_temp.rename('fiber_direction','fiber_direction')
                fiber_file << f0_temp

        # Calculate reaction force at right end
        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})
        bcleft.apply(b)

        f_int_total = b.copy()
        for kk in x_dofs:
            fx_rxn[l] += f_int_total[kk]

        np.save(output_path + "fx",fx_rxn)


        #print(cb_f_array)

        # Calculate reaction force at right end
        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})

        bcleft.apply(b)
        bclower.apply(b)
        bcfront.apply(b)
        bcfix.apply(b)


        f_int_total = b.copy()
        for kk in x_dofs:
            fx_rxn[l] += f_int_total[kk]
        #bcleft.apply(f_int_total)
        #FX = 0
        #for kk in x_dofs:
        #    FX += f_int_total[i]

        #fx_rxn[l] = Fx
        np.save(output_path + "fx",fx_rxn)


        if t <= 10:
            u_D.u_D = u_D.u_D
        if t > 10 and t < 15:
            u_D.u_D += 0.05
        if t >=15:
            u_D.u_D = u_D.u_D
        """and t < 70:
            u_D.u_D -= 0.007
        if  t >= 70 and t < 150:
            u_D.u_D = u_D.u_D
        if t >= 150:
            u_D.u_D += 0.003"""
        #print "time = " + str(t)
        #print hsl_template[l]
        #u_D.u_D = hsl_template[l]-1
        t = t + step_size

        calarray.append(hs.Ca_conc*np.ones(no_of_int_points))
        elapsed = timeit.default_timer() - start_time
        print "time loop elapsed = " + str(elapsed)

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
    if pso:
        passive_params["c"] = c_param.vector()[0]
        passive_params["c2"] = c2_param.vector()[0]
        passive_params["c3"] = c3_param.vector()[0]

    outputs = {
    "rates": rates,
    "dumped_populations": dumped_populations,
    "tarray": tarray,
    "strarray": strarray,
    "pstrarray": pstrarray,
    "alphaarray": darray,
    "calarray": calarray,
    "hsl": hslarray,
    "overlap": overlaparray

    }

    np.save(output_path +"dumped_populations", dumped_populations)
    np.save(output_path + "tarray", tarray)
    np.save(output_path + "stress_array", strarray)
    np.save(output_path + "hsl", hslarray)
    np.save(output_path + "overlap", overlaparray)
    np.save(output_path + "pstress_array",pstrarray)
    #np.save(output_path + "alpha_array",alphaarray)
    np.save(output_path + "calcium",calarray)
    fdataCa.close()

    return(outputs)
