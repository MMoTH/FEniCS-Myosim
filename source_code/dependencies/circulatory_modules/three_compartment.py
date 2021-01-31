import numpy as np

## Initialize three compartment windkessel
def init(params,v0):
    model_class = three_compartment(params, v0)
    return model_class


class three_compartment():

    def __init__(self, params, vcav_init):

        self.Cao = params["Cao"][0]
        self.Cven = params["Cven"][0]
        self.Vart0 = params["Vart0"][0]
        self.Vven0 = params["Vven0"][0]
        self.Rao = params["Rao"][0]
        self.Rven = params["Rven"][0]
        self.Rper = params["Rper"][0]
        self.V_ven = params["V_ven"][0]
        self.V_art = params["V_art"][0]


        print vcav_init
        self.V_cav = vcav_init

        self.Part = 0.0
        self.Pven = 0.0

        self.MV_old = 0
        self.MV_new = 0
        self.AV_old = 1
        self.AV_new = 0




    def load_LV(self):

        self.V_cav += 0.004

        return self.V_cav





    def return_new_LV_volume(self, p_cav, v_cav, step_size):

        self.V_cav = v_cav
        # calculate pressures in compartments
        PLV = p_cav
        self.return_pressures()

        # use pressures to calculate new flows between compartments
        Qao, Qmv, Qper = self.return_flows(PLV)

        """V_cav_prev = V_cav
        V_art_prev = V_art
        V_ven_prev = V_ven
        p_cav_prev = p_cav"""

        self.V_cav += step_size*(Qmv - Qao);
        self.V_art += step_size*(Qao - Qper);
        self.V_ven += step_size*(Qper - Qmv);

        return self.V_cav, self.V_ven, self.V_art

    def return_pressures(self):
        self.P_art = 1.0/self.Cao*(self.V_art - self.Vart0);
        self.P_ven = 1.0/self.Cven*(self.V_ven - self.Vven0);


    def return_flows(self, PLV):
        # need to calculate flow between compartments
        if(PLV <= self.Part):

            Qao = 0.0;
            self.AV_new = 0

        else:

            Qao = 1.0/self.Rao*(PLV - self.Part);
            self.AV_new = 1


        if(PLV >= self.Pven):

            Qmv = 0.0;
            self.MV_new = 0

        else:

            Qmv = 1.0/self.Rven*(self.Pven - PLV);
            self.MV_new = 1

        Qper = 1.0/self.Rper*(self.Part - self.Pven);

        return Qao, Qmv, Qper

    def is_systole(self):
        systole = 0
        if(self.MV_old == 1 and self.MV_new == 0):
            systole = 1
        if(self.AV_old == 1 and self.AV_new == 0):
            systole = 0

        self.MV_old = self.MV_new
        self.AV_old = self.AV_new

        if systole:
            print "********* systole *********"
        else:
            print "********** diastole **********"
