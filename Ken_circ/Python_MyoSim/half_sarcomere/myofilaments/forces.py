# Functions relating to forces
import numpy as np
import scipy.optimize as opt


def set_myofilament_forces(self):
    self.cb_force = return_cb_force(self, 0.0)
    self.pas_force = return_passive_force(self, 0.0)
    self.total_force = self.cb_force + self.pas_force


def check_myofilament_forces(self, delta_hsl):
    d = dict()
    d['cb_force'] = return_cb_force(self, delta_hsl)
    d['pas_force'] = return_passive_force(self, delta_hsl)
    d['total_force'] = d['cb_force'] + d['pas_force']
    return d


def return_cb_force(self, delta_hsl):
    if (self.kinetic_scheme == '3state_with_SRX'):
        bin_pops = self.y[2 + np.arange(0, self.no_of_x_bins)]
        cb_force = \
            self.parent_hs.cb_number_density * \
            self.k_cb * 1e-9 * \
            np.sum(bin_pops * (self.x + self.x_ps +
                               (self.filament_compliance_factor * delta_hsl)))
        return cb_force

def return_x(self,x):
    return x



def return_passive_force(self, delta_hsl):

    if (self.passive_mode == 'linear'):
        pas_force = self.passive_linear_k_p * \
            (self.parent_hs.hs_length + delta_hsl -
             self.passive_l_slack)

    if (self.passive_mode == 'exponential'):
        x = self.parent_hs.hs_length + delta_hsl - self.passive_l_slack
        if (x > 0):
            pas_force = self.passive_exp_sigma * \
                (np.exp(x / self.passive_exp_L) - 1.0)
        else:
            pas_force = -self.passive_exp_sigma * \
                (np.exp(np.abs(x) / self.passive_exp_L) - 1.0)

    return pas_force


def return_hs_length_for_force(self, force):
    
    def f(dx):
        d = check_myofilament_forces(self, dx)
        return d['total_force']
    
    sol = opt.brentq(f,-1000, 1000)
    return self.parent_hs.hs_length + sol

