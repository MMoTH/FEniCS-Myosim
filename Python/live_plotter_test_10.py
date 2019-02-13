import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')

myosim_results = 1

test = 'test_10'

if test == 'test_10':
    
    fenics_output_directory = 'test_10'
    int_point = 0
    no_of_time_steps = 701
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
if test == 'test_9':
    
    fenics_output_directory = 'test_9'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4

if test == 'test_8':
    
    fenics_output_directory = 'test_6'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
if test == 'test_7':
    
    fenics_output_directory = 'test_7'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
if test == 'test_6':
    
    fenics_output_directory = 'test_6'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
if test == 'test_5':
    
    fenics_output_directory = 'test_5'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4

if test == 'test_4':
    
    fenics_output_directory = 'test_4'
    int_point = 0
    no_of_time_steps = 400
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
if test == 'test_3':
    
    fenics_output_directory = 'test_3'
    int_point = 0
    no_of_time_steps = 7408
    no_of_states = 4
    n_array_length = 45   
    no_of_x_bridges = 21
    no_of_transitions = 8
    
if test == 'test_2':
    
    fenics_output_directory = 'test_2_new'
    int_point = 0
    no_of_time_steps = 701
    no_of_states = 3
    n_array_length = 52   
    no_of_x_bridges = 49
    no_of_transitions = 4
    
    

    

#style.use('classic')
fig = plt.figure()

def animate(i):
    
    fig.clear()
    fenics_rates_file = 'C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\rates.npy'
    fenics_pop_file = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\dumped_populations.npy')
    tarray = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\tarray.npy')
    stress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\stress_array.npy')
    #pstress_array = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\pstress_array.npy')
    calcium = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\calcium.npy')
    hsl = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\' + fenics_output_directory + '\\HSL.npy')
    
    if (myosim_results):
        myosim_rates_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\rates.txt'
        myosim_pop_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\populations.txt'
        myosim_summary_file = 'C:\\ProgramData\\Myosim\\MyoSim_output\\summary.txt'
        
        myosim_pop_data = np.zeros((no_of_time_steps,no_of_states))
        columns = tuple(range(1,no_of_states+1))
        myosim_pop_data[:,0:no_of_states] = np.loadtxt(myosim_pop_file, skiprows = 5, usecols = columns)
        myosim_summary_data = np.zeros((no_of_time_steps,2))
        myosim_summary_data[:,0:2] = np.loadtxt(myosim_summary_file, skiprows = 5, usecols = (0,2))
        myosim_rates = np.zeros((no_of_x_bridges,no_of_transitions+1))
        columns = tuple(range(no_of_transitions+1))
        myosim_rates[:,0:no_of_transitions+1] = np.loadtxt(myosim_rates_file, skiprows = 1, usecols = columns)
    
#------------------------------------------------------------------------------

    fenics_pop_data = np.zeros((no_of_time_steps,n_array_length))
    for i in range(no_of_time_steps):    
        fenics_pop_data[i,:] = fenics_pop_file[i,int_point,:]    
    fenics_rates = np.zeros((no_of_x_bridges, no_of_transitions + 1))
    fenics_rates[:,0:no_of_transitions+1] = np.load(fenics_rates_file)
        
    #--------------------------------------------------------------------------
    plt.subplot(421)
    rate3, = plt.plot(fenics_rates[:,0], fenics_rates[:,1],'k')
    rate4, = plt.plot(fenics_rates[:,0], fenics_rates[:,2],'c')
    if (myosim_results):
        plt.scatter(myosim_rates[:,0], myosim_rates[:,1],color='k')
        plt.scatter(myosim_rates[:,0], myosim_rates[:,2],color='g')
    plt.legend((rate3, rate4), ('Rate 1', 'Rate 2'))
    #--------------------------------------------------------------------------
    plt.subplot(423)
    rate3, = plt.plot(fenics_rates[:,0], fenics_rates[:,3],'k')
    rate4, = plt.plot(fenics_rates[:,0], fenics_rates[:,4],'c')
    if (myosim_results):
        plt.scatter(myosim_rates[:,0], myosim_rates[:,3],color='k')
        plt.scatter(myosim_rates[:,0], myosim_rates[:,4],color='c')
    plt.legend((rate3, rate4), ('Rate 3', 'Rate 4'))
    #--------------------------------------------------------------------------
    plt.subplot(425)
    plt.plot(tarray, hsl)
    plt.xlabel('time [s]')
    plt.ylabel("hsl (nm)")
    #--------------------------------------------------------------------------
    plt.subplot(427)
    for i in range(no_of_time_steps):
        plt.plot(fenics_rates[:,0],fenics_pop_data[i,2:n_array_length-1])
    '''plt.plot(np.arange(0,0.05,0.0005),np.arange(0,500,5))
    plt.plot(np.arange(0.05,0.15,0.0005),np.ones(200)*500)
    plt.plot(np.arange(0.15,0.2,0.0005),np.arange(495,-10,-5))
    plt.xlabel('time (s)')
    plt.ylabel("Force")'''
    #--------------------------------------------------------------------------
    plt.subplot(422)
    state_1_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,0], 'k')
    #state_1_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,0], 'k')
    state_2_pops_fenics, = plt.plot(tarray, fenics_pop_data[:,1], 'g')
    if (myosim_results):
        plt.scatter(tarray[::10], myosim_pop_data[::10,0], color = 'k')
        plt.scatter(tarray[::10], myosim_pop_data[::10,1], color = 'g')
    #plt.legend((state_1_pops_fenics, state_2_pops_fenics), ('state 1', 'state 2'))
    plt.title("Myosin Populations")
    plt.xlabel('time (s)')
    plt.ylabel("Proportions")
    #--------------------------------------------------------------------------
    plt.subplot(424)
    state_3_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[:,2:n_array_length-2],1), 'r')

    #binding_sites, = plt.plot(tarray, fenics_pop_data[:,n_array_length-1], 'g')
    if (myosim_results):
        plt.scatter(tarray[::10], myosim_pop_data[::10,2], color = 'r')
    #plt.legend((state_3_pops_fenics, binding_sites), ('FG myosin heads', 'binding sites'))
    plt.xlabel('time (s)')
    plt.ylabel("Proportions")
    #--------------------------------------------------------------------------
    plt.subplot(426)
    active, = plt.plot(tarray, stress_array,'r')
    #passive, = plt.plot(tarray, pstress_array,'b')
    #actpass, = plt.plot(tarray, stress_array+pstress_array,'k')
    #traction, = plt.plot(tarray, np.ones(np.shape(tarray))*0.0)
    
    '''active, = plt.plot(tarray[0:50], stress_array[0:50],'r')
    passive, = plt.plot(tarray[0:50], pstress_array[0:50],'b')
    actpass, = plt.plot(tarray[0:50], stress_array[0:50]+pstress_array[0:50],'k')
    traction, = plt.plot(tarray[0:50], np.ones(np.shape(tarray[0:50]))*0.0)'''
    
    if (myosim_results):
        plt.scatter(myosim_summary_data[::10,0], myosim_summary_data[::10,1],color='r')
    plt.xlabel('time (s)')
    plt.ylabel("Stress (Pa)")
    #plt.legend((active, passive, traction, actpass), ('Active', 'Passive', 'Traction', 'Active + Passive'))
    #--------------------------------------------------------------------------
    plt.subplot(428)
    plt.plot(tarray, calcium)
    plt.xlabel('time (s)')
    plt.ylabel("Calcium [M]")
    #--------------------------------------------------------------------------
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.get_current_fig_manager().full_screen_toggle()
plt.show()