---
title: Finite Elements, Functions and Function Spaces
parent: FEniCS Tutorials
grand_parent: Getting Started
nav_order: 1
---

In general, the goal is to solve for the displacement at the nodes during each time step that satisfies the balance of linear momentum. To do this we need to do the following:  

- Discretize our domain
- Describe the finite elements we want to use to solve our problem
- Describe the weak form we are trying to solve (and specify boundary conditions that aren't in the weak form. Remember, traction boundary conditions show up in the weak form, essential (displacement) boundary conditions are specified).
- Solve and update relevant quantities.

First, let's get familiar with the different types of FEniCS objects. Open docker, start and enter the container (instructions to do so can be found [here](../../installation/installation.md#enter-container-command-line)). The file structure should be consistent. It is recommended to create a "working directory" within the repository so that it can be shared with the Docker container, but this directory should be added to your .gitignore file as to not clog the repository. Navigate to this directory and then execute the following:  
```
ipython
```
