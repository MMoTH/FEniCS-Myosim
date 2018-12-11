import os as os
from dolfin import * 
import numpy as np
from matplotlib import pylab as plt
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver 
#from simpleActiveMaterial import SimpleActiveMaterial as Active
import math


parameters["form_compiler"]["quadrature_degree"]=2
parameters["form_compiler"]["representation"] = "quadrature"

os.system("rm *.pvd")
os.system("rm *.vtu")

class Left(SubDomain):
      def inside(self, x, on_boundary):
          tol = 1E-14
          return on_boundary and abs(x[0]) < tol

class Right(SubDomain):
      def inside(self, x, on_boundary):
          tol = 1E-14
          return on_boundary and abs(x[0]-10.0) < tol

class Lower(SubDomain):
      def inside(self, x, on_boundary):
          tol = 1E-14
          return on_boundary and abs(x[2]) < tol

class Front(SubDomain):
      def inside(self, x, on_boundary):
          tol = 1E-14
          return on_boundary and abs(x[1]) < tol


class Fix(SubDomain):
      def inside(self, x, on_boundary):
         tol = 1E-14
         return on_boundary and abs(x[0]) < tol and abs(x[1]) < tol and abs(x[2]) < tol


nx = 2  
ny = 2 
nz = 2 
mesh = BoxMesh(Point(0.0, 0.0, 0.0), Point(10.0, 1.0, 1.0), nx, ny, nz)
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

left.mark(facetboundaries, 1)
right.mark(facetboundaries, 2)
fix.mark(facetboundaries, 3)
lower.mark(facetboundaries, 4)
front.mark(facetboundaries, 5)

ds = dolfin.ds(subdomain_data = facetboundaries)

##############################################################################


isincomp = True#False
ls0 = 1.85
N = FacetNormal (mesh)
Press = Expression(("P"), P=0.0, degree=0)
Cparam = Constant(1.0e2)


V = VectorFunctionSpace(mesh, 'CG', 2)
TF = TensorFunctionSpace(mesh, 'DG', 1)
Q = FunctionSpace(mesh,'CG',1)

Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
Velem._quad_scheme = 'default'
Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
Qelem._quad_scheme = 'default'
Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
Relem._quad_scheme = 'default'
Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
Quadelem._quad_scheme = 'default'

Telem2 = TensorElement("Quadrature", mesh.ufl_cell(), degree=2, shape=2*(3,), quad_scheme='default')
Telem2._quad_scheme = 'default'
for e in Telem2.sub_elements():
	e._quad_scheme = 'default'
Telem4 = TensorElement("Quadrature", mesh.ufl_cell(), degree=2, shape=4*(3,), quad_scheme='default')
Telem4._quad_scheme = 'default'
for e in Telem4.sub_elements():
	e._quad_scheme = 'default'
W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
Quad = FunctionSpace(mesh, Quadelem)


bcleft= DirichletBC(W.sub(0).sub(0), Constant((0.0)), facetboundaries, 1)
bcright= DirichletBC(W.sub(0).sub(0), Constant((2.05)), facetboundaries, 2)
bcfix = DirichletBC(W.sub(0), Constant((0.0, 0.0, 0.0)), fix, method="pointwise")
bclower= DirichletBC(W.sub(0).sub(2), Constant((0.0)), facetboundaries, 4)
bcfront= DirichletBC(W.sub(0).sub(1), Constant((0.0)), facetboundaries, 5)
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
	 "incompressible": isincomp,
	 "Kappa":Constant(1e5)}

#activeparams = {"mesh": mesh,
#                "facetboundaries": facetboundaries,
#                "facet_normal": N,
#                "displacement_variable": u, 
#                "pressure_variable": p,
#                "fiber": f0,
#                "sheet": s0,
#                "sheet-normal": n0,
#		"t_a": t_a,
#		"dt": dt,
#		"Tact": Tact,
#		#"lsc_variable": lsc,
#		"lscprev_variable": lscprev}	

 
uflforms = Forms(params)
#activeforms = Active(activeparams)

Fmat = uflforms.Fmat()
Cmat = (Fmat.T*Fmat)
Emat = uflforms.Emat()
J = uflforms.J()

n = J*inv(Fmat.T)*N
dx = dolfin.dx(mesh,metadata = {"integration_order":2})

Ematrix = project(Emat, TF)
Wp = uflforms.PassiveMatSEF()

fiso = Function(Quad)
lc = Function(Quad)


ls = sqrt(dot(f0, Cmat*f0))*ls0
Ea = 20.0


lc_vec_old =  np.array(lc.vector().array())
lc_vec_old[lc_vec_old < 1000] = 1.85 - 1.0/20.0 
lc.vector()[:] = lc_vec_old



tmax = 150.0*(ls - (-0.4))
sigmoid_0 = 1.0/(1.0 + exp(-1.0*t_a));
sigmoid_1 = 1.0/(1.0 + exp(-1.0*(tmax-t_a)));
ftwitch = tanh((tmax - t_a)/75.0)*tanh((tmax - t_a)/75.0)*tanh(t_a/75.0)*tanh(t_a/75.0)*sigmoid_0*sigmoid_1;

Pactive = ftwitch*fiso*ls/ls0*(ls - lc)*Ea*as_tensor(f0[i]*f0[j], (i,j))
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
fdata = open("isometric.txt", "w", 0)

lbda = 1.0
tload = 1000.0
tstep = 10
dload = tload/float(tstep)

ls_loading_array = [1.0]
traction_array = [0.0]

# Stretching phase
for nstep in range(0, tstep):

	Press.P += dload 
	solver.solvenonlinear()

	ls = project(sqrt(dot(f0, Cmat*f0))*ls0, Quad).vector().array()[:]
	#PK1 = project(activeforms.PK1Stress(), Quad).vector().array()[:]

	traction_array.append(Press.P)
	ls_loading_array.append(ls[0]/ls0)

        #displacementfile << w.sub(0)

#plt.plot(ls_loading_array, traction_array, 'x')
#plt.show()

# Contraction phase
header_file = open("ArtsODE/ArtsODE.h","r")
code = header_file.read()
header_file.close()

ext_module  = compile_extension_module(code=code, source_directory="ArtsODE", sources=["ArtsODE.cpp"],
             additional_system_headers=["petscvec.h"],
    	     include_dirs=[".", os.path.abspath("ArtsODE"),"/home/likchuan/.hashdist/bld/profile/satc42ktdzvy/include"],
             library_dirs = ['/home/likchuan/.hashdist/bld/gsl/ihjkorvb4zhn/lib'],
             libraries = ['libgsl.a'])

ArtsModel = ext_module.ODEsolver()
_param = {"Tref": 100.0e3};
ArtsModel.params.update(_param)


tarray = []
stress_array = []
ls_array = []
dt.dt = 2.0
tend = 400
nstep = int(float(tend)/dt.dt)


t_analytical, lbda_systole_analytical =  np.load('Analytical_sys.dat.npy')
plt.plot(t_analytical, lbda_systole_analytical)

for tstep in range(0, nstep):

	#print "t_a = ", t_a.t_a, " ls = ", ls[0]
	#print >>fdata,  t_a.t_a, " " , project(Pactive[0,0], Quad).vector().array()[0], " ", ls[0]/ls0
	t_a.t_a = t_a.t_a  + dt.dt

	lc_vec_new =  ArtsModel.ODEsolverstep(lc_vec_old, dt.dt, t_a.t_a, ls)
	lc_vec_old = lc_vec_new;
	lc.vector()[:] = lc_vec_old

	fiso.vector()[:] = ArtsModel.Get_fiso()

	solver.solvenonlinear()

	ls = project(sqrt(dot(f0, Cmat*f0))*ls0, Quad).vector().array()[:]

        displacementfile << w.sub(0)
	tarray.append(t_a.t_a)
	ls_array.append(ls[0]/ls0)
        stress_array.append(project(Pactive[0,0], Quad).vector().array()[0]);


fdata.close()
plt.plot(tarray, ls_array,'x')
plt.title('Isotonic stretch vs. time (dt = 2ms)', fontsize='large')
plt.ylabel(r'Stretch $\lambda$', fontsize='large')
plt.xlabel(r'Time $t$', fontsize='large')
plt.savefig("./doc/dt2.png")
plt.show()
