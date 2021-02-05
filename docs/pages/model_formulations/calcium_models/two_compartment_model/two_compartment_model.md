---
title: Two Compartment Calcium Model
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 1
---
Two Compartment Calcium
-----------------------
Let y be a vector of length 2 such that y[0] represents calcium in the cytoplasm that binds to the thin filament, and y[1] represents sarcoplasmic reticulum calcium. Then the rate of change of calcium between these two compartments can be described by the following system of ODEs:  

<i><sup>dy[0]</sup>&frasl;<sub>dt</sub> = (k<sub>leak</sub> + (activation)k<sub>act</sub>)y[1] - k<sub>serca</sub>y[0]</i>   

<i><sup>dy[1]</sup>&frasl;<sub>dt</sub> = -dy[0]</i>  


k<sub>leak</sub>: The rate of constant flow of calcium from the sarcoplasmic reticulum to the cytoplasm.  
activation: Either 1 or 0 representing status of muscle activation.  
k<sub>act</sub>: The rate at which calcium enters the cytoplasm due to activation.  
k<sub>serca</sub>: The rate at which the serca pump removes calcium from the cytoplasm.  
