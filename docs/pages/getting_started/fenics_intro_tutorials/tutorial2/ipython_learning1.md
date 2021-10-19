---
parent: FEniCS Tutorials
title: FEniCS Tutorials1
nav_order: 2
---

- Open Docker
- Start container
- Enter container

This should bring you to the command line within the docker container that has the necessary files/environment to run fenics. Navigate to the shared folder:

```
cd shared/
````

Create some directory where we can save stuff to view in paraview:

```
mkdir ipython_temp
```

IMPORTANT: This folder is now in the same location housing the repository. This directory should be added to the .gitignore file or deleted before any commits.  

Now we can fire up ipython and get started with FEniCS.  

```
ipython
```

Let's import dolfin

```
from dolfin import *
import numpy as np
```

In general, our goal is to solve for the displacement at each time step that satisfies the balance of linear momentum. To do this, in general we need to do the following:  
- Discretize our domain
- Describe the finite elements we want to use to solve our problem
- Describe the weak form we are trying to solve (and specify boundary conditions that aren't in the weak form. Remember, traction boundary conditions show up in the weak form, essential (displacement) boundary conditions are specified).
- Solve and update relevant quantities.

Typing dolfin. and then using tab for autocomplete will show ALL of the functions we have for dolfin. Let's start by creating a couple of basic unit cube meshes:  

```
mesh1 = UnitCubeMesh(1,1,1)
mesh2 = UnitCubeMesh(10,10,10)
```

Let's save these meshes to view in Paraview:

```
File('mesh1.pvd') << mesh1
File('mesh2.pvd') << mesh2
```

Load these into ParaView and visualize with "Surface with Edges" to see the difference between these two meshes.

Now to do anything interesting with these, we need to define what type of finite elements we want to use. First, consider the definition of a finite element (Ciarlet 1975):  

*"A finite element is a triple (T, V, L), where:
       - T is a closed, bounded subset of R^d with nonempty interior
         and piecewise smooth boundary.
       - V = V(T) is a finite dimensional function space on T of dimension n
       - L is the set of degrees of freedom (nodes) L = {l1,l2,...,ln} and
         is a basis for the dual space V' (space of bounded linear functionals
         on V)"*

More concretely, *T* gives us the discretization of our domain, *V* is the function space we use to approximate the solution on each of the subdomains (elements), and *L* is the evaluation of V on the nodes. Creating the unit cube mesh above, we have discretized our domain (a cube) using tetrahedron elements. Now let's create a full finite element.

```
Q_elem = FiniteElement("CG", mesh1.ufl_cell(), 1, quad_scheme = "default")
```

This creates a finite element over the tetrahedron geometry (given by mesh.ufl_cell()) using continuous lagrange ("CG") polynomials of order 1. You can easily increase the order of the polynomials by changing the third argument, or change from continuous to discontinuous by switching from "CG" to "DG". If we want to represent vector quantities, we can create a vector element similarly:  

```
V_elem = VectorElement("CG", mesh1.ufl_cell(), 2, quad_scheme = "default")
```
Outputting these items yields
```
In [7]: Q_elem
Out[7]: FiniteElement('Lagrange', tetrahedron, 1, quad_scheme='default')

In [8]: V_elem
Out[8]: VectorElement(FiniteElement('Lagrange', tetrahedron, 2, quad_scheme='default'), dim=3)

From these finite elements, we can now construct a global function space on our mesh.
```
It's encouraged to play around with the things we create to view their properties and shapes to get more familiar with them.

Okay, so we've defined types of finite elements we want to use. Now we want to construct global function spaces for our specific geometry:

```
Q_fcn_space = FunctionSpace(mesh1,Q_elem)
V_fcn_space = FunctionSpace(mesh1,V_elem)
```

Because these are typical elements, you can actually skip the formal creation of the finite element and go straight to forming a function space or vector function space. The previous two lines are equivalent to
```
Q_fcn_space = FunctionSpace(mesh1,"CG",1)
V_fcn_space = VectorFunctionSpace(mesh1,"CG",2)
```
However, you cannot skip the element creation and use the FunctionSpace command to create a vector function space.

Keep in mind these functions are global. In mesh1, for quadrate tetrahedrons, there are 27 nodes (one at each vertex, one at each midpoint). For a vector element, we expect each node to have 3 components. For a scalar element, each node has just one element. The first two functions are equivalent, the third is not.

We can assign values to this function, or use it to hold our solution for something like displacement.

However, or MyoSim, we evaluate the contraction model at integration points within the element. This I believe is necessary because we aren't dealing with something nice like linear elasticity where the stress is just a function of the displacement gradient. To do so, we need to create what is called a quadrature element, rather than using one of the standard Lagrange elements:

```
Quadelem = FiniteElement("Quadrature",mesh1.ufl_cell(), 2, quad_scheme = "default")
```

Since the active stress is directed along the fiber direction, we need vectors at these integration points to tell us what that direction is. Let's create a vector quadrature element:

```
VQuadelem = VectorElement("Quadrature", mesh1.ufl_cell(), degree=deg, quad_scheme="default")
```
Now, create our global function spaces using these elements:
```
Quad = FunctionSpace(mesh1, Quadelem)
fiberFS = FunctionSpace(mesh1, VQuadelem)
```

These are useful because now we can calculate/assign things like half-sarcomere lengths (a scalar value) using the Quad function space or fiber orientation using a vector function on the fiberFS.

This hopefully gives an idea about some of the initialization that goes on in FEniCS. Next we need to talk about FEniCS expressions, then down the line we will talk about boundary conditions test and trial functions, creating the weak form, and appropriately updating results.

Let's create a function "hsl" to hold half-sarcomere lengths at the nodes. For now, we are going to ignore quadrature elements and work with standard Lagrange elements.

```
hsl = Function(Q_fcn_space)
```
Let's check that the dimensions of this function make sense:
```
np.shape(hsl.vector().array())
Out[45]: (8,)
```
Since the Q_fcn_space was constructed using a **linear** finite element, we should expect a scalar value at each node (8 nodes in the cube).

Function assign vs. just getting copies of the  values
Assign function value based on a FEniCS expression


- Create element
- Create FunctionSpace using a finite element.
- Create expressions, project onto functionspace

Displacements are solved for at the nodes, but (in general?) strains and stresses are solved for at integration points within the element and interpolated out to the nodes. Integration points are going to be used in the solving of the weak form (it's an integral). These integration points are different from the nodes, so I'm curious if we need to talk about integration points in the weak form because we are dealing with stresses. Investigate this.
