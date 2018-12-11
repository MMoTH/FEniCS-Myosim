# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:18:25 2018

@author: ani228
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:39:10 2018

@author: ani228
"""
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython


no_of_time_steps = 701
n_array_length = 52   

no_of_time_steps = 7408
n_array_length = 45   
 
   

    
fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\dumped_populations.npy')
tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\tarray.npy')
stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\stress_array.npy')
calcium = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\calcium.npy')
HSL = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\HSL.npy')



fenics_pop_data = np.zeros((no_of_time_steps,n_array_length))
for i in range(no_of_time_steps):
    
    fenics_pop_data[i,:] = fenics_pop_file[i,0,:]
    #fenics_pop_data[i,0] = fenics_pop_file[i,0,0] # state 1 pops
    #fenics_pop_data[i,1] = fenics_pop_file[i,0,1] # state 2 pops
    #fenics_pop_data[i,2] = np.sum(fenics_pop_file[i,0,2:n_array_length-1])
    #fenics_pop_data[i,3] = fenics_pop_file[i,0,n_array_length-1]
    #fenics_pop_data[i,4:] = fenics_pop_file[i,0,4:n_array_length]
    
   
myosim_pop_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\populations.txt'
myosim_pop_data = np.zeros((no_of_time_steps,4))
myosim_pop_data[:,0:3] = np.loadtxt(myosim_pop_file, skiprows = 5, usecols = (1,2,3))
myosim_rates_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\rates.txt'
fenics_rates_file = 'C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\rates_fenics.txt'

myosim_summary_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\summary.txt'
myosim_summary_data = np.zeros((no_of_time_steps,2))
myosim_summary_data[:,0:2] = np.loadtxt(myosim_summary_file, skiprows = 5, usecols = (0,2))
myosim_rates = np.zeros((n_array_length-3,5))
myosim_rates[:,0:5] = np.loadtxt(myosim_rates_file, skiprows = 1, usecols = (0,1,2,3,4))
fenics_rates = np.zeros((n_array_length-3,5))
fenics_rates[:,0:5] = np.loadtxt(fenics_rates_file, skiprows = 1, usecols = (0,1,2,3,4))

get_ipython().run_line_magic('matplotlib', 'qt')
#get_ipython().run_line_magic('matplotlib', 'inline')

fig = plt.figure()
#------------------------------------------------------------------------------
plt.subplot(422)

state_1_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,0], 'k')
state_2_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,1], 'b')
state_3_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,2], 'r')

plt.scatter(tarray[::10], myosim_pop_data[::10,0], color = 'k')
plt.scatter(tarray[::10], myosim_pop_data[::10,1], color = 'b')
plt.scatter(tarray[::10], myosim_pop_data[::10,2], color = 'r')

plt.legend((state_1_pops_fenics, state_2_pops_fenics, state_3_pops_fenics), ('OFF', 'ON', 'FG'))
plt.title("Myosin Populations")
plt.xlabel('time (s)')
plt.ylabel("Proportions")


#------------------------------------------------------------------------------
plt.subplot(424)
state_3_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[:,2:n_array_length-2],1), 'r')
binding_sites, = plt.plot(tarray, fenics_pop_data[:,n_array_length-1],'g')

#plt.scatter(tarray, myosim_pop_data[:,2], color = 'r')
plt.scatter(tarray[::10], myosim_pop_data[::10,2], color = 'r')

plt.legend((state_3_pops_fenics, binding_sites), ('Xbridges', 'Binding sites'))
plt.xlabel('time (s)')
plt.ylabel("Proportions")
#------------------------------------------------------------------------------
plt.subplot(426)
plt.plot(tarray, stress_array)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.scatter(myosim_summary_data[::10,0], myosim_summary_data[::10,1],color='r')
plt.xlabel('time (s)')
plt.ylabel("Stress (Pa)")

#------------------------------------------------------------------------------
plt.subplot(428)
plt.plot(tarray, calcium)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.xlabel('time (s)')
plt.ylabel("Calcium [M]")
#------------------------------------------------------------------------------
plt.subplot(421)
plt.plot(tarray, HSL)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.xlabel('time [s]')
plt.ylabel("hsl (nm)")
#------------------------------------------------------------------------------
plt.subplot(423)

plt.scatter(myosim_rates[:,0], myosim_rates[:,1],color='k')
rate1, = plt.plot(fenics_rates[:,0], fenics_rates[:,1],'k')
plt.scatter(myosim_rates[:,0], myosim_rates[:,2],color='r')
rate2, = plt.plot(fenics_rates[:,0], fenics_rates[:,2],'r')
plt.legend((rate1, rate2), ('Rate 1', 'Rate 2'))

#------------------------------------------------------------------------------
plt.subplot(425)

plt.scatter(myosim_rates[:,0], myosim_rates[:,3],color='g')
rate3, = plt.plot(fenics_rates[:,0], fenics_rates[:,3],'g')
plt.scatter(myosim_rates[:,0], myosim_rates[:,4],color='b')
rate4, = plt.plot(fenics_rates[:,0], fenics_rates[:,4],'b')
plt.legend((rate3, rate4), ('Attach', 'Detach'))

#------------------------------------------------------------------------------

#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
#plt.figure()
plt.get_current_fig_manager().full_screen_toggle()
plt.show()