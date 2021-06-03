import numpy as np
import pandas as pd
import Python_MyoSim.half_sarcomere.myofilaments.myofilaments as myofilaments
#import Python_MyoSim.half_sarcomere.membranes.membranes as membranes

#import membranes

## Class for a half sarcomere
#
# One half-sarcomere class is initialized, properties are passed in for each gauss point
class half_sarcomere():

    from .implement import update_simulation, update_data_holder
    from .display import display_fluxes
    import numpy as np

    ## initialization function for class half_sarcomere
    #
    # @param[in] hs_params loaded in from json file as dictionary. Input is \[value "units"\](see fenics.py)
    # @param[in] data_buffer_size = 1 since data is stored in fenics.py
    def __init__(self,hs_params, data_buffer_size):


        self.hs_length = float(hs_params["initial_hs_length"][0])
        self.Ca_conc = 1.0e-9
        self.activation = 0.0

        ## Pull of class parameters
        self.max_rate = float(hs_params["max_rate"][0])
        self.temperature = float(hs_params["temperature"][0])
        self.cb_number_density = float(hs_params["cb_number_density"][0])

        ## Pull of membrane parameters
        # Don't think I need these for fenics
        #membr_params = hs_params.membranes
        #self.membr = membranes.membranes(membr_params, self)

        ## Initialise hs_force, required for myofilament kinetics
        self.hs_force = 0

        ## Pull off the mofilament_params
        myofil_params = hs_params["myofilament_parameters"]
        self.myof = myofilaments.myofilaments(myofil_params,self)

        print(self.myof.cb_force)

        ## Update forces
        self.hs_force = self.myof.cb_force + self.myof.pas_force
        print("hs_force: %f" % self.hs_force)

        ## Create a pandas data structure to store data
        self.data_buffer_size = data_buffer_size
        self.hs_time = 0.0
        self.data_buffer_index = int(0)
        self.hs_data = pd.DataFrame({'hs_time' : np.zeros(self.data_buffer_size),
                                     'hs_length' : self.hs_length * np.ones(self.data_buffer_size),
                                     'hs_force' : np.zeros(self.data_buffer_size),
                                     'cb_force' : np.zeros(self.data_buffer_size),
                                     'pas_force' : np.zeros(self.data_buffer_size),
                                     'Ca_conc' : np.zeros(self.data_buffer_size)})

        ## Add in specific fields for each scheme
        if (self.myof.kinetic_scheme == '3state_with_SRX'):
            # Initialise
            self.hs_data['M_OFF'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['M_ON'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['M_bound'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_off'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_on'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_bound'] = pd.Series(np.zeros(self.data_buffer_size))

            ## Set first values
            self.hs_data.at[self.data_buffer_index, 'M_OFF'] = 1.0
            self.hs_data.at[self.data_buffer_index, 'M_ON'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'M_bound'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'n_off'] = 1.0
            self.hs_data.at[self.data_buffer_index, 'n_on'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'n_bound'] = 0.0

            # Fluxes
            self.hs_data['J1'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J2'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J3'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J4'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['Jon'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['Joff'] = pd.Series(np.zeros(self.data_buffer_size))

        ## Add in specific fields for each scheme
        if (self.myof.kinetic_scheme == '4state_with_SRX'):
            # Initialise
            self.hs_data['M_OFF'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['M_ON'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['M_weakly_bound'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['M_FG'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_off'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_on'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['n_bound'] = pd.Series(np.zeros(self.data_buffer_size))

            ## Set first values
            self.hs_data.at[self.data_buffer_index, 'M_OFF'] = 1.0
            self.hs_data.at[self.data_buffer_index, 'M_ON'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'M_weakly_bound'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'M_FG'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'n_off'] = 1.0
            self.hs_data.at[self.data_buffer_index, 'n_on'] = 0.0
            self.hs_data.at[self.data_buffer_index, 'n_bound'] = 0.0

            # Fluxes
            self.hs_data['J1'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J2'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J3'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J4'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J5'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J6'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J7'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['J8'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['Jon'] = pd.Series(np.zeros(self.data_buffer_size))
            self.hs_data['Joff'] = pd.Series(np.zeros(self.data_buffer_size))

        #if (self.membr.kinetic_scheme == "Ten_Tusscher_2004"):
        #    self.hs_data['membrane_voltage'] = pd.Series(np.zeros(self.data_buffer_size))

        # Other stuff
        self.hs_data['cb_number_density'] = \
            pd.Series(np.zeros(self.data_buffer_size))


    def update_hs_props(self,hs_params):
        #print "updating hs properties"
        # update properties passed in from fenics
        self.myof.kinetic_scheme = hs_params["myofilament_parameters"]["kinetic_scheme"]
        #print self.myof.kinetic_scheme

        if self.myof.kinetic_scheme[0] == "3state_with_SRX":
            self.myof.k_1 = hs_params["myofilament_parameters"]["k_1"][0]
            self.myof.k_force = hs_params["myofilament_parameters"]["k_force"][0]
            self.myof.k_2 = hs_params["myofilament_parameters"]["k_2"][0]
            self.myof.k_3 = hs_params["myofilament_parameters"]["k_3"][0]
            self.myof.k_4_0 = hs_params["myofilament_parameters"]["k_4_0"][0]
            self.myof.k_4_1 = hs_params["myofilament_parameters"]["k_4_1"][0]
            self.myof.k_cb = hs_params["myofilament_parameters"]["k_cb"][0]
            self.myof.x_ps = hs_params["myofilament_parameters"]["x_ps"][0]
            self.myof.k_on = float(hs_params["myofilament_parameters"]["k_on"][0])
            self.myof.k_off = hs_params["myofilament_parameters"]["k_off"][0]
            self.myof.k_coop = hs_params["myofilament_parameters"]["k_coop"][0]
            self.myof.bin_min = hs_params["myofilament_parameters"]["bin_min"][0]
            self.myof.bin_max = hs_params["myofilament_parameters"]["bin_max"][0]
            self.myof.bin_width = hs_params["myofilament_parameters"]["bin_width"][0]
            self.myof.thick_filament_length = hs_params["myofilament_parameters"]["thick_filament_length"][0]
            self.myof.thin_filament_length = hs_params["myofilament_parameters"]["thin_filament_length"][0]
            self.myof.bare_zone_length = hs_params["myofilament_parameters"]["bare_zone_length"][0]
            self.myof.k_falloff = hs_params["myofilament_parameters"]["k_falloff"][0]

        if self.myof.kinetic_scheme[0] == "4state_with_SRX":
            self.myof.k_1 = hs_params["myofilament_parameters"]["k_1"][0]
            self.myof.k_force = hs_params["myofilament_parameters"]["k_force"][0]
            self.myof.k_2 = hs_params["myofilament_parameters"]["k_2"][0]
            self.myof.k_3 = hs_params["myofilament_parameters"]["k_3"][0]
            self.myof.k_4_0 = hs_params["myofilament_parameters"]["k_4_0"][0]
            self.myof.k_4_1 = hs_params["myofilament_parameters"]["k_4_1"][0]
            self.myof.k_cb = hs_params["myofilament_parameters"]["k_cb"][0]
            self.myof.x_ps = hs_params["myofilament_parameters"]["x_ps"][0]
            self.myof.k_on = float(hs_params["myofilament_parameters"]["k_on"][0])
            self.myof.k_off = hs_params["myofilament_parameters"]["k_off"][0]
            self.myof.k_coop = hs_params["myofilament_parameters"]["k_coop"][0]
            self.myof.bin_min = hs_params["myofilament_parameters"]["bin_min"][0]
            self.myof.bin_max = hs_params["myofilament_parameters"]["bin_max"][0]
            self.myof.bin_width = hs_params["myofilament_parameters"]["bin_width"][0]
            self.myof.thick_filament_length = hs_params["myofilament_parameters"]["thick_filament_length"][0]
            self.myof.thin_filament_length = hs_params["myofilament_parameters"]["thin_filament_length"][0]
            self.myof.bare_zone_length = hs_params["myofilament_parameters"]["bare_zone_length"][0]
            self.myof.k_falloff = hs_params["myofilament_parameters"]["k_falloff"][0]
