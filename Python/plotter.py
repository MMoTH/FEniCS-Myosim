# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:39:10 2018

@author: ani228
"""
test_number = 1

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')
get_ipython().run_line_magic('matplotlib', 'inline')

if test_number == 1:
    no_of_time_steps = 10
    no_of_x_bins = 21
    
    fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_1\\dumped_populations.npy')
    tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_1\\tarray.npy')
    stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_1\\stress_array.npy')
    
if test_number == 2:
    no_of_time_steps = 701
    no_of_x_bins = 49

    fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\dumped_populations.npy')
    tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\tarray.npy')
    stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\stress_array.npy')


myosim_pop_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\populations.txt'
myosim_pop_data = np.zeros((no_of_time_steps,4))
myosim_pop_data[:,0:3] = np.loadtxt(myosim_pop_file, skiprows = 5, usecols = (1,2,3))

myosim_summary_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\summary.txt'
myosim_summary_data = np.zeros((no_of_time_steps,2))
myosim_summary_data[:,0:2] = np.loadtxt(myosim_summary_file, skiprows = 5, usecols = (0,1))

fenics_pop_data = np.zeros((no_of_time_steps,4))
for i in range(no_of_time_steps):
    
    #print(dumped_populations[i,0,0], dumped_populations[i,0,1], np.sum(dumped_populations[i,0,2:23]), np.sum(dumped_populations[i,0,0:23]))
    fenics_pop_data[i,0] = fenics_pop_file[i,0,0] # state 1 pops
    fenics_pop_data[i,1] = fenics_pop_file[i,0,1] # state 2 pops
    fenics_pop_data[i,2] = np.sum(fenics_pop_file[i,0,2:no_of_x_bins+2])
    fenics_pop_data[i,3] = np.sum(fenics_pop_file[i,0,0:no_of_x_bins+2])

    myosim_pop_data[i,3] = np.sum(myosim_pop_data[i,0:3])    
    #print(stress_array[i])
    


#plt.ylabel('cb-force')
plt.figure(1)
#plt.subplot(311)
state_1_pops_myosim, = plt.plot(myosim_pop_data[:,0],'r')
state_1_pops_fenics, = plt.plot(fenics_pop_data[:,0],'k')
plt.xlabel('time')
plt.ylabel("State 1 pops")
plt.legend((state_1_pops_fenics, state_1_pops_myosim), ('Myosim in FEniCS', 'Standalone Myosim'))
plt.figure(2)
#plt.subplot(312)
state_2_pops_myosim, = plt.plot(myosim_pop_data[:,1],'r')
state_2_pops_fenics, = plt.plot(fenics_pop_data[:,1],'k')
plt.xlabel('time')
plt.ylabel("State 2 pops")
plt.legend((state_1_pops_fenics, state_1_pops_myosim), ('Myosim in FEniCS', 'Standalone Myosim'))
plt.figure(3)
#plt.subplot(313)
state_3_pops_myosim, = plt.plot(myosim_pop_data[:,2],'r')
state_3_pops_fenics, = plt.plot(fenics_pop_data[:,2],'k')
plt.xlabel('time')
plt.ylabel("State 3 pops")

#myosim, = plt.plot(myosim_summary_data[:,0], myosim_summary_data[:,1],'r')
#fenics, = plt.plot(myosim_summary_data[:,0], stress_array,'k')  


plt.legend((state_1_pops_fenics, state_1_pops_myosim), ('Myosim in FEniCS', 'Standalone Myosim'))
  

plt.show()


#print(dumped_populations[0,0,2:23])