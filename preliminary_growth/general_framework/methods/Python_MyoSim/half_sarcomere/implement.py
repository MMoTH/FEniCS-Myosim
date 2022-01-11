# Functions for implementating half-sarcomere class
import numpy as np
import pandas as pd


def update_simulation(self, time_step, delta_hsl, hsl, y0, pf, cbf, calcium, n_array_length, cell_time,hs_params_new_list,set_data = 0):

    # Need to do some kinetics stuff

    # update gauss point params
    #print "new list  " + str(hs_params_new_list)
    #print "implement hs params"
    #print hs_params_new_list
    self.update_hs_props(hs_params_new_list)
    time_step = time_step/1000.0
    # Update calcium
    #self.membr.evolve_kinetics(time_step, activation)
    #self.Ca_conc = self.membr.myofilament_Ca_conc

    # Update calcium from values loaded in from previous simulation
    # Update all properties of self passed in from FE sim
    self.Ca_conc = calcium

    # Going to loop through integration points here, neglecting myosin isoforms for now
    #num_int_points = np.shape(hsl)
    #num_int_points = num_int_points[0]
    y_pops = np.zeros(np.size(y0))
    y_interp = np.zeros(np.size(y0))
    self.temp_overlaps = 0.0
    #print y0[0:53]
    #for i in range(num_int_points):
    self.hs_length = hsl
    self.myof.cb_force = cbf
    self.myof.pas_force = pf
    self.hs_force = self.myof.cb_force+self.myof.pas_force
    self.myof.y = y0
#        print "myof_y" + str(np.shape(self.myof.y))
        #if i==1:
            #print self.myof.y
        # Myofilaments
        # moving interpolation here, so populations match up with active force
        # generated at end of Newton Iteration
    if (np.abs(delta_hsl) > 0.0):
        #print "moving cb distributions" + str(delta_hsl)
        # Need to move some things
        self.myof.move_cb_distributions(delta_hsl)
    y_interp = self.myof.y
    # passed in overlaps from previous timestep
    #old_overlap = overlap_array[i]
    self.myof.evolve_kinetics(time_step, self.Ca_conc, cell_time)
    #print self.myof.y
    #if i==1:
        #print self.myof.y
    #if (np.abs(delta_hsl[i]) > 0.0):
        # Need to move some things
    #    self.myof.move_cb_distributions(delta_hsl[i])
    #self.hs_length = self.hs_length + delta_hsl

    # enforce n_bound < n_on, needs to be generalized for greater than 3 state
    """decrement_counter = 0
    while self.myof.n_on < self.myof.n_bound:
        self.myof.y[2+decrement_counter] = 0.0
        self.myof.n_bound = np.sum(self.myof.y[2 + np.arange(0, self.myof.no_of_x_bins)])
        decrement_counter += 1"""
    # Assign int point's population vector to larger y vector
    y_pops = self.myof.y
    self.temp_overlaps = self.myof.n_overlap

    # Update forces
    # Don't need these, will be reset at beginning of this fcn
    #self.myof.set_myofilament_forces()
    #self.hs_force = self.myof.total_force
    #print y_pops[0:53]
    return self.temp_overlaps, y_interp, y_pops

def return_rates_fenics(self):
    fluxes, rates = self.myof.return_fluxes(self.myof.y, self.Ca_conc)

    return fluxes, rates

def update_data_holder(self, dt, activation):

    # Update data struct for half-sarcomere
    self.data_buffer_index = self.data_buffer_index + 1
    self.hs_time = self.hs_time + dt
    self.hs_data.at[self.data_buffer_index, 'hs_time'] = self.hs_time
    self.hs_data.at[self.data_buffer_index, 'activation'] = activation
    self.hs_data.at[self.data_buffer_index, 'Ca_conc'] = self.Ca_conc

    self.hs_data.at[self.data_buffer_index, 'hs_length'] = self.hs_length

    self.hs_data.at[self.data_buffer_index, 'hs_force'] = self.hs_force
    self.hs_data.at[self.data_buffer_index, 'cb_force'] = self.myof.cb_force
    self.hs_data.at[self.data_buffer_index, 'pas_force'] = self.myof.pas_force

    if (self.myof.kinetic_scheme == '3state_with_SRX'):
        self.hs_data.at[self.data_buffer_index, 'M_OFF'] = \
            self.myof.y[0]
        self.hs_data.at[self.data_buffer_index, 'M_ON'] = \
            self.myof.y[1]
        self.hs_data.at[self.data_buffer_index, 'M_bound'] = \
            np.sum(self.myof.y[2 + np.arange(self.myof.no_of_x_bins)])
        self.hs_data.at[self.data_buffer_index, 'n_off'] = \
            np.sum(self.myof.y[-2])
        self.hs_data.at[self.data_buffer_index, 'n_on'] = \
            np.sum(self.myof.y[-1])

        # Update fluxes
        fluxes = self.myof.return_fluxes(self.myof.y, self.Ca_conc)
        self.hs_data.at[self.data_buffer_index, 'J1'] = fluxes['J1']
        self.hs_data.at[self.data_buffer_index, 'J2'] = fluxes['J2']
        self.hs_data.at[self.data_buffer_index, 'J3'] = np.sum(fluxes['J3'])
        self.hs_data.at[self.data_buffer_index, 'J4'] = np.sum(fluxes['J4'])
        self.hs_data.at[self.data_buffer_index, 'Jon'] = fluxes['Jon']
        self.hs_data.at[self.data_buffer_index, 'Joff'] = fluxes['Joff']

    if (self.myof.kinetic_scheme == '4state_with_SRX'):
        self.hs_data.at[self.data_buffer_index, 'M_OFF'] = \
            self.myof.y[0]
        self.hs_data.at[self.data_buffer_index, 'M_ON'] = \
            self.myof.y[1]
        self.hs_data.at[self.data_buffer_index, 'M_bound'] = \
            np.sum(self.myof.y[2 + np.arange(self.myof.no_of_x_bins)])
        self.hs_data.at[self.data_buffer_index, 'n_off'] = \
            np.sum(self.myof.y[-2])
        self.hs_data.at[self.data_buffer_index, 'n_on'] = \
            np.sum(self.myof.y[-1])

        # Update fluxes
        fluxes = self.myof.return_fluxes(self.myof.y, self.Ca_conc)
        self.hs_data.at[self.data_buffer_index, 'J1'] = fluxes['J1']
        self.hs_data.at[self.data_buffer_index, 'J2'] = fluxes['J2']
        self.hs_data.at[self.data_buffer_index, 'J3'] = np.sum(fluxes['J3'])
        self.hs_data.at[self.data_buffer_index, 'J4'] = np.sum(fluxes['J4'])
        self.hs_data.at[self.data_buffer_index, 'J5'] = np.sum(fluxes['J5'])
        self.hs_data.at[self.data_buffer_index, 'J6'] = np.sum(fluxes['J6'])
        self.hs_data.at[self.data_buffer_index, 'J7'] = np.sum(fluxes['J7'])
        self.hs_data.at[self.data_buffer_index, 'J8'] = np.sum(fluxes['J8'])
        self.hs_data.at[self.data_buffer_index, 'Jon'] = fluxes['Jon']
        self.hs_data.at[self.data_buffer_index, 'Joff'] = fluxes['Joff']        

    if (self.membr.kinetic_scheme == "Ten_Tusscher_2004"):
        # Ten Tusscher membrane voltage is in mV
        self.hs_data.at[self.data_buffer_index, 'membrane_voltage'] = \
            0.001*self.membr.y[0]

    self.hs_data.at[self.data_buffer_index, 'cb_number_density'] = \
        self.cb_number_density
