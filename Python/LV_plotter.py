# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:15:46 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt

PV = np.loadtxt('C:/Users/ani228/Dropbox/UK/FEniCS/test_8/PV_.txt')

plt.plot(PV[:,2],PV[:,1])
plt.show()

