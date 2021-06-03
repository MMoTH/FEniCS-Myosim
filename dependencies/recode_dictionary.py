import json
import sys
sys.path.append("/Users/charlesmann/Academic/UK/fenics/source_code/dependencies")
import recode_json_strings as rc

## function to iterate through nested dictionaries and convert unicode values to
# python strings
def recode(json_input_dict):

    for v in json_input_dict.values():
        if type(v) is dict:
            recode(v)
        else:
            # This works for a dictionary without dictionary values nested
            #for v in json_input_dict.values():

            counter = 0
            for j in v:

                if type(j) is unicode:
                    rcj = rc._byteify(j)
                    v[counter] = rcj

                counter +=1

    return json_input_dict
