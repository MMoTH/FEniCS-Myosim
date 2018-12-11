# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:15:19 2018

@author: ani228
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:18:25 2018

@author: ani228
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:39:10 2018

@author: ani228
"""
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

test_number = 3
# INPUT DATA
if (test_number == 2):
    fenics_output_directory = 'test_2'
    no_of_time_steps = 701
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4

if (test_number == 3):
    fenics_output_directory = 'test_3'
    no_of_time_steps = 7408
    no_of_states = 4
    n_array_length = 45   
    no_of_x_bridges = 21
    no_of_transitions = 8
       

    
fenics_rates_file = 'C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\rates_fenics.txt'
fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\dumped_populations.npy')
tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\tarray.npy')
stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\stress_array.npy')
calcium = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\calcium.npy')
hsl = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\HSL.npy')

myosim_rates_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\rates.txt'
myosim_pop_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\populations.txt'
myosim_summary_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\summary.txt'


myosim_pop_data = np.zeros((no_of_time_steps,no_of_states))
columns = tuple(range(1,no_of_states+1))
myosim_pop_data[:,0:4] = np.loadtxt(myosim_pop_file, skiprows = 5, usecols = columns)

myosim_summary_data = np.zeros((no_of_time_steps,2))
myosim_summary_data[:,0:2] = np.loadtxt(myosim_summary_file, skiprows = 5, usecols = (0,2))

myosim_rates = np.zeros((no_of_x_bridges,no_of_transitions+1))
columns = tuple(range(no_of_transitions+1))
myosim_rates[:,0:no_of_transitions+1] = np.loadtxt(myosim_rates_file, skiprows = 1, usecols = columns)

#------------------------------------------------------------------------------

fenics_pop_data = np.zeros((no_of_time_steps,n_array_length))

for i in range(no_of_time_steps):
    
    fenics_pop_data[i,:] = fenics_pop_file[i,0,:]
    
fenics_rates = np.zeros((no_of_x_bridges, no_of_transitions + 1))
columns = tuple(range(no_of_transitions+1))
fenics_rates[:,0:no_of_transitions+1] = np.loadtxt(fenics_rates_file, skiprows = 1, usecols = columns)

get_ipython().run_line_magic('matplotlib', 'qt')
#get_ipython().run_line_magic('matplotlib', 'inline')


fig = plt.figure()
#------------------------------------------------------------------------------
plt.subplot(421)
plt.scatter(myosim_rates[:,0], myosim_rates[:,3],color='b')
rate3, = plt.plot(fenics_rates[:,0], fenics_rates[:,3],'b')

plt.scatter(myosim_rates[:,0], myosim_rates[:,4],color='g')
rate4, = plt.plot(fenics_rates[:,0], fenics_rates[:,4],'g')

plt.legend((rate3, rate4), ('Rate 3', 'Rate 4'))
#------------------------------------------------------------------------------
plt.subplot(422)

state_1_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,0], 'k')
state_2_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,1], 'k')

#state_3_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,2], 'r')

plt.scatter(tarray[::200], myosim_pop_data[::200,0], color = 'k')
plt.scatter(tarray[::200], myosim_pop_data[::200,1], color = 'k')
#plt.scatter(tarray[::200], myosim_pop_data[::200,2], color = 'r')

plt.legend((state_1_pops_fenics, state_2_pops_fenics), ('state 1', 'state 2'))
plt.title("Myosin Populations")
plt.xlabel('time (s)')
plt.ylabel("Proportions")
#------------------------------------------------------------------------------
plt.subplot(423)

plt.scatter(myosim_rates[:,0], myosim_rates[:,5],color='c')
rate5, = plt.plot(fenics_rates[:,0], fenics_rates[:,5],'c')

plt.scatter(myosim_rates[:,0], myosim_rates[:,6],color='m')
rate6, = plt.plot(fenics_rates[:,0], fenics_rates[:,6],'m')

plt.legend((rate5, rate6), ('Rate 5', 'Rate 6'))
#------------------------------------------------------------------------------
plt.subplot(424)
state_3_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[:,2:23],1), 'r')
state_4_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[:,23:44],1), 'b')
#binding_sites, = plt.plot(tarray, fenics_pop_data[:,n_array_length-1],'g')

#plt.scatter(tarray, myosim_pop_data[:,2], color = 'r')
plt.scatter(tarray[::200], myosim_pop_data[::200,2], color = 'r')
plt.scatter(tarray[::200], myosim_pop_data[::200,3], color = 'b')

plt.legend((state_3_pops_fenics, state_4_pops_fenics), ('sum of state 3', 'sum of state 4'))
plt.xlabel('time (s)')
plt.ylabel("Proportions")
#------------------------------------------------------------------------------
plt.subplot(425)

plt.scatter(myosim_rates[:,0], myosim_rates[:,7],color='y')
rate7, = plt.plot(fenics_rates[:,0], fenics_rates[:,7],'y')

plt.scatter(myosim_rates[:,0], myosim_rates[:,8],color='r')
rate8, = plt.plot(fenics_rates[:,0], fenics_rates[:,8],'r')

plt.legend((rate7, rate8), ('Rate 7', 'Rate 8'))
#------------------------------------------------------------------------------
plt.subplot(426)
plt.plot(tarray, stress_array)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.scatter(myosim_summary_data[::100,0], myosim_summary_data[::100,1],color='r')
#plt.plot(myosim_summary_data[:,0], myosim_summary_data[:,1],'r')
plt.xlabel('time (s)')
plt.ylabel("Stress (Pa)")
#------------------------------------------------------------------------------
plt.subplot(427)
plt.plot(tarray, calcium)
plt.xlabel('time (s)')
plt.ylabel("Calcium [M]")
#------------------------------------------------------------------------------
plt.subplot(428)
plt.plot(tarray, hsl)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
plt.xlabel('time [s]')
plt.ylabel("hsl (nm)")
#------------------------------------------------------------------------------
#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
#plt.figure()
plt.get_current_fig_manager().full_screen_toggle()
plt.show()