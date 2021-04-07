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


def fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params):
    i,j = indices(2)

    output_path = output_params["output_path"][0]
    displacementfile = File(output_path + "u_disp.pvd")

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


    #prev_ca = np.load("calcium_10.npy")
    #prev_ca = prev_ca[:,0]

    #xml_struct = ut.parse('pm_test10.xml')
    #hs_params = xml_struct.single_circulation_simulation.half_sarcomere
    hs = half_sarcomere.half_sarcomere(hs_params,1)
    cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params)
    calcium = np.zeros(time_steps)
    calcium[0] = cell_ion.model_class.calculate_concentrations(0,0)
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

        # Vector element at gauss points (for fibers)
    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'


    no_of_int_points = 4 * np.shape(mesh.cells())[0]
    #print no_of_int_points

    #plot(mesh)
    #plt.show()
      # Function space for local coordinate system (fiber, sheet, sheet-normal)



    #f0.vector().array()[:] = [1.0,0.0,0.0]

    #f0 = Constant((1.0, 0.0, 0.0))
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
    Quad = FunctionSpace(mesh, Quadelem)

    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))


    # Kurtis trying to initialize vectors
    fiberFS = FunctionSpace(mesh, VQuadelem)
    f0 = Function(fiberFS)

    File(output_path + "fiber1.pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))

    ugrid=vtk_py.convertXMLMeshToUGrid(mesh)

    File(output_path + "fiber2.pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))


    gdim = mesh.geometry().dim()
    xdofmap = fiberFS.sub(0).dofmap().dofs()
    ydofmap = fiberFS.sub(1).dofmap().dofs()
    zdofmap = fiberFS.sub(2).dofmap().dofs()



    xq = fiberFS.tabulate_dof_coordinates().reshape((-1,gdim))
    xq0 = xq[xdofmap]
    print "xq0 shape " + str(np.shape(xq0))

    points = vtk.vtkPoints()
    vertices = vtk.vtkCellArray()
    #ugrid = vtk.vtkUnstructuredGrid()

    nb_cells = ugrid.GetNumberOfCells()
    print "num cells = " + str(nb_cells)
    fvecs = vtk_py.createFloatArray("fvecs",3,24)

    for i in np.arange(24):
        fvecs.InsertTuple(i,[1.0,0.0,0.0])

    cnt=0

    for pt in xq0:
        points.InsertNextPoint([pt[0], pt[1], pt[2]])
        vertex = vtk.vtkVertex()
        vertex.GetPointIds().SetId(0, cnt)
        vertices.InsertNextCell(vertex)
        cnt += 1

    ugrid.SetPoints(points)
    ugrid.SetCells(0, vertices)

    vtk_py.CreateVertexFromPoint(ugrid)

    #fvecs[:] = f0.vector()[:]
    #ugrid.GetCellData().AddArray(f0.vector())


    ugrid.GetCellData().AddArray(fvecs)
    vtk_py.writeXMLUGrid(ugrid, output_path + "fiber_ugrid.vtu")

    cnt = 0
    for pt in xq0:
        print cnt
        fvec = fvecs.GetTuple(cnt)
        f0.vector()[xdofmap[cnt]] = fvec[0]
        f0.vector()[ydofmap[cnt]] = fvec[1]
        f0.vector()[zdofmap[cnt]] = fvec[2]
        cnt +=1

    mesh = vtk_py.convertUGridToXMLMesh(ugrid)

    """cnt =0

    for pt in xq0:
        print "assigning vector"
        f0.vector()[xdofmap[cnt]] = 1.0*cnt; f0.vector()[ydofmap[cnt]] = 0.0; f0.vector()[zdofmap[cnt]] = 0.0;
        cnt +=1"""

    print f0[0]
    print "shape of f0 " + str(np.shape(f0.vector().array()))
    
    #print "free indices of f0 " + str(f0.free_indices())

    
    #f0.vector()[:] = 1.0
    
    File(output_path + "fiber.pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))
    #test_tensor = as_tensor(f0*f0)

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
    	 "Kappa":Constant(1e5)}
    params.update(passive_params)

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
    print "shape of yvecsplit " + str(np.shape(y_vec_split))

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
    Pactive = cb_force * as_tensor(s0[i]*s0[j], (i,j))
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
    hslarray = []
    calarray = []
    strarray = []
    pstrarray = []
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

    Pg, Pff, alpha = uflforms.stress()

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

    t = 0.0
    #delta_hsls = np.zeros((time_steps,24))
    for l in range(time_steps):



        tarray.append(t)
        for  m in range(no_of_int_points):

            for k in range(n_array_length):

                dumped_populations[l, m, k] = y_interp[m * n_array_length + k]

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
        calcium[l] = cell_ion.model_class.calculate_concentrations(cycle,t)

        #calcium[l] = cell_ion.model.calculate_concentrations(0,t)

        # Looping through integration points within Python Myosim, not here
        # Debugging, checking if y_input matches y_output between steps
        #print y_vec_array[0:53]
        # Quick hack
        if l == 0:
            overlap_counter = 1
        else:
            overlap_counter = l

        temp_overlap, y_interp, y_vec_array_new = implement.update_simulation(hs, step_size, delta_hsl_array, hsl_array, y_vec_array, p_f_array, cb_f_array, calcium[l], n_array_length, t,overlaparray[overlap_counter,:])
    #    print y_vec_array_new[0:53]
        y_vec_array = y_vec_array_new # for Myosim
        y_vec.vector()[:] = y_vec_array # for PDE

    #    print y_vec_array[0:53]
        hsl_array_old = hsl_array


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

        hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for PDE

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim

        delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim

        #delta_hsls[l] = delta_hsl_array
        temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        cb_f_array = project(cb_force, Quad).vector().get_local()[:]
        strarray.append(cb_f_array[0])
        pstrarray.append(p_f_array[0])
        hslarray.append(hsl_array[0]+delta_hsl_array[0])
        overlaparray[l,:] = temp_overlap


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
        if t < 20:
            u_D.u_D += 0.001
        else:
            u_D.u_D = u_D.u_D
        t = t + step_size

        calarray.append(hs.Ca_conc*np.ones(no_of_int_points))

        # Update Fiber orientation
        #f0 = f0+step_size*(Cmat*f0-f0)/sqrt(inner(Cmat*f0-f0,Cmat*f0-f0))
        target_vec = Cmat*f0
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
