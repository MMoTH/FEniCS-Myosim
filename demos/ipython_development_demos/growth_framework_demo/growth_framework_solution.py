# @Author: charlesmann
# @Date:   2021-11-10T12:24:40-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-11-19T14:39:33-05:00

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
    # 2) Initialize a stimulus function on the mesh, theta functions
    #    to hold the components of the deformation gradient, and the growth
    #    deformation gradient itself
    # 2) Executes the modified hyperelasticity demo with the created mesh as
    #    an input, and the PK1 stress tensor, deformation gradient as outputs
    # 3) Transform PK1 to PK2 stress, calculate stress in x-direction on mesh
    # 4) Use stress in x-direction as stimulus for concentric growth (calculate
    #    deviation from a set point of 80? kPa, use to calculate theta_dot in Fg)
    # 5) Solve the weak form to get displacement that yields a residual stress
    # 6) Move the mesh nodes using the displacements from (6) to create a new,
    #    grown mesh, reset Fg to identity
    # 7) Repeat (2) - (7) until the resulting PK2 stress in the x-direction is
    #    within some tolerance of the set point

from dolfin import *
import demo_hyperelasticity_modified
import ufl as ufl

# Before we do anything, let's define some of the quantities we will need later:
growth_time_constant = Constant(20.0)
set_point_value = Constant(80.0)
no_grow_mesh = 1
# Note: setting these as "Constant" means we don't have to recompile this part
# of the code every time we change the numeric values of these quantities.

# File to store grown meshes
#grown_mesh_file = File("grown_mesh.pvd")

#-------------------------------------------------------------------------------
# (1) Create a unit cube mesh of refinement 12, 8, 8
mesh = UnitCubeMesh(12, 8, 8)
#-------------------------------------------------------------------------------
# (2)
# Create a function space that can hold a scalar value on the mesh.
# Hint: Look back at the tutorial @ https://mmoth.github.io/FEniCS-Myosim/pages/getting_started/fenics_intro_tutorials/tutorial1/ipython_elements_functions_fcnspaces.html
# Think about what time of finite element to use
Selem = FiniteElement("DG", mesh.ufl_cell(), 1, quad_scheme="default")
Selem._quad_scheme = 'default'
S_fcn_space = FunctionSpace(mesh,Selem)
stimulus = Function(S_fcn_space)
deviation = Function(S_fcn_space)
# initializing deviation to large number for while loop
deviation.vector()[:] = 1000

# We can use the same function space to define our theta's that make up the
# growth deformation gradient
theta_ff = Function(S_fcn_space)
theta_ss = Function(S_fcn_space)
theta_nn = Function(S_fcn_space)

# Let's initialize all of these to one, so that when we later construct the
# growth deformation gradient it is the identity until we change it
theta_ff.vector()[:] = 1.0
theta_ss.vector()[:] = 1.0
theta_nn.vector()[:] = 1.0

# Finally, use these theta values to initialize Fg
# Just like for vector functions, we need to define a function space for these
# tensor quantities:
TF = TensorFunctionSpace(mesh, 'DG', 1)

# What we will actually do is define Fg as the sum of three tensors: m1, m2, m3
# one that controls growth in each direction. Question/note: Do we want to define
# this tensor at the quadrature points rather than using DG1?

# These will become the fiber and cross-fiber directions in our code
x_dir = as_vector([1,0,0])
y_dir = as_vector([0,1,0])
z_dir = as_vector([0,0,1])

M1ij = project(as_tensor(x_dir[i]*x_dir[j], (i,j)),TF)
M2ij = project(as_tensor(y_dir[i]*y_dir[j], (i,j)),TF)
M3ij = project(as_tensor(z_dir[i]*z_dir[j], (i,j)),TF)

Fg = theta_ff*M1ij + theta_ss*M2ij + theta_nn*M3ij

#-------------------------------------------------------------------------------
# (3) Let's solve our weak form, and get the strain energy function, deformation gradient, and displacement
# P and F will be used to calculate the second Piola-Kirchhoff stress tensor,
# u will be used later to move the mesh for a non-identity Fg

#      -- (7) wrapping this in a while loop
iter_counter = 0
tol = 10.0 # Cannot make Constant(), UFL conditions can't be evaluated as bool
while abs(max(project(deviation,S_fcn_space).vector().get_local())) > tol:
    print "iteration",iter_counter
    print max(project(deviation,S_fcn_space).vector().get_local())

    # Fg should be the identity here, check it
    print project(Fg,TF).vector().get_local()
    print "solving demo"
    no_grow_mesh = 1
    P,F,u = demo_hyperelasticity_modified.execute_demo(mesh,S_fcn_space, Fg, no_grow_mesh, iter_counter)
    #print project(psi,FunctionSpace(mesh,'DG',1)).vector().get_local()
    #-------------------------------------------------------------------------------
    # (4) We can transform this to the PK2 stress
    S = inv(F)*P

    # Try to print out S
    #print project(S,TensorFunctionSpace(mesh,'DG',1)).vector().get_local()

    # Let's only worry about the stress in the loading (x) direction
    # Now get the PK2 stress in the x-direction
    pk2_x = inner(x_dir,S*x_dir)

    # This is a dolfin 'inner' object (an inner product) and has no 'vector' attribute to access.
    # If we want to do something useful with it, we have to project it to a function space.
    pk2_x_projection = project(pk2_x,S_fcn_space)

    # Assign this pk2 x projection to our stimulus function.
    stimulus.assign(pk2_x_projection)

    # Calculate deviation from set point
    deviation = stimulus - set_point_value

    # Calculate theta
    # Note: We previously defined Fg using theta_ss. If we were to do
    # theta_ss = project((1./growth_time_constant)*(1+(deviation/set_point_value)),S_fcn_space)
    # I believe this creates a new object that is no longer linked to Fg.
    # Declaring a new variable (theta_ss_temp) to calculate the value and then assigning
    # these values to the existing theta_ss appropriately updates Fg.
    theta_ss_temp = project(1+(1./growth_time_constant)*((deviation/set_point_value)),S_fcn_space)
    theta_ss.assign(theta_ss_temp)
    theta_nn.assign(theta_ss_temp) # same growth in s and n directions for now

    # Check that theta_ss and Fg are appropriately updated
    #print theta_ss.vector().get_local()
    #print project(Fg,TF).vector().array()[0:15]
    #-------------------------------------------------------------------------------
    # (5)
    # now we want to solve our weak form without the external load
    # Fg has been calculated
    no_grow_mesh = 0
    print "solving for growth displacement"
    P,F,u = demo_hyperelasticity_modified.execute_demo(mesh,S_fcn_space, Fg, no_grow_mesh, iter_counter)

    #-------------------------------------------------------------------------------
    # (6)
    # move the mesh according to the new displacement field
    ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
    grown_mesh_file = File("iter_"+str(iter_counter)+"/"+"grown_mesh.pvd")
    grown_mesh_file << mesh

    # Reset thetas to 1 so Fg is the identity
    theta_ff.vector()[:] = 1.0
    theta_ss.vector()[:] = 1.0
    theta_nn.vector()[:] = 1.0
    iter_counter +=1

print "Finished Growing Mesh"
print "Total Iterations:",iter_counter+1
print "Tolerance:",tol
print "Set Point:",float(set_point_value)
print "Final Deviation from Set Point:",max(project(deviation,S_fcn_space).vector().get_local())
