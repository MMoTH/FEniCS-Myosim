---
title: Finite Elements, Functions and Function Spaces
parent: FEniCS Tutorials
grand_parent: Getting Started
nav_order: 1
---

These tutorials will utilize Ipython within the Docker container. Ipython is a command line program that allows for real time execution of python code and is very useful for prototyping. Ipython will allow users to closely look at and experiment with FEniCS code. UFL documentation can be found (here)[https://readthedocs.org/projects/fenics-ufl/downloads/pdf/stable/]. See p.5 - 9 for discussions about finite elements.

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

More concretely, *T* gives us the discretization of our domain, *V* is the function space we use to approximate the solution on each of the subdomains (elements), and *L* is the evaluation of V on the nodes. Creating the unit cube mesh above, we have discretized our domain using tetrahedrons. To form a full finite element, we need to decide on a function space to approximate our solution. Let's start by considering a scalar quantity (say temperature) that we want to approximate as varying linearly within an element, and we want it to be continuous between elements. For this, we would use continuous Lagrange, linear polynomials. To create this type of basic finite element, we use:  
```
Q_elem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme = "default")
```

Where "CG" stands for "Continuous Galerkin" (continuous between elements), "mesh.ufl_cell()" returns "tetrahedron", and "1" is the order of the polynomial (linear). With a tetrahedral geometry using linear polynomials, our degrees of freedom is the evaluation of the polynomials at the four vertices of the tetrahedron.  

 For our problem, we are trying to solve for displacement (a vector quantity) that we assume varies quadratically within an element. For this, we will use the quadratic Lagrange polynomials, and the shortcut command "VectorElement" which is technically a mixed element where all elements are equal:

```
V_elem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme = "default")
```

This is equivalent to declaring a basic quadratic CG element, and using it to declare a mixed element (we will see mixed elements later in our code):
```
Q_elem2 = FiniteElement("CG", mesh.ufl_cell(), 2, quad_scheme = "default")
V_elem2 = Q_elem2 * Q_elem2 * Q_elem2
```


Defining the finite element gives a description of how the solution will be approximated *locally*, and then using the finite element and mesh we construct a global finite element function space:

```
Q_fcn_space = FunctionSpace(mesh,Q_elem)
V_fcn_space = FunctionSpace(mesh,V_elem)
```

With a basis defined and the function space created, we can interpolate to get values anywhere within out geometry.

A quick note: The other type of element we use is called a "Quadrature Element". This element is used to obtain values ONLY AT THE ELEMENT QUADRATURE POINTS. In other words, you cannot interpolate using this element to get values at other coordinates. To do that, a projection must be done to a function space using one of the standard elements. MyoSim is solved using a quadrature element.

We can now define functions that belong to these finite element function spaces. Functions are useful to store the information we solve for along the way. For example, let's create a function that is meant to hold our displacement solution:  
```
u = Function(V_fcn_space)
```
u is a FEniCS object, not just an array of numbers. If we want to view the array of function values, or store a copy of the function values, we can do  
```
u.vector().array()
temp_u = u.vector().array()
```
We could also use the "get_local()" method, which gets the function values on the local process if things are being executed in parallel  
```
u.vector().get_local()
```
Let's just do a quick sanity check to verify the number of elements of our temp_u array. The function u belongs to a vector function space in our three dimensional mesh. Thus, for each node there should be three components (x, y, and z). We are using a basic unit cube mesh with refinement one, and quadratic tets. Thus there is a node at each vertex of a tetrahedron, and also at each midpoint. This leads to 27 nodes, each with 3 components, thus 81 elements in our temp_u array.
```
np.shape(u.vector().array())
```
produces the output  
```
Out[45]: (81,)
```
Now we can see function values, but for them to be useful we need a mapping between the indices of temp_u, and the coordinates of our mesh. Let's create that mapping:
```
gdim = mesh.geometry().dim() # get the dimension of our mesh. Will take on value of 3 for 3-dimensional mesh
V_dofmap = V_fcn_space.tabulate_dof_coordinates().reshape((-1,gdim)) # mapping comes from the function space
Q_dofmap = Q_fcn_space.tabulate_dof_coordinates().reshape((-1,gdim)) # Q is scalar function space, using only tet vertices
V_dofmap
Q_dofmap
np.shape(Q_dofmap)
```
Notice the shape of Q_dofmap is (8,3). Since it's a scalar function space using linear tets, there should only be one value at each vertex (the four corners of the cube). Indeed, looking at Q_dofmap, it's a list of the coordinates representing the corners of the cube.

##Assigning Function Values
