# @Author: charlesmann
# @Date:   2021-12-28T14:23:29-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T17:04:31-05:00
from dolfin import *
import sys
sys.path.append('/home/fenics/shared/source_code/methods/assign_heterogeneous_params/')
import initialize_dolfin_functions

def initialize_functions(mesh, fcn_spaces, f, input_parameters):

    deg = 2
    parameters["form_compiler"]["quadrature_degree"]=deg
    parameters["form_compiler"]["representation"] = "quadrature"

    fcns = {}

    # mesh function needed later
    facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
    f.read(facetboundaries, "ellipsoidal"+"/"+"facetboundaries")


    stimulusFS = fcn_spaces["stimulusFS"]
    tensorFS = fcn_spaces["growth_tensor_space"]
    fiberFS = fcn_spaces["material_coord_system_space"]
    W = fcn_spaces["solution_space"]
    quadFS = fcn_spaces["quadrature_space"]
    quad_vecFS = fcn_spaces["quad_vectorized_space"]

    stimulus_ff = Function(stimulusFS)
    stimulus_ff_temp = Function(stimulusFS)
    stimulus_ss = Function(stimulusFS)
    stimulus_ss_temp = Function(stimulusFS)
    stimulus_nn = Function(stimulusFS)
    stimulus_nn_temp = Function(stimulusFS)
    deviation_ff = Function(stimulusFS)
    deviation_ss = Function(stimulusFS)
    deviation_nn = Function(stimulusFS)
    set_point_ff = Function(stimulusFS)
    set_point_ss = Function(stimulusFS)
    set_point_nn = Function(stimulusFS)


    # initializing deviation to large number for while loop
    deviation_ff.vector()[:] = 1000
    deviation_ss.vector()[:] = 1000
    deviation_nn.vector()[:] = 1000

    # We can use the same function space to define our theta's that make up the
    # growth deformation gradient
    theta_ff = Function(stimulusFS)
    theta_ss = Function(stimulusFS)
    theta_nn = Function(stimulusFS)

    # Let's initialize all of these to one, so that when we later construct the
    # growth deformation gradient it is the identity until we change it
    theta_ff.vector()[:] = 1.0
    theta_ss.vector()[:] = 1.0
    theta_nn.vector()[:] = 1.0

    # Create functions to hold material coordinate system
    f0 = Function(fiberFS)
    s0 = Function(fiberFS)
    n0 = Function(fiberFS)

    # Load these in from f
    f.read(f0,"ellipsoidal/eF")
    f.read(s0,"ellipsoidal/eS")
    f.read(n0,"ellipsoidal/eN")



    # Finally, use these theta values to initialize Fg
    # Just like for vector functions, we need to define a function space for these
    # tensor quantities:
    M1ij = project(as_tensor(f0[i]*f0[j], (i,j)), tensorFS)
    M2ij = project(as_tensor(s0[i]*s0[j], (i,j)), tensorFS)
    M3ij = project(as_tensor(n0[i]*n0[j], (i,j)), tensorFS)

    Fg = theta_ff*M1ij + theta_ss*M2ij + theta_nn*M3ij

    # Initializing passive parameters as functions, in the case of introducing
    # heterogeneity later
    dolfin_functions = {}
    dolfin_functions["passive_params"] = input_parameters["forms_parameters"]["passive_law_parameters"]
    dolfin_functions["cb_number_density"] = input_parameters["myosim_parameters"]["cb_number_density"]
    dolfin_functions = initialize_dolfin_functions.initialize_dolfin_functions(dolfin_functions,quadFS)


    # Some Myosim related functions
    hsl0    = Function(quadFS)
    hsl_old = Function(quadFS)
    pseudo_alpha = Function(quadFS)
    pseudo_old = Function(quadFS)
    pseudo_old.vector()[:] = 1.0
    hsl_diff_from_reference = Function(quadFS)
    hsl_diff_from_reference.vector()[:] = 0.0
    try:
        f.read(hsl0, "ellipsoidal" + "/" + "hsl0")

    except:
        hsl0.vector()[:] = input_parameters["myosim_parameters"]["initial_hs_length"][0]

    # close f
    f.close()

    y_vec   = Function(quad_vecFS)

    #---------------------------------
    # Now functions for the weak form
    w = Function(W)
    dw    = TrialFunction(W)
    wtest = TestFunction(W)
    du,dp,dpendo,dc11 = TrialFunctions(W)
    (u,p,pendo,c11)   = split(w)
    (v,q,qendo,v11)   = TestFunctions(W)

    fcns["theta_ff"] = theta_ff
    fcns["theta_nn"] = theta_nn
    fcns["theta_ss"] = theta_ss
    fcns["stimulus_ff"] = stimulus_ff
    fcns["stimulus_nn"] = stimulus_nn
    fcns["stimulus_ss"] = stimulus_ss
    fcns["deviation_ff"] = deviation_ff
    fcns["deviation_ss"] = deviation_ss
    fcns["deviation_nn"] = deviation_nn
    fcns["w"] = w
    fcns["f0"] = f0
    fcns["s0"] = s0
    fcns["n0"] = n0
    fcns["M1ij"] = M1ij
    fcns["M2ij"] = M2ij
    fcns["M3ij"] = M3ij
    fcns["Fg"] = Fg
    fcns["c11"] = c11
    fcns["pendo"] = pendo
    fcns["p"] = p
    fcns["u"] = u
    fcns["v11"] = v11
    fcns["qendo"] = qendo
    fcns["q"] = q
    fcns["v"] = v
    fcns["dpendo"] = dpendo
    fcns["dc11"] = dc11
    fcns["dp"] = dp
    fcns["du"] = du
    fcns["dw"] = dw
    fcns["wtest"] = wtest
    fcns["dolfin_functions"] = dolfin_functions
    fcns["facetboundaries"] = facetboundaries
    fcns["set_point_ff"] = set_point_ff
    fcns["set_point_ss"] = set_point_ss
    fcns["set_point_nn"] = set_point_nn
    fcns["stimulus_ff_temp"] = stimulus_ff_temp # these are saved during the simulation, and assigned to components of Fg later
    fcns["stimulus_ss_temp"] = stimulus_ss_temp
    fcns["stimulus_nn_temp"] = stimulus_nn_temp
    fcns["hsl0"] = hsl0
    fcns["hsl_old"] = hsl_old
    fcns["pseudo_alpha"] = pseudo_alpha
    fcns["pseudo_old"] = pseudo_old
    fcns["y_vec"] = y_vec

    return fcns
