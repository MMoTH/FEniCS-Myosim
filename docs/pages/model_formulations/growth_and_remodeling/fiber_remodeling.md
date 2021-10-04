---
title: Fiber Remodeling
parent: Model Formulations
nav_order: 2
has_children: false
---

The fiber reorientation law is based on Kroon's[^1] paper, but we wanted to investigate using a different stimulus. The end goal is to have a rerientation law that occurs at each timestep of the cardiac cycle. For the vector f<sub>0</sub> representing the reference fiber direction, the generic differential equation is  

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/growth_and_remodeling/fiber_law.png?raw=true" width="135" height="36">

where &Theta; represents the tensor that is the stimulus for remodeling. Preliminary simulations have investigated using the passive stress tensor, total stress tensor, and Green-Lagrangian strain tensor.
