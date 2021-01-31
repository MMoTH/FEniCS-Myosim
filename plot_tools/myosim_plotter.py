import numpy as np
import os as os
import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

# This script plots relevant myosim information and animates cross-bridge populations
# Assumes the script is called from within the directory containing output information
# and the user provides an integer specifying the gauss point

# To do: tie in gauss point index to location in LV

# fenics writes information to the following csv files:
# active_stress.csv
# half_sarcomere_lengths.csv
# calcium.csv
# populations.csv
# time.csv
# myofiber_passive.csv
# gucc_fiber_pstress.csv
# gucc_trans_pstress.csv
# gucc_shear_pstress.csv
# overlap.csv
# alpha.csv (not plotted here)
# delta_hsl.csv (not plotted here)

# user specifies which gauss point to look at
gp = int(sys.argv[1])
total_gauss_points = 15540 # can get this from loaded info, but don't want to take the
# time to load an entire file

# load in info just from that gauss point
cb_force = np.loadtxt('active_stress.csv', delimiter = ',', usecols=gp)
hsl = np.loadtxt('half_sarcomere_lengths.csv', delimiter = ',', usecols=gp)
calcium = np.loadtxt('calcium.csv', delimiter = ',', usecols=gp)
# time saved incorrectly. For now:
time = np.loadtxt('time.csv', delimiter = ',', skiprows=np.shape(cb_force)[0]-1)
myofiber_passive = np.loadtxt('myofiber_passive.csv', delimiter = ',', usecols=gp)
gucc_fiber_pstress = np.loadtxt('gucc_fiber_pstress.csv', delimiter = ',', usecols=gp)
gucc_trans_pstress = np.loadtxt('gucc_trans_pstress.csv', delimiter = ',', usecols=gp)
gucc_shear_pstress = np.loadtxt('gucc_shear_pstress.csv', delimiter = ',', usecols=gp)
filament_overlap = np.loadtxt('overlap.csv', delimiter = ',', usecols=gp)

# set up sequence of integers that specify which rows to pull out of population file
# transpose population file so you only pull one column out?
"""num_timesteps = np.shape(time)[0]
pop_indices = np.arange(gp,num_timesteps*total_gauss_points,total_gauss_points)
populations = np.loadtxt('populations.csv', delimiter=',', userows"""
data_range = 1699
# plot everything
fig = plt.figure()

#-------------------------------------------------------------------------------
plt.subplot(511)
cbforce, = plt.plot(time[0:1699],cb_force)
plt.legend(['cross-bridge force (Pa)'])
#-------------------------------------------------------------------------------
plt.subplot(512)
hsl_plot, = plt.plot(time[0:1699], hsl)
plt.legend(['half-sarcomere length (nm)'])
#-------------------------------------------------------------------------------
plt.subplot(513)
ca, = plt.plot(time[0:1699],calcium)
plt.legend(['calcium [M]'])
#-------------------------------------------------------------------------------
plt.subplot(514)
f_overlap, = plt.plot(time[0:1699],filament_overlap)
plt.legend(['filament overlap'])
#-------------------------------------------------------------------------------
plt.subplot(515)
fiber_pstress, = plt.plot(time[0:1699], myofiber_passive)
gfiber, = plt.plot(time[0:1699], gucc_fiber_pstress)
gtrans, = plt.plot(time[0:1699], gucc_trans_pstress)
gshear, = plt.plot(time[0:1699], gucc_shear_pstress)
plt.legend((fiber_pstress, gfiber, gtrans, gshear), ('fiber', 'G_fiber', 'G_trans', 'G_shear'))
#-------------------------------------------------------------------------------
plt.xlabel('time (ms)')
plt.show()
