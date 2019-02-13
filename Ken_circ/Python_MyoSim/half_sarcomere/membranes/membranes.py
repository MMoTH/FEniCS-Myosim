import numpy as np
#from scipy.integrate import solve_ivp
from scipy import integrate

from functools import partial

from .Ten_Tusscher_2004 import computeRates_with_activation as \
tt_computeRates_with_activation

class membranes():
    """ Class for membranes """
    
    def __init__(self, membrane_params, parent_half_sarcomere):
        self.parent_hs = parent_half_sarcomere;

        self.kinetic_scheme = membrane_params.kinetic_scheme.cdata

        # Set up the rates and the y vector which are kinetics specific
        if (self.kinetic_scheme == "simple_2_compartment"):
            self.Ca_content = float(membrane_params.Ca_content.cdata)
            self.k_leak = float(membrane_params.k_leak.cdata)
            self.k_act = float(membrane_params.k_act.cdata)
            self.k_serca = float(membrane_params.k_serca.cdata)

            self.y = np.zeros(2)
            self.y[1] = self.Ca_content

            self.myofilament_Ca_conc = self.y[0]

        if (self.kinetic_scheme == "Ten_Tusscher_2004"):
            (self.y, self.constants) = tt.initConsts()
            # Ten_Tusscher model assumese Ca_conc is in mM
            self.myofilament_Ca_conc = 0.001*self.y[3]

    def evolve_kinetics(self, time_step, activation):
        """ evolves kinetics """

        if (self.kinetic_scheme == "simple_2_compartment"):
            # Pull out the v vector
            y = self.y
            
            def derivs(t, y):
                dy = np.zeros(np.size(y))
                dy[0] = (self.k_leak + activation * self.k_act) * y[1] - \
                        self.k_serca * y[0]
                dy[1] = -dy[0]
                return dy
    
            # Evolve
            sol = solve_ivp(derivs, [0, time_step], y, method = 'RK23')
            self.y = sol.y[:, -1]
            self.myofilament_Ca_conc = self.y[0]

        if (self.kinetic_scheme == "Ten_Tusscher_2004"):
            # Ten_Tusscher model assumes time step is in ms
            sol = solve_ivp(partial(tt_computeRates_with_activation,
                                    constants=self.constants,
                                    activation=activation),
                            [0, 1000*time_step], self.y,
                            method='BDF')
            self.y = sol.y[:, -1]
            # Ten_Tusscher model assumese Ca_conc is in mM
            self.myofilament_Ca_conc = 0.001*self.y[3]
