import numpy as np
import random
import test_working_dictionaries
import json
import copy


## Class for particles in the particle swarm optimization
class fenicsParticle:

## Initialization _____________________________________________________________
    def __init__(self, dimensionality, variables_and_bounds, params):

        # x0 is the initial position for this particle
        # randomly selected within the bounds.

        #bounds consists of {[xi_min, xi_max]} pairs for i = 1, ... ,dimensionality

        # Store a copy of all of the parameters used in fenics simulations
        self.all_fenics_params = copy.deepcopy(params)

        #self.fenics_params = {}


        # Unpack parameters to pass to fenics script
        self.sim_params = self.all_fenics_params[0]
        self.file_inputs = self.all_fenics_params[1]
        self.output_params = self.all_fenics_params[2]
        self.passive_params = self.all_fenics_params[3]
        self.hs_params = self.all_fenics_params[4]
        self.cell_ion_params = self.all_fenics_params[5]
        self.monodomain_params = self.all_fenics_params[6]
        self.windkessel_params = self.all_fenics_params[7]


        # Create a "working dictionary" to be updated
        # Each key in this dictionary has value [[bounds],position,velocity]
        self.working_dict = copy.deepcopy(variables_and_bounds)

        # initialize output dictionary to hold results from fenics script
        self.output_dict = {}
        # initialize data holders
        #self.position = []
        #self.velocity = []
        #self.best_ind_position = []
        self.best_ind_error = -1
        self.current_error = -1

        # Initialize copy of working dictionary to store the best particle position
        self.best_particle_position = variables_and_bounds

        # initialize optimization bounds and dimensionality
        self.dimensionality = dimensionality
        #self.bounds = bounds

        # For now, just have a single cell target force
        #self.target = target_force

        #!!!!!!!!!!!!!!!! Need to initiate proper x0 value !!!!!!!!!!!!!!!!!!!!
        # initialize position to x0, to come from pso_driver
        #self.position.append(x0)

        # initialize zero velocity
        for key in self.working_dict.keys():

            # Generalize for more than one variable
            #dim_ub = self.working_dict[key][0][1]
            #dim_lb = self.working_dict[key][0][0]
            #dim_range = dim_ub - dim_lb

            # Should this be zero? - Yes
            self.working_dict[key][2] = 0.0


        # Update simulation parameters to include initialized positions
        for l in range(len(self.all_fenics_params)):
            #print np.shape(self.all_fenics_params[l])
            self.update_all_fenics_params_list(self.all_fenics_params[l])

        self.sim_params = self.all_fenics_params[0]
        self.file_inputs = self.all_fenics_params[1]
        self.output_params = self.all_fenics_params[2]
        self.passive_params = self.all_fenics_params[3]
        self.hs_params = self.all_fenics_params[4]
        self.cell_ion_params = self.all_fenics_params[5]
        self.monodomain_params = self.all_fenics_params[6]
        self.windkessel_params = self.all_fenics_params[7]
        #for var in self.sim_params:
            #test_working_dictionaries.compare_keys(self.working_dict,self.sim_params)



# Methods ______________________________________________________________________

    ## Evaluate objective function at current position and check against previous errors
    """def evaluate_objective(self, fenics_script):

        # Passing base parameters from input file, will update with new particle values
        # Need to map from "position" to param values
        # For now, hard coding
        #hs_params["myofilament_parameters"]["k_3"] = [self.position[0], "text"]

        # Run simulation, and get output information
        # Need to include information to use multiple cores
        self.output_dict = fenics_script.fenics(self.sim_params,self.file_inputs,self.output_params, \
        self.passive_params,self.hs_params,self.cell_ion_params,self.monodomain_params, \
        self.windkessel_params)

        # this was a hard coded objective function.
        #import module like for cell ion params for objective function?



        #predicted_force = self.output_dict["strarray"][-1]
        #self.current_error = np.power(self.target-predicted_force,2)

        # Need to map self.position to keyword dictionary for inputs
        # Will need something like
        # self.current_error = objFunction(sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params)
        # where each dictionary of params is updated with the particle's "position"

        # Check if current position is the best for this particle
        if self.current_error < self.best_ind_error or self.best_ind_error == -1:
            # We have a new best error (or we are initializing)
            self.best_particle_position = self.working_dict
            self.best_ind_error = self.current_error"""

    def run_simulation(self, fenics_script, iter, p_num,base_output_dir,pso):
        #self.update_all_fenics_params_list(self.sim_params)

        self.output_params["output_path"][0] = base_output_dir + "iter_" + str(iter) + "_particle_" + str(p_num) +"/"

        print self.output_params["output_path"][0]

        self.output_dict = fenics_script.fenics(self.sim_params,self.file_inputs,self.output_params, \
            self.passive_params, self.hs_params, self.cell_ion_params, self.monodomain_params, \
            self.windkessel_params,pso)

        try:
            with open(self.output_params["output_path"][0] + 'particle_inputs.json', 'w') as fp2:
                json.dump([self.hs_params], fp2,indent=2, separators=(',', ': '))
        except:
            print "cannot print input params to file"
        return self.output_dict

    def update_particle_errors(self,current_error):
            self.current_error = current_error
            if self.current_error < self.best_ind_error or self.best_ind_error == -1:
                # We have a new best error (or we are initializing)
                self.best_particle_position = self.working_dict
                self.best_ind_error = self.current_error



    def update_all_fenics_params_list(self, dict2):
        # This is the  custom function to replace values in self.all_fenics_params
        # not sure calling the .update() method is recursive with nested dictionaries
        for key in self.working_dict.keys():
            for key2 in dict2.keys():
                if type(dict2[key2]) is dict:
                    # Descend into this dictionary
                    self.update_all_fenics_params_list(dict2[key2])
                else:
                    # Compare this key to the key in dict1
                    if key == key2:
                        # Replace dict2, key2 with dict1 key value
                        # Just replace the parameter values
                        dict2[key2][0] = self.working_dict[key][1]
                    # this will change the 'optimization_parameters' dictionary too, but
                    # that shouldn't matter at this point



        # If we want to, we can now dump all of these into json file

    #Update particle velocity
    #
    # combination of best particle position, best swarm position, and inertia from previous velocity
    def update_particle_velocity(self, w, c1, c2, best_swarm_position):

        #for i in range(0,self.dimensionality):
        for key in self.working_dict:
            # keys in self.working_dict (the current "position") should match
            # keys in stored best particle position dictionary
            r1 = random.random()
            r2 = random.random()

            #print "This particle's best position " + str(self.best_ind_position)
            #print "This particle's current position " + str(self.position)
            #print "This particle's best error " + str(self.best_ind_error)
            #print "This particle's current error " + str(self.current_error)

            #vel_cognitive=c1*r1*(self.best_ind_position[i]-self.position[i])
            vel_cognitive = c1*r1*(self.best_particle_position[key][1]-self.working_dict[key][1])
            #vel_social = c2*r2*(best_swarm_position[i]-self.position[i])
            vel_social = c2*r2*(best_swarm_position[key][1]-self.working_dict[key][1])
            self.working_dict[key][2] = w*self.working_dict[key][2]+vel_cognitive+vel_social


    # Update particle position from updated velocity
    def update_particle_position(self):

        #for i in range(0,self.dimensionality):
        for key in self.working_dict:

            #self.position[i] = self.position[i] + self.velocity[i]
            self.working_dict[key][1] = self.working_dict[key][1]+self.working_dict[key][2]

            # Keep the particle within bounds
            #if self.position[i] > self.bounds[i][1]:
            #    self.position[i] = self.bounds[i][1]

            if self.working_dict[key][1] > self.working_dict[key][0][1]:
                self.working_dict[key][1] = self.working_dict[key][0][1]

            #if self.position[i] < self.bounds[i][0]:
            #    self.position[i] = self.bounds[i][0]
            if self.working_dict[key][1] < self.working_dict[key][0][0]:
                self.working_dict[key][1] = self.working_dict[key][0][0]

            # Update the parameters to pass into the simulation here
            for l in range(len(self.all_fenics_params)):
                #print np.shape(self.all_fenics_params[l])
                self.update_all_fenics_params_list(self.all_fenics_params[l])

            # Update the input dictionaries from master list for fenics simulation call
            self.sim_params = self.all_fenics_params[0]
            self.file_inputs = self.all_fenics_params[1]
            self.output_params = self.all_fenics_params[2]
            self.passive_params = self.all_fenics_params[3]
            self.hs_params = self.all_fenics_params[4]
            self.cell_ion_params = self.all_fenics_params[5]
            self.monodomain_params = self.all_fenics_params[6]
            self.windkessel_params = self.all_fenics_params[7]
