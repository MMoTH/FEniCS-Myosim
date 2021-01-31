---
title: Sarcomere Realignment
parent: Demos
grand_parent: Getting Started
nav_order: 8
---

Summary
-------
A unit cube mesh consisting of six tetrahedron elements is used to model a single muscle cell response.

Simulation Protocol
-------------------
The muscle cell is stretched xx% and activated with a skeletal muscle calcium transient approximation using the two-compartment calcium model.

Boundary Conditions & Assumptions
---------------------------------
- Left face displacement is fixed in the x-direction.
- Right face displacement is prescribed to give the desired magnitude of stretch.
- A single point on the left face is completely fixed to prevent rigid body translation.
- The edges on the ends are fixed in either y or z to allow expansion/compression due to incompressibility while keeping the cross-section area rectangular.

Results
-------
If plotted using the k_plotter.py file, the cell-level model results are below:

* Insert plots

And the cube deformation is seen in Paraview here:
