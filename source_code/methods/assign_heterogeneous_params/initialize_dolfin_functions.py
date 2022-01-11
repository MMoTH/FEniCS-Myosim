# @Author: charlesmann
# @Date:   2021-03-02T15:51:26-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-10T19:52:20-05:00



import numpy as np
import sys
import json
from dolfin import *

def initialize_dolfin_functions(dolfin_functions_dict,fcn_space):

    # This function will recursively go through the dolfin_functions_dict and append
    # an initialized dolfin function to the list that exists as the parameter key's value

    for k,v in dolfin_functions_dict.items():
        if isinstance(v,dict):
            initialize_dolfin_functions(v,fcn_space)

        else:
            append_initialized_function(dolfin_functions_dict,k,fcn_space) #first item in value list must be base value

    #print "new dict", dolfin_functions_dict

    return dolfin_functions_dict


def append_initialized_function(temp_dict,key,fcn_space):
    if isinstance(temp_dict[key][0],str):
        #do nothing
        print "string, not creating function"
    else:
        temp_fcn = Function(fcn_space)
        #print "key",key,"value", temp_dict[key][0]
        temp_fcn.vector()[:] = temp_dict[key][0]
        #print temp_fcn.vector().get_local()
        temp_dict[key].append(temp_fcn)


    return

#--------------------------------------------------------------------------------
# testing with sample json file
"""input_file = sys.argv[1]
# Load in JSON dictionary
with open(input_file, 'r') as json_input:
  input_parameters = json.load(json_input)

all_params = input_parameters

# Defining test mesh and functionspace at quadrature points where myosim is solved
mesh = UnitCubeMesh(1,1,1)
Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
Quadelem._quad_scheme = 'default'
Quad = FunctionSpace(mesh,Quadelem)

initialize_dolfin_functions(all_params,Quad)"""
