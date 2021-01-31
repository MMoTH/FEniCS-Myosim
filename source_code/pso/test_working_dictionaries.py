import json
import sys
sys.path.append('/Users/charlesmann/Academic/UK/fenics/source_code/dependencies')
#import recode_dictionary
#input_file_name = sys.argv[1]
import random

"""with open(input_file_name, 'r') as json_input:
  input_parameters = json.load(json_input)

# Convert any unicode values to python strings so they work with some cpp libraries
recode_dictionary.recode(input_parameters)

## Parse out the different types of parameters
sim_params = input_parameters["simulation_parameters"]
file_inputs = input_parameters["file_inputs"]
output_params = input_parameters["output_parameters"]
passive_params = input_parameters["forms_parameters"]["passive_law_parameters"]
hs_params = input_parameters["myosim_parameters"]
cell_ion_params = input_parameters["electrophys_parameters"]["cell_ion_parameters"]
monodomain_params = input_parameters["electrophys_parameters"]["monodomain_parameters"]
windkessel_params = input_parameters["windkessel_parameters"]
optimization_params = input_parameters["optimization_parameters"]

params = [sim_params, file_inputs, output_params, passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params]

working_param_dict = optimization_params["variables_and_bounds"]"""

"""for key in working_param_dict:
    dim_ub = working_param_dict[key][0][1]
    dim_lb = working_param_dict[key][0][0]
    dim_range = dim_ub - dim_lb

    # Should this be zero?
    working_param_dict[key][2] = random.uniform(-dim_range,dim_range)"""
    #print working_param_dict[key]

# Pretend that the working_param_dictionary has been appropriately updated


# Re-assign new position values to dictionaries to be passed to fenics
def compare_keys(dict1,dict2):

    # Know that dict1 is not a nested dictionary, but dict 2 may be
    for key in dict1.keys():

        for key2 in dict2.keys():

            if type(dict2[key2]) is dict:

                # Descend into this dictionary

                compare_keys(dict1,dict2[key2])

            else:

                # Compare this key to the key in dict1
                if key == key2:

                    # Replace dict2, key2 with dict1 key value
                    # the fenics scripts shouldn't ever try to get the velocity value, just
                    # replace entire value with dict1 value
                    #print dict2[key]
                    dict2[key2] = dict1[key]
                    #print dict1[key]
                    #print dict2[key2]

    return(dict2)

"""for l in params:
    compare_keys(working_param_dict,l)"""

#print working_param_dict, params[4]
