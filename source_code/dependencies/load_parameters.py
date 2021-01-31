import json
import recode_json_strings as rc

## function to load parameters from json input file
def load_and_parse_params(file):

    # Load in json file
    with open(input_file_name, 'r') as json_input:
      params = json.load(json_input)

    ## Parse out the different types of parameters
    sim_params = input_parameters["simulation_parameters"]
    params["file_inputs"] = input_parameters["file_inputs"]
    output_params = input_parameters["output_parameters"]
    passive_params = input_parameters["forms_parameters"]["passive_law_parameters"]
    params["hs_params"] = input_parameters["myosim_parameters"]
    cell_ion_params = input_parameters["electrophys_parameters"]["cell_ion_parameters"]
    monodomain_params = input_parameters["electrophys_parameters"]["monodomain_parameters"]
    force_params = input_parameters["myosim_parameters"]["myofilament_parameters"]["active_force_parameters"]
    force_params["cb_number_density"] = params["hs_params"]["cb_number_density"]

    ## Assign parameters
    params["calcium_path"] = cell_ion_params["path_to_calcium"][0]
    params["json_output_path"] = output_params["output_path"][0]
    # some need to be converted to work with cpp libraries
    params["output_path"] = rc._byteify(params["json_output_path"])
    params["input_path"] = file_inputs["input_directory_path"][0]
    params["rc_input_path"] = rc._byteify(params["input_path"])
    params["json_casename"] = file_inputs["casename"][0]
    params["casename"] = rc._byteify(json_casename)






    # Check that the output path exists. If it does not, create it and let user know
    if not os.path.exists(output_path):
        print "Output path does not exist. Creating it now"
        os.makedirs(output_path)
