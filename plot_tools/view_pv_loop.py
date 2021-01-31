import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy as np
plt.style.use('seaborn-bright')

pv_file_input = sys.argv[1]
time, LV_pressure, arterial_pressure, venous_pressure, LV_vol, ven_vol, art_vol, calcium = np.loadtxt(pv_file_input, skiprows=0, unpack=True, usecols=(0,1,2,3,4,5,6,7))
#time, LV_pressure, LV_vol, ven_vol, art_vol = np.loadtxt(pv_file_input, skiprows=0, unpack=True, usecols=(0,1,2,3,4))


#time = data[:,0]
#pressure = data[:,1]
#volume = data[:2]
fig, (ax1, ax2, ax3)  = plt.subplots(nrows=3,ncols=1)
ax1.plot(LV_vol,LV_pressure)
ax1.set_xlabel('Volume (mL)')
ax1.set_ylabel('LV Pressure (mmHg)')

ax2.plot(time,LV_pressure,label='LV Pressure')
ax2.plot(time,arterial_pressure,label='Arterial Pressure')
ax2.plot(time,venous_pressure,label='Venous Pressure')

#ax2.legend()
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.175), shadow=True, ncol=3)

#ax2.set_xlabel('Time (ms)')
ax2.legend(loc='lower left')
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Pressure (mmHg)')
ax4 = ax2.twinx()
color= 'tab:gray'
ax4.set_ylabel('calcium',color=color)
ax4.plot(time,calcium,color=color)
ax4.tick_params(axis='y',labelcolor=color)

l1 = ax3.plot(time,LV_vol,label='LV Volume')
l3 = ax3.plot(time,art_vol,label='Arterial Volume')
l2 = ax3.plot(time,ven_vol,label='Venous Volume')

ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.175), shadow=True, ncol=3)

#l2 = ax3.plot(time,art_vol,label='Arterial Volume')
#l3 = ax3.plot(time,ven_vol,label='Venous Volume')
#ax3.legend((l1, l2, l3),('LV Volume','Venous Volume','Arterial Volume'))
#ax3.set_xlabel('Time (ms)')
ax3.set_ylabel('Volume (mL)')
#ax3.legend()
ax3.legend(loc='lower left')

fig.tight_layout(pad=0.5)
plt.show()
