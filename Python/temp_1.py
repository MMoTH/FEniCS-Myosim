# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:21:43 2018

@author: ani228
"""

import numpy as np

x = np.arange(9).reshape(3,3)

y = x

x[0,0] = 1000

print(y[0,0])