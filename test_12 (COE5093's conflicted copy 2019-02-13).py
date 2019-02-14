# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:24:20 2019

@author: ani228
"""

import os as os
from dolfin import * 
import numpy as np
from matplotlib import pylab as plt
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver 
import math
from scipy.integrate import solve_ivp

filament_compliance_factor = 0.25
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

BCL = 100 # ms
cycles = 1

hsl0 = 1000
step_size = 0.5 # ms
no_of_time_steps = int(cycles*BCL/step_size)
Ca_flag = 4
constant_pCa = 6.5

deg = 4
parameters["form_compiler"]["quadrature_degree"]=deg
parameters["form_compiler"]["representation"] = "quadrature"

os.system("rm ./test_12/*.pvd")
os.system("rm ./test_12/*.vtu")


############################## Insert Mesh ###########################################
casename = "ellipsoidal"
meshfilename = casename + ".hdf5"

mesh = Mesh()

f = HDF5File(mpi_comm_world(), meshfilename, 'r')
f.read(mesh, casename, False)

no_of_int_points = 14 * np.shape(mesh.cells())[0]

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
#Press = Expression(("P"), P=0.0, degree=0)
Kspring = Constant(100)
LVCavityvol = Expression(("vol"), vol=0.0, degree=2)
Cparam = Constant(5.0e2)


V = VectorFunctionSpace(mesh, 'CG', 2)
TF = TensorFunctionSpace(mesh, 'DG', 1)
Q = FunctionSpace(mesh,'CG',1)

Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
Velem._quad_scheme = 'default'
Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
Qelem._quad_scheme = 'default'
Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
Relem._quad_scheme = 'default'
#Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=deg, quad_scheme="default")
Quadelem = FiniteElement("Quadrature", tetrahedron, degree=deg, quad_scheme="default")
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

#dt = Expression(("dt"), dt=0.0, degree=1)


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

#Active force calculation------------------------------------------------------
y_vec = Function(Quad_vectorized_Fspace)
hsl = sqrt(dot(f0, Cmat*f0))*hsl0
hsl_old = Function(Quad)
delta_hsl = hsl - hsl_old

#f_holder = Constant(0.0)
cb_force = Constant(0.0)

y_vec_split = split(y_vec)

for jj in range(no_of_states):
    
    f_holder = Constant(0.0)

    if state_attached[jj] == 1:

        cb_ext = cb_extensions[jj]

        for k in range(no_of_x_bins):

            dxx = xx[k] + delta_hsl * filament_compliance_factor

            n_pop = y_vec_split[n_vector_indices[jj][0] + k]

            f_holder = f_holder + n_pop * k_cb_multiplier[jj] * (dxx + cb_ext) * conditional(dxx + cb_ext > 0.0, k_cb_pos, k_cb_neg)

        f_holder = f_holder * cb_number_density * 1e-9

        f_holder = f_holder * alpha_value

    cb_force = cb_force + f_holder

Pactive = cb_force * as_tensor(f0[i]*f0[j], (i,j))

# Automatic differentiation  #####################################################################################################
F1 = derivative(Wp, w, wtest)*dx
F2 = inner(Pactive, grad(v))*dx
F3 = derivative(Wvol, w, wtest)
F4 = -Kspring*inner(dot(u,n)*n,v)*ds(epiid)  # traction applied as Cauchy stress!, Pactive is 1PK
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

print("cavity-vol = ", LVCavityvol.vol)

displacementfile = File("./test_12/u_disp.pvd")

if(MPI.rank(comm) == 0):
    fdataPV = open("./test_12/PV_.txt", "w", 0)


tstep = 0
t = 0

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

_FE_params = {"step_size": step_size}
Myosim.FE_params.update(_FE_params)

_Ca_params = {"Ca_flag": Ca_flag}
Myosim.Ca_params.update(_Ca_params)

_Ca_params = {"constant_pCa": constant_pCa}
Myosim.Ca_params.update(_Ca_params)

tarray = []
hslarray = np.zeros((no_of_time_steps+1,no_of_int_points))
calarray = np.zeros((no_of_time_steps+1,no_of_int_points))
strarray = np.zeros((no_of_time_steps+1,no_of_int_points))
pstrarray = np.zeros((no_of_time_steps+1,no_of_int_points))

y_vec_array = y_vec.vector().get_local()[:]

#hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:]
hsl_array = project(hsl, Quad).vector().get_local()[:]

print(np.shape(hsl_array))

delta_hsl_array = np.zeros(no_of_int_points)

for counter in range(0,n_array_length * no_of_int_points,n_array_length):
    y_vec_array[counter] = 1

P, S, T = uflforms.stress()
Pff =  inner(f0,P*f0)
temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"}) 
p_f = interpolate(temp_DG, Quad)
p_f_array = p_f.vector().get_local()[:]

cb_f_array = project(cb_force, Quad).vector().get_local()[:]

ventricle_slack_volume = LVCavityvol.vol
print("ventricle_slack_volume = ", LVCavityvol.vol)

# Loading phase

for lmbda_value in range(0, 4):

    print "Loading phase step = ", lmbda_value
    LVCavityvol.vol += 0.01

    p_cav = uflforms.LVcavitypressure()
    V_cav = uflforms.LVcavityvol()

    hsl_array_old = hsl_array
    
    #solver.solvenonlinear()
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})

    hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for active stress
    
    hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim
    #print(np.shape(hsl_array))
    delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim
    
    temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"}) 
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]

    if(MPI.rank(comm) == 0):
        
        print >>fdataPV, 0.0, 0.0, p_cav*0.0075
        displacementfile << w.sub(0)
    print("cavity-vol = ", LVCavityvol.vol)
    print("cavity-pressure = ", LVcavitypressure()*0.0075)


# Closed-loop phase

no_of_compartments = 6
blood_volume = 1.5

aorta_resistance = 10e3 * 0.0075
aorta_compliance = 1e-6 / 7.5

arteries_resistance = 30e3  * 0.0075
arteries_compliance = 2.5e-7 / 7.5

arterioles_resistance = 30e3 * 0.0075
arterioles_compliance = 1.5e-7 / 7.5

capillaries_resistance =30e3 * 0.0075
capillaries_compliance = 0.8e-6 / 7.5

veins_resistance = 10e3 * 0.0075
veins_compliance = 1.2e-4 / 7.5

ventricle_resistance = 1e3 * 0.0075


resistance = np.array([aorta_resistance,
                       arteries_resistance,
                       arterioles_resistance,
                       capillaries_resistance,
                       veins_resistance,
                       ventricle_resistance])

compliance = np.array([aorta_compliance,
                       arteries_compliance,
                       arterioles_compliance,
                       capillaries_compliance,
                       veins_compliance])

# Set the initial volumes with most of the blood in the veins
#initial_ventricular_volume = 1.5 * ventricle_slack_volume
#initial_ventricular_volume = LVCavityvol.vol
volume = np.zeros(no_of_compartments)

volume[4] = blood_volume - LVCavityvol.vol
volume[5] = LVCavityvol.vol

pressures = np.zeros((no_of_time_steps+1, no_of_compartments))
volumes = np.zeros((no_of_time_steps+1, no_of_compartments))

dumped_populations = np.zeros((no_of_time_steps+1, no_of_int_points, n_array_length))

def derivs(t, pressure):
        # returns dv, derivative of volume
        dv = np.zeros(no_of_compartments)

        # First deduce flows
        
        flows = np.zeros(no_of_compartments)
    
        flows[0] = 0.0
        if (pressure[-1] > pressure[0]):
            flows[0] = (pressure[-1] - pressure[0]) / resistance[0]
        
        flows[1] = (pressure[0] - pressure[1]) / resistance[1]
        
        flows[2] = (pressure[1] - pressure[2]) / resistance[2]
        
        flows[3] = (pressure[2] - pressure[3]) / resistance[3]
        
        flows[4] = (pressure[3] - pressure[4]) / resistance[4]
        
        flows[5] = 0.0
        if (pressure[4] > pressure[5]):
            flows[5] = (pressure[4] - pressure[5]) / resistance[5]
                
        # Different compartments
        dv[0] = flows[0] - flows[1]

        dv[1] = flows[1] - flows[2]

        dv[2] = flows[2] - flows[3]

        dv[3] = flows[3] - flows[4]

        dv[4] = flows[4] - flows[5]

        dv[-1] = flows[5] - flows[0]

        return dv

calarray_temp = []
counter = 0
cycle = 0
while(cycle < cycles):

    p_cav = uflforms.LVcavitypressure()
    V_cav = uflforms.LVcavityvol()

    tstep = tstep + step_size
    cycle = math.floor(tstep/BCL)
    cell_time = tstep - cycle*BCL


    pressure = np.zeros(no_of_compartments)
    
    for x in range(no_of_compartments-1):
        pressure[x] = volume[x] / compliance[x]
    pressure[-1] = p_cav
    '''if counter == 0:
        pressure[4] = p_cav'''
    
    pressures[counter,:] = pressure
    
    if(MPI.rank(comm) == 0):
    
        print "Cycle number = ", cycle, " cell time = ", cell_time, " tstep = ", tstep, " step_size = ", step_size
        print >>fdataPV, tstep, pressure[4]*0.0075 , pressure[5]*0.0075

    if(MPI.rank(comm) == 0):
        
        print "pressure_aorta = ", pressure[0]*0.0075;
        print "pressure_arteries = ", pressure[1]*0.0075;
        print "pressure_arterioles = ", pressure[2]*0.0075;
        print "pressure_capillaries = ", pressure[3]*0.0075;
        print "---------------------------------------------pressure_veins = ", pressure[4]*0.0075;
        print "---------------------------------------------pressure_ventricle = ", pressure[-1]*0.0075;

    sol = solve_ivp(derivs, [0, step_size], volume)
    volume = sol.y[:, -1]
    
    volumes[counter,:] = volume
    
    LVCavityvol.vol = volume[-1]

    if(MPI.rank(comm) == 0):
        
            print "volume_aorta = ", volume[0];
            print "volume_arteries = ", volume[1];
            print "volume_arterioles = ", volume[2];
            print "volume_capillaries = ", volume[3];
            print "volume_veins = ", volume[4];
            print "volume_ventricle = ", volume[-1];


    LVcav_array.append(volume[-1])
    Pcav_array.append(pressure[-1]*0.0075)
    
    cell_counter = int(counter - math.floor(counter/BCL) * BCL)
    
    for  i in range(no_of_int_points):
        
        for j in range(n_array_length):
            
            dumped_populations[counter, i, j] = y_vec_array[i * n_array_length + j]
    
    _Ca_params = {"time_point": cell_counter}
    Myosim.Ca_params.update(_Ca_params)
    
    y_vec.vector()[:] = y_vec_array # for PDE  
    
    y_vec_array_new = Myosim.apply_time_step(y_vec_array, delta_hsl_array, hsl_array, p_f_array, cb_f_array)

    y_vec_array = y_vec_array_new # for Myosim
        
    hsl_array_old = hsl_array
    
    #solver.solvenonlinear()
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    solve(Ftotal == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    cb_f_array = project(cb_force, Quad).vector().get_local()[:]
    
    hsl_old.vector()[:] = project(hsl, Quad).vector().get_local()[:] # for active stress
    
    hsl_array = project(hsl, Quad).vector().get_local()[:]           # for Myosim
    #print(np.shape(hsl_array))
    delta_hsl_array = project(sqrt(dot(f0, Cmat*f0))*hsl0, Quad).vector().get_local()[:] - hsl_array_old # for Myosim
    
    temp_DG = project(Pff, FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"}) 
    p_f = interpolate(temp_DG, Quad)
    p_f_array = p_f.vector().get_local()[:]
    
    #calarray[counter,:] = Myosim.Get_Ca() * np.ones(no_of_int_points)
    calarray_temp.append(Myosim.Get_Ca())
    print(counter)
    counter += 1
    displacementfile << w.sub(0)
    
    tarray.append(tstep)
    
    
    hslarray[counter,:] = hsl_array
    strarray[counter,:] = cb_f_array
    pstrarray[counter,:] = p_f_array

if(MPI.rank(comm) == 0):
    fdataPV.close()

rate_constants = np.zeros((no_of_x_bins,no_of_transitions + 1))

for l in range(no_of_x_bins):

    for m in range(no_of_transitions + 1):

        rate_constants[l,m] = Myosim.dump_rate_constants(l, m, 0)

np.save("/home/fenics/shared/test_12/rates",rate_constants)

np.save("/home/fenics/shared/test_12/dumped_populations",dumped_populations)

np.save("/home/fenics/shared/test_12/tarray",tarray)

np.save("/home/fenics/shared/test_12/stress_array",strarray)

np.save("/home/fenics/shared/test_12/pstress_array",pstrarray)

np.save("/home/fenics/shared/test_12/calcium",calarray)

np.save("/home/fenics/shared/test_12/HSL",hslarray)

np.save("/home/fenics/shared/test_12/pressures",pressures)

np.save("/home/fenics/shared/test_12/volumes",volumes)

######################################################################################################
