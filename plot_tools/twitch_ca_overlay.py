import numpy as np
import matplotlib.pyplot as plt

original_stress = np.load('og_stress.npy')
original_stress = original_stress[0:701,0]
#stress_loaded = np.load('stress_array.npy')
stress_loaded = np.loadtxt('active_stress.csv',delimiter=',')
stress = stress_loaded[:,0]
#ca = np.load('calcium.npy')
#ca = ca[:,0]
#time=np.load('tarray.npy')
time = np.loadtxt('time.csv',delimiter=',')
print np.shape(time)

time=time[0,:]
t_target = [0,30,96,220]
f_target = [0,0,80000,40000]

fig, ax1 = plt.subplots(nrows=1,ncols=1)
ax1.plot(original_stress[0:594])
ax1.plot(stress[0:594])
ax1.plot(t_target,f_target,marker='o',linestyle='none')
"""ax2 = ax1.twinx()
color='tab:gray'
ax2.set_ylabel('calcium',color=color)
ax2.plot(time,ca,color=color)"""


plt.show()
