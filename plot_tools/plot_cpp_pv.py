import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy as np
plt.style.use('seaborn-pastel')

pv_file_input = sys.argv[1]
time, LV_pressure, LV_vol, calcium = np.loadtxt(pv_file_input, skiprows=0, unpack=True, usecols=(0,1,2,3))

fig, (ax1)  = plt.subplots(nrows=1,ncols=1)
ax1.plot(LV_vol,LV_pressure)
ax1.set_xlabel('Volume (mL)')
ax1.set_ylabel('Pressure (mmHg)')

plt.show()
