# @Author: charlesmann
# @Date:   2021-12-29T13:56:50-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-04T13:16:02-05:00
from dolfin import *
import numpy as np

def calculate_thetas(fcn_spaces,functions,input_parameters):

    # should come from instruction file
    # I'm thinking in the initializing functions for function spaces and functions,
    # we get a lot of the growth parameters from the instruction file.
    # Should allow user to specify function spaces to be used, stimulus case, and
    # individual growth constants for each direction

    max_theta = 1.05
    min_theta = 0.95
    growth_time_constant = Constant(input_parameters["growth_and_remodeling"]["f0_time_constant"][0])

    theta_ff_temp = project(1+(1./growth_time_constant)*((functions["deviation"]/functions["set_point"])),fcn_spaces["stimulusFS"])
    theta_ff_array = theta_ff_temp.vector().get_local()
    theta_ff_array[theta_ff_array >= max_theta] = max_theta
    theta_ff_array[theta_ff_array <= min_theta] = min_theta

    #functions["theta_ff"].assign(theta_ff_temp)
    functions["theta_ff"].vector()[:] = theta_ff_array
    # Just for now, only dealing with eccentric growth. These can be calculated using their own
    # stimulus and set points later.
    #theta_ss_temp = project(1+(1./growth_time_constant)*((deviation/set_point_value)),S_fcn_space)
    #theta_nn_temp = project(1+(1./growth_time_constant)*((deviation/set_point_value)),S_fcn_space)



    return functions
