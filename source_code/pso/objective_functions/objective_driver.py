import sys
import numpy as np
sys.path.append("/home/fenics/shared/source_code/pso/objective_functions")


## Class for loading in objective function file
#
# user creates an objective function file to be loaded in here
class objective_driver():

    def __init__(self,obj_fcn_file):

        # Specify model to be ran
        #model_name = params["model"][0]
        #model_params = params["model_inputs"]

        #base_dir = "cell_ion_module"
        #model_name = base_dir + temp
        #model_name = "three_state_calcium"

        #print model_name

        # Import the model
        self.objFunc = __import__(obj_fcn_file)
        self.objFunc_class = self.objFunc.init()
