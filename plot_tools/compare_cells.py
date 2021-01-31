import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-pastel')


# Comparing same cell in a mesh from two different simulations
bins = np.arange(-12,12.5,0.5)
gauss_point = 1000


# Define simulation directories
cell_1_directory = "/Users/charlesmann/Academic/UK/MMotH-Fenics-UK/working_directory_untracked/amir_test14_interp/test_14/"
cell_2_directory = "/Users/charlesmann/Academic/UK/MMotH-Fenics-UK/working_directory_untracked/082315/05_13_2020/ellipsoid_fibers_not_normalize_sameascpp/"
# Load in cell 1 info
cell1_calcium = np.load(cell_1_directory + "calcium.npy")
cell1_hslarray = np.load(cell_1_directory + "HSL.npy")
cell1_pstress = np.load(cell_1_directory + "pstress_array.npy")
cell1_astress = np.load(cell_1_directory + "stress_array.npy")
cell1_tarray = np.load(cell_1_directory + "tarray.npy")
cell1_populations = np.load(cell_1_directory + "dumped_populations.npy")

# Define array length for populations for sim 1
cell1_info = np.shape(cell1_populations)
cell1_timesteps = cell1_info[0]
array_length1 = cell1_info[2]
data_range_1 = np.shape(cell1_tarray)[0]

# Load in cell 2 info
cell2_calcium = np.load(cell_2_directory + "calcium.npy")
cell2_hslarray = np.load(cell_2_directory + "hslarray.npy")
#cell2_hslarray = np.load(cell_2_directory + "HSL.npy")
cell2_pstress = np.load(cell_2_directory + "pstress_array.npy")
cell2_astress = np.load(cell_2_directory + "strarray.npy")
#cell2_astress = np.load(cell_2_directory + "stress_array.npy")
cell2_tarray = np.load(cell_2_directory + "tarray.npy")
cell2_populations = np.load(cell_2_directory + "dumped_populations.npy")

# Define array length for populations for sim 2
cell2_info = np.shape(cell2_populations)
cell2_timesteps = cell2_info[0]
array_length2 = cell2_info[2]
data_range_2 = np.shape(cell2_tarray)[0]
print data_range_2

# Define cell 1 populations
cell1_MOFF = cell1_populations[:,gauss_point,0]
cell1_MON = cell1_populations[:,gauss_point,1]
cell1_MBOUND = np.zeros(data_range_1)
for i in range(data_range_1):
    cell1_MBOUND[i] = np.sum(cell1_populations[i,gauss_point,2:array_length1-3])
cell1_Non = cell1_populations[:,gauss_point,array_length1-1]

# Define cell 2 population
cell2_MOFF = cell2_populations[:,gauss_point,0]
cell2_MON = cell2_populations[:,gauss_point,1]
cell2_MBOUND = np.zeros(data_range_2)

for i in range(data_range_2):
    cell2_MBOUND[i] = np.sum(cell2_populations[i,gauss_point,2:array_length2-3])
cell2_Non = cell2_populations[:,gauss_point,array_length2-1]

fig = plt.figure()

plt.subplot(321)
cell1_HSL_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_hslarray[0:data_range_1,1:2],label="cell1 hsl",color="red")
cell2_HSL_plot, = plt.plot(cell2_tarray[0:data_range_1],cell2_hslarray[0:data_range_2,gauss_point],label="cell2 hsl",color="blue")
plt.subplot(322)
cell1_moff_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_MOFF[0:data_range_1],label='M_OFF',color="red")
cell1_mon_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_MON[0:data_range_1],label='M_ON',color="red",linestyle="dashed")
cell1_mbound_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_MBOUND[0:data_range_1],label='M_BOUND',color="red")

cell2_moff_plot, = plt.plot(cell2_tarray[0:data_range_1],cell2_MOFF[0:data_range_2],label='M_OFF',color="blue")
cell2_mon_plot, = plt.plot(cell2_tarray[0:data_range_1],cell2_MON[0:data_range_2],label='M_ON',color="blue",linestyle="dashed")
cell2_mbound_plot, = plt.plot(cell2_tarray[0:data_range_1],cell2_MBOUND[0:data_range_2],label='M_BOUND',color="blue")
plt.legend()

plt.subplot(323)
cell1_pstress_plot = plt.plot(cell1_tarray[0:data_range_1],cell1_pstress[0:data_range_1,gauss_point],label="cell 1 pstress",color="red")
cell2_pstress_plot = plt.plot(cell2_tarray[0:data_range_2],cell2_pstress[0:data_range_2,gauss_point],label="cell 2 pstress",color="blue")

plt.subplot(324)
cell1_mbound_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_MBOUND[0:data_range_1],label='M_BOUND',color="red")
cell1_non_plot, = plt.plot(cell1_tarray[0:data_range_1],cell1_Non[0:data_range_1],label="N_ON",color="red",linestyle="dashed")
cell2_mbound_plot, = plt.plot(cell2_tarray[0:data_range_1],cell2_MBOUND[0:data_range_2],label='M_BOUND',color="blue")
cell2_non_plot, = plt.plot(cell2_tarray[0:data_range_2],cell2_Non[0:data_range_2],label="N_ON",color="blue",linestyle="dashed")
plt.legend()
plt.subplot(325)
cell1_astress_plot = plt.plot(cell1_tarray[0:data_range_1],cell1_astress[0:data_range_1,gauss_point],label="cell 1 act_stress",color="red")
cell2_astress_plot = plt.plot(cell2_tarray[0:data_range_2],cell2_astress[0:data_range_2,gauss_point],label="cell 2 act_stress",color="blue")
plt.subplot(326)
cell1_calcium_plot = plt.plot(cell1_tarray[0:data_range_1],cell1_calcium[0:data_range_1,gauss_point],label="cell1 calcium",color="red")
cell2_calcium_plot = plt.plot(cell2_tarray[0:data_range_2],cell2_calcium[0:data_range_2,gauss_point],label="cell2 calcium",color="blue")
plt.show()
