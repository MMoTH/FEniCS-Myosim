---
title: Cell Isotonic Twitch
parent: Demos
grand_parent: Getting Started
nav_order: 2
---

Summary
-------
A unit cube mesh consisting of six tetrahedral elements is used to model a single muscle cell tension response to a twitch calcium transient with an applied traction on the right face. The instruction file is included in the repository, and can be downloaded <a href="https://github.com/MMoTH/FEniCS-Myosim/blob/master/demos/cell_isotonic_demo/cell_traction_ramp_hold_demo.json">here</a>.

Simulation Protocol
-------------------
A traction is incrementally applied on the right face of the cube over the first 20 ms, reaching a maximum value of 10 kPa which is fixed for the remainder of the simulation. Then the cell is activated at t = 30 ms with a skeletal muscle calcium transient approximation[^1] using the [two-compartment calcium](../../../model_formulations/calcium_models/two_compartment_model/two_compartment_model.md) model, and stretch held fixed. Cross-bridge mechanics are simulated using a three-state kinetic scheme[^2].

Boundary Conditions & Assumptions
---------------------------------
- Left face displacement is fixed in the x-direction.
- Right face displacement is prescribed to give the desired magnitude of stretch.
- A single point on the left face is completely fixed to prevent rigid body translation.
- The edges on the ends along the y and z-axes are constrained to remain along that axis to allow expansion/compression due to incompressibility while keeping the cross-section area square and prevent rigid-body rotation.
- The passive response is modeled as transversely isotropic using a combination of the Guccione strain energy function[^3] and one representing the myofiber response[^4]. More information about the passive stress formulation can be found [here](https://mmoth.github.io/FEniCS-Myosim/pages/model_formulations/tissue_mechanics/tissue_mechanics.html).

Results
-------------------
If plotted using the k_plotter_npy.py file, the cell-level model results are below:

<video width="800" height="500" controls>
  <source src="test.mp4" type="video/mp4">
</video>

And the cube deformation is seen in Paraview here (some tips for this visualization are included in the [cell isometric demo](https://mmoth.github.io/FEniCS-Myosim/pages/getting_started/running_a_simulation/cell_isometric_demo_page/single_cell_isometric_demo_page.html)):
<video width="800" height="500" controls>
  <source src="deformation_animation.mp4" type="video/mp4">
</video>

Note, the "muscle" shortens while being activated such that the active stress contribution from cross-bridges and the passive stress response satisfies the traction boundary condition. As [Ca<sup>2+</sup>] decreases (and thus, active stress), the muscle cell is lengthened such that the passive stress response bears the majority of the traction boundary condition. Also note the cross-bridges (bottom left plot) are shifted away from x=0 with the length change. In fact, the rapid length change as active stress drops is responsible for pulling the myosin heads off of binding sites, further facilitating relaxation.


[^1]: Baylor, S. M., & Hollingworth, S. (2003). Sarcoplasmic reticulum calcium release compared in slow-twitch and fast-twitch fibres of mouse muscle. J Physiol, 551(Pt 1), 125-138. doi:10.1113/jphysiol.2003.041608
[^2]: Mann, C. K., Lee, L. C., Campbell, K. S., & Wenk, J. F. (2020). Force-dependent recruitment from myosin OFF-state increases end-systolic pressure-volume relationship in left ventricle. Biomechanics and modeling in mechanobiology, 19(6), 2683–2692. https://doi.org/10.1007/s10237-020-01331-6
[^3]: Guccione, J. M., McCulloch, A. D., & Waldman, L. K. (1991). Passive material properties of intact ventricular myocardium determined from a cylindrical model. Journal of biomechanical engineering, 113(1), 42–55. https://doi.org/10.1115/1.2894084
[^4]: Xi, C., Kassab, G. S., & Lee, L. C. (2019). Microstructure-based finite element model of left ventricle passive inflation. Acta biomaterialia, 90, 241–253. https://doi.org/10.1016/j.actbio.2019.04.016
