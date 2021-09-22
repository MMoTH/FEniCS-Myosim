---
title: Fiber Efficiency Disarray
parent: Demos
grand_parent: Getting Started
nav_order: 6
---

Summary
-------
A muscle fiber twitch simulation in which a prescribed traction is applied to the fiber's end once the fiber's active stress is high enough to exceed it. A cylinder geometry in which the ends represent non-contracting, fibrous tissue with a nonlinear stiffness and the quadrature points represent contracting myofibrils. Unit vectors at each quadrature point representing myofibril orientation are drawn from a normal distribution. The instruction file is included in the repository, and can be downloaded <a href="https://github.com/MMoTH/FEniCS-Myosim/blob/master/demos/fiber_efficiency_disarray_demo/fiber_loaded_shortening_disarray_10pct_afterload_demo.json">here</a>. This simulation is part of the manuscript in preparation "Myofibril Disarray Leads to Inefficiency, Quicker Relaxation in Contraction in Finite Element Simulations of Skeletal Muscle Fibers". It is recommended to run this demo with substantial computational resources.

Simulation Protocol
-------------------
The right face of the fiber is displaced 5% over 10 ms to induce a resting tension. This displacement is maintained for the duration of the simulation to keep the fiber length fixed. A calcium concentration of 1e-7 M is maintained to allow the cross-bridges to reach steady state. At t = 300 ms, the myofibrils are activated with a skeletal muscle calcium transient approximation[^1] using the [two-compartment calcium](../../../model_formulations/calcium_models/two_compartment_model/two_compartment_model.md) model. Contraction occurs against the compliant tissue at either end. The contractile parameters are tuned to match twitch stress data from literature[^2]. In this demo, the prescribed traction is 10% of the peak stress generated in the fiber isometric twitch demo. Once the combination of the active and passive stress exceeds the desired traction value, the displacement boundary condition is removed and the traction applied at the right face. This allows the fiber to shorten to maintain equilibrium. Shortening continues until equilibrium cannot be  maintained via active contraction, at which point a displacement boundary condition preserving the shortest length is enforced.

Boundary Conditions & Assumptions
---------------------------------
- Left face displacement is fixed in the x-direction.
- Nodes on the left face on the y and z-axes are constrained to remain on those axes to prevent rigid body rotation and translation
- Right face displacement is prescribed to give the desired magnitude of stretch until the traction is applied.
- The material is incompressible.
- All myofibril active stress is generated along the myofibril direction (no cross-myofibril contraction).

Results
-------
The deformation as viewed in Paraview:

<video width="800" height="500" controls>
  <source src="shortening_animation.mp4" type="video/mp4">
</video>

For traction values of 10%-90% of the peak stress of the aligned fiber, force and length traces are shown below:
![List of containers](rep_aligned_traces.png)


[^1]: Gonzalez, E., Messi, M. L., & Delbono, O. (2000). The specific force of single intact extensor digitorum longus and soleus mouse muscle fibers declines with aging. J Membr Biol, 178(3), 175-183. doi:10.1007/s002320010025

[^2]: Baylor, S. M., & Hollingworth, S. (2003). Sarcoplasmic reticulum calcium release compared in slow-twitch and fast-twitch fibres of mouse muscle. J Physiol, 551(Pt 1), 125-138. doi:10.1113/jphysiol.2003.041608
