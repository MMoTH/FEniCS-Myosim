---
permalink: /getting_started/running_demo/
title: "Running a Simulation"
---

Two demo instruction files are included for the user to test the installation and gain familiarity with functionality. Make sure Docker is running and enter the command line of your container by following the instructions at the bottom of the [previous page](/MMotH-Vent/getting_started/installation/#enter-container-command-line).

Navigate to ```/home/fenics/shared/demos/```, where you will see two directories:  
* ```single_cell_length_control_demo/```
* ```ellipsoidal_ventricle_demo/```

Enter the ```single_cell_length_control_demo/``` directory, which contains the instruction file ```singlecell_demo.json```. In general, the syntax to execute MMotH-Vent is
```
python [path to fenics_driver.py] [path to instruction file]
```
Therefore to execute this instruction file, use the following command:  

```
python ../../source_code/fenics_driver.py singlecell_demo.json
```

The default option in this instruction file is to save all of the output in the same directory in which MMotH-Vent is called. MMotH-Vent output a number of numpy arrays that contain cell-level information. The cell data at any gauss point can be plotted by executing
```
python [path to k_plotter] [gauss point]
```
Assuming the path hierarchy is unchanged from the master repository, after running the demo the MyoSim data can be visualized by
```
python /home/fenics/shared/plot_tools/k_plotter 0
```
which should yield the following plot:
<img src="https://github.com/mmoth-kurtis/MMotH-Vent/blob/master/docs/assets/images/Screen%20Shot%202020-07-01%20at%205.03.18%20PM.png?raw=true" alt="titlepage" width="800"/>  

Finally, the mesh and displacement solutions are saved as ParaView files. It is recommended to download Paraview to view these solutions.

<a href="/MMotH-Vent/getting_started/installation/" class="btn btn--primary"><< Installation</a>
<a href="/MMotH-Vent/getting_started/fenics_input_readme/" class="btn btn--primary">Creating Input Files >></a>
