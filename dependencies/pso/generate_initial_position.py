import numpy as np


## Make this a class to store info so it's not calculated for each particle?

class positionGenerator:

    def __init__(self, num_particles, gen_string, init_dict):

        self.num_particles = num_particles
        self.gen_string = gen_string
        self.num_vars = len(init_dict.keys())
        self.return_dictionary = {}
        self.initial_dictionary = init_dict


        # initialize things needed for certain generator algorithms
        if self.gen_string == "uniform":
            self.refinement = int(float(self.num_particles)**(1.0/self.num_vars))
            self.partition = {}
            # Use linspace to evenly assign starting vales for each variable range?
            #print init_dict
            for key in init_dict.keys():
                self.partition[key] = np.linspace(init_dict[key][0][0],init_dict[key][0][1],num=self.refinement)

            #if self.num_particles > self.refinement*self.num_particles*self.num_vars:
                #print "Unused Particles. Randomly assigning them a position"

            #print sorted(self.partition)
            grid = np.array(np.meshgrid(*(v for _,v in sorted(self.partition.items()))))
            self.grid = grid
            self.grid = self.grid.reshape(np.prod(self.grid.shape)) # returns a 1xnum_particles (hopefully) array

            var_counter = 0
            num_coords = self.refinement**self.num_vars
            self.coord_dict = {}
            # partition up the array to store in the partition dictionary
            for var in sorted(self.partition.keys()):
                print "optimizing " + str(var)
                #print self.grid[var_counter*self.num_particles:(var_counter+1)*(self.num_particles-1)]
                self.coord_dict[var] = self.grid[var_counter*num_coords:(var_counter+1)*(num_coords)]
                var_counter += 1



    def uniform_generator(self,j, init_dict):
        #print "in uniform generator now \n"
        # init_dict values are lists with entries bounds, position, velocity

        for var in init_dict.keys():
            self.initial_dictionary[var][1] = self.coord_dict[var][j]

        return self.initial_dictionary
        # Need to work out what to do with the remainder from refinement. Should
        # be less than n, so place these points on the corners of the hypercube?


        # Need an index, and a counter for each variable
        """self.index_counter_dict = {}
        for var in init_dict.keys():
            self.index_counter_dict[var] = [0, 0]"""


        """self.possible_value_dictionary = {}
        for var in init_dict.keys():

            # Each variable has its own bounds
            lb = float(init_dict[var][0][0])
            ub = float(init_dict[var][0][1])

            # and its own interval to separate points
            interval = (ub - lb)/(self.refinement+1)

            # temporary storage list for the possible values for this variable
            temp = []

            for i in range(0,self.refinement):
                temp[i] = lb + i*interval

            # Assign this list to the full tensor of possible values
            self.possible_value_dictionary[var] = temp"""

        # Now we should have a "num_vars" dimensional dictionary, each value has
        # self.refinement number of elements

        # Assign the appropriate value to the j-th particle
        # j should be the sum of refinement^index, for index ranging from 0 to dimensionality

        # check variable counter to see if we've iterated over it

        # for vars in init_dict.keys()
        #   if checksum less than j
        #

            # set variable value to one of the possible values based on the index
            #init_dict[var][1] = self.partition[var][[self.index_counter_dict][var][0]]
            # update the index and counter dictionary





    def generate_initial_positions(self,i, initial_dictionary):
        ## function to parse which generating function to use
        #
        # for now, just going to have the uniformly distributed case
        if self.gen_string == "uniform":

            self.return_dictionary = self.uniform_generator(i, initial_dictionary)


        return self.return_dictionary
