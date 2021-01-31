import numpy as np
import math
simulation_dir = '/Users/charlesmann/Academic/UK/MMotH-Fenics-UK/working_directory_untracked/082315/coarse/mouse_wk_params/input_fix_fibers/'
stress = np.load(simulation_dir + 'strarray.npy')
print np.shape(stress)
nan_vector = np.zeros(np.shape(stress))
checksum = 0
neg_check = 0
for i in range(0,341):
    for j in range(0,20174):
        nan_vector[i,j]=math.isnan(stress[i,j])
        checksum = checksum + nan_vector[i,j]
        if stress[i,j] < 0.0:
            neg_check = -1.0

print checksum
print neg_check
