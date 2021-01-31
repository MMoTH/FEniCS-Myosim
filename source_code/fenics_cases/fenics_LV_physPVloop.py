from __future__ import division
import sys
sys.path.append("/home/fenics/shared/Research/FEniCS-Myosim/MMotH-Fenics-UK/source_code/dependencies")
import os as os
from dolfin import *
import numpy as np
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver
import math
import Python_MyoSim.half_sarcomere.half_sarcomere as half_sarcomere
import Python_MyoSim.half_sarcomere.implement as implement
import vtk_py
from cell_ion_module import cell_ion_driver
from edgetypebc import *
import objgraph as obg
import pandas as pd
import copy
#np.set_printoptions(threshold=np.inf)

## Fenics simulation function
#
# This simulates some integer number of cardiac cycles.
# As of 07/01/2020, the following is implemented:
# - Combination of Guccione strain-energy function (SEF) and myofiber SEF
# - General MyoSim drives active contraction based on [Ca]2+ from file or 3 state paper
# - 3 compartment Windkessel circulatory system
#
# General layout of this script:
#   - Parse input parameters
#   - Read in mesh, assign fiber, sheet, sheet-normal local coordinate system
#   - Define appropriate finite elements and function spaces
#   - Define variational problem and boundary conditions (active stress calculated here so Newton Iteration can vary it)
#       boundary conditions: zero z-displacement at base, mean x,y displacement = 0
#   - Load ventricle by incrementally increasing cavity volume.
#     No contraction occurs here. Solve for new displacements after each loading step
#   - "Closed Loop Phase"
#       - Solve Windkessel model
#           - Solve for new compartment pressures based on volumes from previous timestep
#           - Calculate blood flow between compartments, update volumes
#       - Solve MyoSim
#           - Calcium updated from cell_ion module before MyoSim call
#           - Interpolate cross-bridges based on solution from previous Newton Iteration
#           - Solve ODEs to get new populations
#       - Solve variational problem to get new displacements
#
# Parameters
# ----------
# @param[in] sim_params Dictionary for setting up the simulation
# @param[in] file_inputs Dictionary containing all file information, now namely just mesh casename
# @param[in] output_params Dictionary to specify output path
# @param[in] passive_params Dictionary for passive material law parameters
# @param[in] hs_params Dictionary for all MyoSim parameters
# @param[in] cell_ion_params Dictionary for cell ion module parameters
# @param[in] monodomain_params Dictionary for monodomain parameters (not implemented)
# @param[in] windkessel_params Dictionary for all Windkessel parameters
# @param[out]
def fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,pso):
    i,j = indices(2)
    #global i
    #global j

    # We don't do pressure control simulations, probably will get rid of this.
    ispressurectrl = False


    #------------------## Load in all information and set up simulation --------

    ## Assign input/output parameters
    output_path = output_params["output_path"][0]
    casename = file_inputs["casename"][0]



    # Assign parameters for Windkessel
    # will be moving circulatory to its own module and pass in dictionary
    # similar to cell_ion module
    Cao = windkessel_params["Cao"][0]
    Cven = windkessel_params["Cven"][0]
    Vart0 = windkessel_params["Vart0"][0]
    Vven0 = windkessel_params["Vven0"][0]
    Rao = windkessel_params["Rao"][0]
    Rven = windkessel_params["Rven"][0]
    Rper = windkessel_params["Rper"][0]
    V_ven = windkessel_params["V_ven"][0]
    V_art = windkessel_params["V_art"][0]


    # --------  Assign parameters for active force calculation  ----------------

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
    hsl_min_threshold = hs_params["myofilament_parameters"]["passive_l_slack"][0]
    hsl_max_threshold = hs_params["myofilament_parameters"]["hsl_max_threshold"][0]
    xfiber_fraction = hs_params["myofilament_parameters"]["xfiber_fraction"][0]


    ## ---------  Set up information for active force calculation --------------

    # Create x interval for cross-bridges
    xx = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)

    # Define number of intervals cross-bridges are defined over
    no_of_x_bins = np.shape(xx)[0]

    # Define the length of the populations vector
    n_array_length = no_of_attached_states * no_of_x_bins + no_of_detached_states + 2 # +2 for binding sites on/off

    # Need to work out a general way to set this based on the scheme
    n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1]]


    #------------  Start setting up simulation ---------------------------------
    sim_duration = sim_params["sim_duration"][0]
    save_output = sim_params["save_output"][0]
    step_size = sim_params["sim_timestep"][0]
    loading_number = sim_params["loading_number"][0]
    if sim_params["sim_geometry"][0] == "ventricle" or sim_params["sim_geometry"][0] == "ventricle_lclee_2" or sim_params["sim_geometry"][0] == "ventricle_physloop":
        # For ventricle for now, specify number of cardiac cycles
        cycles = sim_params["sim_type"][1]
        meshfilename = sim_params["sim_type"][2]
    # Cardiac cycle length and number of cycles will be general
    # For now, just including this info in the input file
    BCL = sim_duration # ms

    hsl0 = hs_params["initial_hs_length"][0] # this is now set when creating mesh
    no_of_time_steps = int(cycles*BCL/step_size)
    no_of_cell_time_steps = int(BCL/step_size)

    deg = 4
    parameters["form_compiler"]["quadrature_degree"]=deg
    parameters["form_compiler"]["representation"] = "quadrature"

    # Clear out any old results files
    os.system("rm " + output_path + "*.pvd")
    os.system("rm " + output_path + "*.vtu")


    #--------------- Load in mesh, initialize things from it -------------------

    mesh = Mesh()
    f = HDF5File(mpi_comm_world(), meshfilename, 'r')
    f.read(mesh, casename, False)

    if casename == "ellipsoidal":
        #loading_number = 25;
        ugrid = vtk_py.convertXMLMeshToUGrid(mesh)
        ugrid = vtk_py.rotateUGrid(ugrid, sx=0.11, sy=0.11, sz=0.11)
        mesh = vtk_py.convertUGridToXMLMesh(ugrid)

        #don't need to do the vtk_py mesh stuff
    else: #assuming we are using a patient specific mesh
        ugrid = vtk_py.convertXMLMeshToUGrid(mesh)
        ugrid = vtk_py.rotateUGrid(ugrid, sx=0.1, sy=0.1, sz=0.1)
        mesh = vtk_py.convertUGridToXMLMesh(ugrid)

    no_of_int_points = 14 * np.shape(mesh.cells())[0]
    print "num_int_points" + str(no_of_int_points)

    facetboundaries = MeshFunction("size_t", mesh, 2)
    edgeboundaries = MeshFunction("size_t", mesh, 1)

    # set surface id numbers:
    topid = 4
    LVendoid = 2
    epiid = 1

    # Define referential facet normal
    N = FacetNormal (mesh)

    # Define spatial coordinate system used in rigid motion constraint
    X = SpatialCoordinate (mesh)

    # ---------  Initialize finite elements  -----------------------------------

    # Vector element at gauss points (for fibers)
    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'

    # General quadrature element whose points we will evaluate myosim at
    Quadelem = FiniteElement("Quadrature", tetrahedron, degree=deg, quad_scheme="default")
    Quadelem._quad_scheme = 'default'

    # Vector element for displacement
    Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
    Velem._quad_scheme = 'default'

    # Quadrature element for pressure
    Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
    Qelem._quad_scheme = 'default'

    # Real element for rigid body motion boundary condition
    Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
    Relem._quad_scheme = 'default'

    # Mixed element for rigid body motion. One each for x, y displacement. One each for
    # x, y, z rotation
    VRelem = MixedElement([Relem, Relem, Relem, Relem, Relem])


    # ------- Define function spaces on mesh using above elements --------------

    # Quadrature space for information needed at gauss points, such as
    # hsl, cb_force, passive forces, etc.
    Quad = FunctionSpace(mesh, Quadelem)

    # Function space for myosim populations
    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))

    # Function space for local coordinate system (fiber, sheet, sheet-normal)
    fiberFS = FunctionSpace(mesh, VQuadelem)

    # Mixed function space for displacement, pressure, rigid body constraint
    if(ispressurectrl):
        W = FunctionSpace(mesh, MixedElement([Velem,Qelem,VRelem]))
    else:
        W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem,VRelem]))



    # V isn't used? Could define function spaces V: Velem, Q:Qelem,VR: VRelem, then W = V*W*VR
    # but below W is explicitly defined using the elements?
    # could define these once and use them for all projections
    #V = VectorFunctionSpace(mesh, 'CG', 2)
    #TF = TensorFunctionSpace(mesh, 'DG', 1)
    #Q = FunctionSpace(mesh,'CG',1)


    # ------ Initalize functions on above spaces -------------------------------

    # fiber, sheet, and sheet-normal functions
    f0 = Function(fiberFS)
    print f0.vector().array()
    print np.shape(f0.vector())
    #print "free indices of f0 " + str(f0.free_indices())
    s0 = Function(fiberFS)
    n0 = Function(fiberFS)

    # function for original hsl distribution
    hsl0_transmural = Function(Quad)

    # These are now functions because they don't have to be uniform
    c_param = Function(Quad)
    c2_param = Function(Quad)
    c3_param = Function(Quad)

    # Setting the value of the passive functions
    c_param.vector()[:] = passive_params["c"][0]
    c2_param.vector()[:] = passive_params["c2"][0]
    c3_param.vector()[:] = passive_params["c3"][0]

    # Go ahead and read in rest of info from mesh file and close
    # mesh lclee created doesn't have hsl0 variation
    f.read(hsl0_transmural, casename+"/"+"hsl0")
    f.read(f0, casename+"/"+"eF")
    f.read(s0, casename+"/"+"eS")
    f.read(n0, casename+"/"+"eN")

    # read in more mesh info, using MeshFunction for these
    f.read(facetboundaries, casename+"/"+"facetboundaries")
    f.read(edgeboundaries, casename+"/"+"edgeboundaries")

    # finished with the mesh file, close it
    f.close()
    #print f0[0]
    #print np.shape(f0.vector().array())

    # define rest of needed functions
    # mixed function for solver
    w = Function(W)

    # define trial function
    dw = TrialFunction(W)

    # define test function
    wtest = TestFunction(W)

    # separate out individual functions for displacement, pressure, bdry
    if(ispressurectrl):
        du,dp,dc11 = TrialFunctions(W)
    	(u,p,c11) = split(w)
    	(v,q,v11) = TestFunctions(W)
    else:
        du,dp,dpendo,dc11 = TrialFunctions(W)
      	(u,p, pendo,c11) = split(w)
        #(u,p, pendo,c11,lm11) = w.split(True)
      	(v,q, qendo,v11) = TestFunctions(W)

    # function for myosim populations
    y_vec = Function(Quad_vectorized_Fspace)

    # not explicitly defined as a function, but product
    #hsl = sqrt(dot(f0, Cmat*f0))*hsl0_transmural

    # Store old hsl and use for calculation of delta_hsl
    hsl_old = Function(Quad)


    # ------- Set up files for saving information -----------------------------

    # save initial mesh information
    File(output_path + "facetboundaries.pvd") << facetboundaries
    File(output_path + "edgeboundaries.pvd") << edgeboundaries
    File(output_path + "fiber.pvd") << project(f0, VectorFunctionSpace(mesh, "CG", 1))
    File(output_path + "sheet.pvd") << project(s0, VectorFunctionSpace(mesh, "CG", 1))
    File(output_path + "sheet-normal.pvd") << project(n0, VectorFunctionSpace(mesh, "CG", 1))

    # Define paraview files to visualize on mesh
    displacementfile = File(output_path + "u_disp.pvd")
    pk1file = File(output_path + "pk1_act_on_f0.pvd")
    hsl_file = File(output_path + "hsl_mesh.pvd")
    alpha_file = File(output_path + "alpha_mesh.pvd")

    # Instead, initialize file for each of these arrays, and append each time step?
    """calcium_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    active_stress_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    myofiber_passive_stress_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    gucc_fiber_pstress_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    gucc_trans_pstress_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    gucc_shear_pstress_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    alpha_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    filament_overlap_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')
    delta_hsl_df = pd.DataFrame(np.zeros((no_of_time_steps+1,no_of_int_points)),dtype='f8')"""

    calcium = np.zeros(no_of_time_steps)
    calcium_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    calcium_ds = calcium_ds.transpose()

    active_stress_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    active_stress_ds = active_stress_ds.transpose()

    dumped_populations_ds = pd.DataFrame(np.zeros((no_of_int_points,n_array_length)))

    tarray_ds = pd.DataFrame(np.zeros(no_of_time_steps+1),index=None)
    tarray_ds = tarray_ds.transpose()
    tarray = np.zeros(no_of_time_steps)

    p_f_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    p_f_array_ds = p_f_array_ds.transpose()

    pgf_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgf_array_ds = pgf_array_ds.transpose()

    pgt_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgt_array_ds = pgt_array_ds.transpose()

    pgs_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
    pgs_array_ds = pgs_array_ds.transpose()

    #overlaparray = np.zeros((no_of_time_steps+1,no_of_int_points)) # need from previous step
    temp_overlap_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    temp_overlap_ds = temp_overlap_ds.transpose()

    alpha_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    alpha_array_ds = alpha_array_ds.transpose()

    hsl_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
    hsl_array_ds = hsl_array_ds.transpose()

    delta_hsl_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
    delta_hsl_array_ds = delta_hsl_array_ds.transpose()

    temp_overlap = np.zeros((no_of_int_points))
    y_vec_array_new = np.zeros(((no_of_int_points)*n_array_length))
    j3_fluxes = np.zeros((no_of_int_points,no_of_time_steps))
    j4_fluxes = np.zeros((no_of_int_points,no_of_time_steps))
    y_interp = np.zeros((no_of_int_points+1)*n_array_length)


    #test_cbf_storage = pd.Series(np.zeros(no_of_int_points))

    # Saving pressure/volume data
    # define communicator
    comm = mesh.mpi_comm()

    if(MPI.rank(comm) == 0):
        fdataPV = open(output_path + "PV_.txt", "w", 0)
        """hsl_data_file = open(output_path + "hsl_file.txt", "w", 0)
        cbforce_file = open(output_path + "cbforce.txt", "w", 0)
        calcium_data_file = open(output_path + "calcium.txt", "w", 0)
        myosim_fiber_passive_file = open(output_path + "fiber_passive.txt", "w", 0)
        guccione_fiber_pstress_file = open(output_path + "gucc_fiber.txt", "w", 0)
        guccione_trans_pstress_file = open(output_path + "gucc_trans.txt", "w", 0)
        guccione_shear_pstress_file = open(output_path + "gucc_shear.txt", "w", 0)
        alpha_txt_file = open(output_path + "alpha.txt", "w", 0)
        overlap_file = open(output_path + "overlap.txt", "w", 0)"""

    #--------- some miscellaneous definitions ----------------------------------
    isincomp = True#False

    # initialize LV cavity volume
    LVCavityvol = Expression(("vol"), vol=0.0, degree=2)

    y_vec_array_new = np.zeros(no_of_int_points*n_array_length)

    #Press = Expression(("P"), P=0.0, degree=0)
    #Kspring = Constant(100)

    if(ispressurectrl):
    	pendo = []

    # ------- Dirichlet bdry for fixing base in z ------------------------------
    bctop = DirichletBC(W.sub(0).sub(2), Expression(("0.0"), degree = 2), facetboundaries, topid)
    bcs = [bctop]


    # ------- Set parameters for forms file, where stresses and things are calculated
    params= {"mesh": mesh,
             "facetboundaries": facetboundaries,
             "facet_normal": N,
             "mixedfunctionspace": W,
             "mixedfunction": w,
             "displacement_variable": u,
             "pressure_variable": p,
             "lv_volconst_variable": pendo,
             "lv_constrained_vol":LVCavityvol,
             "LVendoid": LVendoid,
             "LVendo_comp": 2,
             "fiber": f0,
             "sheet": s0,
             "sheet-normal": n0,
             "incompressible": isincomp,
             "Kappa":Constant(1e5)}

    # Update params from loaded in parameters from json file
    params.update(passive_params)
    params["c"] = c_param
    params["c2"] = c2_param
    params["c3"] = c3_param

    # initialize the forms module
    uflforms = Forms(params)


    # --------- Calculate quantities from form file used in weak form ----------

    LVCavityvol.vol = uflforms.LVcavityvol()
    print("cavity-vol = ", LVCavityvol.vol)

    # Get deformation gradient
    Fmat = uflforms.Fmat()

    # Get right cauchy stretch tensor
    Cmat = (Fmat.T*Fmat)


    # Get Green strain tensor
    Emat = uflforms.Emat()

    # jacobian of deformation gradient
    J = uflforms.J()

    # facet normal in current config
    n = J*inv(Fmat.T)*N

    # integration measure
    dx = dolfin.dx(mesh,metadata = {"integration_order":2})

    # get passive material strain energy function
    Wp = uflforms.PassiveMatSEF()

    #Active force calculation------------------------------------------------------
    # can we move this to the forms file?
    # define 'active_params' as dict and send to forms?
    #hsl = sqrt(dot(f0, Cmat*f0))*hsl0_transmural # must project if want to set directly
    hsl = sqrt(dot(f0, Cmat*f0))*hsl0
    #f0 = 1/k(U(f0) - f0)
    delta_hsl = hsl - hsl_old
    cb_force = Constant(0.0)
    y_vec_split = split(y_vec)
    print "shape of y_vec_split is " + str(np.shape(y_vec_split))

    for jj in range(no_of_states):

        f_holder = Constant(0.0)

        if state_attached[jj] == 1:

            cb_ext = cb_extensions[jj]

            for k in range(no_of_x_bins):
                temp_holder = Constant(0.0)

                dxx = xx[k] + delta_hsl * filament_compliance_factor

                n_pop = y_vec_split[n_vector_indices[jj][0] + k]

                temp_holder = n_pop * k_cb_multiplier[jj] * (dxx + cb_ext) * conditional(gt(dxx + cb_ext,0.0), k_cb_pos, k_cb_neg)
                #temp_holder = temp_holder * conditional(gt(abs(dxx),x_bin_max),0.0,1.0)
                f_holder = f_holder + temp_holder
                #f_holder = f_holder + conditional(gt(temp_holder,0.0),temp_holder,0.0)

            f_holder = f_holder * cb_number_density * 1e-9

            f_holder = f_holder * alpha_value

        cb_force = cb_force + f_holder

    cb_force = cb_force * conditional(gt(cb_force,0.0),1.0,0.0)

    # use cb_force to form active stress tensor
    print np.shape(f0)
    Pactive = cb_force * as_tensor(f0[i]*f0[j], (i,j)) + xfiber_fraction*cb_force * as_tensor(s0[i]*s0[j], (i,j))+ xfiber_fraction*cb_force * as_tensor(n0[i]*n0[j], (i,j))


    # -------- pre-allocation and initialization -------------------------------

    tstep = 0
    #t = 0

    LVcav_array = np.zeros(no_of_time_steps+1)
    LVcav_array[0] = uflforms.LVcavityvol()
    Pcav_array = np.zeros(no_of_time_steps+1)
    Pcav_array[0] = uflforms.LVcavitypressure()*0.0075

    # Contraction phase
    #tarray = []



    # Get array of cross-bridge populations
    y_vec_array = y_vec.vector().get_local()[:]

    hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:]

    #delta_hsl_array = np.zeros(no_of_int_points)

    for init_counter in range(0,n_array_length * no_of_int_points,n_array_length):
        # Initializing myosin heads in the off state
        y_vec_array[init_counter] = 1
        # Initialize all binding sites to off state
        y_vec_array[init_counter-2] = 1

    Pg, Pff, alpha = uflforms.stress()
    # Pg is guccione stress tensor as first Piola-Kirchhoff

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

    # ------ Define terms for variational problem ------------------------------

    # passive material contribution
    F1 = derivative(Wp, w, wtest)*dx

    # active stress contribution (Pactive is PK1, transform to PK2)
    F2 = inner(Fmat*Pactive, grad(v))*dx

    # volumetric stress
    if(ispressurectrl):
        pressure = Expression(("p"), p=0.0, degree=2)
        F3 = inner(pressure*n, v)*ds(LVendoid)
    else:
        Wvol = uflforms.LVV0constrainedE()
        F3 = derivative(Wvol, w, wtest)

    # constrain rigid body motion
    L4 = inner(as_vector([c11[0], c11[1], 0.0]), u)*dx + \
    	 inner(as_vector([0.0, 0.0, c11[2]]), cross(X, u))*dx + \
    	 inner(as_vector([c11[3], 0.0, 0.0]), cross(X, u))*dx + \
    	 inner(as_vector([0.0, c11[4], 0.0]), cross(X, u))*dx
    F4 = derivative(L4, w, wtest)

    Ftotal = F1 + F2 + F3 + F4

    Jac1 = derivative(F1, w, dw)
    Jac2 = derivative(F2, w, dw)
    Jac3 = derivative(F3, w, dw)
    Jac4 = derivative(F4, w, dw)

    Jac = Jac1 + Jac2 + Jac3 + Jac4

    # ----- Set up solver, using default but can use LCLee nsolver -------------
    solverparams = {"Jacobian": Jac,
                    "F": Ftotal,
                    "w": w,
                    "boundary_conditions": bcs,
                    "Type": 0,
                    "mesh": mesh,
                    "mode": 0
                    }

    solver= NSolver(solverparams)


    # -----------------------------


    # Loading phase
    #print "memory growth before loading:"
    #obg.show_growth()

    print("cavity-vol = ", LVCavityvol.vol)
    for lmbda_value in range(0, loading_number):

        print "Loading phase step = ", lmbda_value

        LVCavityvol.vol += 0.004 #LCL change to smaller value

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        hsl_array_old = hsl_array

        #solver.solvenonlinear()
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim


        temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        delta_hsl_array = hsl_array - hsl_array_old

        temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        alphas = interpolate(temp_DG_1, Quad)
        alpha_array = alphas.vector().get_local()[:]

        temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)
        pgf_array = pgf.vector().get_local()[:]
        temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgt = interpolate(temp_DG_3, Quad)
        pgt_array = pgt.vector().get_local()[:]
        temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgs = interpolate(temp_DG_4, Quad)
        pgs_array = pgs.vector().get_local()[:]


        if(MPI.rank(comm) == 0):

            print >>fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, V_cav, 0.0, 0.0, 0.0
            displacementfile << w.sub(0)
            pk1temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'DG',1))
            pk1temp.rename("pk1temp","pk1temp")
            pk1file << pk1temp
            hsl_temp = project(hsl,FunctionSpace(mesh,'DG',1))
            hsl_temp.rename("hsl_temp","hsl")
            hsl_file << hsl_temp
            alpha_temp = project(alphas,FunctionSpace(mesh,'DG',0))
            alpha_temp.rename("alpha_temp","alpha_temp")
            alpha_file << alpha_temp

        print("cavity-vol = ", LVCavityvol.vol)
        print("p_cav = ", uflforms.LVcavitypressure())


    # Closed-loop phase

    # Initialize the half-sarcomere class. Its methods will be used to solve for cell populations
    hs = half_sarcomere.half_sarcomere(hs_params,1)

    # Need to create a list of dictionaries for parameters for each gauss point
    hs_params_list = [{}]*no_of_int_points
    passive_params_list = [{}]*no_of_int_points

    # For now, uniform properties
    for jj in np.arange(np.shape(hs_params_list)[0]):
        hs_params_list[jj] = copy.deepcopy(hs_params)
        passive_params_list[jj] = copy.deepcopy(passive_params)

    # Initialize cell ion module
    cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params)

    # Initialize calcium
    calcium[0] = cell_ion.calculate_concentrations(0,0)

    #dumped_populations = np.zeros((no_of_time_steps+1, no_of_int_points, n_array_length))
    dumped_populations = np.zeros((no_of_int_points,n_array_length))

    counter = 0
    cell_counter = 0
    cycle = 0
    AV_old = 0
    MV_old = 1
    systole = 0

    #print "memory growth before closed loop"
    #obg.show_growth()
    while(cycle < cycles):

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        tstep = tstep + step_size
        cycle = math.floor(tstep/BCL)
        cell_time = tstep - cycle*BCL


        if(MPI.rank(comm) == 0):

            print "Cycle number = ", cycle, " cell time = ", cell_time, " tstep = ", tstep, " step_size = ", step_size
            #print >>fdataPV, tstep, p_cav*0.0075 , V_cav, Myosim.Get_Ca()


        Part = 1.0/Cao*(V_art - Vart0);
        Pven = 1.0/Cven*(V_ven - Vven0);
        PLV = p_cav;

        if(MPI.rank(comm) == 0):
            print "P_ven = ",Pven;
            print "P_LV = ", PLV;
            print "P_art = ", Part;

        if(PLV <= Part):

            Qao = 0.0;
            AV_new = 0

        else:

            Qao = 1.0/Rao*(PLV - Part);
            AV_new = 1


        if(PLV >= Pven):

            Qmv = 0.0;
            MV_new = 0

        else:

            Qmv = 1.0/Rven*(Pven - PLV);
            MV_new = 1

        Qper = 1.0/Rper*(Part - Pven);

        if(MV_old == 1 and MV_new == 0):
            systole = 1
        if(AV_old == 1 and AV_new == 0):
            systole = 0

        MV_old = MV_new
        AV_old = AV_new

        if(MPI.rank(comm) == 0):

                print "Q_mv = ", Qmv ;
                print "Q_ao = ", Qao ;
                print "Q_per = ", Qper ;
                if(systole == 1):
                    print "********systole**********"
                else:
                    print "***diastole***"

        """V_cav_prev = V_cav
        V_art_prev = V_art
        V_ven_prev = V_ven
        p_cav_prev = p_cav"""

        V_cav = V_cav + step_size*(Qmv - Qao);
        V_art = V_art + step_size*(Qao - Qper);
        V_ven = V_ven + step_size*(Qper - Qmv);

        LVCavityvol.vol = V_cav

        if(MPI.rank(comm) == 0):

                print "V_ven = ", V_ven;
                print "V_LV = ", V_cav;
                print "V_art = ", V_art;


        #LVcav_array.append(V_cav)
        LVcav_array[counter] = V_cav
        Pcav_array[counter] = p_cav*0.0075
        #Pcav_array.append(p_cav*0.0075)

        if (counter > 0 and (int(counter/no_of_cell_time_steps) == (counter/no_of_cell_time_steps))):
            cell_counter = 0

        cell_counter += 1

        print "cell_counter = ", cell_counter
        """for  i in range(no_of_int_points):

            for j in range(n_array_length):

                dumped_populations[counter, i, j] = y_vec_array[i * n_array_length + j]"""

        # Initialize MyoSim solution holder
        #y_vec_array_new = np.zeros(no_of_int_points*n_array_length)

        # Update calcium
        calcium[counter] = cell_ion.calculate_concentrations(cycle,tstep) #LCL Commented off

        # Now print out volumes, pressures, calcium
        if(MPI.rank(comm) == 0):
            print >>fdataPV, tstep, p_cav*0.0075 , Part*.0075, Pven*.0075, V_cav, V_ven, V_art, calcium[counter]

        # Quick hack
        if counter == 0:
            overlap_counter = 1
        else:
            overlap_counter = counter
    # Going to try to loop through integration points in python, not in fenics script
        #temp_overlap, y_interp, y_vec_array_new = implement.update_simulation(hs, step_size, delta_hsl_array, hsl_array, y_vec_array, p_f_array, cb_f_array, calcium[counter], n_array_length, cell_time, overlaparray[overlap_counter,:])
        #temp_overlap, y_interp, y_vec_array_new = implement.update_simulation(hs, step_size, delta_hsl_array, hsl_array, y_vec_array, p_f_array, cb_f_array, calcium[counter], n_array_length, cell_time)
        for mm in np.arange(no_of_int_points):
                    #print hsl_array[mm]
                    temp_overlap[mm], y_interp[mm*n_array_length:(mm+1)*n_array_length], y_vec_array_new[mm*n_array_length:(mm+1)*n_array_length] = implement.update_simulation(hs, step_size, delta_hsl_array[mm], hsl_array[mm], y_vec_array[mm*n_array_length:(mm+1)*n_array_length], p_f_array[mm], cb_f_array[mm], calcium[counter], n_array_length, tstep,hs_params_list[mm])
        for  i in range(no_of_int_points):

            for j in range(n_array_length):

                dumped_populations[i, j] = y_interp[i * n_array_length + j]


        y_vec_array = y_vec_array_new # for Myosim

        #Kurtis moved to here
        y_vec.vector()[:] = y_vec_array # for PDE

        hsl_array_old = hsl_array

        #print hsl_array_old
        # Kurtis assigning hsl_old function for newton iteration
        hsl_old.vector()[:] = hsl_array_old[:]


###########################################################################

        #solver.solvenonlinear()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        """try:
            solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})
        except:
            print "Newton Iteration non-convergence, saving myosim info"
            np.save(output_path +"dumped_populations", dumped_populations)
            np.save(output_path + "tarray", tarray)
            np.save(output_path + "stress_array", strarray)
            np.save(output_path + "hsl", hslarray)
            np.save(output_path + "overlap", overlaparray)
            np.save(output_path + "gucc_fiber", gucc_fiber)
            np.save(output_path + "gucc_trans", gucc_trans)
            np.save(output_path + "gucc_shear", gucc_shear)
            np.save(output_path + "deltahsl", deltahslarray)
            np.save(output_path + "pstress_array",pstrarray)
            #np.save(output_path + "alpha_array",alphaarray)
            np.save(output_path + "calcium",calarray)"""
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        cb_f_array[:] = project(cb_force, Quad).vector().get_local()[:]

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim

        delta_hsl_array = hsl_array - hsl_array_old

        temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        alphas = interpolate(temp_DG_1, Quad)
        alpha_array = alphas.vector().get_local()[:]

        temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)
        pgf_array = pgf.vector().get_local()[:]
        temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgt = interpolate(temp_DG_3, Quad)
        pgt_array = pgt.vector().get_local()[:]
        temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgs = interpolate(temp_DG_4, Quad)
        pgs_array = pgs.vector().get_local()[:]

        displacementfile << w.sub(0)
        pk1temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'DG',1))
        pk1temp.rename("pk1temp","pk1temp")
        pk1file << pk1temp
        hsl_temp = project(hsl,FunctionSpace(mesh,'DG',1))
        hsl_temp.rename("hsl_temp","hsl")
        hsl_file << hsl_temp
        alpha_temp = project(alphas,FunctionSpace(mesh,'DG',0))
        alpha_temp.rename("alpha_temp","alpha_temp")
        alpha_file << alpha_temp

        print "shape of time array" + str(np.shape(tarray))
        tarray[counter] = tstep
        counter += 1

        if save_output:

            active_stress_ds.iloc[0,:] = cb_f_array[:]
            active_stress_ds.to_csv(output_path + 'active_stress.csv',mode='a',header=False)

            #active_stress_ds = active_stress_ds.transpose()
            hsl_array_ds.iloc[0,:] = hsl_array[:]
            hsl_array_ds.to_csv(output_path + 'half_sarcomere_lengths.csv',mode='a',header=False)

            calcium_ds.iloc[0,:] = calcium[counter]
            calcium_ds.to_csv(output_path + 'calcium.csv',mode='a',header=False)

            for i in range(no_of_int_points):
                dumped_populations_ds.iloc[i,:] = dumped_populations[i,:]
            dumped_populations_ds.to_csv(output_path + 'populations.csv',mode='a',header=False)

            tarray_ds[counter] = tarray[counter]
            tarray_ds.to_csv(output_path + 'time.csv',mode='a',header=False)

            p_f_array_ds.iloc[0,:] = p_f_array[:]
            p_f_array_ds.to_csv(output_path + 'myofiber_passive.csv',mode='a',header=False)

            pgf_array_ds.iloc[0,:] = pgf_array[:]
            pgf_array_ds.to_csv(output_path + 'gucc_fiber_pstress.csv',mode='a',header=False)

            pgt_array_ds.iloc[0,:] = pgt_array[:]
            pgt_array_ds.to_csv(output_path + 'gucc_trans_pstress.csv',mode='a',header=False)

            pgs_array_ds.iloc[0,:] = pgs_array[:]
            pgs_array_ds.to_csv(output_path + 'gucc_shear_pstress.csv',mode='a',header=False)

            temp_overlap_ds.iloc[0,:] = temp_overlap[:]
            temp_overlap_ds.to_csv(output_path + 'overlap.csv',mode='a',header=False)

            alpha_array_ds.iloc[0,:] = alpha_array[:]
            alpha_array_ds.to_csv(output_path + 'alpha.csv',mode='a',header=False)

            delta_hsl_array_ds.iloc[0,:] = delta_hsl_array[:]
            delta_hsl_array_ds.to_csv(output_path + 'delta_hsl.csv',mode='a',header=False)

        #overlaparray[counter,:] = temp_overlap

    if(MPI.rank(comm) == 0):
        fdataPV.close()
        #fdataCa.close()

    #fluxes, rates = implement.return_rates_fenics(hs)


    # Generate dictionary for output
    """outputs = {
    "rates": rates,
    "dumped_populations": dumped_populations,
    "tarray": tarray,
    "strarray": strarray,
    "pstrarray": pstrarray,
    "gucc_fiber": gucc_fiber,
    "gucc_trans": gucc_trans,
    "gucc_shear": gucc_shear,
    "alphaarray": alphaarray,
    "calarray": calarray,
    "hsl": hslarray,
    "overlap": overlaparray
    }"""

    success = 1
    return(success)

    ######################################################################################################
