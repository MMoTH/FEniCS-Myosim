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

<img src="%3Cimg+src%3D%22http%3A%2F%2Fwww.sciweavers.org%2Ftex2img.php%3Feq%3D%255Cfrac%257Bd%255BCa%255E%257B2%252B%257D%255D%255E%257Bi%257D%257D%257Bdt%257D%2520%253D%2520%2528k_%257Bleak%257D%2520%252B%2520%2528act%2529k_%257Bact%257D%2529%255BCa%255E%257B2%252B%257D%255D%255E%257Bo%257D%2520-%2520k_%257Bserca%257D%255BCa%255E%257B2%252B%257D%255D%255E%257Bi%257D%2520%2520%250A%26bc%3DWhite%26fc%3DBlack%26im%3Djpg%26fs%3D12%26ff%3Dmathdesign%26edit%3D0%22+align%3D%22center%22+border%3D%220%22+alt%3D%22%5Cfrac%7Bd%5BCa%5E%7B2%2B%7D%5D%5E%7Bi%7D%7D%7Bdt%7D+%3D+%28k_%7Bleak%7D+%2B+%28act%29k_%7Bact%7D%29%5BCa%5E%7B2%2B%7D%5D%5E%7Bo%7D+-+k_%7Bserca%7D%5BCa%5E%7B2%2B%7D%5D%5E%7Bi%7D++%22+width%3D%22369%22+height%3D%2239%22+%2F%3E" align="center" border="0" alt="\frac{d[Ca^{2+}]^{i}}{dt} = (k_{leak} + (act)k_{act})[Ca^{2+}]^{o} - k_{serca}[Ca^{2+}]^{i}  " width="369" height="39" />

k<sub>leak</sub>: The rate of constant flow of calcium from the sarcoplasmic reticulum to the cytoplasm.  
activation: Either 1 or 0 representing status of muscle activation.  
k<sub>act</sub>: The rate at which calcium enters the cytoplasm due to activation.  
k<sub>serca</sub>: The rate at which the serca pump removes calcium from the cytoplasm.  
