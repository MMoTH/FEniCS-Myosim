"""
Created on Wed Oct  9 12:40:00 PM 2019

@author: Kurtis Mann

Modifying Amir's plotter to hopefully plot generic LV simulation
Currently, IPython only works using python 2.7
"""
import os as os
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as ticker
import time
plt.style.use('seaborn-pastel')
gauss_point = 0
import math
import pandas as pd
gauss_point = int(sys.argv[1])

sim_dir = os.getcwd()
font_size = 14

# Set up plot style info here
font = {'weight':'normal',
    'size': 14}

purple = '#7656E7'
red = '#F99394'
green = '#92FF93'
blue = '#ABD2FF'
gray = '#707180'

csv_flag = int(sys.argv[2]) # 1 for csv files
print "csv = " + str(csv_flag)

#plt.rcParams('tick',labelsize=15)

def get_yticks(y_bound=[]):

    def get_my_ceil(number,decimals):
        number = number * 10**decimals
        ceil = math.ceil(number/5)*5/(10**decimals)
        return ceil
    def get_my_floor (number,decimals):
        number = number * 10**decimals
        floor = math.floor(number/5)*5/(10**decimals)
        return floor

    y_max = y_bound[1]
    #print "y max " + str(y_max)
    y_min = y_bound[0]

    y_max_tick = int(math.ceil(y_max/5)*5)
    #print "ymax tick " + str(y_max_tick)
    y_min_tick = int(math.floor(y_min/5)*5)

    if y_max < 0.01:
        y_max_tick = get_my_ceil(y_max,3)
        y_min_tick = get_my_floor(y_min,3)
    elif y_max < 1 :
        y_max_tick = get_my_ceil(y_max,2)
        y_min_tick = get_my_floor(y_min,2)
    elif y_max<10:
        y_max_tick = int(math.ceil(y_max))
        y_min_tick = int(math.floor(y_min))

    if y_min_tick<0:
        y_min_tick = 0

    y_ticks = [y_min_tick,y_max_tick]

    return y_ticks

def find_all_char_index(str,sub_str):
    index_array = []
    start_index = 0
    while start_index < len(str):
        start_index = str.find(sub_str,start_index)
        if  start_index == -1:
            return index_array
        else:
            index_array.append(start_index)
            start_index += 1
    return index_array

def get_labelpad(y_max_tick,x_range):
    max_len_ticks = 4
    x_mid = 50 #x_range/2
    len_y_tick = len(str(y_max_tick))
    if '.' in str(y_max_tick):
       len_y_tick = len_y_tick - 0.5

    len_dif_ticks = max_len_ticks-len_y_tick

    labelpad = x_mid+len_dif_ticks*10

    return labelpad

def get_y_label_y_coord(string):

    number_of_lines =string.count("\n")+1
    line_index_array = find_all_char_index(string,'\n')
    half_line_counter = 0
    start_index = 0
    if len(line_index_array) == 0:
        if '^' in string:
            half_line_counter = 1
    else:
        for i in range(number_of_lines):
            if i < len(line_index_array):
                end_index = line_index_array[i]
            else:
                end_index = -1
            if '^' in string[start_index:end_index]:
                half_line_counter += 1
            if end_index != -1:
                 start_index = end_index + 1

    number_of_lines = number_of_lines + half_line_counter*1
    y_coord = 0.5-number_of_lines*0.1

    return y_coord

# For now, hard coding bin discretization information
xmin = -10
xmax = 10
bin_width = 1.0
cb_domain = np.arange(xmin,xmax+bin_width,bin_width)
num_bins = np.shape(cb_domain)

# overlap is saved last, so will use shape to determine data range
if csv_flag:
    print csv_flag

    overlap_loaded = pd.read_csv('overlap.csv',delimiter=',')
    overlap = overlap_loaded.to_numpy()
    overlap = overlap[:,gauss_point+1]
    #tarray_loaded = pd.read_csv('time.csv',delimiter=',')
    #tarray_new = tarray_loaded.to_numpy()
    #print np.shape(tarray_new)
    #tarray = np.zeros(np.shape(tarray_new)[0])
    #for i in np.arange(np.shape(tarray_new)[0]):
    #    tarray[i] = tarray_new[i,i]
    #tarray = np.load('time.npy')
    tarray = np.linspace(0,200,399)
    calcium_loaded = pd.read_csv('calcium.csv',delimiter=',')
    calcium = calcium_loaded.to_numpy()
    calcium = calcium[:,gauss_point+1]
    HSL_loaded = pd.read_csv('half_sarcomere_lengths.csv',delimiter=',')
    #print HSL.type()
    HSL = HSL_loaded.to_numpy()
    HSL = HSL[:,gauss_point+1]
    stress_array_loaded = pd.read_csv('active_stress.csv',delimiter=',')
    stress_array = stress_array_loaded.to_numpy()
    stress_array = stress_array[:,gauss_point+1]
    fenics_pop_data_loaded = pd.read_csv('populations.csv',delimiter=',')
    fenics_pop_data_uncropped = fenics_pop_data_loaded.to_numpy()
    fenics_pop_data = fenics_pop_data_uncropped[:,1:26]
    pstress_loaded = pd.read_csv('myofiber_passive.csv',delimiter=',')
    pstress = pstress_loaded.to_numpy()
    pstress = pstress[:,gauss_point+1]
    sim_info = np.shape(fenics_pop_data)
    array_length = sim_info[1]
    num_timesteps = np.shape(tarray)[0]+1
    print "shape of pops " + str(sim_info[0]+1)
    print "no of time steps " +str(num_timesteps)
    #num_int_points = sim_info[0]/num_timesteps
    num_int_points = (sim_info[0]+1)/(num_timesteps)
    print "no of int points = " + str(num_int_points)
    data_range = np.shape(overlap)[0]

else:
    overlap = np.load(sim_dir + '/overlap.npy')
    tarray = np.load(sim_dir+'/tarray.npy')
    #tarray = np.linspace(0,100,200)
    calcium = np.load(sim_dir + '/calcium.npy')
    HSL = np.load(sim_dir + '/hsl.npy')
    HSL = HSL[:,gauss_point]
    stress_array = np.load(sim_dir + '/stress_array.npy')
    stress_array = stress_array[:,gauss_point]
    fenics_pop_data = np.load(sim_dir + '/dumped_populations.npy')
    pstress = np.load(sim_dir + '/pstress_array.npy')
    pstress = pstress[:,gauss_point]
    sim_info = fenics_pop_data.shape
    array_length = sim_info[2]
    num_timesteps = np.shape(tarray)[0]
    num_int_points = sim_info[0]/num_timesteps
    data_range = np.shape(overlap)[0]-1

    #gucc_fiber = np.load(sim_dir + '/gucc_fiber_pstress.npy')
    #gucc_trans = np.load(sim_dir + '/gucc_trans_pstress.npy')
    #gucc_shear = np.load(sim_dir + '/gucc_shear_pstress.npy')

if stress_array.ndim > 1:
    # single cell sims only save for one gauss point, dimension is one less than
    # ventricle simulation
    single_cell_sim_flag = 1
else:
    single_cell_sim_flag = 1

# Define number of time steps and array length here
#print sim_info

#print "array length is = " + str(array_length)
#print sys.argv[0]
#print sys.argv[1]

#gauss_point = 1000
#data_range = 400
#data_range = 50
# Look at how info is dumped from FEniCS. For now, hard code number of detached and attached states, and bins
# Want to be able to visualize distributions, will need this info to set up arrays.
#num_d_states
#num_a_states
#num_bins
#bin_min
#bin_max

#fenics_pop_data = np.zeros((num_timesteps,array_length))
M_OFF = np.zeros(data_range)
M_ON =  np.zeros(data_range)
M_BOUND =  np.zeros(data_range)
N_ON =  np.zeros(data_range)
N_OFF = np.zeros(data_range)
#print np.shape(fenics_pop_data)

#print fenics_pop_data[0,0]
print "shape of cropped pops " + str(np.shape(fenics_pop_data))
print " num int points " + str(num_int_points)

max_nbound = 0.0
#max_nbound = np.amax(fenics_pop_data[:,2:array_length-3])

for i in range(data_range):

    # Reading in information from just one Gauss point [i = timestep, 0 = gauss point, : is all pop info]
    if csv_flag:
        #print np.shape(fenics_pop_data)

        M_OFF[i] = fenics_pop_data[i*num_int_points+gauss_point,0]
        M_ON[i] = fenics_pop_data[i*num_int_points+gauss_point,1]
        M_BOUND[i] = np.sum(fenics_pop_data[i*num_int_points+gauss_point,2:array_length-3])
        N_ON[i] = fenics_pop_data[i*num_int_points+gauss_point,array_length-1]
        if np.amax(fenics_pop_data[i*num_int_points+gauss_point,2:array_length-3]) > max_nbound:
            max_nbound = np.amax(fenics_pop_data[i*num_int_points+gauss_point,2:array_length-3])
        else:
            max_nbound = max_nbound
    else:
        M_OFF[i] = fenics_pop_data[i,gauss_point,0]
        M_ON[i] = fenics_pop_data[i,gauss_point,1]
        M_BOUND[i] = np.sum(fenics_pop_data[i,gauss_point,2:array_length-3])
        N_ON[i] = fenics_pop_data[i,gauss_point,array_length-1]
        N_OFF[i] = fenics_pop_data[i,gauss_point,array_length-2]
        if np.amax(fenics_pop_data[i,num_int_points+gauss_point,2:array_length-3]) > max_nbound:
            max_nbound = np.amax(fenics_pop_data[i,num_int_points+gauss_point,2:array_length-3])
        else:
            max_nbound = max_nbound
fig = plt.figure(figsize=(16,9),dpi=144)
#fig.set_size_inches([22,8])
#------------------------------------------------------------------------------
ax2 = plt.subplot(421)
right_side = ax2.spines["right"]
bottom = ax2.spines["bottom"]
top = ax2.spines["top"]
right_side.set_visible(False)
bottom.set_visible(False)
top.set_visible(False)

ax2.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,
    labelsize = 15)
ax2.tick_params(
    axis='y',
    direction='out'
)
#print np.amin(HSL)

majors = [int(0.9*np.amin(HSL[0:data_range])),1.1*int(np.amax(HSL[0:data_range]))]
print np.amax(HSL)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(majors[1]-majors[0]))

plt.ylim((0.9*np.amin(HSL[0:data_range]),1.1*np.amax(HSL)))



if single_cell_sim_flag > 0:
    plt.plot(tarray[0:data_range],HSL[0:data_range],color=purple,linewidth=4)
else:
    plt.plot(tarray[0:data_range], HSL[0:data_range,:],color=purple,linewidth=4)

#plt.xlabel('Time [ms]',fontdict=font)
#plt.ylabel("Half-sarcomere Length \n  (nm)",fontdict=font,rotation=0)
ax2.yaxis.set_label_coords(-0.25,0.5)
y_bound = ax2.get_ybound()
y_ticks = get_yticks(y_bound)
print "time"
print np.shape(tarray)
x_range = [tarray[0],tarray[data_range-1]]
ax2.set_ylim(y_ticks)
ax2.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = 'Half-sarcomere Length \n (nm)'
y_coord = get_y_label_y_coord(y_label)
ax2.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)

#------------------------------------------------------------------------------

ax3 = plt.subplot(422)
right_side3 = ax3.spines["right"]
bottom3 = ax3.spines["bottom"]
top3 = ax3.spines["top"]
right_side3.set_visible(False)
bottom3.set_visible(False)
top3.set_visible(False)

ax3.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)

plt.ylim((0,1))

#print np.shape(tarray)
#print np.shape(M_OFF)
state_1_pops_fenics, = plt.plot(tarray[0:data_range], M_OFF[0:data_range],label='SRX',color=gray,linewidth=4)
state_2_pops_fenics, = plt.plot(tarray[0:data_range], M_ON[0:data_range],label='Detached',color=green,linewidth=4)
state_3_pops_fenics, = plt.plot(tarray[0:data_range], M_BOUND[0:data_range],label='M Bound',color=red,linewidth=4)

plt.legend((state_1_pops_fenics,state_2_pops_fenics,state_3_pops_fenics), ('M_SRX', 'M_DRX', 'M_FG'))
#plt.title("Myosin Populations")
#plt.xlabel('Time (ms)')
#plt.ylabel("Proportions",fontdict=font,rotation=0)
y_bound = ax3.get_ybound()
y_ticks = get_yticks(y_bound)
ax3.set_ylim(y_ticks)
ax3.set_yticks(y_ticks)
x_range = [tarray[0],tarray[data_range-1]]
ax3.set_ylim(y_ticks)
ax3.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = 'Myosin Populations \n (Proportion)'
y_coord = get_y_label_y_coord(y_label)
ax3.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
#---------------------------------------------------------------------------------
ax4 = plt.subplot(423)
right_side4 = ax4.spines["right"]
bottom4 = ax4.spines["bottom"]
top4 = ax4.spines["top"]
right_side4.set_visible(False)
bottom4.set_visible(False)
top4.set_visible(False)

ax4.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)

plt.ylim((0.9*np.amin(pstress),1.1*np.amax(pstress)))

if single_cell_sim_flag > 0:
    fiber_pstress, = plt.plot(tarray[0:data_range], pstress[0:data_range],color=purple,linewidth=4)
else:
    fiber_pstress, = plt.plot(tarray[0:data_range], pstress[0:data_range,gauss_point])
    gfiber, = plt.plot(tarray[0:data_range], gucc_fiber[0:data_range,gauss_point])
    gtrans, = plt.plot(tarray[0:data_range], gucc_trans[0:data_range,gauss_point])
    gshear, = plt.plot(tarray[0:data_range], gucc_shear[0:data_range,gauss_point])
    plt.legend((fiber_pstress, gfiber, gtrans, gshear), ('fiber', 'G_fiber', 'G_trans', 'G_shear'))

#plt.plot(tarray, pstress[0:data_range])
#plt.ylabel('Passive Stress (Pa)',fontdict=font,rotation=0)
y_bound = ax4.get_ybound()
y_ticks = get_yticks(y_bound)
x_range = [tarray[0],tarray[data_range-1]]
ax4.set_ylim(y_ticks)
ax4.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = ' Myofiber Passive Stress\n (Pa)'
y_coord = get_y_label_y_coord(y_label)
ax4.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
ax4.set_ylim(y_ticks)
ax4.set_yticks(y_ticks)
#------------------------------------------------------------------------------
ax5 = plt.subplot(424)
right_side5= ax5.spines["right"]
bottom5= ax5.spines["bottom"]
top5= ax5.spines["top"]
right_side5.set_visible(False)
bottom5.set_visible(False)
top5.set_visible(False)
#state_3_pops_fenics, = plt.plot(tarray, np.sum(fenics_pop_data[0:data_range,2:array_length-2]), 'r')
state_3_pops_fenics, = plt.plot(tarray[0:data_range], M_BOUND[0:data_range],color=red,linewidth=4)
binding_sites, = plt.plot(tarray[0:data_range], N_ON[0:data_range],color=blue,linewidth=4)

ax5.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)

plt.ylim((0,1))

plt.legend((binding_sites,state_3_pops_fenics), ('Binding Sites','M_FG'))
#plt.xlabel('Time (ms)')
#plt.ylabel("Proportions",fontdict=font,rotation=0)
y_bound = ax5.get_ybound()
y_ticks = get_yticks(y_bound)
ax5.set_ylim(y_ticks)
ax5.set_yticks(y_ticks)
x_range = [tarray[0],tarray[data_range-1]]
ax5.set_ylim(y_ticks)
ax5.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = '  Filament Populations \n (Proportion)'
y_coord = get_y_label_y_coord(y_label)
ax5.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
#------------------------------------------------------------------------------
ax6=plt.subplot(425)
right_side6 = ax6.spines["right"]
bottom6 = ax6.spines["bottom"]
top6 = ax6.spines["top"]
right_side6.set_visible(False)

plt.ylim((0.9*np.amin(overlap[0:data_range]),1.1*np.amax(overlap[0:data_range])))


#bottom.set_visible(False)
top6.set_visible(False)
plt.plot(tarray[0:data_range], overlap[0:data_range],color=purple,linewidth=4)
"""plt.plot(tarray[0:data_range],N_ON[0:data_range])
plt.plot(tarray[0:data_range],N_OFF[0:data_range])
plt.plot(tarray[0:data_range],N_ON[0:data_range]+N_OFF[0:data_range])"""
plt.ylabel('Filament Overlap',fontdict=font,rotation=0)
y_bound = ax6.get_ybound()
y_ticks = get_yticks(y_bound)
plt.xlabel('Time (ms)',fontdict=font)
#ax6.set_xlabel('Time (ms)', fontsize = font_size)
ax6.set_ylim(y_ticks)
ax6.set_yticks(y_ticks)
x_range = [tarray[0],tarray[data_range-1]]
ax6.set_ylim(y_ticks)
ax6.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = 'Filament \n Overlap \n (Proportion)'
y_coord = get_y_label_y_coord(y_label)
ax6.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
#------------------------------------------------------------------------------
ax7 = plt.subplot(426)
right_side7 = ax7.spines["right"]
bottom7 = ax7.spines["bottom"]
top7 = ax7.spines["top"]
right_side7.set_visible(False)
bottom7.set_visible(False)
top7.set_visible(False)

ax7.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)

plt.ylim((0.9*np.amin(stress_array),1.1*np.amax(stress_array)))


if single_cell_sim_flag > 0:
    plt.plot(tarray[0:data_range],stress_array[0:data_range],color=purple,linewidth=4)
else:
    plt.plot(tarray[0:data_range], stress_array[0:data_range,gauss_point],color=purple,linewidth=4)

#plt.xlabel('Time (ms)')
#plt.ylabel("Active Stress (Pa)",fontdict=font,rotation=0)
y_bound = ax7.get_ybound()
y_ticks = get_yticks(y_bound)
ax7.set_ylim(y_ticks)
ax7.set_yticks(y_ticks)
x_range = [tarray[0],tarray[data_range-1]]
ax7.set_ylim(y_ticks)
ax7.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = 'Active Stress \n (Pa)'
y_coord = get_y_label_y_coord(y_label)
ax7.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
#------------------------------------------------------------------------------
ax8 = plt.subplot(428)
right_side8 = ax8.spines["right"]
bottom8 = ax8.spines["bottom"]
top8 = ax8.spines["top"]
right_side8.set_visible(False)
#bottom.set_visible(False)
top8.set_visible(False)
pca = -1*np.log10(calcium)
plt.plot(tarray[0:data_range], pca[0:data_range],color=purple,linewidth=4)
#plt.scatter(myosim_summary_data[:,0], myosim_summary_data[:,1],color='r')
ax8.set_xlabel('Time (ms)', fontsize = font_size)
#plt.ylabel("Calcium [M]",fontdict=font,rotation=0)
#plt.ylim((0.9*np.amin(calcium[0:data_range,0]),1.1*np.amax(calcium[0:data_range,0])))
#ax8.set_ylim(0.9*np.amin(calcium[0:data_range,0]),1.1*np.amax(calcium[0:data_range,0]))
#x_range = [tarray[0],tarray[data_range-1]]
y_bound = ax8.get_ybound()
#print "ybound " + str(y_bound)
y_ticks = get_yticks(y_bound)
#print "y ticks " + str(y_ticks[1])
ax8.set_ylim(y_ticks)
ax8.set_yticks(y_ticks)
#x_range = [tarray[0],tarray[data_range-1]]
#ax8.set_ylim(y_ticks)
#ax8.set_yticks(y_ticks)
labelpad= get_labelpad(y_ticks[1],x_range)
y_label = '          pCa'
y_coord = get_y_label_y_coord(y_label)
ax8.set_ylabel(y_label, fontsize = font_size,rotation=0,labelpad=labelpad,y=y_coord)
ax8.invert_yaxis()
#------------------------------------------------------------------------------
# Animate cross-bridges during simulation

#print max_nbound
ax1 = plt.subplot(427,xlim=(xmin-1,xmax+1),ylim=(0.00,1.1*np.amax(max_nbound)))
y_label = 'M_FG(x)                       \n (Proportion)                   '
y_coord = get_y_label_y_coord(y_label)
ax1.set_ylabel(y_label, fontsize = font_size, rotation=0,y=y_coord)
#y_bound = ax1.get_ybound()
y_ticks = get_yticks(y_bound)
#ax1.set_ylim(max_nbound)
#ax1.set_yticks(y_ticks)
ax1.set_xlabel('Working Cross-bridge \n Range \n (nm)', fontsize = font_size)
#plt.xlabel('Working Cross-bridge Range (nm)')
right_side1 = ax1.spines["right"]
bottom1 = ax1.spines["bottom"]
top1 = ax1.spines["top"]
right_side1.set_visible(False)
#bottom.set_visible(False)
top1.set_visible(False)
#ax = plt.axes(xlim=(xmin,xmax),ylim=(0,1))
line1, = ax1.plot([],[],lw=4,color=red)
line2, = ax2.plot([],[],lw=4,color=red)
line3, = ax3.plot([],[],lw=4,color=red)
line = [line1, line2, line3]

def init():
    line[0].set_data([],[])
    line[1].set_data([],[])
    line[2].set_data([],[])
    return line

t, m, m2 = [], [], []
y = np.zeros(np.shape(cb_domain))
def animate(i):
    # array_length -1 for cpp, -2 for python
    #y = fenics_pop_file[i,gauss_point,2:array_length-2]
    #print np.shape(fenics_pop_data)
    if csv_flag:
        y = fenics_pop_data[i*num_int_points+gauss_point,2:array_length-2]
    else:
        y = fenics_pop_data[i,num_int_points+gauss_point,2:array_length-2]
    #print np.shape(cb_domain)
    if single_cell_sim_flag > 0:
        m.append(HSL[i])
        m2.append(stress_array[i])
    else:
        m.append(HSL[i,gauss_point])
        m2.append(stress_array[i,gauss_point])
    #print np.shape(cb_domain)
    t.append(tarray[i])
    print "time = " + str(t[i])
    #print np.shape(y)
    line[0].set_data(cb_domain,y)
    line[1].set_data(t,m)
    line[2].set_data(t,m2)
    #time.sleep(0.25)
    return line



anim = FuncAnimation(fig, animate, init_func=init, frames = num_timesteps-1, interval = 50, blit=True,save_count=200)

#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
#plt.figure()

plt.subplots_adjust(left=.175,right=.95,wspace=0.5)
plt.plot(HSL)
#plt.switch_backend('Qt4Agg')
#mng=plt.get_current_fig_manager()
#mng.window.showMaximized()

#mng.show()
#print(anim.to_html5_video())
anim.save('test.mp4','ffmpeg',15)
#anim.to_html5_video('test_animation')
plt.show()
#plt.show()
