# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:41:26 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt


fenics_results = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\fenics_results.npy')

gsl_results = np.loadtxt('C:\\Users\\ani228\\Dropbox\\UK/Cpp\\gsl_results.txt',usecols=(0,1,2))


plt.plot(gsl_results[:,0],gsl_results[:,1],'r')
plt.plot(fenics_results[:,0],fenics_results[:,1],'k')

plt.show()