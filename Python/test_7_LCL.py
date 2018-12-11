from dolfin import *
import dolfin
import os as os
import numpy as np
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver
# LCL change
#from math import *
import math as math  #LCL
import matplotlib.pyplot as plt

filament_compliance_factor = 0.5

no_of_states = 3
no_of_attached_states = 1
no_of_detached_states = 2
no_of_transitions = 4
state_attached = [0, 0, 1]
cb_extensions = [ 0, 0, 4.75642]
k_cb_multiplier = [ 1.0, 1.0, 1.0]
k_cb_pos = 0.001
k_cb_neg = 0.001
cb_number_density = 7.67e16
alpha_value = 1.0

x_bin_min = -12
x_bin_max = +12
x_bin_increment = 0.5
xx = np.arange(x_bin_min, x_bin_max + x_bin_increment, x_bin_increment)
no_of_x_bins = np.shape(xx)[0]
n_array_length = no_of_attached_states * no_of_x_bins + no_of_detached_states + 1
n_vector_indices = [[0,0], [1,1], [2,2+no_of_x_bins-1]]

hsl0 = 1000
time_steps = 400
step_size = 0.0005
Ca_flag = 4

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

#plot(mesh)
#plt.show()
f0 = Constant((1.0, 0.0, 0.0))
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
Press = Expression(("P"), P=0.0, degree=0)
Cparam = Constant(1.0e2)                                                        #??


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

# assigning BCs
u_D = Expression(("u_D"), u_D = 0.0, degree = 2)
bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
bcright= DirichletBC(W.sub(0).sub(0), u_D, facetboundaries, 2)
bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise") # at one vertex u = v = w = 0
bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)        # u3 = 0 on lower face
bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)        # u2 = 0 on front face
bcs = [bcleft, bcright, bcfix, bclower, bcfront]

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
     "C_param": Cparam,
	 "incompressible": isincomp,
	 "Kappa":Constant(1e5)}

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
delta_hsl = Function(Quad)
stress = Function(Quad)
stress_array = np.zeros(no_of_int_points)

for ii in range(no_of_int_points):

    cb_adjustment = delta_hsl.vector()[ii] * filament_compliance_factor
    cb_force = 0.0

    # cycle through the states
    for jj in range(no_of_states):

    		f_holder = 0.0
    		n_holder = 0.0

    		if state_attached[jj] == 1: # only attached states generate force

    			cb_ext = cb_extensions[jj]

    			for k in range(no_of_x_bins):

    				dxx = xx[k] + cb_adjustment
    				n_pop = y_vec.vector()[ii * n_array_length + n_vector_indices[jj][0] + k]

    				if dxx > -cb_ext:

    					f_holder = f_holder + n_pop * k_cb_multiplier[jj] *	k_cb_pos * (dxx + cb_ext)

    				else:

    					f_holder = f_holder + n_pop * k_cb_multiplier[jj] *	k_cb_neg * (dxx + cb_ext)

    	 		#Correct for number density,nm units and alpha value
    	 		f_holder = f_holder * cb_number_density * 1e-9

    	 		# Adjust for variability
    	 		f_holder = f_holder * alpha_value

    	 	# Add in the cb force
    		cb_force = cb_force + f_holder
    stress_array[ii] = cb_force
stress.vector()[:] = stress_array

# LCL example to show how explicitly you can define stress as a ufl function of stretch ###########################################
# The stretch is define by lbda_current so it is a function of the displacement field
# To get it discrete value, you need to project to some function space in which case I always use the quadrature space
lbda_current = inner(f0, Cmat*f0)
lbda_prev = Function(Quad)
lbda_prev.vector()[:] = 1
delta_hsl = lbda_current - lbda_prev

Pactive_scalar = Constant(0.0)
y_vec_list = split(y_vec)

for jj in range(no_of_states):
    	for k in range(no_of_x_bins):
		indices_of_y_vec_for_npop = jj # You need to change this

		n_pop = y_vec[indices_of_y_vec_for_npop]

    		cb_ext = cb_extensions[jj]
		dxx = xx[k] + delta_hsl * filament_compliance_factor

		Pactive_scalar = Pactive_scalar * n_pop * k_cb_multiplier[jj] *  (dxx + cb_ext) * conditional(dxx - cb_ext > 0.0, k_cb_pos, k_cb_neg)

Pactive = Pactive_scalar * as_tensor(f0[i]*f0[j], (i,j))
###################################################################################################################################

# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Pactive, grad(v))*dx
Ftotal = F1 + F2

Jac1 = derivative(F1, w, dw)
Jac2 = derivative(F2, w, dw)
Jac = Jac1 + Jac2
##################################################################################################################################

# Contraction phase
header_file = open("./C++/hs.h","r")
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


darray = []
tarray = []
hslarray = []
calarray = []
strarray = []


y_vec_array = np.array(y_vec.vector().get_local())

for counter in range(0,n_array_length * no_of_int_points,n_array_length):
    y_vec_array[counter] = 1

hsl = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad)
hsl_array = np.array(hsl.vector().get_local())

# LCL Change #################################################################################
#delta_hsl_array = np.array(delta_hsl.vector().get_local())
delta_hsl_array = np.array(project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local())
##############################################################################################

p_f = project(uflforms.Cauchy_fiber(), Quad)
p_f_array = np.array(p_f.vector().get_local())

cb_f_array = np.array(stress.vector().get_local())

dumped_populations = np.zeros((time_steps, no_of_int_points, n_array_length))

t = 0.0

for l in range(time_steps):

    tarray.append(t)
    darray.append(u_D.u_D)
    hslarray.append(hsl_array[0])
    strarray.append(cb_f_array[0])
            
    _Ca_params = {"time_point": l};
    Myosim.Ca_params.update(_Ca_params)

    y_vec_array_new = Myosim.apply_time_step(y_vec_array, delta_hsl_array, hsl_array, p_f_array, cb_f_array)

    y_vec_array = y_vec_array_new
    
    hsl_array_old = hsl_array
    
    # active force update
    y_vec.vector()[:] = y_vec_array_new
    
    # LCL - I don't think you need this ################################
    #delta_hsl.vector()[:] = delta_hsl_array
    ####################################################################

    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    # LCL - Update the stretch ##########################################
    lbda_prev.vector()[:] = project(lbda_current, Quad).vector().get_local()[:]
    #####################################################################
    stop

    hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:]
    
    delta_hsl_array = hsl_array - hsl_array_old
    
    p_f_array = project(uflforms.Cauchy_fiber(), Quad).vector().get_local()[:]
    
    cb_f_array = stress.vector().get_local()[:]
    
    

    if l >= 0 and l < 100:
        u_D.u_D = 0.0
    elif l >= 100 and l < 200:
        u_D.u_D += 0.001
    elif l >= 200 and l < 300:
        u_D.u_D -= 0.001
    elif l >= 300:
        u_D.u_D = 0.0

    t = t + step_size

    calarray.append(Myosim.Get_Ca())
    
    for  m in range(no_of_int_points):

        for k in range(n_array_length):

            dumped_populations[l, m, k] = y_vec.vector().get_local()[m * n_array_length + k]

rate_constants = np.zeros((no_of_x_bins,no_of_transitions + 1))

for l in range(no_of_x_bins):

    for m in range(no_of_transitions + 1):

        rate_constants[l,m] = Myosim.dump_rate_constants(l, m, 0)


np.save("/home/fenics/shared/test_7/rates",rate_constants)

np.save("/home/fenics/shared/test_7/dumped_populations",dumped_populations)

np.save("/home/fenics/shared/test_7/tarray",tarray)

np.save("/home/fenics/shared/test_7/stress_array",strarray)

np.save("/home/fenics/shared/test_7/calcium",calarray)

np.save("/home/fenics/shared/test_7/displacements",darray)

np.save("/home/fenics/shared/test_7/HSL",hslarray)

print("Done!")
