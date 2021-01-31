"""
Created on Wed Oct  9 12:40:00 PM 2019

@author: Kurtis Mann

Modifying Amir's plotter to hopefully plot generic LV simulation
Currently, IPython only works using python 2.7
"""
import os as os
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation
import time
plt.style.use('seaborn-pastel')


sim_dir = os.getcwd()

# For now, hard coding bin discretization information
xmin = -10
xmax = 10
bin_width = 1.0
cb_domain = np.arange(xmin,xmax+bin_width,bin_width)
num_bins = np.shape(cb_domain)

# overlap is saved last, so will use shape to determine data range
overlap = np.loadtxt(sim_dir + '/overlap.csv', delimiter=',')
#tarray = np.loadtxt(sim_dir+'/time.csv', delimiter=',')
tarray = np.linspace(0,100,200)
calcium = np.loadtxt(sim_dir + '/calcium.csv', delimiter=',')
HSL = np.loadtxt(sim_dir + '/half_sarcomere_lengths.csv', delimiter=',')
stress_array = np.loadtxt(sim_dir + '/active_stress.csv', delimiter=',')
fenics_pop_data = np.loadtxt(sim_dir + '/populations.csv', delimiter=',')
pstress = np.loadtxt(sim_dir + '/myofiber_passive.csv', delimiter=',')
gucc_fiber = np.loadtxt(sim_dir + '/gucc_fiber_pstress.csv', delimiter=',')
gucc_trans = np.loadtxt(sim_dir + '/gucc_trans_pstress.csv', delimiter=',')
gucc_shear = np.loadtxt(sim_dir + '/gucc_shear_pstress.csv', delimiter=',')

if stress_array.ndim > 1:
    # single cell sims only save for one gauss point, dimension is one less than
    # ventricle simulation
    single_cell_sim_flag = 0
else:
    single_cell_sim_flag = 1

# Define number of time steps and array length here
sim_info = fenics_pop_data.shape
num_timesteps = np.shape(tarray)[0]
num_int_points = sim_info[0]/num_timesteps
array_length = sim_info[1]
#print sys.argv[0]
#print sys.argv[1]
gauss_point = int(sys.argv[1])

#gauss_point = 1000
data_range = np.shape(overlap)[0]-1
#data_range = 400
#data_range = 50
# Look at how info is dumped from FEniCS. For now, hard code number of detached and attached states, and bins
# Want to be able to visualize distributions, will need this info to set up arrays.
#num_d_states
#num_a_states
#num_bins
#bin_min
#bin_max

#fenics_pop_data = np.zeros((num_timesteps,array_length))
M_OFF = np.zeros(data_range)
M_ON =  np.zeros(data_range)
M_BOUND =  np.zeros(data_range)
N_ON =  np.zeros(data_range)
print data_range
print np.shape(tarray)
for i in range(data_range):

    # Reading in information from just one Gauss point [i = timestep, 0 = gauss point, : is all pop info]
    #print i
    M_OFF[i] = fenics_pop_data[i*num_int_points+gauss_point,0]
    M_ON[i] = fenics_pop_data[i*num_int_points+gauss_point,1]
    M_BOUND[i] = np.sum(fenics_pop_data[i*num_int_points+gauss_point,2:array_length-3])
    N_ON[i] = fenics_pop_data[i*num_int_points+gauss_point,array_length-1]

fig = plt.figure()
#------------------------------------------------------------------------------
ax2 = plt.subplot(421)
if single_cell_sim_flag > 0:
    plt.plot(tarray[0:data_range],HSL[0:data_range])
else:
    plt.plot(tarray[0:data_range], HSL[0:data_range,:])

plt.xlabel('time [ms]')
plt.ylabel("hsl (nm)")
#------------------------------------------------------------------------------

plt.subplot(422)
print np.shape(tarray)
print np.shape(M_OFF)
state_1_pops_fenics, = plt.plot(tarray[0:data_range], M_OFF[0:data_range],label='SRX')
state_2_pops_fenics, = plt.plot(tarray[0:data_range], M_ON[0:data_range],label='Detached')
state_3_pops_fenics, = plt.plot(tarray[0:data_range], M_BOUND[0:data_range],label='M Bound')

plt.legend((M_OFF,M_ON,M_BOUND), ('OFF', 'ON', 'FG'))
plt.title("Myosin Populations")
plt.xlabel('time (ms)')
plt.ylabel("Proportions")

#---------------------------------------------------------------------------------
plt.subplot(423)
if single_cell_sim_flag > 0:
    fiber_pstress, = plt.plot(tarray[0:data_range], pstress[0:data_range])
else:
    fiber_pstress, = plt.plot(tarray[0:data_range], pstress[0:data_range,gauss_point])
    gfiber, = plt.plot(tarray[0:data_range], gucc_fiber[0:data_range,gauss_point])
    gtrans, = plt.plot(tarray[0:data_range], gucc_trans[0:data_range,gauss_point])
    gshear, = plt.plot(tarray[0:data_range], gucc_shear[0:data_range,gauss_point])
    plt.legend((fiber_pstress, gfiber, gtrans, gshear), ('fiber', 'G_fiber', 'G_trans', 'G_shear'))

#plt.plot(tarray, pstress[0:data_range])
plt.ylabel('Passive Stress (Pa)')
#------------------------------------------------------------------------------
plt.subplot(424)
#state_3_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[0:data_range,2:array_length-2]), 'r')
state_3_pops_fenics, = plt.plot(tarray[0:data_range], M_BOUND[0:data_range])
binding_sites, = plt.plot(tarray[0:data_range], N_ON[0:data_range])


plt.legend((binding_sites,state_3_pops_fenics), ('Binding sites','Xbridges'))
plt.xlabel('time (ms)')
plt.ylabel("Proportions")
#------------------------------------------------------------------------------
plt.subplot(425)
plt.plot(tarray[0:data_range], overlap[0:data_range,gauss_point])
plt.ylabel('Overlap')
#------------------------------------------------------------------------------
ax3 = plt.subplot(426)
if single_cell_sim_flag > 0:
    plt.plot(tarray[0:data_range],stress_array[0:data_range])
else:
    plt.plot(tarray[0:data_range], stress_array[0:data_range,gauss_point])

plt.xlabel('time (ms)')
plt.ylabel("Stress (Pa)")

#------------------------------------------------------------------------------
plt.subplot(428)
plt.plot(tarray[0:data_range], calcium[0:data_range,0])
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.xlabel('time (ms)')
plt.ylabel("Calcium [M]")

#------------------------------------------------------------------------------
# Animate cross-bridges during simulation
max_nbound = np.max(fenics_pop_data[:,2])
#print max_nbound
ax1 = plt.subplot(427,xlim=(xmin-1,xmax+1),ylim=(0.00,max_nbound/3))
#ax = plt.axes(xlim=(xmin,xmax),ylim=(0,1))
line1, = ax1.plot([],[],lw=3)
line2, = ax2.plot([],[])
line3, = ax3.plot([],[])
line = [line1, line2, line3]

def init():
    line[0].set_data([],[])
    line[1].set_data([],[])
    line[2].set_data([],[])
    return line

t, m, m2 = [], [], []
y = np.zeros(np.shape(cb_domain))
def animate(i):
    # array_length -1 for cpp, -2 for python
    #y = fenics_pop_file[i,gauss_point,2:array_length-2]
    y = fenics_pop_data[i*num_int_points+gauss_point,2:array_length-2]
    if single_cell_sim_flag > 0:
        m.append(HSL[i])
        m2.append(stress_array[i])
    else:
        m.append(HSL[i,gauss_point])
        m2.append(stress_array[i,gauss_point])
    #print np.shape(cb_domain)
    t.append(tarray[i])
    #print np.shape(y)
    line[0].set_data(cb_domain,y)
    line[1].set_data(t,m)
    line[2].set_data(t,m2)
    time.sleep(0.25)
    return line


anim = FuncAnimation(fig, animate, init_func=init, frames = num_timesteps-1, interval = 1, blit=True)

#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
#plt.figure()

plt.get_current_fig_manager().full_screen_toggle()
plt.show()
