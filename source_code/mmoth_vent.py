# @Author: charlesmann
# @Date:   2021-09-20T19:22:52-04:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T17:11:57-05:00



from __future__ import division
import sys
sys.path.append("/mnt/home/f0101140/Desktop/FEniCS-Myosim/dependencies/")
sys.path.append("/mnt/home/f0101140/Desktop/FEniCS-Myosim/source_code/")
#sys.path.append("/home/fenics/shared/dependencies/")
#sys.path.append("/home/fenics/shared/source_code/")
import os as os
from dolfin import *
import numpy as np
from forms import Forms
from nsolver import NSolver as NSolver
import math
import Python_MyoSim.half_sarcomere.half_sarcomere as half_sarcomere
import Python_MyoSim.half_sarcomere.implement as implement
from cell_ion_module import cell_ion_driver
from edgetypebc import *
import pandas as pd
import copy
from methods import mesh_import
from methods.mesh_import import mesh_import as mesh_import
from methods.assign_initial_hsl import assign_initial_hsl as assign_hsl
from methods.assign_local_coordinate_system import assign_local_coordinate_system as lcs
from methods.assign_heterogeneous_params import assign_heterogeneous_params as assign_params
from methods.assign_heterogeneous_params import initialize_dolfin_functions as initialize_dolfin_functions
from methods.set_boundary_conditions import set_bcs as set_bcs
from methods.circulatory_module import circulatory_module as cm
from methods.update_boundary_conditions import update_boundary_conditions
from methods.save_solution import save_solution
from methods.load_solution import load_solution as load_sol
from methods.grow_mesh import grow_mesh
import recode_dictionary
import json
import timeit
import scipy.interpolate as interpol

#import datetime
#import append_to_log as aplog


#def fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params):
def fenics(sim_params):

    # declare these as indices for things like as_tensor()
    i,j = indices(2)
    m,k = indices(2)


    ## Assign simulation parameters
    sim_geometry = sim_params["simulation_geometry"][0] #unit_cube, cylinder, ventricle
    if sim_geometry == "unit_cube":
        geo_options = {}
        print "creating empy geo_options dictionary"
    else:
        geo_options = sim_params["geometry_options"]

    sim_protocol = sim_params["protocol"] # contains simulation dependent options

    sim_timestep = sim_protocol["simulation_timestep"][0]
    sim_duration = sim_protocol["simulation_duration"][0] # can be overwritten in ventricle protocol once number of cycles and heartrate specified
    no_of_time_steps = int(sim_duration/sim_timestep)
    t = np.linspace(0,sim_duration,no_of_time_steps)
    save_cell_output = sim_params["save_cell_output"][0] # myosim output
    save_visual_output = sim_params["save_visual_output"][0] # paraview files for visualization
    if "load_solution" in sim_params.keys():
	load_solution = sim_params["load_solution"][0]
	load_solution_dir = sim_params["load_solution"][1]
    else:
	load_solution = 0
    if "save_solution" in sim_params.keys():
	save_solution_flag = sim_params["save_solution"][0]
    else:
	save_solution_flag = 0
    output_path = sim_params["output_path"][0]
    print "output path: ", output_path

    # assign amount of random variation in f0 (cube and cylinder simulations, 0 means normal alignment)
    gaussian_width = sim_params["fiber_orientation"]["fiber_randomness"][0]

    # growth parameters
    #if 'growth_params' in locals():
    #print "ASSIGNING GROWTH PARAMS"
    if "save_fx_only" in sim_params.keys():
        save_fx_only = sim_params["save_fx_only"][0]
    else:
        save_fx_only = 0
    if 'growth_params' in globals():
        print "loading growth params"
        if "eccentric_growth" in growth_params.keys():
            ecc_growth_rate = growth_params["eccentric_growth"]["time_constant"][0]
            set_point = growth_params["eccentric_growth"]["passive_set_point"][0]
            k_myo_damp = Constant(growth_params["eccentric_growth"]["k_myo_damp"][0])
        if "fiber_reorientation" in growth_params.keys():
            print "ASSIGNING FIBER REMODELING LAW PARAMS"
            ordering_law = growth_params["fiber_reorientation"]["law"][0]
            kroon_time_constant = growth_params["fiber_reorientation"]["time_constant"][0]
            print "KROON TIME CONSTANT =",kroon_time_constant
            reorient_start_time = growth_params["fiber_reorientation"]["reorient_t_start"][0]
            stress_name = growth_params["fiber_reorientation"]["stress_type"][0]
            #print "reorient start timestep", float(reorient_start_time)/float(sim_timestep)+1
            #print "loaded growth params"
    else:
        k_myo_damp = 0.0




#------------------------------------------------------------------------------
#           Mesh Information
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#           Initialize myosim info for active stress calculation
#------------------------------------------------------------------------------

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
    xfiber_fraction = hs_params["myofilament_parameters"]["xfiber_fraction"][0]

    # Create x interval for cross-bridges
    xx = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)
    # Define number of intervals cross-bridges are defined over
    no_of_x_bins = np.shape(xx)[0]
    # Define the length of the populations vector
    n_array_length = no_of_attached_states * no_of_x_bins + no_of_detached_states + 2
    # need to generalize this
    if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "3state_with_SRX":
        n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1]]
    if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "4state_with_SRX":
        n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1], [(2+no_of_x_bins), (2+no_of_x_bins)+no_of_x_bins-1]]

    # Load in previous solution?
    if load_solution > 0:
        expressions_loaded,functions_loaded,wk_params_loaded = load_sol.load_solution(load_solution_dir,sim_geometry,sim_protocol,n_array_length)
        mesh = functions_loaded["mesh"]
        facetboundaries = functions_loaded["facetboundaries"]
        edgeboundaries = functions_loaded["edgeboundaries"]
        subdomains = functions_loaded["subdomains"]
    else:
        mesh,lv_options = mesh_import.import_mesh(sim_geometry, geo_options)
        facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
        edgeboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-2)
        subdomains = MeshFunction('int', mesh, 3)
    print "checking geo_options after mesh import"
    print geo_options
    File(output_path + '/test_mesh_import.pvd') << mesh

    # define communicator, for running with multiple cores in parallel
    comm = mesh.mpi_comm()


    no_of_cells = len(subdomains.array())
    #print 'no_of_cells: ', no_of_cells


    # from the mesh, define some things
    if sim_geometry == "cylinder" or sim_geometry == "unit_cube" or sim_geometry == "box_mesh" or sim_geometry == "gmesh_cylinder":
        no_of_int_points = 4 * np.shape(mesh.cells())[0]
        deg = 2
        ds = dolfin.ds(subdomain_data = facetboundaries)
        fx_rxn = np.zeros((no_of_time_steps))

    else:
        #ventricle modeling
        # Kurtis changing this 6/17/21 to test accuracy/time
        #deg = 4
        #no_of_int_points = 14 * np.shape(mesh.cells())[0]

        deg = 2
        no_of_int_points = 4 * np.shape(mesh.cells())[0]
        #set surface id numbers
        topid = 4
        LVendoid = 2
        epiid = 1

    parameters["form_compiler"]["quadrature_degree"]=deg
    parameters["form_compiler"]["representation"] = "quadrature"
    #edgeboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-2)
    N = FacetNormal (mesh)
    X = SpatialCoordinate (mesh)
    dx = dolfin.dx(mesh,metadata = {"integration_order":2})
    isincomp = True

    # periodic boundary condition
    class PeriodicBoundary(SubDomain):
        def inside(self, x, on_boundary):
            tol = 1E-14
            return on_boundary and abs(x[1]) < tol
        def map(self, x, y):
            # map coordinate from x on top to y on bottom
            y[0] = x[0]
            y[1] = x[1]-1.0
            y[2] = x[2]

    pbc = PeriodicBoundary()



    #hsl0 = hs_params["initial_hs_length"][0]

#------------------------------------------------------------------------------
#           Storage data frames
#------------------------------------------------------------------------------

    ## Create files for saving information if needed.
    # cell level info is saved through a pandas command later
    displacement_file = File(output_path + "u_disp.pvd")
    if save_visual_output:
        # Can visualize pretty much anything. For now, just looking at deformation
        # and the active stress magnitude
        tensor_file = File(output_path + "active_stress_tensor.pvd")
        displacement_file = File(output_path + "u_disp.pvd")
        active_stress_file = File(output_path + "active_stress_magnitude.pvd")
        hsl_file = File(output_path + "hsl_mesh.pvd")
        pk2_fiber_passive_file = File(output_path + "pk2_passive_f0.pvd")
        rxn_force_file = File(output_path + "rxn_force.pvd")
        # Want to visualize fiber directions through simulation
        fiber_file = File(output_path + "f0_vectors.pvd")
        sheet_file = File(output_path + "s0_vectors.pvd")
        sheet_normal_file = File(output_path+"n0_vectors.pvd")
        mesh_file = File(output_path + "mesh_growth.pvd")
        #fibrotc_fiber_file = File(output_path + "fibrotic_f0.pvd")
        # set up f0 vs time array
        f0_vs_time_array = np.zeros((no_of_int_points,3,no_of_time_steps))
        print "shape of f0 vs time",np.shape(f0_vs_time_array)
        #stress visualization
        pk2_passive_file = File(output_path + "pk2_passive.pvd")
        f0_deformed_file = File(output_path + "f0_deformed.pvd")
        #alpha_file = File(output_path + "alpha_mesh.pvd")
        #eigen_file = File(output_path + "stress_eigen.pvd")
        shearfs_file = File(output_path + "shear_fs.pvd")
        shearfn_file = File(output_path + "shear_fn.pvd")
	shearsn_file = File(output_path + "shear_sn.pvd")

        stress_eigen_ds = pd.DataFrame(np.zeros((no_of_int_points,3)),index=None)
        f_adjusted_ds = pd.DataFrame(np.zeros((no_of_int_points,3)),index=None)


    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        # initialize a file for pressures and volumes in windkessel
        if (MPI.rank(comm) == 0):
            fdataPV = open(output_path + "PV_.txt", "w", 0)

    if save_cell_output:

        # storage arrays to print to file
        # active stress
        active_stress_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        active_stress_ds = active_stress_ds.transpose()

        # saving f0 vectors
        f0_components = np.empty((no_of_int_points,3,no_of_time_steps))
        f0_components[:] = np.NaN

        calcium_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        calcium_ds = calcium_ds.transpose()

        # myosim populations
        dumped_populations_ds = pd.DataFrame(np.zeros((no_of_int_points,n_array_length)))
        dumped_populations = np.zeros((no_of_int_points,n_array_length))

        # passive stressed in myofiber
        p_f_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        p_f_array_ds = p_f_array_ds.transpose()

        # guccione bulk passive stress in fiber direction
        pgf_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        pgf_array_ds = pgf_array_ds.transpose()

        # guccione bulk passive stress in transverse directions
        pgt_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        pgt_array_ds = pgt_array_ds.transpose()

        # guccione bulk passive shear stress
        pgs_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
        pgs_array_ds = pgs_array_ds.transpose()

        # thick and thin filament overlaps
        temp_overlap_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        temp_overlap_ds = temp_overlap_ds.transpose()

        # stretch
        alpha_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        alpha_array_ds = alpha_array_ds.transpose()

        # half-sarcomere length
        hsl_array_ds =pd.DataFrame(np.zeros(no_of_int_points),index=None)
        hsl_array_ds = hsl_array_ds.transpose()

        # change in half-sarcomere length
        delta_hsl_array_ds = pd.DataFrame(np.zeros(no_of_int_points),index=None)
        delta_hsl_array_ds = delta_hsl_array_ds.transpose()

    # Initialize some data holders that are necessary
    temp_overlap = np.zeros((no_of_int_points))
    y_vec_array_new = np.zeros(((no_of_int_points)*n_array_length))
    j3_fluxes = np.zeros((no_of_int_points,no_of_time_steps))
    j4_fluxes = np.zeros((no_of_int_points,no_of_time_steps))
    j7_fluxes = np.zeros((no_of_int_points,no_of_time_steps))
    y_interp = np.zeros((no_of_int_points)*n_array_length)
    calcium = np.zeros(no_of_time_steps)
    rxn_force = np.zeros(no_of_time_steps+21)
    avg_fdiff_x_array = np.zeros(no_of_time_steps)
    avg_fdiff_y_array = np.zeros(no_of_time_steps)
    avg_fdiff_z_array = np.zeros(no_of_time_steps)
    reorient_finish_array = np.zeros(no_of_time_steps)
    avg_fdiff_norm_array = np.zeros(no_of_time_steps)
    delta_hsl_array = np.zeros(no_of_int_points)
    traction_switch_flag = 0


    # Put any needed expressions here
    #--------------------------------
    # initialize LV cavity volume, only updated if windkessel is called

    if load_solution > 0:
        LVCavityvol = expressions_loaded["LVCavityvol"]
        u_D = expressions_loaded["u_D"]
        u_top = expressions_loaded["u_top"]
        u_front = expressions_loaded["u_front"]
        Press = expressions_loaded["Press"]
        # define cb for
    else:
        LVCavityvol = Expression(("vol"), vol=0.0, degree=2)
        # displacement boundary expression for end of cell or fiber sims
        u_D = Expression(("u_D"), u_D = 0.0, degree = 0)
        # Forcing volume preserving for biaxial case
        u_top = Expression(("u_top"), u_top = 0.0, degree = 0)
        u_front = Expression(("u_front"), u_front = 0.0, degree = 0)
        # traction boundary condition for end of cell/fiber, could use this to apply
        # a traction to epicardium or something
        Press = Expression(("P"), P=0.0, degree=0)

    sim_protocol["start_diastolic_pressure"] = Press.P

    end_systole = 0
    end_diastole = 0

    # Sometimes define an expression for active stress
    #cb_force2 = Expression(("f"), f=0.0, degree=0)

    expressions = {
        "u_D":u_D,
        "u_top":u_top,
        "u_front":u_front,
        "Press":Press
    }

    if sim_protocol["simulation_type"][0] == "custom":
        custom_disp_array = np.load("./custom_displacement.npy")
    else:
        custom_disp_array = []

#-------------------------------------------------------------------------------
#           Initialize finite elements and function spaces
#-------------------------------------------------------------------------------

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

    Telem2 = TensorElement("Quadrature", mesh.ufl_cell(), degree=deg, shape=2*(3,), quad_scheme='default')
    Telem2._quad_scheme = 'default'
    for e in Telem2.sub_elements():
    	e._quad_scheme = 'default'

    # Mixed element for rigid body motion. One each for x, y displacement. One each for
    # x, y, z rotation
    VRelem = MixedElement([Relem, Relem, Relem, Relem, Relem])


    # ------- Define function spaces on mesh using above elements --------------

    # Constant function space for element-wise application of heterogeneous parameters
    V0 = FunctionSpace(mesh, 'DG', 0)
    param = Function(V0)
    # Quadrature space for information needed at gauss points, such as
    # hsl, cb_force, passive forces, etc.
    Quad = FunctionSpace(mesh, Quadelem)
    # go ahead and get coordinates of quadrature points
    gdim = mesh.geometry().dim()
    xq = Quad.tabulate_dof_coordinates().reshape((-1,gdim))
    np.save(output_path + 'quadrature_dof',xq)
    geo_options["xq"] = xq
    #print "xq 0",xq[0]
    #print "quadrature coordinates", xq
    #print "shape of xq",np.shape(xq)

    # Function space for myosim populations
    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))

    # Function space for local coordinate system (fiber, sheet, sheet-normal)
    fiberFS = FunctionSpace(mesh, VQuadelem)

    # Tensor function space
    TF = TensorFunctionSpace(mesh, 'DG', 1)
    TFQuad = FunctionSpace(mesh, Telem2)
    TF_kroon = TensorFunctionSpace(mesh,'DG',1)

    # Initializing functions to hold growth stimuli
    if load_solution > 0:
        concentric_growth_stimulus = functions_loaded["concentric_growth_stimulus"]
        eccentric_growth_stimulus = functions_loaded["eccentric_growth_stimulus"]
        W = functions_loaded["W"]
        x_dofs = W.sub(0).sub(0).dofmap().dofs() # will use this for x rxn forces later
    else:
        concentric_growth_stimulus = Function(FunctionSpace(mesh, "DG",1))
        eccentric_growth_stimulus = Function(FunctionSpace(mesh,"DG",1))
        if sim_geometry == "cylinder" or sim_geometry == "unit_cube" or sim_geometry == "box_mesh" or sim_geometry == "gmesh_cylinder":
            if sim_protocol["simulation_type"][0] == "ramp_and_hold_simple_shear":
                print "implementing periodic boundary condition"
                W = FunctionSpace(mesh, MixedElement([Velem,Qelem]),constrained_domain=PeriodicBoundary())
            else:
                #W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem]))
                W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
            x_dofs = W.sub(0).sub(0).dofmap().dofs() # will use this for x rxn forces later
            #print "assigned W"
        else:
            W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem,VRelem]))

    #print str(W)
    # Function space to differentiate fibrous tissue from contractile for fiber simulations
    # Can use thise to mark gauss points according to a user defined law in "assign_heterogeneous_params"
    marker_space = FunctionSpace(mesh, 'CG', 1)

#-------------------------------------------------------------------------------
#           Initialize functions on the above spaces
#-------------------------------------------------------------------------------

    # fiber, sheet, and sheet-normal functions
    if load_solution > 0:
        f0 = functions_loaded["f0"]
        s0 = functions_loaded["s0"]
        n0 = functions_loaded["n0"]
    else:
        f0 = Function(fiberFS)
        s0 = Function(fiberFS)
        n0 = Function(fiberFS)

    x_dir = Function(VectorFunctionSpace(mesh,"CG",1))
    x_vec = Function(fiberFS)
    #x_shape = np.shape(x_dir.vector())
    #print x_shape
    #print "x shape"
    x2_shape = np.shape(x_dir.vector().get_local())
    #print x2_shape
    #x_dir.vector()[:] = Constant((1.,0.,0.))
    for jj in np.arange(int(x2_shape[0]/3)):
        x_dir.vector()[jj*3] = 1.
        x_dir.vector()[jj*3+1] = 0.
        x_dir.vector()[jj*3+2] = 0.
    for jj in np.arange(no_of_int_points):
        x_vec.vector()[jj*3] = 1.
        x_vec.vector()[jj*3+1] = 0.
        x_vec.vector()[jj*3+1] = 0.

    #print x_dir.vector().get_local()
    #f0_dot_xvec = inner(f0,x_vec)
    #f0_dot_xvec_array = project(f0_dot_xvec, Quad).vector().get_local()[:]
    #angle_array = np.arccos(f0_dot_xvec_array) # both f0 and x_vec are unit, just need their dot product
    #np.save(output_path + "angle_array.npy",angle_array)
    #f0_array = f0.vector().get_local()[:]
    #x_vec_array = x_vec.vector().get_local()[:]
    #np.save(output_path + "f0_array.npy",f0_array)
    #np.save(output_path + "x_vec_array.npy",x_vec_array)
    #for jj in np.arange(no_of_int_points):
        #x_dir.vector()[jj*3] = 1.
        #x_dir.vector()[jj*3+1] = 0.
        #x_dir.vector()[jj*3+2] = 0.


    # put these in a dictionary to pass to function for assignment
    coord_params = {
        "f0":f0,
        "s0":s0,
        "n0":n0,
        "fiberFS":fiberFS,
        "marker_space":marker_space,
        "sim_geometry":sim_geometry,
        "mesh":mesh,
        "Quad":Quad,
        "no_of_int_points":no_of_int_points,
        "geo_options":geo_options,
        "facetboundaries":facetboundaries,
        "edgeboundaries":edgeboundaries
    }

    # create lists of dictionaries that hold parameters for each gauss point
    # These will remain scalars. I anticipate this will be the case for
    # any parameters that will be passed into existing modules (myosim parameters,
    # possible calcium models, etc)
    hs_params_list = [{}]*no_of_int_points
    #passive_params_list = [{}]*no_of_int_points

    # Must make a deep copy so each item in the list is independent, and not linked
    # to the original paramter dictionary
    for jj in np.arange(np.shape(hs_params_list)[0]):
        hs_params_list[jj] = copy.deepcopy(hs_params) # because this is a copy, everything is initialized
        #passive_params_list[jj] = copy.deepcopy(passive_params)

    # create dictionary of parameters that will be initialized as dolfin functions
    # (anything used by dolfin in calculations will become a function, ex. passive SEF
    # or active stress calculation).
    # dolfin_functions is a nested dictionary
    dolfin_functions = {}
    dolfin_functions["passive_params"] = passive_params
    dolfin_functions["cb_number_density"] = hs_params["cb_number_density"]
    #print "dolfin dict init"
    #print dolfin_functions
    # If anything else needs to eventually be initialized as a function for heterogeneity,
    # add it here. For example if introducing heterogeneity with cell_ion_params:
    # dolfin_functions["cell_ion_params"]=cell_ion_params
    # then it will be searched through for hetereogeneity in the appropriate function

    # Initialize all dolfin functions to take on their base value
    # Kurtis putting in conditional. For fiber sims, need coordinates of points to assign heterogeneity
    if (sim_geometry == "gmesh_cylinder"):
        # fiber simulation
        dolfin_functions = initialize_dolfin_functions.initialize_dolfin_functions(dolfin_functions,Quad)
    else:
        #print "element wise assignment of dolfin functions!!!!!!"
        # element wise assignment
        dolfin_functions = initialize_dolfin_functions.initialize_dolfin_functions(dolfin_functions,Quad)

    # parameters that are heterogeneous declared here as functions
    # Do these need to come from the input file? As part of declaration, "heterogenous = true"?
    # for key in input dictionary:
    #    if dict[key] has value "heterogeneous =  true":
    #        add this param to the list, but how to declare as a function? Hard code for now...

    #c_param = Function(Quad)
    #c2_param = Function(Quad)
    #c3_param = Function(Quad)

    # create heterogeneous function list to be passed in to method "assign_heterogeneous_params"
    # Then
    #heterogeneous_fcn_list = [c_param, c2_param, c3_param]

    # functions for the weak form
    if load_solution > 0:
        #wtemp = functions_loaded["w"]
        w = functions_loaded["w"]
    else:
        w = Function(W)
        #w.assign(wtemp)
        #print "checking w",w.vector().get_local()
    #w     = Function(W)
    #w_array = wtemp.vector().get_local()[:]
    #print "w array",w_array
    #w.assign(w_array)
    #w.assign(wtemp)
    #w.vector().get_local()[:] = wtemp.vector().get_local()[:]
    #print "checking w again",w.vector().get_local()
    dw    = TrialFunction(W)
    wtest = TestFunction(W)

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        # Need the pressure function
        du,dp,dpendo,dc11 = TrialFunctions(W)
        (u,p,pendo,c11)   = split(w)
        (v,q,qendo,v11)   = TestFunctions(W)
        ventricle_params  = {
            "lv_volconst_variable": pendo,
            "lv_constrained_vol":LVCavityvol,
            "LVendoid": LVendoid,
            "LVendo_comp": 2,
        }

    else:
        du,dp = TrialFunctions(W)
        #(u,p,c11) = split(w)
        (u,p) = split(w)
        #(v,q,v11) = TestFunctions(W)
        (v,q) = TestFunctions(W)

    # Initial and previous timestep half-sarcomere length functions
    if load_solution > 0:
        hsl0 = functions_loaded["hsl0"]
        y_vec = functions_loaded["y_vec"]
        #print "loaded y_vec, checking here"
        print y_vec.vector().get_local()
    else:
        hsl0    = Function(Quad)
        y_vec = Function(Quad_vectorized_Fspace)
        hsl0 = assign_hsl.assign_initial_hsl(lv_options,hs_params,sim_geometry,hsl0)
        f0,s0,n0,geo_options = lcs.assign_local_coordinate_system(lv_options,coord_params,sim_params)
    hsl_old = Function(Quad)
    # save array of f0
    f0_array = project(f0,fiberFS).vector().get_local()[:]
    f0_array.reshape((no_of_int_points,3))
    f0_array1 = np.reshape(f0_array,(no_of_int_points,3))
    np.save(output_path+'f0_array.npy',f0_array)

    # Defining functions to calculate how far hsl is from reference, to be used
    # to get back to reference length over time
    pseudo_alpha = Function(Quad)
    pseudo_old = Function(Quad)
    pseudo_old.vector()[:] = 1.0
    hsl_diff_from_reference = Function(Quad)
    hsl_diff_from_reference.vector()[:] = 0.0

    # Population solution holder for myosim, allows active stress to be calculated
    # and adjusted as the Newton Solver tries new displacements

    y_vec_array = y_vec.vector().get_local()[:]

#-------------------------------------------------------------------------------
#           Assign function values
#-------------------------------------------------------------------------------



    f0_dot_x_vec = inner(f0,x_vec)
    f0_dot_xvec_array = project(f0_dot_x_vec,Quad).vector().get_local()[:]
    angles_array = np.arccos(f0_dot_xvec_array)
    np.save(output_path+"angles_array.npy",angles_array)
    f0_array = project(f0,fiberFS).vector().get_local()[:]
    x_vec_array = x_vec.vector().get_local()[:]
    np.save(output_path+"f0_array.npy",f0_array)
    np.save(output_path+"x_vec_array.npy",x_vec_array)

    # Assign the heterogeneous parameters
    #heterogeneous_fcn_list,hs_params_list,passive_params_list = assign_params.assign_heterogeneous_params(sim_params,hs_params_list,passive_params_list,geo_options,heterogeneous_fcn_list,no_of_int_points)
    hs_params_list,dolfin_functions = assign_params.assign_heterogeneous_params(sim_params,hs_params,hs_params_list,dolfin_functions,geo_options,no_of_int_points,no_of_cells)
    #print "cb density"
    #print dolfin_functions["passive_params"]["bt"][-1].vector().get_local()
    #print "k3"

    # Select fibers for visualization (exclude stiff regions)
    binary_mask = np.zeros((no_of_int_points),dtype=int)
    #print 'binary_mask vs c_param length: ', str(len(binary_mask)) + '/'+ str(len(dolfin_functions["passive_params"]["c"][-1].vector().get_local()))
    """for jj in np.arange(no_of_cells):
        hetero_c_param = dolfin_functions["passive_params"]["c"][-1].vector().get_local()[jj]
        original_c_param = float(passive_params["c"][0])
        if hetero_c_param != original_c_param:
            binary_mask[jj*4:jj*4+4] = 1"""

    #print 'first for c_param and binary mask: ', str(dolfin_functions["passive_params"]["c"][-1].vector().get_local()[0]) + '/' + str(binary_mask[:4])

    temp_fcn_visualization = Function(Quad)
    for mm in np.arange(no_of_int_points):
        temp_fcn_visualization.vector()[mm] = hs_params_list[mm]["myofilament_parameters"]["k_force"][0]
    File(output_path + "k_force.pvd") << project(temp_fcn_visualization,FunctionSpace(mesh,"DG",0))
    File(output_path + "c_param.pvd") << project(dolfin_functions["passive_params"]["c"][-1],FunctionSpace(mesh,"DG",0))
    File(output_path + "cb_density.pvd") << project(dolfin_functions["cb_number_density"][-1],FunctionSpace(mesh,"DG",0))
#-------------------------------------------------------------------------------
#           Save initial values
#-------------------------------------------------------------------------------

    #save initial f0, s0, n0, hsl0
    if save_visual_output:
        hsl_temp = project(hsl0,FunctionSpace(mesh,'DG',0))
        hsl_temp.rename("hsl_temp","half-sarcomere length")
        hsl_file << hsl_temp

    # Test select visualization for fibers
    temp_f0 = f0.copy(deepcopy=True)
    #print 'len(temp_f0): ', len(temp_f0.vector().get_local())
    #print 'len(binary_mask): ', len(binary_mask)
    for index in np.arange(len(binary_mask)):
        if binary_mask[index] == 1:
            temp_f0.vector()[index*3] = 0.0
            temp_f0.vector()[index*3+1] = 0.0
            temp_f0.vector()[index*3+2] = 0.0
    #print 'no_of_int_points: ', no_of_int_points

    File(output_path + "fiber.pvd") << project(temp_f0, VectorFunctionSpace(mesh, "DG", 0))
    File(output_path + "sheet.pvd") << project(s0, VectorFunctionSpace(mesh, "DG", 0))
    File(output_path + "sheet-normal.pvd") << project(n0, VectorFunctionSpace(mesh, "DG", 0))

#-------------------------------------------------------------------------------
#           Initialize the solver and forms parameters, continuum tensors
#-------------------------------------------------------------------------------

    # Initialize growth functions if needed

    # Create growth tensor. Initialized as identity
    M1ij = project(as_tensor(f0[m]*f0[k], (m,k)),TF)
    M2ij = project(as_tensor(s0[m]*s0[k], (m,k)),TF)
    M3ij = project(as_tensor(n0[m]*n0[k], (m,k)),TF)
    #M1ij = Function(TFQuad)
    #print "m1ij shape = " + str(np.shape(M1ij.vector()))
    #M2ij = Function(TFQuad)
    #M3ij = Function(TFQuad)

    Theta1 = Function(FunctionSpace(mesh,"DG",1))
    Theta1.vector()[:] = 1.0

    Theta2 = Function(FunctionSpace(mesh,"DG",1))
    Theta2.vector()[:] = 1.0

    Theta3 = Function(FunctionSpace(mesh,"DG",1))
    Theta3.vector()[:] = 1.0

    # Based on the material coordinates, we can define different Growth Tensor Construct

    Fg = Theta1*(M1ij) +  Theta2*M2ij + Theta3*M3ij #always created, only updated if growth

    #print "fg"
    #print str(Fg.vector().get_local())
    #Fg = as_tensor([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
    #print "Fg"
    #print Fg[0][0]





    # parameters for forms file
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
             "incompressible": isincomp,
             "hsl0": hsl0,
             "Kappa":Constant(1e5),
             "growth_tensor": Fg,
             "M1": M1ij,
             "M2": M2ij,
             "M3": M3ij,
             "TF": TF}

    # update passive params because now they are heterogeneous functions
    # need to generalize this? Need to initialize passive functions (and cb density)
    # and pass these to assign_heterogeneous_params. Then map back from heterogeneous_fcn_list
    # to passive list, and use that passive list here

    #######
    # this needs to probably actually be passive_params_list/dictionary
    # and this list will include a dictionary of functions that can be
    params.update(dolfin_functions["passive_params"])
    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        params.update(ventricle_params)
    #params["c"] = c_param
    #params["c2"] = c2_param
    #params["c3"] = c3_param

    # Initialize the forms module
    uflforms = Forms(params)

    #LVCavityvol.vol = uflforms.LVcavityvol() may initialize this later to avoid another if statement here

    # Get deformation gradient
    Fmat = uflforms.Fmat()
    Fe = uflforms.Fe()
    #print project(Fmat,TensorFunctionSpace(mesh,"DG",1)).vector().get_local()
    #Fmat = uflforms.Fe()
    test_FS = FunctionSpace(mesh,Velem)
    Fmat2 = Function(TF)
    #d = u.ufl_domain().geometric_dimension()
    #Fmat2= Identity(d) + grad(u)
    #print "shape of Fmat:", np.shape(Fmat)
    #print "Shape of u: ", np.shape(u)

    # Get right cauchy stretch tensor
    #Cmat = (Fmat.T*Fmat)
    Cmat = uflforms.Cmat()

    # Get Green strain tensor
    Emat = uflforms.Emat()

    # Polar decomposition stretch tensor, used for Kroon (for now)
    #Umat = uflforms.Umat()     #Umat no longer needed for kroon law as of 2/10/21 (Cmat used instead)

    # jacobian of deformation gradient
    J = uflforms.J()

    # facet normal in current config
    n = J*inv(Fmat.T)*N

#-------------------------------------------------------------------------------
#           Initialize boundary conditions
#-------------------------------------------------------------------------------
    # returns a dictionary of bcs and potentially a test_marker_fcn for work loops
    bc_output = set_bcs.set_bcs(sim_geometry,sim_protocol,geo_options,mesh,W,facetboundaries,expressions)
    bcs = bc_output["bcs"]
    #print "bcs",bcs
    bcright = bcs[-1]
    if (sim_protocol["simulation_type"][0] != "cycle"):
        test_marker_fcn = bc_output["test_marker_fcn"]
    #print "testing display array"
    #print sim_protocol["end_disp_array"]

#-------------------------------------------------------------------------------
#           Active stress calculation
#-------------------------------------------------------------------------------
    # Start with active stress calculation here to validate mmoth_vent, then try
    # to move it to the forms file

    print "hsl0"
    print hsl0.vector().get_local()
    # Calculate a pseudo stretch, not based on deformation gradient
    hsl_old.vector()[:] = hsl0.vector()[:]
    hsl_diff_from_reference = (hsl_old - hsl0)/hsl0
    #print "hsl diff from ref:"
    #print hsl_diff_from_reference.vector().get_local()[:]
    pseudo_alpha = pseudo_old*(1.-(k_myo_damp*(hsl_diff_from_reference)))
    #
    #print "pseudo_alpha:"
    #print project(pseudo_alpha,Quad).vector().get_local()[:]
    alpha_f = sqrt(dot(f0, Cmat*f0)) # actual stretch based on deformation gradient
    #print "alpha_f:"
    #print project(alpha_f,Quad).vector().get_local()[:]
    hsl = pseudo_alpha*alpha_f*hsl0
    #print "hsl:"
    #print project(hsl,Quad).vector().get_local()[:]
    delta_hsl = hsl - hsl_old

    cb_force = Constant(0.0)

    y_vec_split = split(y_vec)
    Wp = uflforms.PassiveMatSEF(hsl)

    for jj in range(no_of_states):
        f_holder = Constant(0.0)
        temp_holder = 0.0

        if state_attached[jj] == 1:
            cb_ext = cb_extensions[jj]

            for kk in range(no_of_x_bins):
                dxx = xx[kk] + delta_hsl * filament_compliance_factor
                n_pop = y_vec_split[n_vector_indices[jj][0] + kk]
                temp_holder = n_pop * k_cb_multiplier[jj] * (dxx + cb_ext) * conditional(gt(dxx + cb_ext,0.0), k_cb_pos, k_cb_neg)
                #temp_holder = conditional(gt(np.abs(dxx),x_bin_max),0,temp_holder)
                #temp_holder_proj = project(temp_holder,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
                #temp_holder_interp = interpolate(temp_holder_proj,Quad)
                #temp_holder_vec = temp_holder_interp.vector().get_local()
                #temp_holder_vec[temp_holder_vec<0.0] = 0.0
                #temp_holder.vector().set_local()[:] = temp_holder_vec
                f_holder = f_holder + temp_holder

            f_holder = f_holder * dolfin_functions["cb_number_density"][-1] * 1e-9
            f_holder = f_holder * alpha_value

        cb_force = cb_force + f_holder

    Pactive = cb_force * as_tensor(f0[m]*f0[k], (m,k))+ xfiber_fraction*cb_force * as_tensor(s0[m]*s0[k], (m,k))+ xfiber_fraction*cb_force * as_tensor(n0[m]*n0[k], (m,k))


    cb_f_array = project(cb_force, Quad).vector().get_local()[:]


#-------------------------------------------------------------------------------
#           Now hsl function is initiated, make sure all arrays are initialized
#-------------------------------------------------------------------------------

    #create hsl_array from projection
    hsl_array = project(hsl, Quad).vector().get_local()[:]

    #initialize y_vec_array to put all hads in SRX and all binding sites to off
    if load_solution < 1:
        for init_counter in range(0,n_array_length * no_of_int_points,n_array_length):
            #print "initializing heads to off state"
            # Initializing myosin heads in the SRX state
            y_vec_array[init_counter] = 1
            # Initialize all binding sites to off state
            y_vec_array[init_counter-2] = 1

    #Get passive stress tensor, magnitude of myofiber passive stress
    PK2_passive,Sff = uflforms.stress(hsl)

    # need p_f_array for myosim
    temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]

    if load_solution > 0:
        print load_sol
        cb_f_array = expressions_loaded["cb_force_loaded"][:]
        p_f_array = expressions_loaded["p_force_loaded"]
    print "cb force array"
    print cb_f_array
    #print np.shape(cb_f_array)
    print "passive array"
    print p_f_array

    # calculate magnitude of passive stress for guccione_fiber, guccione_transverse, and guccione_shear
    #if save_cell_output:

        # Magnitude of bulk passive stress in fiber direction
        #Pg_fiber = inner(f0,Pg*f0)
        #Pg_transverse = inner(n0,Pg*n0)
        #Pg_shear = inner(n0,Pg*f0)

        #temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        #alphas = interpolate(temp_DG_1, Quad)
        #alpha_array = alphas.vector().get_local()[:]

        #temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        #pgf = interpolate(temp_DG_2, Quad)
        #pgf_array = pgf.vector().get_local()[:]
        #temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        #pgt = interpolate(temp_DG_3, Quad)
        #pgt_array = pgt.vector().get_local()[:]
        #temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        #pgs = interpolate(temp_DG_4, Quad)
        #pgs_array = pgs.vector().get_local()[:]




# for LV, initialize LV cavity and LV pressure arrays, and get first values from forms

#-------------------------------------------------------------------------------
#           Weak Form
#-------------------------------------------------------------------------------
    # passive material contribution
    F1 = derivative(Wp, w, wtest)*dx

    # active stress contribution (Pactive is PK2, transform to PK1)
    F2 = inner(Fmat*Pactive, grad(v))*dx

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        print "using F4"
        # LV volume increase
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

    else:
        #print "not using F4"
        F3 = inner(Press*N, v)*ds(2, domain=mesh)

        # constrain rigid body motion
        #L4 = inner(as_vector([0.0, 0.0, c11]), u)*dx
    	 #inner(as_vector([0.0, 0.0, c11[2]]), cross(X, u))*dx + \
    	 #inner(as_vector([c11[3], 0.0, 0.0]), cross(X, u))*dx + \
    	 #inner(as_vector([0.0, c11[4], 0.0]), cross(X, u))*dx

        #F4 = derivative(L4, w, wtest)

        Ftotal = F1 + F2 - F3 #+ F4

        Jac1 = derivative(F1, w, dw)
        Jac2 = derivative(F2, w, dw)
        Jac3 = derivative(F3, w, dw)
        #Jac4 = derivative(F4, w, dw)
        Jac = Jac1 + Jac2 - Jac3 #+ Jac4

    # Can use Dr. Lee's Nsolver if solver needs debugging
    solverparams = {"Jacobian": Jac,
                    "F": Ftotal,
                    "w": w,
                    "boundary_conditions": bcs,
                    "Type": 0,
                    "mesh": mesh,
                    "mode": 0
                    }

    solver= NSolver(solverparams)

#-------------------------------------------------------------------------------
#           Initial loading (for ventricle)
#-------------------------------------------------------------------------------


    # Growing mesh here starting from reference mesh. Hard coded stuff for preliminary sim
    """if growth_params:
        load_stimuli_path = sim_params["load_stimuli_path"][0]
        f = HDF5File(mpi_comm_world(),load_stimuli_path,'r')
        growth_fcn_space = FunctionSpace(mesh,"DG",1)
        concentric_growth_stimulus_loaded = Function(growth_fcn_space)
        eccentric_growth_stimulus_loaded = Function(growth_fcn_space)
        conc_set_point = Function(growth_fcn_space)
        ecc_set_point = Function(growth_fcn_space)
        f.read(concentric_growth_stimulus_loaded,"concentric_growth_stimulus")
        f.read(eccentric_growth_stimulus_loaded,"eccentric_growth_stimulus")
        assign(conc_set_point,concentric_growth_stimulus_loaded)
        assign(ecc_set_point,eccentric_growth_stimulus_loaded)
        f.close()
        conc_set_point *= 0.9
        ecc_set_point *= 0.9
        conc_set_point = project(conc_set_point,growth_fcn_space)
        ecc_set_point = project(ecc_set_point,growth_fcn_space)

        # trying to solve before changing anything.
        LVCavityvol.vol = uflforms.LVcavityvol()
        p_cav = uflforms.LVcavitypressure()
        hsl_array_old = hsl_array
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        hsl_array = project(hsl, Quad).vector().get_local()[:]
        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0"""

        #delta_hsl_array = hsl_array - hsl_array_old

        #for i in np.arange(10):
            #Theta1 += (1/10.)*(concentric_growth_stimulus_loaded - conc_set_point)/conc_set_point
            #Theta2.vector()[:] += 0.01
            #Theta3.vector()[:] += 0.01
            #Fg = project(Theta1*(M1ij) +  Theta2*M2ij + Theta3*M3ij,TF)
            #print "FG"
            #print Fg.vector().get_local()[0:9]
            #uflforms.parameters["growth_tensor"] = Fg
            #Fe = uflforms.Fe()
            #print "FE"
            #print project(Fe,TF).vector().get_local()[0:9]
            #Fmat = uflforms.Fmat()
            #print project(Fmat,TF).vector().get_local()[0:9]

            #solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
            #print "FG"
            #print project(Fg,TF).vector().get_local()[0:9]
            #print "Fe"
            #Fe = uflforms.Fe()
            #print project(Fe,TF).vector().get_local()[0:9]
            #print "F"
            #print project(Fmat,TF).vector().get_local()[0:9]
            #displacement_file << w.sub(0)
            #p_cav = uflforms.LVcavitypressure()
            #V_cav = uflforms.LVcavityvol()
            #LVCavityvol.vol = V_cav
            #print >>fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, LVCavityvol.vol, 0.0, 0.0, 0.0





            #PK2_passive,Sff = uflforms.stress(hsl)
            #hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:]
            #print "Theta1",project(Theta1,growth_fcn_space).vector().get_local()
            #Theta3 += (1/10.)*(concentric_growth_stimulus_loaded - conc_set_point)/conc_set_point
            #print "Theta3",project(Theta3,growth_fcn_space).vector().get_local()
            #Fg = Theta1*(M1ij) + Theta2*M2ij + Theta3*M3ij
            #uflforms.update_Fg(Theta1,Theta2,Theta3)
            #uflforms.parameters["growth_tensor"] = Fg
            #Fe = uflforms.Fe()
            #Fmat = uflforms.Fmat()
            #print "Fg"
            #print project(Fg,TF).vector().get_local()
            #Fe = uflforms.Fe()
            #print "Fe"
            #print project(Fe,TF).vector().get_local()
            #print "Fe", Fe.vector().get_local()
            #print "F",project(Fmat).vector().get_local()
            #hsl_array_old = hsl_array

            #PK2_passive,Sff = uflforms.stress(hsl)
            #Passive_fiber = inner(f0,PK2_passive*f0)

            #temp_DG_2 = project(Passive_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            #pgf = interpolate(temp_DG_2, Quad)
            #pgf_array = pgf.vector().get_local()[:]
            #print "passive in fiber before solve", pgf_array"""


            #solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
            #Fe = uflforms.Fe()
            #print "F after solve",project(Fmat).vector().get_local()
            #hsl_array = project(hsl, Quad).vector().get_local()[:]
            #temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            #p_f = interpolate(temp_DG, Quad)
            #p_f_array = p_f.vector().get_local()[:]

            #for ii in range(np.shape(hsl_array)[0]):
                #if p_f_array[ii] < 0.0:
                    #p_f_array[ii] = 0.0

            #delta_hsl_array = hsl_array - hsl_array_old
            #displacement_file << w.sub(0)
            #PK2_passive,Sff = uflforms.stress(hsl)
            #Passive_fiber = inner(f0,PK2_passive*f0)

            #temp_DG_2 = project(Passive_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            #pgf = interpolate(temp_DG_2, Quad)
            #pgf_array = pgf.vector().get_local()[:]
            #print "passive in fiber after solve", pgf_array
            #p_cav = uflforms.LVcavitypressure()"""
            #print >>fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, LVCavityvol.vol, 0.0, 0.0, 0.0

        #ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
        #File(output_path + "mesh_grown.pvd") << mesh
        #Theta2.vector()[:] = 1.0
        #Theta3.vector()[:] = 1.0
        #solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        #print "FG"
        #print project(Fg,TF).vector().get_local()[0:9]
        #print "Fe"
        #Fe = uflforms.Fe()
        #print project(Fe,TF).vector().get_local()[0:9]
        #print "F"
        #print project(Fmat,TF).vector().get_local()[0:9]
        #displacement_file << w.sub(0)

        #print "KURTIS STOP HERE TO LOOK AT GROWN MESH"


    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):

        LVcav_array = np.zeros(no_of_time_steps)
        LVcav_array[0] = uflforms.LVcavityvol() # hoping that by loading in LVCavityvol and previous stresses, this and Pcav are correct
        Pcav_array = np.zeros(no_of_time_steps)
        Pcav_array[0] = uflforms.LVcavitypressure()*0.0075
        if load_solution > 0:
            print "no initial loading of ventricle"

        else:

            # Load the ventricle from the reference configuration
            LVcav_array = np.zeros(no_of_time_steps)
            LVcav_array[0] = uflforms.LVcavityvol()
            Pcav_array = np.zeros(no_of_time_steps)
            Pcav_array[0] = uflforms.LVcavitypressure()*0.0075

            LVCavityvol.vol = uflforms.LVcavityvol()
            print "Unloaded LV Cavity Volume = ", LVCavityvol.vol

            # Calculate the increment to LV volume
            end_diastolic_volume = sim_protocol["initial_end_diastolic_volume"][0]
            total_vol_loading = end_diastolic_volume - LVCavityvol.vol
            volume_increment = total_vol_loading/sim_protocol["reference_loading_steps"][0]

            for lmbda_value in range(0, sim_protocol["reference_loading_steps"][0]):

                print "Diastolic loading step " + str(lmbda_value)

                LVCavityvol.vol += volume_increment

                p_cav = uflforms.LVcavitypressure()
                V_cav = uflforms.LVcavityvol()

                hsl_array_old = hsl_array

                #solver.solvenonlinear()
                solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

                #print "FG"
                #print project(Fg,TF).vector().get_local()[0:9]
                #print "Fe"
                #Fe = uflforms.Fe()
                #print project(Fe,TF).vector().get_local()[0:9]
                #print "F"
                #print project(Fmat,TF).vector().get_local()[0:9]

                hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim
                print "HALF SARCOMERE LENGTHS",hsl_array[0:20]


                temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
                p_f = interpolate(temp_DG, Quad)
                p_f_array = p_f.vector().get_local()[:]

                for ii in range(np.shape(hsl_array)[0]):
                    if p_f_array[ii] < 0.0:
                        p_f_array[ii] = 0.0

                delta_hsl_array = hsl_array - hsl_array_old

                #if save_cell_output:
                    #temp_DG_1 = project(alpha, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
                    #alphas = interpolate(temp_DG_1, Quad)
                    #alpha_array = alphas.vector().get_local()[:]
                    #temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
                    #pgf = interpolate(temp_DG_2, Quad)
                    #pgf_array = pgf.vector().get_local()[:]
                    #temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
                    #pgt = interpolate(temp_DG_3, Quad)
                    #pgt_array = pgt.vector().get_local()[:]
                    #temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
                    #pgs = interpolate(temp_DG_4, Quad)
                    #pgs_array = pgs.vector().get_local()[:]


                if(MPI.rank(comm) == 0):

                    print >>fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, V_cav, 0.0, 0.0, 0.0

                    if save_visual_output:
                        displacement_file << w.sub(0)
                        pk2temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'DG',0),form_compiler_parameters={"representation":"uflacs"})
                        pk2temp.rename("pk2_active","active_stress")

                        active_stress_file << pk2temp
                        hsl_temp = project(hsl,FunctionSpace(mesh,'DG',0))
                        hsl_temp.rename("hsl_temp","half-sarcomere length")
                        hsl_file << hsl_temp
                        #pk2_save = project(PK2_passive,TensorFunctionSpace(mesh,"DG",0),form_compiler_parameters={"representation": "uflacs"})
                        #rxn_force_file << 0.0
                        #pk2_save.rename("pk2_passive","pk2_passive")
                        #pk2_passive_file << pk2_save


                print("cavity-vol = ", LVCavityvol.vol)
                print("p_cav = ", uflforms.LVcavitypressure())

#-------------------------------------------------------------------------------
#           Time Loop
#-------------------------------------------------------------------------------
    # Initialize half-sarcomere class. Methods used to calculate cross-bridges
    # at gauss points
    hs = half_sarcomere.half_sarcomere(hs_params,1)

    # Initialize cell ion module
    cell_ion = cell_ion_driver.cell_ion_driver(cell_ion_params,sim_timestep,sim_duration)

    # Initialize calcium concentration from cell_ion module
    calcium[0] = cell_ion.calculate_concentrations(sim_timestep,0,0)

    # Initializing growth class if needed
    if 'growth_params' in globals():
        print "initializing growth class"
        #growth_class = grow_mesh.growth(growth_params,FunctionSpace(mesh,'DG',1),sim_timestep)
    else:
        print "no growth parameters given"

    # Load in circulatory module
    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        windkessel_params["PLV"] = [0.0]
        windkessel_params["Part"] = [0.0]
        windkessel_params["Pven"] = [0.0]
        if load_solution > 0:
            windkessel_params["V_ven"][0] = wk_params_loaded["V_ven"]
            windkessel_params["V_art"][0] = wk_params_loaded["V_art"]
            windkessel_params["Part"][0] = wk_params_loaded["Part"]
            windkessel_params["Pven"][0] = wk_params_loaded["Pven"]
            windkessel_params["PLV"][0] = wk_params_loaded["PLV"]
        circ_model = cm.circ_module(windkessel_params)




    for l in np.arange(no_of_time_steps):
        tic = timeit.default_timer()

        """if growth_params:
            print "growth params in locals"
            if "growth_law" in growth_params.keys():
                growth_class.grow_ellipsoid(mesh,concentric_growth_stimulus,windkessel_params["PLV"][0],expressions,bcs,fdataPV,Wp,w,wtest,dx,c11,X,u,dw,displacement_file,uflforms,Pactive,Fmat,v)
        else:
            print "skipping growing ellipsoid" """

        print "Time step number " + str(l)
        if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):

            # update calcium
            calcium[l] = cell_ion.calculate_concentrations(sim_timestep,t[l],l)

            # Update circulatory model
            p_cav = uflforms.LVcavitypressure()
            V_cav = uflforms.LVcavityvol()
            print "Volume of LV = ",V_cav
            circ_dict = circ_model.update_compartments(p_cav,V_cav,sim_timestep)
            LVCavityvol.vol = circ_dict["V_cav"]
            LVcav_array[l] = circ_dict["V_cav"]
            end_systole = circ_dict["end_systole"]
            end_diastole = circ_dict["end_diastole"]
            #LVCavityvol.vol = V_cav
            #LVcav_array[l] = V_cav
            Pcav_array[l] = p_cav*0.0075

            # Now print out volumes, pressures, calcium
            if(MPI.rank(comm) == 0):
                print >>fdataPV, t[l], circ_dict["p_cav"]*0.0075 , circ_dict["Part"]*.0075, circ_dict["Pven"]*.0075, circ_dict["V_cav"], circ_dict["V_ven"], circ_dict["V_art"], calcium[l]

        # update calcium
        # Don't need cycle time for all simulations. For now, just alexus' work loop simulation
        if "track_and_update" in sim_protocol.keys():
            cycle_l = sim_protocol["track_and_update"]["cycle_l"][0]
        else:
            cycle_l = t[l]

        if not ((sim_geometry == "ventricle") or (sim_geometry == "ellipsoid")):
            print sim_timestep
            print "cycle_l",cycle_l
            calcium[l] = cell_ion.calculate_concentrations(sim_timestep,cycle_l,l)

	# else, calcium already calculated for ventricle sims. Standardize time input for calcium!

        # Quick hack
        if l == 0:
            overlap_counter = 1
        else:
            overlap_counter = l

        # At each gauss point, solve for cross-bridge distributions using myosim
        print "calling myosim"
        for mm in np.arange(no_of_int_points):
            temp_overlap[mm], y_interp[mm*n_array_length:(mm+1)*n_array_length], y_vec_array_new[mm*n_array_length:(mm+1)*n_array_length] = implement.update_simulation(hs, sim_timestep, delta_hsl_array[mm], hsl_array[mm], y_vec_array[mm*n_array_length:(mm+1)*n_array_length], p_f_array[mm], cb_f_array[mm], calcium[l], n_array_length, t,hs_params_list[mm])
            temp_flux_dict, temp_rate_dict = implement.return_rates_fenics(hs)
            j3_fluxes[mm,l] = sum(temp_flux_dict["J3"])
            j4_fluxes[mm,l] = sum(temp_flux_dict["J4"])
            if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "4state_with_SRX":
              j7_fluxes[mm,l] = sum(temp_flux_dict["J7"])

        if save_cell_output:
            for  i in range(no_of_int_points):
                for j in range(n_array_length):
                    # saving the interpolated populations. These match up with active
                    # stress from previous timestep
                    dumped_populations[i, j] = y_interp[i * n_array_length + j]

        # Update the populations
        y_vec_array = y_vec_array_new # for Myosim

        # Update the population function for fenics
        y_vec.vector()[:] = y_vec_array # for PDE

        # Update the array for myosim
        hsl_array_old = hsl_array

        # Update the hsl_old function for fenics
        hsl_old.vector()[:] = hsl_array_old[:]
        #print "hsl_old before solve"
        #print project(hsl_old,Quad).vector().get_local()[:]

        # including call to nsolver commented out to show it can be used
        #solver.solvenonlinear()

        print "calling Newton Solver"
        # solve for displacement to satisfy balance of linear momentum

        print "checking things before solve"
        print "cb force"
        print cb_f_array[0:20]
        print "p_f_array"
        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]
        print p_f_array[0:20]



	try:
            solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        except:
            np.save(output_path + 'f0_vs_time.npy',f0_vs_time_array)
	    f0_dot_x_vec = inner(f0,x_vec)
	    f0_dot_x_vec_array = project(f0_dot_x_vec,Quad).vector().get_local()[:]
	    angles_array = np.arccos(f0_dot_x_vec_array)
	    np.save(output_path+"final_angles_array.npy",angles_array)

	#print "FG"
        #print project(Fg,TF).vector().get_local()[0:9]
        #print "Fe"
        #Fe = uflforms.Fe()
        #print project(Fe,TF).vector().get_local()[0:9]
        #print "F"
        #print project(Fmat,TF).vector().get_local()[0:9]



        print "PK2"
        PK2 = project(PK2_passive,TensorFunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})

        # Saving concentric growth stimulus here
        #print "saving stimuli"
        #if end_systole > 0:
        #    end_systolic_stress_calc = inner(f0,(PK2 + Pactive)*f0)
        #    concentric_growth_stimulus = project(end_systolic_stress_calc,FunctionSpace(mesh,"DG",1))
        #print "saving end diastole"
        #if end_diastole > 0:
        #    end_diastolic_stress_calc = inner(f0,(PK2+Pactive)*f0)
        #    eccentric_growth_stimulus = project(end_diastolic_stress_calc,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
        #print PK2.vector().get_local().reshape(24,3,3)
        #total_stress = project(PK2_passive + Pactive,TensorFunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
        #print "checking displacement at midpoints"
        #u_temp,p_temp,c_temp = w.split(True)
        #u_temp,p_temp = w.split(True)
        #print u_temp.vector().get_local().reshape(27,3)
        #print "u bottom middle"
        #p1 = Point(0.5,0.0,0.5)
        #print u_temp(0.5,0,0.5)
        #print "u top middle"
        #print u_temp(0.5,1.,0.5)
        """stress_eigen = uflforms.eigen(PK2,Quad,fiberFS)
        if stress_eigen == "zero array":
            stress_eigen = f0"""

        # Update functions and arrays
        print "cb f array"
        cb_f_array[:] = project(cb_force, Quad).vector().get_local()[:]
        if save_visual_output:
            pk2temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'DG',0),form_compiler_parameters={"representation":"uflacs"})
            pk2temp.rename("pk2_active","active_stress")
            active_stress_file << pk2temp
        #print "hsl_old after solve"
        #print project(hsl_old,Quad).vector().get_local()[:]
        hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for PDE
        pseudo_old.vector()[:] = project(pseudo_alpha, Quad).vector().get_local()[:]
        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim
        print "HALF-SARCOMERE LENGTHS",hsl_array[0:20]
        delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim


        #delta_hsl_array = project(delta_hsl, Quad).vector().get_local()[:]
        #pseudo_old = pseudo_alpha
        #pseudo_old.vector().get_local()[:] = project(pseudo_alpha,Quad).vector().get_local()[:]
        #print "pseudo old"
        #print project(pseudo_old,Quad).vector().get_local()[:]
        #print "pseudo alpha:"
        #print project(pseudo_alpha,Quad).vector().get_local()[:]
        #print "real alpha"
        #print project(alpha_f,Quad).vector().get_local()[:]
        #print "hsl diff from ref "
        #print project(hsl_diff_from_reference,Quad).vector().get_local()[:]
        #print "hsl_old"
        #print project(hsl_old,Quad).vector().get_local()[:]
        #print "hsl0"
        #print project(hsl0,Quad).vector().get_local()[:]
        #print "hsl"
        #print project(hsl,Quad).vector().get_local()[:]

        # For growth
        """temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)"""
        print "p_f_array"
        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        # Kroon update fiber orientation?
	"""if stress_name == "passive":
            driver_type = PK2_passive
        elif stress_name == "active":
            driver_type = Pactive
        elif stress_name == "total":
            driver_type = PK2_passive + Pactive
	elif stress_name == "strain":
	    driver_type = Emat
	if ordering_law == "strain_kroon":
	    driver_type = Emat"""
        #print "Kroon"
        if 'kroon_time_constant' in locals():
            if stress_name == "passive":
                driver_type = PK2_passive
            elif stress_name == "active":
                driver_type = Pactive
            elif stress_name == "total":
                driver_type = PK2_passive + Pactive
            if ordering_law == "strain_kroon":
                driver_type = Emat
            if l > float(reorient_start_time)/float(sim_timestep):
                print "updating fiber orientation"
                if ordering_law == "stress_kroon":
                    fdiff = uflforms.stress_kroon(PK2,Quad,fiberFS,TF_kroon,float(sim_timestep),kroon_time_constant)
                elif ordering_law == "strain_kroon":
                    fdiff = uflforms.kroon_law(fiberFS,float(sim_timestep),kroon_time_constant,binary_mask)
		    f0.vector()[:] += fdiff.vector()[:]
                elif ordering_law == "new_stress_kroon":
                    fdiff = uflforms.new_stress_kroon(driver_type,fiberFS,float(sim_timestep),kroon_time_constant,binary_mask)
		    f0.vector()[:] += fdiff.vector()[:]
                    print "CHECKING NUMBER OF FIBER VECTORS"
                    print np.shape(f0.vector().get_local())
                    print "Fiber orientation updated"
	        #update fiber orientations
                s0,n0 = lcs.update_local_coordinate_system(f0,coord_params)


            """if l == (no_of_time_steps - 1):
                if ordering_law == "stress_kroon":
                    stress_eigen = uflforms.eigen(PK2,Quad,fiberFS)
                    print "stress eigen: "
                    print np.reshape(stress_eigen.vector().get_local(),(no_of_int_points,3))
                else:
                    C_array = project(Cmat,TF_kroon,form_compiler_parameters={"representation":"uflacs"})
                    strain_eigen = uflforms.eigen(C_array,Quad,fiberFS)
                    print "strain eigen: "
                    print np.reshape(strain_eigen.vector().get_local(),(no_of_int_points,3))"""


        """# Kurtis putting call to growth function here
        if "growth_law" in growth_params.keys():
            Theta1, Theta2, Theta3 = growth_class.grow_mesh(PK2_passive,f0,Theta1,Theta2,Theta3,t[l])
            print "theta values"
            print project(Theta1,FunctionSpace(mesh,"CG",1),form_compiler_parameters={"representation":"uflacs"}).vector().get_local()
            Fg = Theta1*(M1ij) + Theta2*M2ij + Theta3*M3ij
            uflforms.parameters["growth_tensor"] = Fg
            Fe = uflforms.Fe()
            solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
            ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
            File(output_path + "mesh_grown.pvd") << mesh"""



        print "updating boundary conditions"
        # Update boundary conditions/expressions (need to include general displacements and tractions)
        # quick hack
        if sim_geometry == "ellipsoid" or sim_geometry == "ventricle":
            x_dofs = 0.0
            x_dofs = 0.0
            test_marker_fcn = 0.0
            traction_switch_flag = 0.0
            x_dir = 0.0 # generalize the input to bc_update dict to be a dictionary that is updated as needed
        bc_update_dict = update_boundary_conditions.update_bcs(bcs,sim_geometry,Ftotal,geo_options,sim_protocol,expressions,t[l],traction_switch_flag,x_dofs,test_marker_fcn,w,mesh,bcright,x_dir,l,W,facetboundaries,custom_disp_array)
        bcs = bc_update_dict["bcs"]
        #print "current bcs"
        #print bcs
        if not (sim_geometry == "ventricle" or sim_geometry == "ellipsoid"):
            traction_switch_flag = bc_update_dict["traction_switch_flag"]
            rxn_force[l] = bc_update_dict["rxn_force"]
            u_D = bc_update_dict["expr"]["u_D"]
            Press = bc_update_dict["expr"]["Press"]
            print "current traction: ", Press.P

        if save_fx_only:
            np.save(output_path + 'fx',rxn_force)
            displacement_file << w.sub(0)
            np.save(output_path+"j7",j7_fluxes)
        
        # Save visualization info
        if save_visual_output:
            displacement_file << w.sub(0)

            # Save all fiber vectors
            f0_vs_time_temp = project(f0,fiberFS).vector().get_local()[:]
            f0_vs_time_temp2 = f0_vs_time_temp.reshape((no_of_int_points,3))
            print "shape of temp f0_vs-time",np.shape(f0_vs_time_temp2)
            f0_vs_time_array[:,:,l] = f0_vs_time_temp2
            if cb_number_density != 0:
		        #pk2temp = project(inner(f0,Pactive*f0),FunctionSpace(mesh,'DG',1),form_compiler_parameters={"representation":"uflacs"})
		        #pk2temp.rename("pk2_active","active_stress")
		        #active_stress_file << pk2temp
                hsl_temp = project(hsl,FunctionSpace(mesh,'DG',0))
                hsl_temp.rename("hsl_temp","half-sarcomere length")
                hsl_file << hsl_temp
                #Pactive_temp = project(Pactive,TensorFunctionSpace(mesh,'DG',0),form_compiler_parameters={"representation":"uflacs"})
                #Pactive_temp.rename("Pactive","Pactive")
                #tensor_file << Pactive_temp

            #rxn_force_file << temp_rxn_force
            np.save(output_path + 'fx',rxn_force)
            # Save fiber vectors associated with non-fibrotic regions separately
            """temp_f0 = f0.copy(deepcopy=True)
            for index in np.arange(len(binary_mask)):
                if binary_mask[index] == 1:
                    temp_f0.vector()[index*3] = 0.0
                    temp_f0.vector()[index*3+1] = 0.0
                    temp_f0.vector()[index*3+2] = 0.0
            f0_temp = project(temp_f0, VectorFunctionSpace(mesh, "DG", 0))
            f0_temp.rename('f0','f0')
            fiber_file << f0_temp"""
            print "saving f0"
            f0_temp = project(f0, VectorFunctionSpace(mesh, "DG", 0))
            f0_temp.rename('f0','f0')
            fiber_file << f0_temp
            # Save fiber vectors associated with fibrotic regions separately
            temp_fibrotic_f0 = f0.copy(deepcopy=True)
            """for index in np.arange(len(binary_mask)):
                if binary_mask[index] == 0:
                    temp_fibrotic_f0.vector()[index*3] = 0.0
                    temp_fibrotic_f0.vector()[index*3+1] = 0.0
                    temp_fibrotic_f0.vector()[index*3+2] = 0.0
            f0_temp = project(temp_fibrotic_f0, VectorFunctionSpace(mesh, "DG", 0))
            f0_temp.rename('fibrotic f0','fibrotic f0')"""
            #fibrotc_fiber_file << f0_temp
	    # Save fdiff for unit cube and simple shear simulations
            if "reorient_start_time" in locals():
                if l > float(reorient_start_time)/float(sim_timestep) and (sim_protocol["simulation_type"][0] == "ramp_and_hold" or sim_protocol["simulation_type"][0] == "ramp_and_hold_simple_shear") and (not (sim_geometry == "gmesh_cylinder")):
		    no_of_vectors = int(len(fdiff.vector().get_local())/3)
		    fdiff_array = abs(fdiff.vector().get_local().reshape(no_of_vectors,3))
		    for i in range(no_of_vectors-1):
		        fdiff_array[0] += fdiff_array[i+1]
		    avg_fdiff_array = fdiff_array[0]/no_of_vectors
		    avg_fdiff_x_array[l] = avg_fdiff_array[0]
		    avg_fdiff_y_array[l] = avg_fdiff_array[1]
		    avg_fdiff_z_array[l] = avg_fdiff_array[2]
		    avg_fdiff_norm_array[l]	= np.linalg.norm(avg_fdiff_array)
		    np.save(output_path + 'avg_fdiff_x', avg_fdiff_x_array)
		    np.save(output_path + 'avg_fdiff_y', avg_fdiff_y_array)
		    np.save(output_path + 'avg_fdiff_z', avg_fdiff_z_array)
		    np.save(output_path + 'avg_fdiff_norm', avg_fdiff_norm_array)
		    if np.linalg.norm(avg_fdiff_array) < 1E-4:
		        reorient_finish_array[l] = l/sim_timestep
		        np.save(output_path + 'reorient_finish',reorient_finish_array)
            #s0_temp = project(s0, VectorFunctionSpace(mesh, "DG", 0))
            #s0_temp.rename('s0','s0')
            #sheet_file << s0_temp
            #n0_temp = project(n0, VectorFunctionSpace(mesh, "DG", 0))
            #n0_temp.rename('n0','n0')
            #sheet_normal_file << n0_temp
            #pk2_passive_save = project(PK2_passive,TensorFunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
            #pk2_passive_save.rename("pk2_passive","pk2_passive")
            #pk2_passive_file << pk2_passive_save
            np.save(output_path+"j7",j7_fluxes)
            np.save(output_path+"j4",j4_fluxes)
            #f0_deformed = project(Fmat*f0,VectorFunctionSpace(mesh,"DG",0))
            #f0_deformed.rename('f0','f0_deformed')
            #f0_deformed_file << f0_deformed
            #File(output_path + "fiber.pvd") << project(f0, VectorFunctionSpace(mesh, "DG", 0))
            """eigen_temp = project(stress_eigen,VectorFunctionSpace(mesh,'DG',0))
            eigen_temp.rename('eigen_temp','stress eigen')
            eigen_file << eigen_temp"""

            if "reorient_t_start" in locals():
                shearfn_temp = project(inner(n0,driver_type*f0),FunctionSpace(mesh,'CG',1),form_compiler_parameters={"representation":"uflacs"})
                shearfn_temp.rename("shear fn","shear fn")
                shearfn_file << shearfn_temp

                shearfs_temp = project(inner(s0,driver_type*f0),FunctionSpace(mesh,'CG',1),form_compiler_parameters={"representation":"uflacs"})
                shearfs_temp.rename("shear fs","shear fs")
                shearfs_file << shearfs_temp

	        shearsn_temp = project(inner(s0,driver_type*n0),FunctionSpace(mesh,'CG',1),form_compiler_parameters={"representation":"uflacs"})
	        shearsn_temp.rename("shear_sn","shear_sn")
	        shearsn_file << shearsn_temp
            """stress_eigen_ds.iloc[:] = stress_eigen.vector().get_local().reshape(no_of_int_points,3)[:]
            stress_eigen_ds.to_csv(output_path + 'stress_eigen.csv',mode='a',header=False)

            f_adjusted_ds.iloc[:] = fdiff.vector().get_local().reshape(no_of_int_points,3)[:]
            f_adjusted_ds.to_csv(output_path + 'f_adjusted.csv',mode='a',header=False)"""


        # Save cell info
        tic_save_cell = timeit.default_timer()
        if save_cell_output:

            """temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            pgf = interpolate(temp_DG_2, Quad)
            pgf_array = pgf.vector().get_local()[:]
            temp_DG_3 = project(Pg_transverse, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            pgt = interpolate(temp_DG_3, Quad)
            pgt_array = pgt.vector().get_local()[:]
            temp_DG_4 = project(Pg_shear, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
            pgs = interpolate(temp_DG_4, Quad)
            pgs_array = pgs.vector().get_local()[:]"""

            active_stress_ds.iloc[0,:] = cb_f_array[:]
            active_stress_ds.to_csv(output_path + 'active_stress.csv',mode='a',header=False)

            # if we want an array of the fiber vectors in the current configuration throughout time
            #f0_components[:,:,l] = np.reshape(project(Fmat*f0,fiberFS).vector().get_local()[:],(24,3))
            #np.save(output_path+'f0_current_config.npy',f0_components)

            #active_stress_ds = active_stress_ds.transpose()
            hsl_array_ds.iloc[0,:] = hsl_array[:]
            hsl_array_ds.to_csv(output_path + 'half_sarcomere_lengths.csv',mode='a',header=False)

            calcium_ds.iloc[0,:] = calcium[l]
            calcium_ds.to_csv(output_path + 'calcium.csv',mode='a',header=False)

            for i in range(no_of_int_points):
                dumped_populations_ds.iloc[i,:] = dumped_populations[i,:]
            dumped_populations_ds.to_csv(output_path + 'populations.csv',mode='a',header=False)

            #tarray_ds[l] = tarray[l]
            #tarray_ds.to_csv(output_path + 'time.csv',mode='a',header=False)
            np.save(output_path+"time", t) # fix this

            p_f_array_ds.iloc[0,:] = p_f_array[:]
            p_f_array_ds.to_csv(output_path + 'myofiber_passive.csv',mode='a',header=False)

            """pgf_array_ds.iloc[0,:] = pgf_array[:]
            pgf_array_ds.to_csv(output_path + 'gucc_fiber_pstress.csv',mode='a',header=False)

            pgt_array_ds.iloc[0,:] = pgt_array[:]
            pgt_array_ds.to_csv(output_path + 'gucc_trans_pstress.csv',mode='a',header=False)

            pgs_array_ds.iloc[0,:] = pgs_array[:]
            pgs_array_ds.to_csv(output_path + 'gucc_shear_pstress.csv',mode='a',header=False)"""

            temp_overlap_ds.iloc[0,:] = temp_overlap[:]
            temp_overlap_ds.to_csv(output_path + 'overlap.csv',mode='a',header=False)

            #alpha_array_ds.iloc[0,:] = alpha_array[:]
            #alpha_array_ds.to_csv(output_path + 'alpha.csv',mode='a',header=False)

            delta_hsl_array_ds.iloc[0,:] = delta_hsl_array[:]
            delta_hsl_array_ds.to_csv(output_path + 'delta_hsl.csv',mode='a',header=False)

        if l == (no_of_time_steps-1): # at last time step
            # save full f0_vs_time
            if 'kroon_time_constant' in locals():
                np.save(output_path+"f0_vs_time.npy",f0_vs_time_array)
            # interpolate cross-bridges one last time to account for final solve
            for mm in np.arange(no_of_int_points):
                delta_x = delta_hsl_array[mm]*filament_compliance_factor
                if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "3state_with_SRX":
                    temp_y = y_vec_array[mm*n_array_length:(mm+1)*n_array_length]
                    interp_positions = xx - delta_x
                    bin_indices = 2 + np.arange(0,no_of_x_bins)
                    before_heads = np.sum(temp_y[bin_indices])
                    temp_y[bin_indices] = interpol.interp1d(xx,temp_y[bin_indices],fill_value=0,bounds_error=False)(interp_positions)

                    temp = temp_y[bin_indices]
                    temp[np.nonzero(temp<0.0)] = 0.0
                    temp_y[bin_indices] = temp

                    after_heads = np.sum(temp_y[bin_indices])
                    temp_y[1] = temp_y[1] + (before_heads-after_heads)

                    y_vec_array[mm*n_array_length:(mm+1)*n_array_length] = temp_y

                if hs_params["myofilament_parameters"]["kinetic_scheme"][0] == "4state_with_SRX":
                    temp_y = y_vec_array[mm*n_array_length:(mm+1)*n_array_length]
                    interp_positions = xx - delta_x

                    for i in np.arange(2):
                        if (i == 0):
                            bin_indices = 2 + np.arange(0, no_of_x_bins)
                        else:
                            bin_indices = 2 + no_of_x_bins + np.arange(0, no_of_x_bins)

                        # Count bridges before
                        before_heads = np.sum(temp_y[bin_indices])
                        temp_y[bin_indices] = interpol.interp1d(xx,
                                              temp_y[bin_indices],
                                              fill_value=0,
                                              bounds_error=False)(interp_positions)

                        # Make sure we don't have any negative populations
                        temp = temp_y[bin_indices]
                        temp[np.nonzero(temp<0.0)] = 0.0
                        temp_y[bin_indices] = temp

                        # Count bridges now
                        after_heads = np.sum(temp_y[bin_indices])
                        # These appear in M_on
                        temp_y[1] = temp_y[1] + (before_heads - after_heads)
                        y_vec_array[mm*n_array_length:(mm+1)*n_array_length] = temp_y

            y_vec.vector()[:] = y_vec_array # for PDE




        toc_save_cell = timeit.default_timer() - tic_save_cell
        print "time to save cell info = " + str(toc_save_cell)
        toc = timeit.default_timer() - tic
        print "time loop performance time = " + str(toc)
    if sim_geometry == "ventricle" or sim_geometry == "ellipsoid":
        if(MPI.rank(comm) == 0):
            fdataPV.close()
    # This was for fiber simulations
    #f0_dot_x_vec = inner(f0,x_vec)
    #f0_dot_x_vec_array = project(f0_dot_x_vec,Quad).vector().get_local()[:]
    #angles_array = np.arccos(f0_dot_x_vec_array)
    #np.save(output_path+"final_angles_array.npy",angles_array)

    if save_solution_flag > 0:
        print "Trying to save full solution to load into another simulation"
        hsl = project(hsl,Quad)
        #wk_params_to_save = {}
        """if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
            wk_params_to_save["Part"] = circ_dict["Part"]
            wk_params_to_save["Pven"] = circ_dict["Pven"]
            wk_params_to_save["PLV"] = circ_dict["PLV"]
            wk_params_to_save["V_ven"] = circ_dict["V_ven"]
            wk_params_to_save["V_art"] = circ_dict["V_art"]"""

        save_solution.save_solution(output_path,mesh,f0,n0,s0,facetboundaries,edgeboundaries,subdomains,LVCavityvol,u_D,u_top,u_front,Press,hs_params_list,dolfin_functions,W,w,hsl,y_vec,bcs,concentric_growth_stimulus,eccentric_growth_stimulus,cb_f_array,p_f_array)

    # -------------- Attempting growth here --------------------------------

        # Unload ventricle

    """LVCavityvol.vol = uflforms.LVcavityvol()
    print "Unloaded LV Cavity Volume = ", LVCavityvol.vol

    # Calculate the increment to LV volume
    #end_diastolic_volume = sim_protocol["initial_end_diastolic_volume"][0]
    #total_vol_loading = end_diastolic_volume - LVCavityvol.vol
    #volume_increment = total_vol_loading/sim_protocol["reference_loading_steps"][0]

    for lmbda_value in range(0, sim_protocol["reference_loading_steps"][0]):

        print "Diastolic loading step " + str(lmbda_value)

        LVCavityvol.vol -= volume_increment

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        hsl_array_old = hsl_array

        #solver.solvenonlinear()
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        displacement_file << w.sub(0)

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim


        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        delta_hsl_array = hsl_array - hsl_array_old
    #Press.P = 0.0
    Fe = uflforms.Fe()
    #solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})

    for n in np.arange(10):
        # Kurtis putting call to growth function here
        Theta1.vector()[:] += 0.02
        #Fg = project(Theta1*(M1ij) +  Theta2*M2ij + Theta3*M3ij,TFQuad)
        #uflforms.parameters["growth_tensor"] = Fg
        #Fe = uflforms.Fe()
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        print "FG"
        print project(Fg).vector().get_local()[0:9]
        print "Fe"
        Fe = uflforms.Fe()
        print project(Fe).vector().get_local()[0:9]
        print "F"
        print project(Fmat).vector().get_local()[0:9]
        displacement_file << w.sub(0)
        #b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})
        #for boundary_condition_i in np.arange(np.shape(bcs)[0]-1):
        #    bcs[boundary_condition_i+1].apply(b)
        #f_int_total = b.copy()
        #for kk in x_dofs:
        #    rxn_force[l+(n+1)] += f_int_total[kk]
        if "growth_law" in growth_params.keys():
            PK2_passive,Sff = uflforms.stress(hsl)
            Theta1, Theta2, Theta3 = growth_class.grow_mesh(PK2_passive,f0,Theta1,Theta2,Theta3,t[l])
            print "theta"
            #print project(Theta1,FunctionSpace(mesh,'DG',1),form_compiler_parameters={"representation":"uflacs"}).vector().get_local()
            #print "theta values"
            #print project(Theta1,FunctionSpace(mesh,"CG",1),form_compiler_parameters={"representation":"uflacs"}).vector().get_local()
            Fg = project(Theta1*(M1ij) +  Theta2*M2ij + Theta3*M3ij,TFQuad)
            print "FG"
            #print Fg.vector().get_local()[0:9]
            uflforms.parameters["growth_tensor"] = Fg
            Fe = uflforms.Fe()
            print "FE"
            #print project(Fe,TFQuad).vector().get_local()[0:9]
            Fmat = uflforms.Fmat()
            #print project(Fmat,TFQuad).vector().get_local()[0:9]
            solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
            PK2_passive,Sff = uflforms.stress(hsl)
            hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:]
            print "growing mesh"




    #Press.P = 0.0




    #solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
    #displacement_file << w.sub(0)
    ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
    File(output_path + "mesh_grown.pvd") << mesh
    Theta1.vector()[:] = 1.0
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
    displacement_file << w.sub(0)

    #Re load, see how diastole differs
        # Unload ventricle

    LVCavityvol.vol = uflforms.LVcavityvol()
    print "Unloaded LV Cavity Volume = ", LVCavityvol.vol

    # Calculate the increment to LV volume
    end_diastolic_volume = sim_protocol["initial_end_diastolic_volume"][0]
    total_vol_loading = end_diastolic_volume - LVCavityvol.vol
    volume_increment = total_vol_loading/sim_protocol["reference_loading_steps"][0]

    for lmbda_value in range(0, sim_protocol["reference_loading_steps"][0]):

        print "Diastolic loading step " + str(lmbda_value)

        LVCavityvol.vol += volume_increment

        p_cav = uflforms.LVcavitypressure()
        V_cav = uflforms.LVcavityvol()

        hsl_array_old = hsl_array

        #solver.solvenonlinear()
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

        displacement_file << w.sub(0)

        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim


        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        delta_hsl_array = hsl_array - hsl_array_old

    Theta2.vector()[:] = 1.0

    # reloading mesh to look for difference in deformation
    for nload in np.arange(10):
        Press.P +=500
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        displacement_file << w.sub(0)
        print "traction is ",Press.P
        b = assemble(Ftotal,form_compiler_parameters={"representation":"uflacs"})
        for boundary_condition_i in np.arange(np.shape(bcs)[0]-1):
            bcs[boundary_condition_i+1].apply(b)
        f_int_total = b.copy()
        for kk in x_dofs:
            rxn_force[l+10+(nload+1)] += f_int_total[kk]

    np.save('fx.npy',rxn_force)


    for n_grow in np.arange(10):


        #Get passive stress tensors from forms
        PK2_passive= uflforms.stress(hsl)
        Pg_fiber = inner(f0,Pg*f0)


        # For growth
        temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)
        pgf_array = pgf.vector().get_local()[:]

        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]


        print " deviation from set point = " + str(p_f_array[0]+pgf_array[0]-set_point)
        Fg00 *= 1.+ecc_growth_rate*((p_f_array[0]+pgf_array[0]-set_point)/set_point)
        Theta1.vector()[:] = Fg00
        Theta2.vector()[:] = 1./Fg00
        Fg = project(Theta1*(M1ij) + Theta2*(M2ij + M3ij))
        uflforms.parameters["growth_tensor"] = Fg
        #Fg22 = 1./Fg00
        #M2ij.vector()[:] = Fg11
        #M3ij.vector()[:] = Fg22

        #Fg = as_tensor([[Fg00,0.,0.],[0.,Fg11,0.],[0.,0.,Fg22]])

        print Fg.vector().get_local()[:]
        Fe = uflforms.Fe()
        print Fe
        print "myof passive before solving:"
        print p_f_array[0]
        print "gucc fiber passive before solving:"
        print pgf_array[0]

        #Theta1.vector()[:] = Theta1.vector().array()+ecc_growth_rate*((p_f + pgf-set_point)/set_point)
        #Theta2.vector()[:] = 1./theta1.vector().array()
        solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"},solver_parameters={"newton_solver":{"relative_tolerance":1e-8},"newton_solver":{"maximum_iterations":50},"newton_solver":{"absolute_tolerance":1e-8}})
        #Get passive stress tensors from forms
        PK2_passive = uflforms.stress(hsl)
        Pg_fiber = inner(f0,Pg*f0)
        # Update functions and arrays
        cb_f_array[:] = project(cb_force, Quad).vector().get_local()[:]
        hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for PDE
        hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim
        delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim

        # For growth
        temp_DG_2 = project(Pg_fiber, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        pgf = interpolate(temp_DG_2, Quad)
        pgf_array = pgf.vector().get_local()[:]

        temp_DG = project(Sff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
        p_f = interpolate(temp_DG, Quad)
        p_f_array = p_f.vector().get_local()[:]
        print "myof passive after solving:"
        print p_f_array[0]
        print "gucc fiber passive after solving:"
        print pgf_array[0]

        for ii in range(np.shape(hsl_array)[0]):
            if p_f_array[ii] < 0.0:
                p_f_array[ii] = 0.0

        if save_cell_output:
            p_f_array_ds.iloc[0,:] = p_f_array[:]
            p_f_array_ds.to_csv(output_path + 'myofiber_passive.csv',mode='a',header=False)

            pgf_array_ds.iloc[0,:] = pgf_array[:]
            pgf_array_ds.to_csv(output_path + 'gucc_fiber_pstress.csv',mode='a',header=False)

            hsl_array_ds.iloc[0,:] = hsl_array[:]
            hsl_array_ds.to_csv(output_path + 'half_sarcomere_lengths.csv',mode='a',header=False)

    ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
    File(output_path + "mesh_grown.pvd") << mesh"""

        #ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
        #File(output_path + "mesh_"+str(n_grow)+".pvd") << mesh
    #print "displacement during growth = " + str(u_D.u_D)
        #displacement_file << w.sub(0)





#-------------------------------------------------------------------------------
# for stand-alone testing
input_file = sys.argv[1]
#start_time = datetime.datetime.now()
start = timeit.default_timer()
# Load in JSON dictionary
with open(input_file, 'r') as json_input:
  input_parameters = json.load(json_input)

# Convert any unicode values to python strings so they work with some cpp libraries.
recode_dictionary.recode(input_parameters)

# Parse out the different types of parameters.
sim_params = input_parameters["simulation_parameters"]
passive_params = input_parameters["forms_parameters"]["passive_law_parameters"]
hs_params = input_parameters["myosim_parameters"]
print "hs_params"
print hs_params
cell_ion_params = input_parameters["electrophys_parameters"]["cell_ion_parameters"]
all_params = [sim_params,passive_params,hs_params,cell_ion_params]
#monodomain_params = input_parameters["electrophys_parameters"]["monodomain_parameters"]
if "windkessel_parameters" in input_parameters.keys():
    windkessel_params = input_parameters["windkessel_parameters"]
if "growth_and_remodeling" in input_parameters.keys():
    print "assigning growth_params"
    growth_params = input_parameters["growth_and_remodeling"]
    if 'growth_params' in locals():
        print "growth check worked"
    all_params.append(growth_params)
#optimization_params = input_parameters["optimization_parameters"]

fenics(sim_params)
sim_duration = timeit.default_timer() - start
#aplog.append_to_log(all_params,start_time,sim_duration,input_file)
