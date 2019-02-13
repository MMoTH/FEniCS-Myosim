# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:27:11 2018

@author: ani228
"""
import numpy as np
import matplotlib.pyplot as plt

no_of_time_steps = 701

myosim_summary_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\summary.txt'
myosim_summary_data = np.zeros((no_of_time_steps,2))
myosim_summary_data[:,0:2] = np.loadtxt(myosim_summary_file, skiprows = 5, usecols = (0,2))
#plt.plot(myosim_summary_data[:,0],myosim_summary_data[:,1])

fenics_output_directory = 'test_10'
stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\stress_array.npy')
stress_array_2 = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\stress_array_test_2.npy')
plt.plot(myosim_summary_data[:,0],stress_array,'r')
plt.plot(myosim_summary_data[:,0],stress_array_2,'k')

plt.show()



