# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:50:22 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')

PV = np.loadtxt('C:/Users/ani228/Dropbox/UK/FEniCS/output/PV_.txt')

#plt.plot(PV[:,2], PV[:,1])
#plt.plot(PV[0:1200,0], PV[0:1200,1])
plt.plot(PV[:,0], PV[:,1])
'''
fenics_output_directory = 'test_5'
int_point = 0
no_of_time_steps = 20
no_of_states = 4
n_array_length = 52   
no_of_x_bridges = 49
no_of_transitions = 4

fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\dumped_populations.npy')

fenics_pop_data = np.zeros((no_of_time_steps,n_array_length))
for i in range(no_of_time_steps):    
        fenics_pop_data[i,:] = fenics_pop_file[i,int_point,:]
plt.plot(range(no_of_time_steps), np.sum(fenics_pop_data[:,2:n_array_length-2],1), 'r')
'''
plt.show()