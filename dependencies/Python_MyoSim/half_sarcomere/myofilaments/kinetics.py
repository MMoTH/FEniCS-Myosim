# @Author: charlesmann
# @Date:   2022-07-26T08:20:25-04:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-07-26T08:31:57-04:00



# Functions for myofilament kinetics
import numpy as np
import scipy.constants as scipy_constants
from scipy.integrate import solve_ivp


def evolve_kinetics(self, time_step, Ca_conc, cell_time):
    """Updates kinetics, switches to different sub-functions as required"""
    if (self.kinetic_scheme[0] == '3state_with_SRX'):
        update_3state_with_SRX(self, time_step, Ca_conc,cell_time)

    if (self.kinetic_scheme[0] == '4state_with_SRX') or (self.kinetic_scheme[0] == 'new4state_with_SRX'):
        update_4state_with_SRX(self, time_step, Ca_conc,cell_time)

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

        if Jon <= 0.0:
            Jon = 0.0

        if (self.n_overlap > 0.0):
            Joff = self.k_off * (n_on - n_bound) * \
            (1.0 + self.k_coop * ((self.n_overlap - n_on) / self.n_overlap))
        else:
            Joff = 0.0
        if Joff <= 0.0:
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

    # Returns fluxes
    if (self.kinetic_scheme[0] == '4state_with_SRX'):

        # Pre-calculate rates

        r1 = np.minimum(self.parent_hs.max_rate,
                        self.k_1 *(1.0 + self.k_force * self.parent_hs.hs_force))

        r2 = np.minimum(self.parent_hs.max_rate, self.k_2)

        r3 = self.k_3 * \
                np.exp(-self.k_cb * (self.x**2) /
                    (2.0 * 1e18 * scipy_constants.Boltzmann * self.parent_hs.temperature))
        r3[r3 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r4 = self.k_4_0 + (self.k_4_1 * np.power(self.x, 4))
        r4[r4 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r5 = self.k_5_0 / \
                (1.0 + np.exp(self.k_5_1 * (self.x + (self.x_ps / 2.0))))
        r5[r5 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r6 = self.k_6 * np.ones(len(self.x))
        r6[r6 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r7 = self.k_7_0 + (self.k_7_1 * np.power(self.x, 4))
        r7[r7 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r8 = self.k_8 * np.ones(len(self.x))
        r8[r8 > self.parent_hs.max_rate] = self.parent_hs.max_rate


#        print("rates")
#        print(r1)
#        print(r2)
#        print(r3)
#        print(r4)
#        print(r5)
#        print(r6)
#        print(r7)
#        print(r8)
#        exit()


        # Unpack
        M3_indices = 2 + np.arange(0, self.no_of_x_bins)
        M4_indices = (2 + self.no_of_x_bins) + \
                    np.arange(0, self.no_of_x_bins)

        M_OFF = y[0]
        M_ON = y[1]
        M_3 = y[M3_indices]
        M_4 = y[M4_indices]
        M_bound = M_3 + M_4
        n_off = y[-2]
        n_on = y[-1]
        n_bound = np.sum(M_bound)

        # Calculate fluxes
        J1 = r1 * M_OFF
        J2 = r2 * M_ON
        J3 = r3 * self.bin_width * M_ON * (n_on - n_bound)
        J4 = r4 * M_3
        J5 = r5 * M_3
        J6 = r6 * M_4
        J7 = r7 * M_4
        J8 = r8 * self.bin_width * M_ON * (n_on - n_bound)

        if (self.n_overlap > 0.0):
            Jon = (self.k_on * Ca_conc * (self.n_overlap - n_on) *
                (1.0 + self.k_coop * (n_on / self.n_overlap)))
        else:
            Jon = 0.0

        if (self.n_overlap > 0.0):
            Joff = self.k_off * (n_on - n_bound) * \
                (1.0 + self.k_coop * ((self.n_overlap - n_on) /
                                      self.n_overlap))
        else:
            Joff = 0.0

        fluxes = dict()
        fluxes['J1'] = J1
        fluxes['J2'] = J2
        fluxes['J3'] = J3
        fluxes['J4'] = J4
        fluxes['J5'] = J5
        fluxes['J6'] = J6
        fluxes['J7'] = J7
        fluxes['J8'] = J8
        fluxes['Jon'] = Jon
        fluxes['Joff'] = Joff

        rates = dict()
        rates['R1'] = r1
        rates['R2'] = r2
        rates['R3'] = r3
        rates['R4'] = r4
        rates['R5'] = r5
        rates['R6'] = r6
        rates['R7'] = r7
        rates['R8'] = r8

        return fluxes, rates

    # Returns fluxes
    if (self.kinetic_scheme[0] == 'new4state_with_SRX'):

        # Pre-calculate rates

        r1 = np.minimum(self.parent_hs.max_rate,
                        self.k_1 *(1.0 + self.k_force * self.parent_hs.hs_force))

        r2 = np.minimum(self.parent_hs.max_rate, self.k_2)

        r3 = self.k_3 * \
                np.exp(-self.k_cb * (self.x**2) /
                    (2.0 * 1e18 * scipy_constants.Boltzmann * self.parent_hs.temperature))
        r3[r3 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r4 = self.k_4_0 + (self.k_4_1 * np.power(self.x, 4))
        r4[r4 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r5 = self.k_5_0 * np.ones(len(self.x))
        r5[r5 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r6 = self.k_6 * np.ones(len(self.x))
        r6[r6 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r7 = self.k_7_0 + (self.k_7_1 * np.power(self.x, 4))
        r7[r7 > self.parent_hs.max_rate] = self.parent_hs.max_rate

        r8 = self.k_8 * np.ones(len(self.x))
        r8[r8 > self.parent_hs.max_rate] = self.parent_hs.max_rate


#        print("rates")
#        print(r1)
#        print(r2)
#        print(r3)
#        print(r4)
#        print(r5)
#        print(r6)
#        print(r7)
#        print(r8)
#        exit()


        # Unpack
        M3_indices = 2 + np.arange(0, self.no_of_x_bins)
        M4_indices = (2 + self.no_of_x_bins) + \
                    np.arange(0, self.no_of_x_bins)

        M_OFF = y[0]
        M_ON = y[1]
        M_3 = y[M3_indices]
        M_4 = y[M4_indices]
        M_bound = M_3 + M_4
        n_off = y[-2]
        n_on = y[-1]
        n_bound = np.sum(M_bound)

        # Calculate fluxes
        J1 = r1 * M_OFF
        J2 = r2 * M_ON
        J3 = r3 * self.bin_width * M_ON * (n_on - n_bound)
        J4 = r4 * M_3
        J5 = r5 * M_3
        J6 = r6 * M_4
        J7 = r7 * M_4
        J8 = r8 * self.bin_width * M_ON * (n_on - n_bound)

        if (self.n_overlap > 0.0):
            Jon = (self.k_on * Ca_conc * (self.n_overlap - n_on) *
                (1.0 + self.k_coop * (n_on / self.n_overlap)))
        else:
            Jon = 0.0

        if (self.n_overlap > 0.0):
            Joff = self.k_off * (n_on - n_bound) * \
                (1.0 + self.k_coop * ((self.n_overlap - n_on) /
                                      self.n_overlap))
        else:
            Joff = 0.0

        fluxes = dict()
        fluxes['J1'] = J1
        fluxes['J2'] = J2
        fluxes['J3'] = J3
        fluxes['J4'] = J4
        fluxes['J5'] = J5
        fluxes['J6'] = J6
        fluxes['J7'] = J7
        fluxes['J8'] = J8
        fluxes['Jon'] = Jon
        fluxes['Joff'] = Joff

        rates = dict()
        rates['R1'] = r1
        rates['R2'] = r2
        rates['R3'] = r3
        rates['R4'] = r4
        rates['R5'] = r5
        rates['R6'] = r6
        rates['R7'] = r7
        rates['R8'] = r8

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

def update_4state_with_SRX(self, time_step, Ca_conc, cell_time):
    """ updates kinetics for thick and thin filaments with 4 state system """

    # Pull out the myofilaments vector
    y = self.y

    # Get the overlap
    self.n_overlap = self.return_n_overlap()

    def derivs(t, y):
        dy = np.zeros(np.size(y))

        fluxes, rates = return_fluxes(self, y, Ca_conc)

        # Calculate the derivs
        dy[0] = -fluxes['J1'] + fluxes['J2']
        dy[1] = (fluxes['J1'] + np.sum(fluxes['J4']) + np.sum(fluxes['J7'])) - \
                (fluxes['J2'] + np.sum(fluxes['J3']) + np.sum(fluxes['J8']))
        J3 = fluxes['J3']
        J4 = fluxes['J4']
        J5 = fluxes['J5']
        J6 = fluxes['J6']
        J7 = fluxes['J7']
        J8 = fluxes['J8']
        for i in np.arange(0, self.no_of_x_bins):
            dy[i + 2] = (J3[i] + J6[i]) - (J4[i] + J5[i])
            dy[i + self.no_of_x_bins + 2] = \
                (J5[i] + J8[i]) - (J6[i] + J7[i])
        dy[-2] = -fluxes['Jon'] + fluxes['Joff']
        dy[-1] = fluxes['Jon'] - fluxes['Joff']

        return dy

    # Evolve the system
    sol = solve_ivp(derivs, [0, time_step], y, method='RK23')
    self.y = sol.y[:, -1]
    self.n_on = y[-1]
    self.n_bound = np.sum(self.y[2 + np.arange(0, self.no_of_x_bins)]) + \
                    np.sum(self.y[2 + self.no_of_x_bins +
                                  np.arange(0, self.no_of_x_bins)])

    # Do some tidying for extreme situations
    self.y[np.nonzero(self.y > 1.0)] = 1.0
    self.y[np.nonzero(self.y < 0.0)] = 0.0
    sum_of_heads = np.sum(self.y[np.arange(2+(2*self.no_of_x_bins))])
    # These appear in M_off
    self.y[0] = self.y[0] + (1.0-sum_of_heads)

#    print("Total: %f" % np.sum(self.y[np.arange(0, self.no_of_x_bins+2)]))
#    if any(self.y < -1e-2):
#        print(self.y)
#        print("self.y is less than 0")
#        quit()
