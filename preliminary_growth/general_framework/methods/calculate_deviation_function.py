# @Author: charlesmann
# @Date:   2021-12-29T13:53:51-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-07T12:29:14-05:00

from dolfin import *

def calculate_deviation_function(fcn_spaces,functions):

    # deviation and stimulus need to be from same function space
    temp_deviation_ff = functions["stimulus_ff"] - functions["set_point_ff"]
    temp_deviation_ff = project(temp_deviation_ff,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    functions["deviation_ff"].assign(temp_deviation_ff)

    temp_deviation_ss = functions["stimulus_ss"] - functions["set_point_ss"]
    temp_deviation_ss = project(temp_deviation_ss,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    functions["deviation_ss"].assign(temp_deviation_ss)

    temp_deviation_nn = functions["stimulus_nn"] - functions["set_point_nn"]
    temp_deviation_nn = project(temp_deviation_nn,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})
    functions["deviation_nn"].assign(temp_deviation_nn)

    return functions
