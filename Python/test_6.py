import os as os
from dolfin import * 
import numpy as np
from matplotlib import pylab as plt
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver 
import math

BCL = 701.0
beats = 1.0
no_of_x_bins = 49
no_of_transitions = 4
n_array_length = 52 
hsl0 = 1000
step_size = 0.0005
Ca_flag = 2

deg = 4
parameters["form_compiler"]["quadrature_degree"]=deg
parameters["form_compiler"]["representation"] = "quadrature"

os.system("rm ./test_5/*.pvd")
os.system("rm ./test_5/*.vtu")

############################## Insert Mesh ###########################################
casename = "ellipsoidal"
meshfilename = casename + ".hdf5"

mesh = Mesh()

f = HDF5File(mpi_comm_world(), meshfilename, 'r')
f.read(mesh, casename, False)

no_of_int_points = 4 * np.shape(mesh.cells())[0]
#print (mesh.ufl_cell())

facetboundaries = MeshFunction("size_t", mesh, 2)
VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
VQuadelem._quad_scheme = 'default'
fiberFS = FunctionSpace(mesh, VQuadelem)

f0 = Function(fiberFS)
s0 = Function(fiberFS)
n0 = Function(fiberFS)
f.read(facetboundaries, casename+"/"+"facetboundaries")

f.read(f0, casename+"/"+"eF")
f.read(s0, casename+"/"+"eS")
f.read(n0, casename+"/"+"eN")
f.close()
File("facetboundaries.pvd") << facetboundaries
topid = 4
LVendoid = 2
epiid = 1
##############################################################################

comm = mesh.mpi_comm()



##############################################################################


isincomp = True#False
N = FacetNormal (mesh)
Press = Expression(("P"), P=0.0, degree=0)
Kspring = Constant(100)
LVCavityvol = Expression(("vol"), vol=0.0, degree=2)
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
Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
Quadelem._quad_scheme = 'default'

Telem2 = TensorElement("Quadrature", mesh.ufl_cell(), degree=deg, shape=2*(3,), quad_scheme='default')
Telem2._quad_scheme = 'default'
for e in Telem2.sub_elements():
    e._quad_scheme = 'default'
Telem4 = TensorElement("Quadrature", mesh.ufl_cell(), degree=deg, shape=4*(3,), quad_scheme='default')
Telem4._quad_scheme = 'default'
for e in Telem4.sub_elements():
    e._quad_scheme = 'default'
W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem]))
Quad = FunctionSpace(mesh, Quadelem)

Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))

bctop = DirichletBC(W.sub(0).sub(2), Expression(("0.0"), degree = 2), facetboundaries, topid)
bcs = [bctop]

w = Function(W)
dw = TrialFunction(W)
wtest = TestFunction(W)
du,dp,dpendo = TrialFunctions(W)
(u,p, pendo) = split(w)
(v,q, qendo) = TestFunctions(W)

dt = Expression(("dt"), dt=0.0, degree=1)


params= {"mesh": mesh,
         "facetboundaries": facetboundaries,
         "facet_normal": N,
         "mixedfunctionspace": W,
         "mixedfunction": w,
         "displacement_variable": u, 
         "pressure_variable": p,
         "lv_volconst_variable": pendo,
         "lv_constrained_vol":LVCavityvol,
         "LVendoid": LVendoid,
         "LVendo_comp": 2,
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

Ematrix = project(Emat, TF)
Wp = uflforms.PassiveMatSEF()
Wvol = uflforms.LVV0constrainedE()

stress = Function(Quad)

Pactive = stress * as_tensor(f0[i]*f0[j], (i,j))

# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Pactive, grad(v))*dx
F3 = derivative(Wvol, w, wtest)
F4 = -Kspring*inner(dot(u,n)*n,v)*ds(epiid) 
Ftotal = F1 + F2 + F3 + F4

Jac1 = derivative(F1, w, dw)
Jac2 = derivative(F2, w, dw) 
Jac3 = derivative(F3, w, dw) 
Jac4 = derivative(F4, w, dw) 
Jac = Jac1 + Jac2 + Jac3 + Jac4
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


LVCavityvol.vol = uflforms.LVcavityvol()

displacementfile = File("./test_5/u_disp.pvd")

if(MPI.rank(comm) == 0):
    fdataPV = open("./test_5/PV_.txt", "w", 0)



# Closed loop cycle
tstep = 0
# circ parameters
Cao = 0.005;
Cven = 0.2*10;
Vart0 = 350;
Vven0 = 2200.0;
Rao = 10*1000.0 ;
Rven = 1000.0;
Rper = 150000.0;
V_ven = 5000; 
V_art = 450;

beat = 0.0
t = 0
tstep = 0
dt.dt = step_size

LVcav_array = [uflforms.LVcavityvol()]
Pcav_array = [uflforms.LVcavitypressure()*0.0075]

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

_FE_params = {"step_size": dt.dt};
Myosim.FE_params.update(_FE_params)

_Ca_params = {"Ca_flag": Ca_flag};
Myosim.Ca_params.update(_Ca_params)

y_vec = Function(Quad_vectorized_Fspace)

y_vec_old = np.array(y_vec.vector().get_local())

for counter in range(0,n_array_length * no_of_int_points,n_array_length):
    y_vec_old[counter] = 1
    
hsl = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:]

delta_hsl = np.array(hsl)
delta_hsl[:] = 0.0

p_f = np.array(hsl)
p_f[:] = 0.0

cb_f = np.array(hsl)
cb_f[:] = 0.0

# Loading phase
for lmbda_value in range(0, 4):

    print "Loading phase step = ", lmbda_value
    LVCavityvol.vol += 5

    p_cav = uflforms.LVcavitypressure()
    V_cav = uflforms.LVcavityvol()

    solver.solvenonlinear()

    hsl = np.round(project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:], 10)
    print "Minimum ls"
    print np.amin(hsl)
    print "Maximum ls"
    print np.amax(hsl)


    if(MPI.rank(comm) == 0):
        
        print >>fdataPV, 0.0, p_cav*0.0075 , V_cav
        displacementfile << w.sub(0)


# Closed-loop phase
dumped_populations = np.zeros((beats * BCL, no_of_int_points, n_array_length))

counter = 0
while(beat < beats):
#while(counter < 20):

    p_cav = uflforms.LVcavitypressure()
    V_cav = uflforms.LVcavityvol()

    tstep = tstep + dt.dt
    beat = math.floor(tstep/BCL)
    t = tstep - beat*BCL


    if(MPI.rank(comm) == 0):
        print "Cycle number = ", beat, " cell time = ", t, " tstep = ", tstep, " dt = ", dt.dt
        print >>fdataPV, tstep, p_cav*0.0075 , V_cav

    Part = 1.0/Cao*(V_art - Vart0);
    Pven = 1.0/Cven*(V_ven - Vven0);
    PLV = p_cav;

    if(MPI.rank(comm) == 0):
        
        print "P_ven = ",Pven;
        print "P_LV = ", PLV;
        print "P_art = ", Part;

        if(PLV <= Part):
             Qao = 0.0;
        else:
             Qao = 1.0/Rao*(PLV - Part);
        

        if(PLV >= Pven):
            Qmv = 0.0;
        else: 
            Qmv = 1.0/Rven*(Pven - PLV);
        

        Qper = 1.0/Rper*(Part - Pven);

    if(MPI.rank(comm) == 0):
        
            print "Q_mv = ", Qmv ;
            print "Q_ao = ", Qao ;
            print "Q_per = ", Qper ;

    V_cav_prev = V_cav
    V_art_prev = V_art
    V_ven_prev = V_ven
    p_cav_prev = p_cav

    V_cav = V_cav + dt.dt*(Qmv - Qao);
    V_art = V_art + dt.dt*(Qao - Qper);
    V_ven = V_ven + dt.dt*(Qper - Qmv);

    LVCavityvol.vol = V_cav

    if(MPI.rank(comm) == 0):
        
            print "V_ven = ", V_ven;
            print "V_LV = ", V_cav;
            print "V_art = ", V_art;


    LVcav_array.append(V_cav)
    Pcav_array.append(p_cav*0.0075)
    
    counter = counter - math.floor(counter/BCL) * BCL
    _Ca_params = {"cell_time": counter};
    Myosim.Ca_params.update(_Ca_params)
    
    y_vec_new = Myosim.apply_time_step(y_vec_old, delta_hsl, hsl, p_f, cb_f)
    
    for  i in range(no_of_int_points):
        
        for j in range(n_array_length):
            
            dumped_populations[counter, i, j] = y_vec_new[i * n_array_length + j]
    
    y_vec_old = np.copy(y_vec_new)
    
    stress.vector()[:] = Myosim.Get_cb_force_vec()
    
    cb_f = stress.vector().get_local()[:]
    
    hsl_old = np.copy(hsl)       
    
    
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    hsl = np.round(project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:], 10)
    
    delta_hsl = np.subtract(hsl, hsl_old)

    p_f = project(uflforms.Cauchy_fiber(), Quad).vector().get_local()[:]
    
    counter += 1
    displacementfile << w.sub(0)

if(MPI.rank(comm) == 0):
    fdataPV.close()

np.save("/home/fenics/shared/test_5/dumped_populations",dumped_populations)

######################################################################################################