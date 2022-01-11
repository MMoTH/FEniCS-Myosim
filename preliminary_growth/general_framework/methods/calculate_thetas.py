# @Author: charlesmann
# @Date:   2021-12-29T13:56:50-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-08T11:16:58-05:00
from dolfin import *
import numpy as np

def calculate_thetas(fcn_spaces,functions,input_parameters):

    # should come from instruction file
    # I'm thinking in the initializing functions for function spaces and functions,
    # we get a lot of the growth parameters from the instruction file.
    # Should allow user to specify function spaces to be used, stimulus case, and
    # individual growth constants for each direction

    max_theta = 1.04
    min_theta = 0.96
    growth_time_constant = Constant(input_parameters["growth_and_remodeling"]["f0_time_constant"][0])


    theta_ff_temp = project(1+(1./growth_time_constant)*((functions["deviation_ff"]/functions["set_point_ff"])),fcn_spaces["stimulusFS"])
    theta_ff_array = theta_ff_temp.vector().get_local()
    theta_ff_array[theta_ff_array >= max_theta] = max_theta
    theta_ff_array[theta_ff_array <= min_theta] = min_theta
    functions["theta_ff"].vector()[:] = theta_ff_array
    # overwriting, don't want eccentric growth right now
    functions["theta_ff"].vector()[:] = 1.0

    theta_ss_temp = project(1+(1./growth_time_constant)*((functions["deviation_ss"]/functions["set_point_ss"])),fcn_spaces["stimulusFS"])
    theta_ss_array = theta_ss_temp.vector().get_local()
    theta_ss_array[theta_ss_array >= max_theta] = max_theta
    theta_ss_array[theta_ss_array <= min_theta] = min_theta
    functions["theta_ss"].vector()[:] = theta_ss_array

    theta_nn_temp = project(1+(1./growth_time_constant)*((functions["deviation_nn"]/functions["set_point_nn"])),fcn_spaces["stimulusFS"])
    theta_nn_array = theta_nn_temp.vector().get_local()
    theta_nn_array[theta_nn_array >= max_theta] = max_theta
    theta_nn_array[theta_nn_array <= min_theta] = min_theta
    functions["theta_nn"].vector()[:] = theta_nn_array




    return functions
