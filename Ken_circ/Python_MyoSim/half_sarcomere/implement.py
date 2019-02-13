# Functions for implementating half-sarcomere class
import numpy as np
import pandas as pd


def update_simulation(self, time_step, delta_hsl, activation, set_data = 0):

    if (time_step > 0.0):
        # Need to do some kinetics stuff

        # Update calcium
        self.membr.evolve_kinetics(time_step, activation)
        self.Ca_conc = self.membr.myofilament_Ca_conc

        # Myofilaments
        self.myof.evolve_kinetics(time_step, self.Ca_conc)

    if (np.abs(delta_hsl) > 0.0):
        # Need to move some things
        self.myof.move_cb_distributions(delta_hsl)
        self.hs_length = self.hs_length + delta_hsl

    # Update forces
    self.myof.set_myofilament_forces()
    self.hs_force = self.myof.total_force


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

    if (self.membr.kinetic_scheme == "Ten_Tusscher_2004"):
        # Ten Tusscher membrane voltage is in mV
        self.hs_data.at[self.data_buffer_index, 'membrane_voltage'] = \
            0.001*self.membr.y[0]

    self.hs_data.at[self.data_buffer_index, 'cb_number_density'] = \
        self.cb_number_density

