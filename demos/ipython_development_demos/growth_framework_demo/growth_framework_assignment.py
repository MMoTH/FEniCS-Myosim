# @Author: charlesmann
# @Date:   2021-11-10T12:24:40-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-11-17T13:34:15-05:00
from dolfin import *
import demo_hyperelasticity_modified
import ufl as ufl

# This assignment is going to provide a basic framework that aims
# to grow a unit cube mesh in response to some stimulus. Some things
# this assignment will introduce/help solidify with respect to FEniCS

# Finite elements, function spaces and functions, as well as indexing
# functions

# FEniCS Expressions

# Formation of continuum quantities and tensors (deformation gradient, stretch)
#-------------------------------------------------------------------------------
#  Goal:
## Write a script that:
    # 1) Creates a unit cube mesh
    # 2) Executes the modified hyperelasticity demo with the created mesh as
    #    an input, and the PK1 stress tensor, deformation gradient as outputs
    # 3) Transform PK1 to PK2 stress, calculate stress in x-direction on mesh
    # 4) Use stress in x-direction as stimulus for concentric growth (calculate
    #    deviation from a set point of 80? kPa, use to calculate theta_dot in Fg)
    # 5) Calculate Fg, the growth deformation for the mesh
    # 6) Solve the weak form to get displacement that yields a residual stress
    # 7) Move the mesh nodes using the displacements from (6) to create a new,
    #    grown mesh
    # 8) Repeat (2) - (7) until the resulting PK2 stress in the x-direction is
    #    within some tolerance of the set point




# Let's create our mesh
mesh = UnitCubeMesh(12, 8, 8)

# A lot of the interesting stuff takes place in the demo_hyperelasticity_modified file. We
# can focus on those specifics later

# Let's create a function space to hold our stimulus (and deviation from set point) on our mesh
# Let's let the stimulus vary linearly within an element, but make no assumptions about
# inter-element continuity
Selem = FiniteElement("DG", mesh.ufl_cell(), 1, quad_scheme="default")
Selem._quad_scheme = 'default'
S_fcn_space = FunctionSpace(mesh,Selem)
stimulus = Function(S_fcn_space)



# Let's solve our weak form, and get the strain energy function and the deformation gradient
P,F = demo_hyperelasticity_modified.execute_demo(mesh)
#print project(psi,FunctionSpace(mesh,'DG',1)).vector().get_local()

# Now calculate our stress. For hyperelastic materials, we can get the stress by
# differentiating our SEF with respect to F this gives the First Piola Kirchhoff Stress

# Differentiating wrt F, F must be declared a dolfin variable
#F = variable(F)
#P = diff(psi,F)
#print project(P,TensorFunctionSpace(mesh,'DG',1)).vector().get_local()

# We can transform this to the PK2 stress
S = inv(F)*P

# Try to print out S
#print project(S,TensorFunctionSpace(mesh,'DG',1)).vector().get_local()

# Let's only worry about the stress in the loading (x) direction
x_dir = Constant((1,0,0))

# Now get the PK2 stress in the x-direction
pk2_x = inner(x_dir,S*x_dir)

# This is a dolfin 'inner' object (an inner product) and has no 'vector' attribute to access.
# If we want to do something useful with it, we have to project it to a function space.
pk2_x_projection = project(pk2_x,S_fcn_space)

stress_file = File('pk2_x_projection.pvd')
stress_file << pk2_x_projection

# Define some arbitrary set point
set_point = Constant(80)
