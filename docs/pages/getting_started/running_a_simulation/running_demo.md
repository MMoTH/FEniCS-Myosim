---
title: Demos
parent: Getting Started
nav_order: 2
has_children: true
has_toc: false
---

MMotH-Vent relies on user-specified information in the form of instruction files. These instruction files use the JSON format and define dictionaries of information to be parsed. Note, the convention is for input values to be specified as elements of a list, e.g. "keyword": [value] rather than "keyword": value. Demos are provided to show some of the current simulations that can be performed. Instruction file found [here](https://github.com/MMoTH/FEniCS-Myosim/blob/master/demos/ellipsoid_lv_steady_state_demo/ellipsoid_ventricle_5beats_demo.json).

How to Run An Instruction File
------------------------------
Make sure Docker is running and enter the command line of your container by following the instructions at the bottom of the [previous page](../installation/installation.md#enter-container-command-line). Then navigate to the directory that contains the instruction file. In general, the syntax for executing the code is:

```
python <path to mmoth_vent.py> <path to instruction file>
```

Assuming the file structure is the default from the repository, an instruction file from its directory by executing the following:

```
python /home/fenics/shared/revised_structure_attempt/mmoth_vent.py <name of instruction file>
```

Note, some of the demos are still under construction.  

Demos  
-----
- [Cell Isometric Twitch](/cell_isometric_demo_page/single_cell_isometric_demo_page.md)
- [Cell Isotonic Twitch](/cell_isotonic_twitch_page/cell_isotonic_twitch_demo.md)
- [Fiber Isometric Twitch Aligned](/fiber_isometric_twitch_with_compliance_page/fiber_isometric_twitch_with_compliance_demo.md)
- [Fiber Isometric Twitch Disarray](/fiber_isometric_twitch_with_compliance_disarray/fiber_isometric_twitch_with_compliance_disarray_demo.md)
- [Fiber Efficiency Aligned](/fiber_efficiency_aligned/fiber_efficiency_aligned_demo.md)
- [Fiber Efficiency Disarray](/fiber_efficiency_disarray/fiber_efficiency_disarray_demo.md)
- [Ellipsoidal LV](/ventricle_ellipsoid_page/ventricle_ellipsoid_demo.md)


<a href="../installation/installation.html" class="btn btn--primary"><< Installation</a>
<a href="../building_a_mesh/mesh_generation_readme.html" class="btn btn--primary">Building a Mesh >></a>
