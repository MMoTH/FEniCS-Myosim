import numpy as np
import scipy.interpolate as interpol


def move_cb_distributions(self, delta_hsl):
    """ Moves cb distributions """

    delta_x = delta_hsl * self.filament_compliance_factor

    if (self.kinetic_scheme == '3state_with_SRX'):
        interp_positions = self.x - delta_x
        bin_indices = 2 + np.arange(0, self.no_of_x_bins)
        
        # Count bridges before
        before_heads = np.sum(self.y[bin_indices])
        self.y[bin_indices] = interpol.interp1d(self.x,
                                  self.y[bin_indices],
                                  fill_value=0,
                                  bounds_error=False)(interp_positions)

        # Make sure we don't have any negative populations
        temp = self.y[bin_indices]
        temp[np.nonzero(temp<0.0)] = 0.0
        self.y[bin_indices] = temp

        # Count bridges now
        after_heads = np.sum(self.y[bin_indices])
        # These appear in M_on
        self.y[1] = self.y[1] + (before_heads - after_heads)
