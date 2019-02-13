# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:15:46 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')

PV = np.loadtxt('C:/Users/ani228/Dropbox/UK/FEniCS/test_12/PV_.txt')
#pressures = np.load('C:/Users/ani228/Dropbox/UK/FEniCS/test_12/pressures')
#volumes = np.load('C:/Users/ani228/Dropbox/UK/FEniCS/test_12/volumes')

plt.plot(PV[:,0],PV[:,1],'r')
plt.plot(PV[:,0],PV[:,2],'k')

plt.plot(PV[:,0],PV[:,2],'k')

#print(PV[:,1])



plt.get_current_fig_manager().full_screen_toggle()
plt.show()

