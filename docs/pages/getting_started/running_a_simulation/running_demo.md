---
title: Demos
parent: Getting Started
nav_order: 2
has_children: true
has_toc: false
---

MMotH-Vent relies on user-specified information in the form of instruction files. These instruction files use the JSON format and define dictionaries of information to be parsed. Note, the convention is for input values to be specified as elements of a list, e.g. "keyword": [value] rather than "keyword": value. This page gives an overview of the expected keywords of an instruction file and their options. Demos are provided to show some of the current simulations that can be performed.  

How to Run An Instruction File
------------------------------
Make sure Docker is running and enter the command line of your container by following the instructions at the bottom of the [previous page](../installation/installation.md#enter-container-command-line). Then navigate to the directory that contains the instruction file. In general, the syntax for running MMotH-Vent is:

```
python <path to fenics_driver.py> <path to instruction file>
```

Assuming the file structure is the default from the repository, an instruction file from its direction by executing the following:

```
python /home/fenics/shared/source_code/fenics_driver.py <name of instruction file>
```

Demos
-----
- [Cell Isometric Twitch](/cell_isometric_demo_page/single_cell_isometric_demo_page.md)
- [Cell Isotonic Twitch](/cell_isotonic_twitch_page/cell_isotonic_twitch_demo.md)
- [Fiber Isometric Twitch With Compliance](/fiber_isometric_twitch_with_compliance_page/fiber_isometric_twitch_with_compliance_demo.md)
- [Fiber Isotonic Twitch With Compliance](/fiber_isotonic_twitch_page/fiber_isotonic_twitch_demo.md)
- [Fiber Isometric Tetanus](/fiber_isometric_tetanus_page/fiber_isometric_tetanus_demo.md)
- [Ellipsoidal Ventricle](/ventricle_ellipsoid_page/ventricle_ellipsoid_demo.md)
- [Rat Ventricle](/ventricle_rat_page/ventricle_rat_demo.md)
- [Sarcomere Realignment](/fiber_realignment_page/fiber_realignment_demo.md)
- [Particle Swarm Optimization](/particle_swarm_page/particle_swarm_demo.md)

<a href="../installation/installation.html" class="btn btn--primary"><< Installation</a>
<a href="../creating_input_files/fenics_input_readme.html" class="btn btn--primary">Building a Mesh >></a>
