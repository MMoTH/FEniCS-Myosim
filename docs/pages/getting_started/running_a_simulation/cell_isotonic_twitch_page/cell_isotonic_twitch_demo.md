---
title: Cell Isotonic Twitch
parent: Demos
grand_parent: Getting Started
nav_order: 2
---

Summary
-------
A unit cube mesh consisting of six tetrahedron elements is used to model a single muscle cell response.

Simulation Protocol
-------------------
The muscle cell is stretched 5% over the first 10 time steps. Then the cell is activated with a skeletal muscle calcium transient approximation from (citation) using the [two-compartment calcium](../../../model_formulations/calcium_models/two_compartment_model/two_compartment_model.md) In the 12th time-step, a traction boundary condition of 50 kPa is applied for the remainder of the simulation.

Boundary Conditions & Assumptions
---------------------------------
- Left face displacement is fixed in the x-direction.
- Right face displacement is prescribed to give the desired magnitude of stretch for the first 10 time step, then switched to a traction boundary on this face of 50 kPa.
- A single point on the left face is completely fixed to prevent rigid body translation.
- The edges on the ends are fixed in either y or z to allow expansion/compression due to incompressibility while keeping the cross-section area rectangular.

Results
-------------------
If plotted using the k_plotter_npy.py file, the cell-level model results are below:

<video width="800" height="500" controls>
  <source src="cube_deformation_isotonic_twitch.m4v" type="video/mp4">
</video>

And the cube deformation is seen in Paraview here:
<video width="800" height="500" controls>
  <source src="cube_deformation_isotonic_twitch_paraview.m4v" type="video/mp4">
</video>

Note, "muscle" shortens while being activated such that the active stress contribution from cross-bridges satisfies the traction boundary condition. As [Ca<sup>2+</sup>] decreases (and thus, active stress), the muscle cell is lengthened such that the passive stress response bears the majority of the traction boundary condition. Also note the cross-bridges (bottom left plot) are shifted away from x=0 with the length change. In fact, the rapid length change as active stress drops is responsible for pulling the myosin heads off of binding sites, further facilitating relaxation.
