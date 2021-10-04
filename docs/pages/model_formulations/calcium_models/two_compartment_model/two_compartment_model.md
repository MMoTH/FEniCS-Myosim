---
title: Two Compartment Calcium Model
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 1
---
Two Compartment Calcium
-----------------------
Let y be a vector of length 2 such that y[0] represents calcium in the cytoplasm that binds to the thin filament, and y[1] represents sarcoplasmic reticulum calcium. Then the rate of change of calcium between these two compartments can be described by the following system of ODEs:  

<center><i><sup>dy[0]</sup>&frasl;<sub>dt</sub> = (k<sub>leak</sub> + (activation)k<sub>act</sub>)y[1] - k<sub>serca</sub>y[0]</i></center>  

<center><i><sup>dy[1]</sup>&frasl;<sub>dt</sub> = -dy[0]</i></center>  

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7Bd%5BCa%5E%7B2%2B%7D%5D%5E%7Bi%7D%7D%7Bdt%7D%20%3D%20%28k_%7Bleak%7D%20%2B%20%28act%29k_%7Bact%7D%29%5BCa%5E%7B2%2B%7D%5D%5E%7Bo%7D%20-%20k_%7Bserca%7D%5BCa%5E%7B2%2B%7D%5D%5E%7Bi%7D%20%20%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathdesign&edit=0" align="center" border="0" alt="\frac{d[Ca^{2+}]^{i}}{dt} = (k_{leak} + (act)k_{act})[Ca^{2+}]^{o} - k_{serca}[Ca^{2+}]^{i}  " width="369" height="39" />

k<sub>leak</sub>: The rate of constant flow of calcium from the sarcoplasmic reticulum to the cytoplasm.  
activation: Either 1 or 0 representing status of muscle activation.  
k<sub>act</sub>: The rate at which calcium enters the cytoplasm due to activation.  
k<sub>serca</sub>: The rate at which the serca pump removes calcium from the cytoplasm.  
