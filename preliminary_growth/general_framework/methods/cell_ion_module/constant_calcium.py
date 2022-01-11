import numpy as np


## Initialize constant calcium class
#
# constant calcium class is passed back to fenics script
# @param[in] params Dictionary for cell ion model in the input file under "model_inputs"
# @param[out] model_class Class object generated, passed back to fenics script
def init(params):

    model_class = constant_calcium(params)
    return model_class

## Constant calcium class
#
# This is the class whose method returns a constant calcium value
#
#
class constant_calcium():

    def __init__(self,params):

        # Hard coding, have established this transient
        # these could be set in params if needed
        self.t_act = params["t_act"][0]
        self.pCa = params["pCa"][0]

    ## calculate calcium concentration method
    #
    # returns constant calcium value according to user defined pCa value after
    # time exceeds t_act. Uses class properties self.t_act and self.pCa
    # @param[in] cycle Integer denoting current cardiac cycle. Not needed for this
    # @param[in] time float denoting the current cell time, specified in ms
    # @param[out] calcium_value float calculated calcium value
    def calculate_concentrations(self,cycle,time):

        print "calculating calcium"
        print "time = " + str(time) + " (ms)"
        print "t_act = " + str(self.t_act)
        t = time/1000
        print "t = " + str(t)

        calcium_value = 0.0
        if t > self.t_act:
            calcium_value = np.power(10.0,-self.pCa)
            print "calcium is " + str(calcium_value)
        else:
            calcium_value = np.power(10.0,-9.0)
        return calcium_value
