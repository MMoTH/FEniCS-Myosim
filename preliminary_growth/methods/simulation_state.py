# @Author: charlesmann
# @Date:   2022-01-06T12:38:20-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-06T14:25:10-05:00

class simulation_state():

    def __init__(self,params):

        # simulation protocol
        self.timestep = params["simulation_parameters"]["protocol"]["simulation_timestep"][0]
        self.duration = params["simulation_parameters"]["protocol"]["simulation_duration"][0]
        self.edv = params["simulation_parameters"]["protocol"]["initial_end_diastolic_volume"][0]


        # circulatory stuff
        self.wk_params = params["windkessel_parameters"]
        # Add pressures
        self.wk_params["Part"] = 0.0
        self.wk_params["Pven"] = 0.0
        self.wk_params["PLV"] = 0.0

        # Will add things as needed
