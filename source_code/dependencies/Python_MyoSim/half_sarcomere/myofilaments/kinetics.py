# Functions for myofilament kinetics
import numpy as np
import scipy.constants as scipy_constants
from scipy.integrate import solve_ivp


def evolve_kinetics(self, time_step, Ca_conc, cell_time):
    """Updates kinetics, switches to different sub-functions as required"""
    if (self.kinetic_scheme[0] == '3state_with_SRX'):
        update_3state_with_SRX(self, time_step, Ca_conc,cell_time)

def return_fluxes(self, y, Ca_conc):
    # Returns fluxes
    if (self.kinetic_scheme[0] == '3state_with_SRX'):

        # Unpack
        M_OFF = y[0]
        M_ON = y[1]
        M_bound = y[2 + np.arange(self.no_of_x_bins)]
        n_off = y[-2]
        n_on = y[-1]
        n_bound = np.sum(M_bound)

        r1 = np.minimum(self.parent_hs.max_rate,
                        self.k_1 *(1.0 + self.k_force * self.parent_hs.hs_force))
        J1 = r1 * M_OFF

        r2 = np.minimum(self.parent_hs.max_rate, self.k_2)
        J2 = r2 * M_ON

        r3 = self.k_3 * \
                np.exp(-self.k_cb * (self.x**2) /
                    (2.0 * 1e18 * scipy_constants.Boltzmann * self.parent_hs.temperature))
        r3[r3 > self.parent_hs.max_rate] = self.parent_hs.max_rate
        J3 = r3 * self.bin_width * M_ON * (n_on - n_bound)

        r4 = self.k_4_0 + (self.k_4_1 * np.power(self.x, 4))
        r4[r4 > self.parent_hs.max_rate] = self.parent_hs.max_rate
        J4 = r4 * M_bound
        if (self.n_overlap > 0.0):
            Jon = (self.k_on * Ca_conc * (self.n_overlap - n_on) *
            (1.0 + self.k_coop * (n_on / self.n_overlap)))
        else:
            Jon = 0.0

        if (self.n_overlap > 0.0):
            Joff = self.k_off * (n_on - n_bound) * \
            (1.0 + self.k_coop * ((self.n_overlap - n_on) / self.n_overlap))
        else:
            Joff = 0.0
        """if (self.n_overlap > 0.0):
            if self.n_overlap > n_on:
                Jon = (self.k_on * Ca_conc * (self.n_overlap - n_on) *
                (1.0 + self.k_coop * (n_on / self.n_overlap)))
            else:
                # overlap has fallen equal to, or below n_on
                # force n_on to be the same as the overlap
                n_on_new = self.n_overlap
                self.y[-1] = n_on_new
                # Take ones that were forced off, put in n_off population
                self.y[-2] += n_on-n_on_new
                # Re-update n_on in case it's used in any other calculations
                n_on = n_on_new
                # Finally, set Jon to zero so no more sites activate
                Jon = 0.0
        else:
            # Overlap is zero, force n_on to be zero as well. If any binding sites are turned
            # off from this, put them back in n_off
            n_on_new = self.n_overlap
            self.y[-1] = n_on_new
            self.y[-2] += n_on - n_on_new
            n_on = n_on_new
            Jon = 0.0

        if (self.n_overlap > 0.0):
            if self.n_overlap > n_on:
                Joff = self.k_off * (n_on - n_bound) * \
                (1.0 + self.k_coop * ((self.n_overlap - n_on) /
                                      self.n_overlap))

            else:
                Joff = self.k_off * (n_on - n_bound)
        else:
            Joff = 0.0"""

        fluxes = dict()
        fluxes['J1'] = J1
        fluxes['J2'] = J2
        fluxes['J3'] = J3
        fluxes['J4'] = J4
        fluxes['Jon'] = Jon
        fluxes['Joff'] = Joff
        #fluxes['d_overlap_dt'] = self.n_overlap-old_overlap
        #print fluxes['d_overlap_dt']

        rates = dict()
        rates['R1'] = r1
        rates['R2'] = r2
        rates['R3'] = r3
        rates['R4'] = r4

        return fluxes, rates


def update_3state_with_SRX(self, time_step, Ca_conc, cell_time):
    """ Updates kinetics for thick and thin filaments """

    # Pull out the myofilaments vector
    y = self.y
    # Get the overlap
    self.n_overlap = self.return_n_overlap()

    def derivs(t, y):
        dy = np.zeros(np.size(y))

        fluxes, rates = return_fluxes(self, y, Ca_conc)

        # Calculate the derivs
        dy[0] = -fluxes['J1'] + fluxes['J2']
        dy[1] = (fluxes['J1'] + np.sum(fluxes['J4'])) - \
            (fluxes['J2'] + np.sum(fluxes['J3']))
        J3 = fluxes['J3']
        J4 = fluxes['J4']
        for i in np.arange(0, self.no_of_x_bins):
            dy[i + 2] = J3[i] - J4[i]
        dy[-2] = -fluxes['Jon'] + fluxes['Joff'] #- fluxes['d_overlap_dt']
        dy[-1] = fluxes['Jon'] - fluxes['Joff']
        return dy

    # Evolve the system

    sol = solve_ivp(derivs, [0, time_step], y, method='RK23')
    #self.y[26] = 0.01*(1+np.sin((1.0/16.0)*cell_time+80.2))
    #print self.y[13]
    self.y = sol.y[:, -1]
    self.n_on = y[-1]
    self.n_bound = np.sum(self.y[2 + np.arange(0, self.no_of_x_bins)])


    # Do some tidying for extreme situations
    self.y[np.nonzero(self.y > 1.0)] = 1.0
    self.y[np.nonzero(self.y < 0.0)] = 0.0
    sum_of_heads = np.sum(self.y[np.arange(2+self.no_of_x_bins)])
    # These appear in M_off
    self.y[0] = self.y[0] + (1.0-sum_of_heads)

#    print("Total: %f" % np.sum(self.y[np.arange(0, self.no_of_x_bins+2)]))
#    if any(self.y < -1e-2):
#        print(self.y)
#        print("self.y is less than 0")
#        quit()
