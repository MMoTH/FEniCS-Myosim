import numpy as np
import sys
import json
from dolfin import *

def flag_heterogeneous_params(list_of_all_params,fcn_space):

     # takes a list of dictionaries that  contain all instruction file information
     # and recursively searches the parameter value lists looking for "heterogeneous=True"
     # If found, creates a fenics function for that parameter and puts it into a dictionary
     # to be used by assign_heterogeneous_params.py

     # Maybe not recursive. Need to store a master dictionary
     hetero_dict = {}

     for i in np.arange(np.shape(list_of_all_params)[0]):

         # send dictionary from list_of_all_params[i] to recursive fcn
         search_flag(hetero_dict,list_of_all_params[i],fcn_space)

     print "final heterogeneity dictionary",hetero_dict


#-------------------------------------------------------------------------------

def search_flag(het_dict,temp_dictionary,fcn_space):

    # Loop through keys of dictionary
    # First, check if the key value is itself a dictionary
    for k, v in temp_dictionary.items():
        if isinstance(v,dict):
            search_flag(het_dict,v,fcn_space)

        else:
            # Going through actual parameters

            # these values should be a list whose first entry is the base
            # parameter value. If the parameter will be homogeneous, the
            # list will contain a dictionary
            for j in v:
                if isinstance(j,dict):
                    check = j["heterogeneous"]
                    if check:
                        # this parameters should be homogeneous
                        temp_law = j["law"]
                        base_value = v[0] #first entry is base value
                        temp_init_function = Function(fcn_space)
                        het_dict[k]=[base_value,temp_init_function,temp_law]




#--------------------------------------------------------------------------------
# testing with sample json file
"""input_file = sys.argv[1]
# Load in JSON dictionary
with open(input_file, 'r') as json_input:
  input_parameters = json.load(json_input)

all_params = [input_parameters]

# Defining test mesh and functionspace at quadrature points where myosim is solved
mesh = UnitCubeMesh(1,1,1)
Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
Quadelem._quad_scheme = 'default'
Quad = FunctionSpace(mesh,Quadelem)

flag_heterogeneous_params(all_params,Quad)
"""
