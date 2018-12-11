import numpy as np
import matplotlib.pyplot as plt

good = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\dumped_populations_good.npy')

bad = np.load('C:\\Users\\ani228\\Dropbox\\UK\\FEniCS\\test_2\\dumped_populations_bad.npy')

diff = good - bad

error = []
for i in range((np.shape(diff)[0])):
    error.append(np.sum(pow(diff[i,0,:],2)))
    
#print(max(error))
#plt.plot(np.arange(701),error)

diff_1 = bad[294,0,:] - good[294,0,:]

plt.plot(np.arange(52), diff_1,'r')


#plt.plot(np.arange(52), bad[294,0,:],'r')
#plt.plot(np.arange(52), good[294,0,:],'g')

plt.show()