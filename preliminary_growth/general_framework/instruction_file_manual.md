This is a markdown file that will explain the instruction files used for MyoFE. MyoFE uses JSON files to specify parameters for simulations. JSON files are read in as dictionaries into python. The convention in the code is that all parameters are in a list [], so that descriptions of the parameters can be included. This instruction file is for the file "MyoFE.py", and as such currently only works for cardiac mechanics simulations. The file "mmoth_vent.py" is required for unit cube and fiber simulations.

The instruction files are broken up into dictionaries that describe different parameters needed for a cardiac simulation. These dictionaries contain parameters that in turn may be dictionaries themselves. The convention used to described the parameters is:  
"Dictionary_Name": {
  "parameter1": [parameter1_type, parameter1_description],
  "parameter2": [parameter2_type, parameter2_description],
  ...
}
# Mandatory Structures  
"geometry": {
  "mesh_path": [string, "Parameter should be a string representing the path to the mesh to be loaded in"]
}

"protocol": {
  "cardiac_period": [scalar, "Total time for one cardiac cycle"],
  "termination_condition": [string, "see below description (1)"]
  "simulation_timestep": [scalar, "time step"],
  "initial_end_diastolic_volume": [scalar, "LV cavity end diastolic volume. Simulation loads the LV to this volume before turning on contraction and solving the circulatory system"],
  "reference_loading_steps": [integer, "number of loading steps for initial loading from reference volume to first end diastolic volume"]
}

"output_options": {
  "output_path": [string, "path to save output files"]
}



- 1) Choose one of the following termination conditions:
  - "simulation_end_time": Used for cardiac simulations without growth. Specify duration of simulation in ms as second option as a scalar, e.g.:
    "termination_condition": ["simulation_end_time",170]
  - "growth_convergence": Used for cardiac simulations with growth. Checks for convergence of pressure-volume loops between growth steps. Specify maximum number of growth cycles as second option as an integer in the case of non-convergence or prolonged simulations.
