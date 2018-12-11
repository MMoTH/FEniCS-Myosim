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


hsl0 = 1000
time_steps = 100
step_size = 0.0005
Ca_flag = 1
constant_pCa = 6.5

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
bcs = [bcleft, bcfix, bclower, bcfront]

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

cb_force = Expression(("F"), F=0.0, degree=0)
Pactive = cb_force * as_tensor(f0[i]*f0[j], (i,j))
Press = Expression(("P"), P=0.0, degree=0)

# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Pactive, grad(v))*dx
F3 = inner(Press*N, v)*ds(2, domain=mesh)
Ftotal = F1 + F2 - F3 

Jac1 = derivative(F1, w, dw)
Jac2 = derivative(F2, w, dw)
Jac3 = derivative(F3, w, dw)
Jac = Jac1 + Jac2 - Jac3 
##################################################################################################################################
tarray = []
strarray = []
pstrarray = []
tracarray = []


P,S,T = uflforms.stress()
Pff =  inner(f0,P*f0) # no need to push forward f0 for 1_PK stress
temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"}) 
p_f = interpolate(temp_DG, Quad)
p_f_array = p_f.vector().get_local()[:]




cb_f_array = project(cb_force, Quad).vector().get_local()[:]


t = 0.0
for l in range(5):
    
    print(cb_f_array[0])
    print(p_f_array[0])

    tarray.append(t)
    strarray.append(cb_f_array[0])
    pstrarray.append(p_f_array[0])
    tracarray.append(Press.P)
    
    cb_force.F += 1.0
    
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})
    
    temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"}) 
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]
    
    #print(p_f_array)
    
    cb_f_array = project(cb_force, Quad).vector().get_local()[:]
    
    t = t + step_size
    
    

np.save("/home/fenics/shared/test_9_temp/tarray",tarray)

np.save("/home/fenics/shared/test_9_temp/stress_array",strarray)

np.save("/home/fenics/shared/test_9_temp/pstress_array",pstrarray)

np.save("/home/fenics/shared/test_9_temp/trac_array",tracarray)

print("Done!")
