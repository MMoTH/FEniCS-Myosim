import numpy as np
import matplotlib.pyplot as plt

stress_loaded = np.load('stress_array.npy')
stress = stress_loaded[0:701,0]
ca = np.load('calcium.npy')
ca = ca[:,0]
time=np.load('tarray.npy')


fig, (ax1,ax3) = plt.subplots(nrows=1,ncols=1)
ax1.plot(time[0:701],stress)
ax2 = ax1.twinx()
color='tab:gray'
ax2.set_ylabel('calcium',color=color)
ax2.plot(time,calcium,color=color)

ax3.plot(time,calcium)

plt.show()
