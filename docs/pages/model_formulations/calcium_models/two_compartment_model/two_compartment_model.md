---
title: Two Compartment Calcium Model
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 1
---
Two Compartment Calcium
-----------------------
Let [Ca<sup>2+</sup>]<sup>i</sup> represent calcium in the cytoplasm that binds to the thin filament, and [Ca<sup>+2</sup>]<sup>o</sup> representrepresents sarcoplasmic reticulum calcium. Then the rate of change of calcium between these two compartments can be described by the following system of ODEs:  

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/calcium_models/two_compartment_model/ca_1_eqn.jpeg?raw=true" align="center" border="0"  width="369" height="39" />

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/calcium_models/two_compartment_model/ca_2_eqn.png?raw=true" align="center" border="0"  width="162" height="39" />

k<sub>leak</sub>: The rate of constant flow of calcium from the sarcoplasmic reticulum to the cytoplasm.  
act: Either 1 or 0 representing status of muscle activation.  
k<sub>act</sub>: The rate at which calcium enters the cytoplasm due to activation.  
k<sub>serca</sub>: The rate at which the serca pump removes calcium from the cytoplasm.  
