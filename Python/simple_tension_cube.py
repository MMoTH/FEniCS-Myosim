from fenics import *
import dolfin
import os as os
import numpy as np
from petsc4py import PETSc
from forms import Forms
#from nsolver import NSolver as NSolver
# LCL change
#from math import *
import math as math  #LCL
import matplotlib.pyplot as plt

deg = 2
parameters["form_compiler"]["quadrature_degree"]=deg
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
ls0 = 1.85                                                                      #??
N = FacetNormal (mesh)
Press = Expression(("P"), P=0.0, degree=0)
Cparam = Constant(1.0e2)                                                        #??


#V = VectorFunctionSpace(mesh, 'CG', 2)
TF = TensorFunctionSpace(mesh, 'DG', 1)
#Q = FunctionSpace(mesh,'CG',1)

#Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
Velem = VectorElement("Lagrange", tetrahedron, 2, quad_scheme="default")
Velem._quad_scheme = 'default'
#Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
Qelem = FiniteElement("Lagrange", tetrahedron, 1, quad_scheme="default")
Qelem._quad_scheme = 'default'
#Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
#Relem = FiniteElement("Real", tetrahedron, 0, quad_scheme="default")
#Relem._quad_scheme = 'default'
#Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
Quadelem._quad_scheme = 'default'

#Telem2 = TensorElement("Quadrature", mesh.ufl_cell(), degree=2, shape=2*(3,), quad_scheme='default')
#Telem2._quad_scheme = 'default'
#for e in Telem2.sub_elements():
#	e._quad_scheme = 'default'
#Telem4 = TensorElement("Quadrature", mesh.ufl_cell(), degree=2, shape=4*(3,), quad_scheme='default')
#Telem4._quad_scheme = 'default'
#for e in Telem4.sub_elements():
#	e._quad_scheme = 'default'
W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
Quad = FunctionSpace(mesh, Quadelem)

# assigning BCs
bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
bcright= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 2)       # u1 = 0 on right face
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

t_a = Expression(("t_a"), t_a=0.0, degree=1)
dt = Expression(("dt"), dt=0.0, degree=1)


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
	 "incompressible": isincomp,                                                   #??
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


# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Press*n, v)*ds(2, domain=mesh)
Ftotal = F1 - F2

Jac1 = derivative(F1, w, dw)
Jac2 = derivative(F2, w, dw)
Jac = Jac1 - Jac2
##################################################################################################################################


solverparams = {"Jacobian": Jac,
    "F": Ftotal,
    "w": w,
    "boundary_conditions": bcs,
		"Type": 0,
		"mesh": mesh,
		"mode": 0
		}


#solver= NSolver(solverparams)


displacementfile = File("./output/u_disp.pvd")

tload = 1000.0
tstep = 10
dload = tload/float(tstep)

ls_loading_array = [1.0]
traction_array = [0.0]
p_f_array = []
# Stretching phase
for nstep in range(0, tstep):

    Press.P += dload
    #solver.solvenonlinear()
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    ls = project(sqrt(dot(f0, Cmat*f0))*ls0, Quad).vector().get_local()[:]

    traction_array.append(Press.P)
    ls_loading_array.append(ls[0]/ls0)
    
    T = uflforms.Cauchy()
    Tff =  inner(f0,T*f0)
    temp = project(Tff, Quad).vector().get_local()[0]
    print'Cauchy fiber stress = ', temp
    #displacementfile << w.sub(0)

#plt.plot(ls_loading_array, traction_array, 'x')

#plt.show()