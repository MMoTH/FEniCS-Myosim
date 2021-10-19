---
title: Finite Elements, Functions and Function Spaces
parent: FEniCS Tutorials
grand_parent: Getting Started
nav_order: 1
---

These tutorials will utilize Ipython within the Docker container. Ipython is a command line program that allows for real time execution of python code and is very useful for prototyping. Ipython will allow users to closely look at and experiment with FEniCS code.

In general, the goal is to solve for the displacement at the nodes during each time step that satisfies the balance of linear momentum. To do this we need to do the following:  

- Discretize the domain
- Describe the finite elements we want to use to solve our problem
- Describe the weak form we are trying to solve (and specify boundary conditions that aren't in the weak form. Remember, traction boundary conditions show up in the weak form, essential (displacement) boundary conditions are specified).
- Solve and update relevant quantities.

First, let's get familiar with the different types of FEniCS objects. Open docker, start and enter the container (instructions to do so can be found [here](../../installation/installation.md#enter-container-command-line)). The file structure should be consistent. It is recommended to create a "working directory" within the repository so that it can be shared with the Docker container, but this directory should be added to your .gitignore file as to not clog the repository. Navigate to this directory and then execute the following:  
```
ipython
```

This should take you to the starting Ipython screen as seen below:  
<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/getting_started/fenics_intro_tutorials/tutorial1/ipython_start_screen.png?raw=true" width="800" height="500">

Now we can execute python code. Let's start with importing numpy and dolfin:
```
from dolfin import *
import numpy as np
```
Let's start with a basic built-in unit cube mesh provide by FEniCS:
```
mesh = UnitCubeMesh(1,1,1)
mesh2 = UnitCubeMesh(10,8,6)
```
where the inputs define the refinement in the x, y, and z-directions respectively. These meshes can be saved and viewed in Paraview:
```
File('mesh.pvd') << mesh
File('mesh2.pvd') << mesh2
```
Mesh 2 is shown below. Note the refinement in x, y, and z. The rest of this tutorial will use the coarse unit cube mesh.
<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/getting_started/fenics_intro_tutorials/tutorial1/mesh2.png?raw=true" width="800" height="500">
