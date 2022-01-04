# @Author: charlesmann
# @Date:   2021-12-29T13:53:51-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-29T14:24:17-05:00

from dolfin import *

def calculate_deviation_function(fcn_spaces,functions):

    # deviation and stimulus need to be from same function space
    temp_deviation_fcn = functions["stimulus"] - functions["set_point"]
    temp_deviation_fcn = project(temp_deviation_fcn,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})

    return temp_deviation_fcn
