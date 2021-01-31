---
permalink: /getting_started/fenics_input_readme/
title: "Input Files"
---

<div class="notice--info">
  <h4>Message</h4>
  <p>This page is under  construction.</p>
</div>

This document explains each input in the "fenics_input.json" file. Terms in "" represent the parameter name, and terms in [] represent the possible values.
Note: All inputs must be in brackets [] (making it a Python list), as the code loads in the first value in the list. This was to be able to include units next to input values, and standardize input.  

## Structure for cell ion modules, notes from Kurtis
fenics_LV calls cell_ion_driver, which imports the generic module specified by the user. Cell_ion_drive.py accepts "params" defined by the user, including cell_ion_module name and a dictionary containing parameters needed for the module. Each calcium/cell ion module should now have an init function, that accepts "params". This init function should initialize a class, which is used to save things used at each timestep. This way, for example, the calcium lookup table provided in "file_input.py" doesn't have to be loaded each time, and the cell ion stuff doesn't need to be carried around in the fenics_LV file. The structure of a cell ion module should look like:

```python
import stuff

def init(params):
  #initialize class here
  model_class = name_of_class_below(params)
  return model_class

class name_of_class():
  def __init__(self,params):

    # params is the dictionary defined in the json input file "model_inputs"
    # initialize what is needed for the ion calculation, for example, an activation time
    # from the model inputs dictionary
    self.t_act = params["activation_time"]

  def calculate_concentrations(self,cycle,time,file):
    # fenics_LV currently gives this function the cardiac cycle number, simulation time,
    # and a file pointer to save the ion concentrations if needed

    # run your ion model here, for now it's just calcium
    generic_calcium_concentration = (something)+(something_else)*(a_third_something)
    return generic_calcium_concentration
```

## Simulation Parameters
**"sim_geometry"**: Choose between [single_cell], [sheet], or [ventricle].  
  +[single_cell]: Simulates a unit cube meant to represent a single half sarcomere.  
  +[sheet]: A 2D thin sheet of sarcomeres.  
  +[ventricle]: Full ventricle simulations. Can choose specific meshes or use ellipsoidal.  

**"sim_type"**: For the given geometry, choose what type of simulation.  

**Single Cell** | Description   
----------------|-------  
[isometric]:| Unit cube where length is fixed.
[ktr]:| Tension recovery experiment.  
[force]:| Unit cube where a given force boundary condition is enforced.  
[single_cell_custom]:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Allows for a combination of length and force controlled simulations. Also allows for length changes.  

Tissue Sheet | Description
-------------|---------------
[sheet]:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Place-holder for now. Will use this for fiber splay simulations or spiral dynamics.  

Left Ventricle | Description
---------------|--------------
[beat, "path/to/mesh"]:| Supply the (relative?) path to the desired mesh and it will "beat" for "sim_duration"  
[vena_cava_occlusion, "path/to/mesh"]:| Use the specified mesh and simulate a vena cava occlusion. Useful for calculating ESPVR.  

**"sim_duration":** Enter an **integer** time for the simulation in milliseconds.  

**"sim_timestep":** Time-step to be used in implicit finite element solver.  

## File Inputs
**"input_directory_path":** Specify the path to the inputs for the simulation. Do we need this? Is the path specified in the input file for the mesh? Don't even need to specify a mesh for single cell stuff.  

**"casename":** I think this is only needed to differentiate between the ellipsoidal case, and all patient specific meshes are "New Mesh" unless I modify the script that creates the mesh. That means the user has to know the casename for a mesh they are using, which may not always be the case.  

## Output Parameters  
**"output_path":** Specify path where the outputs of the simulation are to be saved.  

## Forms Parameters
**"passive_law":** Select one of the available passive tissue laws.  
* [guccione_transverse_isotropy]: Phenomenological model. See "". Must define C, bf, bt, bfs.  
    * [c]:  
    * [bf]:  
    * [bt]:  
    * [bfs]:  
* [semi_structural]: Separates out the myofiber passive stress from bulk response. Requires Guccione parameters AND c2, c3. See above and "Microstructure-based finite element model of left ventricle passive inflation" by Xi, et al.  
    * [c]:  
    * [c2]:  
    * [c3]:  
    * [bf]:  
    * [bt]:  
    * [bfs]:  
* [full_structural]: Plan to implement a fully structural model.
  "Kappa"

## MyoSim Parameters  
**"max_rate":** [5000,"s^-1"]  
**"temperature":** [288, "Kelvin"]  
**"cb_number_density":** [7.67e16, "number of cb's/m^2"]  
**"initial_hs_length":** [1000, "nm"]  

#### Myofilament Parameters  
  **"kinetic_scheme":** ["3state_with_SRX"]  
  **"num_states":** [3]  
  **"num_attached_states":** [1]  
  **"num_transitions":** [4]  
  **"cb_extensions":** [[0.0, 0.0, 4.75642], "power-stroke distance in nm"]  
  **"state_attached":** [[0, 0, 1]]  
  **"k_cb_multiplier":** [[1.0, 1.0, 1.0]]  
  **"k_cb_pos":** [0.001, "N*m^-1"]  
  **"k_cb_neg":** [0.001, "N*m^-1"]  
  **"alpha":**[1.0]  
  **"k_1":** [9.623166, "s^-1"]  
  **"k_force":** [1.96345e-4, "(N^-1)(m^2)"]  
  **"k_2":** [1000, "s^-1"]  
  **"k_3":** [5435.531288, "(nm^-1)(s^-1)"]  
  **"k_4_0":** [2543.864648, "s^-1"]  
  **"k_4_1":** [0.18911849, "nm^-4"]  
  **"k_cb":** [0.001, "N*m^-1"]  
  **"x_ps":** [4.75642, "nm"]  
  **"k_on":** [1.5291356e8, "(M^-1)(s^-1)"]  
  **"k_off":** [100, "s^-1"]  
  **"k_coop":** [6.38475]  
  **"bin_min":** [-12, "nm"]  
  **"bin_max":** [12, "nm"]  
  **"bin_width":** [0.5, "nm"]  
  **"filament_compliance_factor":** [0.5]  
  **"thick_filament_length":** [815, "nm"]  
  **"thin_filament_length":** [1120, "nm"]  
  **"bare_zone_length":** [80, "nm"]  
  **"k_falloff":** [0.0024]  
  **"passive_mode":** ["exponential"]  
  **"passive_exp_sigma":** [500]  
  **"passive_exp_L":** [80]  
  **"passive_l_slack":** [900, "nm"]  

## Electrophysiology Parameters  

#### Cell Ion Parameters  
  **"model":** Choose from ["three_state_calcium"], ... Include info about each model (as they become available, do this in a table?)
  **initial_calcium":** Set an initial calcium value.
  **path_to_calcium":** If another calcium transient needs to be loaded in. This should be deprecated, as you cannot control the time-step or even know there are enough calcium values to use.

#### Monodomain Parameters  

## Circulatory Parameters  

This code currently uses a 3 compartment Windkessel model. The three compartments are the left ventricle, arteries, and veins? The parameters needed for this model are listed below:  
  **"Cao":**  
  **"Cven":**  
  **"Vart0":**  
  **"Vven0":**  
  **"Rao":**  
  **"Rven":**  
  **"V_ven":**  
  **"V_art":**  
<a href="/MMotH-Vent/getting_started/running_demo/" class="btn btn--primary"><< Running a Simulation</a>
<a href="/MMotH-Vent/getting_started/mesh_generation_readme/" class="btn btn--primary">Building a Mesh >></a>
