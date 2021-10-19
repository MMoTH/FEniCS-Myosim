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

Now to do anything interesting with our mesh, we need to define what type of finite elements we want to use. First, consider the definition of a finite element (Ciarlet 1975):  

*"A finite element is a triple (T, V, L), where:  
       - T is a closed, bounded subset of R^d with nonempty interior
         and piecewise smooth boundary.  
       - V = V(T) is a finite dimensional function space on T of dimension n  
       - L is the set of degrees of freedom (nodes) L = {l1,l2,...,ln} and
         is a basis for the dual space V' (space of bounded linear functionals
         on V)"*

More concretely, *T* gives us the discretization of our domain, *V* is the function space we use to approximate the solution on each of the subdomains (elements), and *L* is the evaluation of V on the nodes. Creating the unit cube mesh above, we have discretized our domain using tetrahedrons. To form a full finite element, we need to decide on a function space to approximate our solution. Let's start by considering a scalar quantity (say temperature) that we want to approximate as varying linearly within an element, and we want it to be continuous between elements. For this, we would use continuous Lagrange, linear polynomials. To create this type of finite element, we use:  
```
Q_elem = FiniteElement("CG", mesh1.ufl_cell(), 1, quad_scheme = "default")
```

 For our problem, we are trying to solve for displacement (a vector quantity) that we assume varies quadratically within an element. For this, we will use the quadratic Lagrange polynomials:

```
V_elem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme = "default")
```

Here, we specify that we want a vector element ()
