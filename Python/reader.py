# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:12:28 2018

@author: ani228
"""

import numpy as np

'''
summary_smooth_calcium_file = 'C:\ProgramData\Myosim\\twitch\summary_smooth_calcium.txt'

passive_forces = np.zeros((701,4))
passive_forces[:,0:4] = np.loadtxt(summary_smooth_calcium_file, skiprows = 5, usecols = (3,17,31,45))
np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\passive_forces",passive_forces)
'''

'''
hs_lengths = np.zeros((701,4))
hs_lengths[:,0:4] = np.loadtxt(summary_smooth_calcium_file, skiprows = 5, usecols = (5,19,33,47))
np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\twitch_test_1\\hs_lengths",hs_lengths)
'''

#time_steps = 7408
time_steps = 701

#summary_file = "C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\summary.txt"
summary_file = "C:\\ProgramData\\MyoSim\\MyoSim_output\\summary.txt"

#passive_forces = np.zeros((time_steps,1))
passive_forces = np.loadtxt(summary_file, skiprows = 5, usecols = 3)
#hsls = np.loadtxt(summary_file, skiprows = 5, usecols = 5)
np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_10\\passive_forces",passive_forces)
#np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\hsls",hsls)

'''
protocol_file = 'C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\protocol.txt'
np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\hsl_incs",hsl_incs)
'''
'''
hsl_myosim = np.zeros((time_steps,1))
hsl_myosim[:,0] = np.loadtxt(summary_file, skiprows = 5, usecols = (5))
np.save("C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_3\\hsl_summary",hsl_myosim)
'''



