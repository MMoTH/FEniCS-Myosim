import numpy as np


class myofilaments():
    """Class for myofilaments"""

    from .kinetics import evolve_kinetics, return_fluxes
    from .move import move_cb_distributions
    from .forces import set_myofilament_forces, check_myofilament_forces, \
        return_hs_length_for_force, return_passive_force

    def __init__(self, myofil_params, parent_half_sarcomere):
        self.parent_hs = parent_half_sarcomere

        # Thin filament
        self.k_on = float(myofil_params.k_on.cdata)
        self.k_off = float(myofil_params.k_off.cdata)
        self.k_coop = float(myofil_params.k_coop.cdata)

        self.kinetic_scheme = myofil_params.kinetic_scheme.cdata

        self.filament_compliance_factor = \
            float(myofil_params.filament_compliance_factor.cdata)

        self.bin_min = float(myofil_params.bin_min.cdata)
        self.bin_max = float(myofil_params.bin_max.cdata)
        self.bin_width = float(myofil_params.bin_width.cdata)

        self.x = np.arange(self.bin_min, self.bin_max+self.bin_width,
                           self.bin_width)
        self.no_of_x_bins = np.size(self.x)
        print(self.x)

        self.thick_filament_length = \
            float(myofil_params.thick_filament_length.cdata)
        self.thin_filament_length = \
            float(myofil_params.thin_filament_length.cdata)
        self.bare_zone_length = float(myofil_params.bare_zone_length.cdata)
        self.k_falloff = float(myofil_params.k_falloff.cdata)
        self.n_overlap = self.return_n_overlap()

        # Set up the rates and the y vector which are kinetics specific
        if (self.kinetic_scheme == '3state_with_SRX'):

            self.k_1 = float(myofil_params.k_1.cdata)
            self.k_force = float(myofil_params.k_force.cdata)
            self.k_2 = float(myofil_params.k_2.cdata)
            self.k_3 = float(myofil_params.k_3.cdata)
            self.k_4_0 = float(myofil_params.k_4_0.cdata)
            self.k_4_1 = float(myofil_params.k_4_1.cdata)
            self.k_cb = float(myofil_params.k_cb.cdata)
            self.x_ps = float(myofil_params.x_ps.cdata)

            self.y_length = self.no_of_x_bins + 4
            self.y = np.zeros(self.y_length)
            # Start with all myosins in M1 and all binding sites off
            self.y[0] = 1.0
            self.y[-2] = 1.0

        # Set up passive forces
        self.passive_mode = \
            myofil_params.passive_mode.cdata
            
        if (self.passive_mode == 'linear'):
            self.passive_linear_k_p = \
                float(myofil_params.passive_linear_k_p.cdata)
            self.passive_l_slack = \
                float(myofil_params.passive_l_slack.cdata)
        if (self.passive_mode == 'exponential'):
            self.passive_exp_sigma = \
                float(myofil_params.passive_exp_sigma.cdata)
            self.passive_exp_L = \
                float(myofil_params.passive_exp_L.cdata)
            self.passive_l_slack = \
                float(myofil_params.passive_l_slack.cdata)

        # Initialise forces and then update
        self.cb_force = 0.0
        self.pas_force = 0.0
        self.total_force= 0.0
        self.set_myofilament_forces()

    def return_n_overlap(self):
        """ returns n_overlap """
        x_no_overlap = self.parent_hs.hs_length - self.thick_filament_length
        x_overlap = self.thin_filament_length - x_no_overlap
        max_x_overlap = self.thick_filament_length - self.bare_zone_length

        if (x_overlap < 0.0):
            n_overlap = 0.0

        if ((x_overlap > 0.0) & (x_overlap <= max_x_overlap)):
            n_overlap = x_overlap / max_x_overlap

        if (x_overlap > max_x_overlap):
            n_overlap = 1.0

        if (self.parent_hs.hs_length < self.thin_filament_length):
            n_overlap = 1.0 + self.k_falloff * \
                (self.parent_hs.hs_length - self.thin_filament_length)
            if (n_overlap < 0.0):
                n_overlap = 0.0

        return n_overlap
