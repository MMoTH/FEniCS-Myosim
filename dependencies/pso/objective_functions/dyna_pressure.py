import sys
import numpy as np
from scipy import interpolate as interp
sys.path.append("/home/fenics/shared/")

# all objective function files should have the function "return_objective"
# due to memory issues, information is printed out and not passed as dictionary
# object functions will need access to particle output directory

# This will be a class for feeding pressure traces from the dyna 3 state paper
# as a target for the objective function

def init():
    objFunc_class = dyna_pressure_objective()
    return objFunc_class


class dyna_pressure_objective():

    def __init__(self):

        # Load in target pressure here
        self.exp_data = np.loadtxt('/home/fenics/shared/working_directory_untracked/test_pso_objectives/diastolic_pressure/target_sim/PV_.txt')
        self.exp_time = self.exp_data[:,0]
        self.loading_num = np.arange(0,len(self.exp_time))
        self.exp_pressure = self.exp_data[:,1]
        print "target pressure = " + str(self.exp_pressure)

        #Create interpolation function to qinterpolate experimental data to simulation time points
        self.f = interp.interp1d(self.loading_num,self.exp_pressure)


    def evaluate(self,output_dir,iter,p_num):

        # load in particle pressure
        pv_file_input = output_dir +"/PV_.txt"
        p_sim = np.loadtxt(pv_file_input,usecols=(0,1))

        #interpolate experimental pressure to same time points as simulation pressure
        # but get rid of first loading_num number of points (time independent loading)
        particle_time = p_sim[:,0]
        p_loading_num = np.arange(0,len(particle_time))
        interpolated_exp_pressure = self.f(p_loading_num)

        # Look at differences in experimental pressure and simulation predicted pressure
        particle_error_array = np.power(interpolated_exp_pressure-p_sim[:,1],2*np.ones(len(particle_time)))
        particle_error = np.sum(particle_error_array)

        return particle_error
