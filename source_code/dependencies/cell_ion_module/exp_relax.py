import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1,1000,1000)
ca_values =np.zeros(np.shape(t))
C = 0.0
A1 = 72.0
A2 = 28.0
t1 = 18.3
t2 = 742.2

for i in np.arange(np.shape(t)[0]):
    ca_values[i] = C + A1*np.exp((-t[i]/t1))+A2*np.exp((-t[i]/t2))
    if ca_values[i] <51 and ca_values[i]>49:
        counter = i
print t[counter]

plt.plot(t,ca_values)
plt.show()
