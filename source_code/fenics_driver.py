import sys
sys.path.append("/home/fenics/shared/source_code/")
sys.path.append("/home/fenics/shared/source_code/fenics_cases")
import json
import os
import dependencies
import fenics_cases
import pso
from pso import pso_driver
from fenics_cases import fenics_singlecell_isometric
#from fenics_cases import fenics_LV
from dependencies import recode_dictionary
from dependencies import load_parameters
import numpy as np
import pandas as pd


def sim_driver(input_file_name):

    ## This is the simulation driver function.
    #
    # sim_driver is the function that is called when the user executes this script.
    # The high level parsing of the instruction file is done here, including
    # determining which fenics script to execute (single cell, full ventricle, etc.)
    # and saving the output of that script upon successful execution.
    #
    # Parameters
    # ----------
    # input_file_name: string
    #   JSON formatted input file. The structure of this file should follow that
    #   seen [here](https://mmoth-kurtis.github.io/MMotH-Fenics-UK/getting_started/fenics_input_readme/)

    # Check that the file exists, if not , exit.
    if not os.path.exists(input_file_name):
        print "input file does not exist"
        exit()

    # Load in JSON dictionary
    with open(input_file_name, 'r') as json_input:
      input_parameters = json.load(json_input)

    # Convert any unicode values to python strings so they work with some cpp libraries.
    recode_dictionary.recode(input_parameters)

    # Parse out the different types of parameters.
    sim_params = input_parameters["simulation_parameters"]
    file_inputs = input_parameters["file_inputs"]
    output_params = input_parameters["output_parameters"]
    passive_params = input_parameters["forms_parameters"]["passive_law_parameters"]
    hs_params = input_parameters["myosim_parameters"]
    cell_ion_params = input_parameters["electrophys_parameters"]["cell_ion_parameters"]
    monodomain_params = input_parameters["electrophys_parameters"]["monodomain_parameters"]
    windkessel_params = input_parameters["windkessel_parameters"]
    optimization_params = input_parameters["optimization_parameters"]

    # Assign input/output parameters.
    output_path = output_params["output_path"][0]
    #input_path = file_inputs["input_directory_path"][0]

    # This may only be needed in ventricle simulations.
    casename = file_inputs["casename"][0]

    # Check that the output path exists. If it does not, create it and let user know.
    if not os.path.exists(output_path):
        print "Output path does not exist. Creating it now"
        os.makedirs(output_path)

    # Figure out which script needs to be executed.
    if sim_params["sim_geometry"][0] == "ventricle":
        fenics_script = "fenics_LV"
    elif sim_params["sim_geometry"][0] == "alexus":
        fenics_script = "fenics_singlecell_cylinder_alexus"
    elif sim_params["sim_geometry"][0] == "ventricle_physloop":
        fenics_script = "fenics_LV_physPVloop"
    elif sim_params["sim_geometry"][0] == "single_cell":
        fenics_script = "fenics_singlecell_isometric"
    elif sim_params["sim_geometry"][0] == "single_cell_fiber":
        fenics_script = "fenics_singlecell_fiber_reorientation"
    elif sim_params["sim_geometry"][0] == "cylinder":
	fenics_script = "myosim_cylinder"
    elif sim_params["sim_geometry"][0] == "ellipsoid_set_hsl":
        fenics_script = "fenics_LV_physPVloop_forcehsl"
    elif sim_params["sim_geometry"][0] == "kroon":
        fenics_script = "fenics_isometric_kroon_kurtis"
    elif sim_params["sim_geometry"][0] == "kroon_alexus":
        fenics_script = "fenics_isometric_kroon_alexus"
    else:
        sys.exit("FEnICS cript does not exist. Please include an existing fenics script.")

    # Import the script as a module so inputs and outputs can be passed.
    script_name = __import__(fenics_script)

    # Call the "fenics" function within the script
    if optimization_params["num_variables"][0] > 0:
        final_inputs, opt_history = pso_driver.particle_swarm_optimization(optimization_params,sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,script_name)
        #print opt_history["best_global_error"]
        print final_inputs
        with open(output_path + 'opt_final_inputs.json', 'w') as fp2:
            json.dump([final_inputs, opt_history], fp2,indent=2, separators=(',', ': '))
            #json.dump(opt_history, fp2, indent=2, separators=(',', ': '))

    else:
        output_data = script_name.fenics(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,0)

    # Save the appropriate output information
    """output_data['calcium'][0].to_csv(output_path + 'gauss_calcium.csv')
    output_data['active_stress'][0].to_csv(output_path + 'gauss_active_stress.csv')
    output_data['myofiber_passive_stress'][0].to_csv(output_path + 'gauss_fiber_passive_stress.csv')
    output_data['gucc_fiber_pstress'][0].to_csv(output_path + 'gauss_gucc_fiber_pstress.csv')
    output_data['gucc_trans_pstress'][0].to_csv(output_path + 'gauss_gucc_trans_pstress.csv')
    output_data['gucc_shear_pstress'][0].to_csv(output_path + 'gauss_gucc_shear_pstress.csv')
    output_data['alpha'][0].to_csv(output_path + 'gauss_alpha.csv')
    #output_data['filament_overlap'][0].to_csv(output_path + 'gauss_overlap.csv')
    output_data['delta_hsl'][0].to_csv(output_path + 'gauss_deltahsl.csv')"""

    # Right now, single cell outputs dictionary


# Execute script if input file is given
if np.shape(sys.argv) > 0:
    sim_driver(sys.argv[1])
else:
    sys.exit("Error: No input file given.")
