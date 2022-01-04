import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
import pandas as pd




# Get desired gauss point we want to look at
gauss_point = int(sys.argv[1])
is_npy = int(sys.argv[2]) # user inputs 0 for csv files, 1 if saved as npy


# Assuming this script is called from the directory containing output data
if is_npy > 0:
    populations = np.load('populations.npy')
    active_stress = np.load('active_stress.npy')
    overlap = np.load('overlap.npy')
    hsl = np.load('hsl.npy')
else:
    populations = pd.read_csv('populations.csv',delimiter=',')
    populations = populations.to_numpy()
    populations = populations[:,1:] # get rid of first column
    np.save("populations",populations)
    #populations = np.load('populations.npy')

    #populations = populations[0:6569212]

    active_stress = pd.read_csv('active_stress.csv',delimiter=',')
    active_stress = active_stress.to_numpy()
    active_stress = active_stress[:,1:]
    active_stress = active_stress[:,gauss_point]
    np.save("active_stress",active_stress)

    overlap = pd.read_csv('overlap.csv',delimiter=',')
    overlap = overlap.to_numpy()
    overlap = overlap[:,1:]
    overlap = overlap[:,gauss_point]
    np.save("overlap",overlap)

    hsl = pd.read_csv('half_sarcomere_lengths.csv',delimiter=',')
    hsl = hsl.to_numpy()
    hsl = hsl[:,1:]
    hsl = hsl[:,gauss_point]
    np.save("hsl",hsl)

#data_range = np.shape(active_stress)[0]
data_range = 1500
t = np.load('time.npy')
#t = t[:-1]
#t = t[0:1301]

print "shape of pops", np.shape(populations)
# Again, hard coding this
bins = np.linspace(-10,10,21)
num_bins = 21
#num_int_points = np.shape(populations)[0]/(np.shape(t)[0])
num_int_points = 6648
#t = t[:-1]
t=t[0:data_range]
print "number of integration points:",num_int_points


# Start parsing out the populations, hard coded for 4 state
SRX = np.zeros(data_range)
DRX = np.zeros(data_range)
wb_cb = np.zeros((data_range,num_bins))
fg_cb = np.zeros((data_range,num_bins))
a1_bound = np.zeros(data_range)
a2_bound = np.zeros(data_range)
n_on = np.zeros(data_range)
n_off = np.zeros(data_range)

max_nbound = 0.0

for i in np.arange(data_range-1):


    SRX[i] = populations[i*num_int_points+gauss_point,0]
    DRX[i] = populations[i*num_int_points+gauss_point,1]
    a1_bound[i] = np.sum(populations[i*num_int_points+gauss_point,2:(2+num_bins)])
    wb_cb[i,:] = populations[i*num_int_points+gauss_point,2:(2+num_bins)]
    a2_bound[i] = np.sum(populations[i*num_int_points+gauss_point,(2+num_bins):(2+2*num_bins)])
    fg_cb[i,:] = populations[i*num_int_points+gauss_point,(2+num_bins):(2+2*num_bins)]
    n_on[i] = populations[i*num_int_points+gauss_point,-1]
    n_off[i] = populations[i*num_int_points+gauss_point,-2]
    if np.amax(wb_cb[i,:]) > max_nbound:
        max_nbound = np.amax(wb_cb[i,:])
    if np.amax(fg_cb[i,:]) > max_nbound:
        max_nbound = np.amax(fg_cb[i,:])
    else:
        max_nbound = max_nbound


fig = plt.figure(figsize=(16,9),dpi=144)
# testing plot
ax1 = plt.subplot(321)
srx_plot, = plt.plot(t,SRX)
drx_plot, = plt.plot(t,DRX)
a1bound_plot, = plt.plot(t,a1_bound)
a2bound_plot, = plt.plot(t,a2_bound)
#sum_plot, = plt.plot(t,SRX+DRX+a1_bound+a2_bound)
plt.legend([srx_plot,drx_plot,a1bound_plot,a2bound_plot], ['M_SRX', 'M_DRX', 'M_WB','M_FG'])

ax2 = plt.subplot(322)
ax2.plot(t,active_stress[0:data_range])
ax2.set_ylabel('Active Stress (Pa)')
#ax2.ylabel('Active Stress (Pa)')

ax4 = plt.subplot(323)
ax4.plot(t,hsl[0:data_range])
ax4.set_ylabel('hsl (nm)')
#ax4.ylabel('hsl (nm)')

ax5 = plt.subplot(325)
ax5.plot(t,n_on)
ax5.plot(t,n_off)
ax5.plot(t,n_on+n_off)
ax5.plot(t,a2_bound,color='#d62728')
ax5.set_ylabel('thin filament + FG state')
#ax5.ylabel('thin filament + FG state')

ax6 = plt.subplot(326)
ax6.plot(t,overlap[0:data_range])
ax6.set_ylabel('overlap')
#ax6.ylabel('overlap')

# Trying to animate cross-bridges from a1 and a2-------------------------------

ax3 = plt.subplot(324,xlim=(bins[0]-1,bins[-1]+1),ylim=(0.00,1.1*np.amax(max_nbound)))
#y_label = 'M_FG(x)                       \n (Proportion)                   '
#y_coord = get_y_label_y_coord(y_label)
#ax1.set_ylabel(y_label, fontsize = font_size, rotation=0,y=y_coord)

#y_ticks = get_yticks(y_bound)

#ax1.set_xlabel('Working Cross-bridge \n Range \n (nm)', fontsize = font_size)

#right_side1 = ax1.spines["right"]
#bottom1 = ax1.spines["bottom"]
#top1 = ax1.spines["top"]
#right_side1.set_visible(False)

#top1.set_visible(False)

line1, = ax3.plot([],[],lw=4,color='#2ca02c')
line2, = ax3.plot([],[],lw=4,color='#d62728')
#line3, = ax3.plot([],[],lw=4,color=red)
line = [line1, line2]

def init():
    line[0].set_data([],[])
    line[1].set_data([],[])
    return line

t, m, m2 = [], [], []
y1 = np.zeros(np.shape(bins))
y2 = np.zeros(np.shape(bins))
def animate(i):

    #if csv_flag:
    #    y = fenics_pop_data[i*num_int_points+gauss_point,2:array_length-2]
    #else:
    #    y = fenics_pop_data[i,num_int_points+gauss_point,2:array_length-2]
    y1 = wb_cb[i,:]
    y2 = fg_cb[i,:]
    #if single_cell_sim_flag > 0:
    #    m.append(HSL[i])
    #    m2.append(stress_array[i])
    #else:
    #    m.append(HSL[i,gauss_point])
    #    m2.append(stress_array[i,gauss_point])
    #t.append(tarray[i])
    #print "time = " + str(t[i])
    line[0].set_data(bins,y1)
    line[1].set_data(bins,y2)
    #line[2].set_data(t,m2)
    return line



anim = FuncAnimation(fig, animate, init_func=init, frames = data_range-1, interval = 50, blit=True,save_count=200)

#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
#plt.figure()

#plt.subplots_adjust(left=.175,right=.95,wspace=0.5)
#plt.plot(HSL)
#plt.switch_backend('Qt4Agg')
#mng=plt.get_current_fig_manager()
#mng.window.showMaximized()

#mng.show()
#print(anim.to_html5_video())
anim.save('test.mp4','ffmpeg',15)
#anim.to_html5_video('test_animation')
plt.show()
