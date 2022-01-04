# @Author: charlesmann
# @Date:   2021-12-28T14:23:29-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-30T11:35:32-05:00
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

    stimulus = Function(stimulusFS)
    stimulus_temp = Function(stimulusFS)
    deviation = Function(stimulusFS)
    set_point = Function(stimulusFS)

    # initializing deviation to large number for while loop
    deviation.vector()[:] = 1000

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

    # close f
    f.close()

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
    dolfin_functions = initialize_dolfin_functions.initialize_dolfin_functions(dolfin_functions,quadFS)


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
    fcns["stimulus"] = stimulus
    fcns["deviation"] = deviation
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
    fcns["set_point"] = set_point
    fcns["stimulus_temp"] = stimulus_temp # saving at end diastole, then assigning to stimulus before growth

    return fcns
