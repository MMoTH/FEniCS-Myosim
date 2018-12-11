# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:59:15 2018

@author: ani228
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'inline')

times = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\active_stretch_cube_times.npy')

displacements = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\active_stretch_cube_displacements.npy')

hsl = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\active_stretch_cube_hsl.npy')

#plt.scatter(times, displacements)

plt.scatter(times, hsl)

plt.show()
