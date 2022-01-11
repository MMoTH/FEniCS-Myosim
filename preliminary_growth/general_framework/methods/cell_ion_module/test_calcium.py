import numpy as np
import matplotlib.pyplot as plt
import cell_ion_driver
t = np.linspace(0.0,1000,2001)

params = {"model":["two_compartment"],"model_inputs":{"Ca_content":[1e-3],"k_leak":[0.008000800080008],"k_act":[1.4472186384349266],"k_serca":[250.0]}}
peak_ca = 18.5*1e-6
resting_ca = 1e-7
ca_total = 1e-7 + 1e-3
ks = params["model_inputs"]["k_serca"][0]
params["model_inputs"]["k_leak"][0] = (ks*resting_ca/(ca_total - resting_ca))*1.0
kact = (peak_ca*ks - (ks*resting_ca*(ca_total-peak_ca)/(ca_total-resting_ca)))/(ca_total-peak_ca)
params["model_inputs"]["k_act"][0] = kact*1.46
ca_class = cell_ion_driver.cell_ion_driver(params)
print "kleak = " +str(params["model_inputs"]["k_leak"][0])
print "kact = " +str(params["model_inputs"]["k_act"][0])

ca_class.activation = np.zeros(np.shape(t))
ca_class.activation[31:40]=1.0

for i in np.arange(50):
    ca_class.activation[80+20*i:80+(20*i+9)]=1.0
for i in np.arange(30):
    ca_class.activation[1000+15*i:1000+(15*i+9)]=1.0

ca_class.activation[1400:] = 1.

ca_value = np.zeros(np.shape(t)[0])
for i in np.arange(np.shape(t)[0]):
    ca_value[i] = ca_class.calculate_concentrations(0.5,i)


plt.plot(t[0:80],ca_value[0:80])
target_times = [36,39,45]
target_ca = [(18.5/2)*1e-6,18.5*1e-6,(18.5/2)*1e-6]
plt.plot(t[target_times],target_ca,marker="o",linestyle="none")
plt.show()
