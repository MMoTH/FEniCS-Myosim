# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:02:06 2018

@author: ani228
"""

from __future__ import division
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
n_array_length = 2 



isincomp = True#False
N = FacetNormal (mesh)
Press = Expression(("P"), P=0.0, degree=0)
Cparam = Constant(1.0e2)                                                        #??


#V = VectorFunctionSpace(mesh, 'CG', 2)
#TF = TensorFunctionSpace(mesh, 'DG', 1)
#Q = FunctionSpace(mesh,'CG',1)

Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
Velem._quad_scheme = 'default'

Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
Qelem._quad_scheme = 'default'

Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
Quadelem._quad_scheme = 'default'


W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
Quad = FunctionSpace(mesh, Quadelem)

Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))


# assigning BCs
bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)         # u1 = 0 on left face
bcright= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 2)       # u1 = 0 on right face
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

stress = Function(Quad)


Pactive = stress * as_tensor(f0[i]*f0[j], (i,j))

# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Pactive, grad(v))*dx
F3 = inner(Press*n, v)*ds(2, domain=mesh)
Ftotal = F1 - F3 + F2

Jac1 = derivative(F1, w, dw)
Jac2 = derivative(F2, w, dw)
Jac3 = derivative(F3, w, dw)
Jac = Jac1 - Jac3 + Jac2
##################################################################################################################################


solverparams = {"Jacobian": Jac,
    "F": Ftotal,
    "w": w,
    "boundary_conditions": bcs,
		"Type": 0,
		"mesh": mesh,
		"mode": 0
		}


solver= NSolver(solverparams)


displacementfile = File("./output/u_disp.pvd")

# Contraction phase
header_file = open("./C++_test/hs.h","r")
code = header_file.read()
header_file.close()

ext_module = compile_extension_module(code=code, source_directory="C++_test", sources=["hs.cpp"],
     additional_system_headers=["petscvec.h"],
     include_dirs=[".", os.path.abspath("C++_test"),"/usr/include", "./C++_test"],
     library_dirs = ['/usr/lib/x86_64-linux-gnu'],
     libraries = ['libgsl.a'])

Myosim = ext_module.hs()

dt.dt = 1.0


tarray = []
stress_array = []

y_vec = Function(Quad_vectorized_Fspace)

y_vec_old = np.array(y_vec.vector().get_local())
#print(np.shape(y_vec_old))

no_of_int_points = 24
for counter in range(0,n_array_length * no_of_int_points,n_array_length):
    y_vec_old[counter] = 1

results = np.zeros((100,3))

for i in range(100):

    #solver.solvenonlinear()
    y_vec_new = Myosim.apply_time_step(y_vec_old)
     
    results[i,0] = i
    results[i,1] = y_vec_old[0]
    results[i,2] = y_vec_old[1]
    
    y_vec_old = y_vec_new
    

np.save("/home/fenics/shared/fenics_results",results)

print("Done!")




    




