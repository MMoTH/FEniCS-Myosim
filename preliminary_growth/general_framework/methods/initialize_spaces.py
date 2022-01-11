# @Author: charlesmann
# @Date:   2021-12-28T14:07:31-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T16:53:43-05:00
from dolfin import *
import numpy as np

def initialize_spaces(mesh, n_array_length):

    deg = 2
    no_of_int_points = 4 * np.shape(mesh.cells())[0] #4 comes from using degree 2

    parameters["form_compiler"]["quadrature_degree"]=deg
    parameters["form_compiler"]["representation"] = "quadrature"
    fcn_spaces = {}


    # Set up Vector quadrature space for the material coordinate system {f0,s0,n0}
    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'
    fiberFS = FunctionSpace(mesh, VQuadelem)

    # General quadrature element whose points we will evaluate myosim at (and passive parameters defined here
    # if heterogeneity is desired)
    Quadelem = FiniteElement("Quadrature", tetrahedron, degree=deg, quad_scheme="default")
    Quadelem._quad_scheme = 'default'
    Quad = FunctionSpace(mesh, Quadelem)

    # Function space for myosim populations
    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))


    # For the weak form
    #-------------------
    # Vector element for displacement
    Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
    Velem._quad_scheme = 'default'

    # Quadrature element for hydrostatic pressure
    Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
    Qelem._quad_scheme = 'default'

    # Real element for rigid body motion boundary condition
    Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
    Relem._quad_scheme = 'default'

    # Mixed element for rigid body motion. One each for x, y displacement. One each for
    # x, y, z rotation
    VRelem = MixedElement([Relem, Relem, Relem, Relem, Relem])

    # Function space with subspaces for displacement, hydrostatic pressure, lv pressure, and boundary condition
    W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem,VRelem]))

    # For growth:
    # ----------
    # Set up element and function space for scalar values (stimulus, deviation)
    Selem = FiniteElement("DG", mesh.ufl_cell(), 1, quad_scheme="default")
    Selem._quad_scheme = 'default'
    stimulusFS = FunctionSpace(mesh,Selem)

    # Set up tensor function space for components of Fg
    tensorFS = TensorFunctionSpace(mesh, 'DG', 1)
    fcn_spaces["stimulusFS"] = stimulusFS
    fcn_spaces["growth_tensor_space"] = tensorFS

    fcn_spaces["material_coord_system_space"] = fiberFS
    fcn_spaces["solution_space"] = W
    fcn_spaces["quadrature_space"] = Quad
    fcn_spaces["quad_vectorized_space"] = Quad_vectorized_Fspace

    return fcn_spaces, no_of_int_points
