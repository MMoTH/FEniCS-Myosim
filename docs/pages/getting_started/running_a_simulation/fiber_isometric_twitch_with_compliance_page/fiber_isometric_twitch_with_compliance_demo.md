---
title: Fiber Isometric Twitch With Compliance
parent: Demos
grand_parent: Getting Started
nav_order: 3
---

Summary
-------
A muscle fiber twitch simulation with fixed fiber length. A cylinder geometry in which the ends represent non-contracting, fibrous tissue with a nonlinear stiffness and the quadrature points represent contracting myofibrils.  

Simulation Protocol
-------------------
The right end of the fiber is displaced to the right 14% over 5 ms to induce a passive stress response. This stretch is maintained for 10 ms at a calcium concentration of 1e-7 M to allow the cross-bridges to reach steady state. Then the cell is activated with a skeletal muscle calcium transient approximation[^1] using the [two-compartment calcium](../../../model_formulations/calcium_models/two_compartment_model/two_compartment_model.md) model, and stretch held fixed, allowing the myofibrils to contract against the compliance at either end. The contractile parameters are tuned to match twitch stress data from literature[^2].

Boundary Conditions & Assumptions
---------------------------------
- Left face displacement is fixed in the x-direction.
- Notes on the left fact on the y and z-axes are constrained to remain on those axes to prevent rigid body rotation and translation
- Right face displacement is prescribed to give the desired magnitude of stretch.
- The material is incompressible.
- All myofibril active stress is along the long-axis.

Results
-------
*(update with final contraction parameters when paper is submitted)*  
A representative myofibril result plot obtained from k_plotter_npy.py:  
* Insert plots

The mesh deformation, color coded to indicate magnitude of active-stress:  


The stress on the right face (reaction force in the x-direction resolved over the reference area of the right face):  


[^1]: Gonzalez, E., Messi, M. L., & Delbono, O. (2000). The specific force of single intact extensor digitorum longus and soleus mouse muscle fibers declines with aging. J Membr Biol, 178(3), 175-183. doi:10.1007/s002320010025

[^2]: Baylor, S. M., & Hollingworth, S. (2003). Sarcoplasmic reticulum calcium release compared in slow-twitch and fast-twitch fibres of mouse muscle. J Physiol, 551(Pt 1), 125-138. doi:10.1113/jphysiol.2003.041608
