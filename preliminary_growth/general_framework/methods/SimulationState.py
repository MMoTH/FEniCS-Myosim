# @Author: charlesmann
# @Date:   2022-01-06T12:38:20-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T10:02:17-05:00
import numpy as np

class SimulationState():

    def __init__(self,params):

        # some initial values
        self.edv = params["protocol"]["initial_end_diastolic_volume"][0]
        self.timestep = params["protocol"]["simulation_timestep"][0]
        self.termination_condition = params["protocol"]["termination_condition"][0]
        self.reference_load_steps = params["protocol"]["reference_loading_steps"][0]
        self.cardiac_period = params["protocol"]["cardiac_period"][0]
        # Go ahead and set how many cycles to steady state. Eventually will check for steady state
        self.num_cycles_to_steady_state = 1
        # determine maximum number of cycles too
        if self.termination_condition == "simulation_end_time":
            self.sim_duration = params["protocol"]["termination_condition"][1]
            self.max_cycles = params["protocol"]["termination_condition"][1]/params["protocol"]["cardiac_period"][0]

        if self.termination_condition == "growth_convergence":
            # allot enough time to run one cardiac cycle and grow the maximum number of times
            # if we are running to steady state between growth, this will have to change
            # will probably have to specify number of cycles to approximate steady state
            self.sim_duration = params["protocol"]["termination_condition"][1]*self.cardiac_period
            self.max_cycles = self.num_cycles_to_steady_state*params["protocol"]["termination_condition"][1]

        # Verifying things
        print "Prescribed EDV:", self.edv
        print "Timestep:", self.timestep
        print "Termination condition:", self.termination_condition
        print "Simulation Duration:", self.sim_duration

        # circulatory stuff
        self.wk_params = params["windkessel_parameters"]
        # Add pressures
        self.wk_params["Part"] = 0.0
        self.wk_params["Pven"] = 0.0
        self.wk_params["PLV"] = 0.0

        # Will add things as needed
