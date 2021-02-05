---
title: Two Compartment Calcium Model
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 1
---
Two Compartment Calcium
-----------------------
Let y be a vector of length 2 such that y[0] represents intracellular calcium that binds to the thin filament, and y[1] represents sarcoplasmic reticulum calcium. Then the rate of change of calcium between these two compartments can be described by the following system of ODEs:  

<sup>dy[0]</sup>&frasl;<sub>dt</sub> = (k<sub>leak</sub> + activation*k<sub>act</sub>) * y[1] - k<sub>serca</sub> * y[0]  

<sup>dy[1]</sup>&frasl;<sub>dt</sub> = -dy[0]
