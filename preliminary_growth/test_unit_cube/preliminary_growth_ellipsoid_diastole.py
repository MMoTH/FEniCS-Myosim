# @Author: charlesmann
# @Date:   2021-11-10T12:24:40-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-28T14:30:51-05:00

# This assignment is going to provide a basic framework that aims
# to grow a unit cube mesh in response to some stimulus. Some things
# this assignment will introduce/help solidify with respect to FEniCS

# Finite elements, function spaces and functions, as well as indexing
# functions

# FEniCS Expressions

# Formation of continuum quantities and tensors (deformation gradient, stretch)
#-------------------------------------------------------------------------------


from dolfin import *
import numpy as np
#import demo_hyperelasticity_modified
import ufl as ufl
import json
import sys
sys.path.append('/home/fenics/shared/dependencies/')
import recode_dictionary
sys.path.append('/home/fenics/shared/source_code/')
from mmoth_vent import fenics

deg = 2
parameters["form_compiler"]["quadrature_degree"]=deg
parameters["form_compiler"]["representation"] = "quadrature"

# Before we do anything, let's define some of the quantities we will need later:
growth_time_constant = Constant(20.0)
#set_point_value = Constant(80.0)
no_grow_mesh = 1
# Note: setting these as "Constant" means we don't have to recompile this part
# of the code every time we change the numeric values of these quantities.

# File to store grown meshes
#grown_mesh_file = File("grown_mesh.pvd")

#-------------------------------------------------------------------------------
# (1) Load in instruction file and parse out some stuff
input_file = sys.argv[1]

with open(input_file, 'r') as json_input:
  input_parameters = json.load(json_input)

# We recursively iterate through the instruction file to make sure we
# have all json strings instead of unicode
recode_dictionary.recode(input_parameters)

# Get the simulation parameters and geometry options
sim_params = input_parameters["simulation_parameters"]
geo_options = sim_params["geometry_options"]
mesh_path = geo_options["mesh_path"][0]

# Create a dolfin mesh object
mesh = Mesh()

# Read the mesh into the mesh object
f = HDF5File(mpi_comm_world(), mesh_path, 'r')
f.read(mesh,"ellipsoid_scaled",False)
#f.close()
# don't close the file yet, we will need to read in the fiber coordinate system later
# Save the reference mesh
File('./output/reference_mesh.pvd') << mesh
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
deg=2
Telem2 = TensorElement("Quadrature", mesh.ufl_cell(), degree=deg, shape=2*(3,), quad_scheme='default')
Telem2._quad_scheme = 'default'
for e in Telem2.sub_elements():
    e._quad_scheme = 'default'
TFQuad = FunctionSpace(mesh, Telem2)

# What we will actually do is define Fg as the sum of three tensors: m1, m2, m3
# one that controls growth in each direction. Question/note: Do we want to define
# this tensor at the quadrature points rather than using DG1?

# These will become the fiber and cross-fiber directions in our code
#x_dir = as_vector([1,0,0])
#y_dir = as_vector([0,1,0])
#z_dir = as_vector([0,0,1])
# We now want the fiber coordinate system. These exist at the quadrature
# points, so we need to create a vector function space at the
# quadrature points. Then we create a function for the fiber, sheet, and sheet
# normal directions

VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
VQuadelem._quad_scheme = 'default'
fiberFS = FunctionSpace(mesh, VQuadelem)
f0 = Function(fiberFS)
s0 = Function(fiberFS)
n0 = Function(fiberFS)
f.read(f0,"ellipsoidal/eF")
#File('./output/f0.pvd') << project(f0,VectorFunctionSpace(mesh,"DG",0))
f.read(s0,"ellipsoidal/eS")
f.read(n0,"ellipsoidal/eN")
f.close()

M1ij = project(as_tensor(f0[i]*f0[j], (i,j)), TF)
M2ij = project(as_tensor(s0[i]*s0[j], (i,j)), TF)
M3ij = project(as_tensor(n0[i]*n0[j], (i,j)), TF)

Fg = theta_ff*M1ij + theta_ss*M2ij + theta_nn*M3ij

# Let's inflate the ellipsoid to an end-diastolic volume of .25 mL
# and use this to set our set-point
# This uses the instruction file (where I've specified one time step, so essentially
# this is just forced diastolic loading). It returns the total passive stress in the
# fiber direction
ecc_set_point = fenics(input_parameters,Fg)

# Let's change the set point
ecc_set_point *= 1.1



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
    #print project(Fg,TF).vector().get_local()
    print "solving demo"
    no_grow_mesh = 1
    ecc_stimulus = fenics(input_parameters)
    #P,F,u = demo_hyperelasticity_modified.execute_demo(mesh,S_fcn_space, Fg, no_grow_mesh, iter_counter)
    #print project(psi,FunctionSpace(mesh,'DG',1)).vector().get_local()
    #-------------------------------------------------------------------------------
    # (4) We can transform this to the PK2 stress
    #S = inv(F)*P

    # Try to print out S
    #print project(S,TensorFunctionSpace(mesh,'DG',1)).vector().get_local()

    # Let's only worry about the stress in the loading (x) direction
    # Now get the PK2 stress in the x-direction
    #pk2_x = inner(x_dir,S*x_dir)

    # This is a dolfin 'inner' object (an inner product) and has no 'vector' attribute to access.
    # If we want to do something useful with it, we have to project it to a function space.
    #pk2_x_projection = project(pk2_x,S_fcn_space)

    # Assign this pk2 x projection to our stimulus function.
    #stimulus.assign(pk2_x_projection)

    # Calculate deviation from set point
    deviation = ecc_stimulus - ecc_set_point

    # Calculate theta
    # Note: We previously defined Fg using theta_ss. If we were to do
    # theta_ss = project((1./growth_time_constant)*(1+(deviation/set_point_value)),S_fcn_space)
    # I believe this creates a new object that is no longer linked to Fg.
    # Declaring a new variable (theta_ss_temp) to calculate the value and then assigning
    # these values to the existing theta_ss appropriately updates Fg.
    theta_ff_temp = project(1+(1./growth_time_constant)*((deviation/set_point_value)),S_fcn_space)
    theta_ff.assign(theta_ss_temp)
    #theta_nn.assign(theta_ss_temp) # same growth in s and n directions for now

    # Check that theta_ss and Fg are appropriately updated
    #print theta_ss.vector().get_local()
    #print project(Fg,TF).vector().array()[0:15]
    #-------------------------------------------------------------------------------
    # (5)
    # now we want to solve our weak form without the external load
    # Fg has been calculated
    no_grow_mesh = 0
    print "solving for growth displacement"
    #P,F,u = demo_hyperelasticity_modified.execute_demo(mesh,S_fcn_space, Fg, no_grow_mesh, iter_counter)
    # Need to solve the weak form with no loading


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
