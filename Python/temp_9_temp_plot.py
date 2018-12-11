# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:00:07 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')


stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_9_temp\\stress_array.npy')
pstress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_9_temp\\pstress_array.npy')
tracarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_9_temp\\trac_array.npy')
tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_9_temp\\tarray.npy')

active, = plt.plot(tarray, stress_array,'r')

passive, = plt.plot(tarray, pstress_array,'b')

actpass, = plt.plot(tarray, stress_array+pstress_array,'k')

plt.scatter(tarray,tracarray)



plt.scatter(tarray, )

plt.xlabel('time (s)')
plt.ylabel("Stress (Pa)")
#plt.legend((active, passive, traction, actpass), ('Active', 'Passive', 'Traction', 'Active + Passive'))
plt.get_current_fig_manager().full_screen_toggle()
plt.show()