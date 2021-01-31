---
permalink: /model_development/notes/
title: "Notes"
---
Going to keep track of things I learn through the development of mmoth-vent here.  

## Fiber Orientation Vectors
Fiber, sheet, and sheet-normal orientation vectors are orthogonal and form a local coordinate system within the elements. These are created within the python script ```LVTest.py```. The fibers that are created here and stored within the hdf5 file are normalized. Upon reading these in within ```fenics_LV.py```, Dr. Lee has shown that these fibers are indeed normalized at the Gauss points. However, if the vectors are projected onto the mesh (i.e. onto the nodal coordinates), they are not guaranteed to be normalized, and likely will not be. It is recommended that the vectors are not projected onto a VectorFunctionSpace.  

## Building an Ellipsoidal Mesh

*To be included in the mesh generation page?*
The building of patient-specific meshes includes generating .stl files that contain the endo and epicardial surfaces. However, these don't exist for the simple ellipsoidal mesh. Within the vtk_py directory, there is the python script ```create_ellipsoidalal_LV.py```. I have slightly modified it to include a function call at the bottom to execute the code. The input `meshsize` controls the refinement of the mesh. To generate the ```ellipsoidal_refined.hdf5``` mesh, a meshsize of 0.1 was used. Once this script is ran, the ```LV_Test.py``` can be executed, making sure the casename matches the files generated from the ellipsoidal script.

## Boundary Conditions
Still trying to sort this out. Base is constrained to have zero displacement in longitudinal (z) direction. Sprint tractions on the epicardium do not work, for me gave weird rigid body rotations on a patient specific mesh. Dr. Lee's original boundary condition of constraining the mean x- and y displacements to be zero limited diastolic filling in the longitudinal direction. Now, radial expansion at the base is prescribed, but the expansion must be specified at each loading and time step.
