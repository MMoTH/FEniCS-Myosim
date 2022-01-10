# @Author: charlesmann
# @Date:   2022-01-06T12:21:52-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-06T12:57:38-05:00



import sys
import numpy as np

class circulatory_system():

    def __init__(self,params):

        # Initialize what is needed for chosen circulatory model
        # params is the dictionary imported from the instruction file

        # WILL NEED TO MAKE SURE THINGS ARE INITIALIZED FROM A PREVIOUS SIMULATION
        # STATE CORRECTLY

        if params["model"][0] == "three_compartment_wk":

            self.model = "three_compartment_wk"
            self.Cao   = params["Cao"][0]
            self.Cven  = params["Cven"][0]
            self.Vart0 = params["Vart0"][0]
            self.Vven0 = params["Vven0"][0]
            self.Rao   = params["Rao"][0]
            self.Rven  = params["Rven"][0]
            self.Rper  = params["Rper"][0]
            self.V_ven = params["V_ven"][0]
            self.V_art = params["V_art"][0]

            # Markers for where you are in the cardiac cycle
            self.AV_old = 0
            self.MV_old = 1
            self.systole = 0
            self.AV_new = 0
            self.MV_new = 0
            self.end_systole = 0

            # Compartment pressures
            if "Part" in params.keys():
                # from a previous simulation state, load it in
                self.Part = params["Part"]
                self.Pven = params["Pven"]
                self.PLV = params["PLV"]
            else:
                # first cycle, intialize to zero
                self.Part = 0.0
                self.Pven = 0.0
                self.PLV = 0.0

            # Flow between compartments
            self.Qao = 0.0
            self.Qmv = 0.0
            self.Qper = 0.0

            # Volumes of compartments
            #self.V_cav = 0.0
            #self.V_art = 0.0
            #self.V_ven = 0.0

            # output dictionary
            self.output_dict = {}

    def update_compartments(self,p_cav,V_cav,step_size):

        if self.model == "three_compartment_wk":

            # Always set "end_systole" tp 0. Should only switch to 1 once
            self.end_systole = 0
            self.end_diastole = 0
            print "updating windkessel"

            self.V_cav = V_cav
            self.Part = 1.0/self.Cao*(self.V_art - self.Vart0);
            self.Pven = 1.0/self.Cven*(self.V_ven - self.Vven0);
            self.PLV = p_cav;

            print "LV pressure = ",self.PLV
            print "Aorta pressure = ",self.Part
            print "Venous pressure = ",self.Pven

            if(self.PLV <= self.Part):

                self.Qao = 0.0;
                self.AV_new = 0

            else:
                print "ejection"

                self.Qao = 1.0/self.Rao*(self.PLV - self.Part);
                self.AV_new = 1
                print "flow into aorta = ",self.Qao


            if(self.PLV >= self.Pven):

                self.Qmv = 0.0;
                self.MV_new = 0

            else:

                self.Qmv = 1.0/self.Rven*(self.Pven - self.PLV);
                self.MV_new = 1

            self.Qper = 1.0/self.Rper*(self.Part - self.Pven);

            if(self.MV_old == 1 and self.MV_new == 0):
                self.end_diastole = 1
                self.systole = 1
            if(self.AV_old == 1 and self.AV_new == 0):
                self.systole = 0
                self.end_systole = 1

            self.MV_old = self.MV_new
            self.AV_old = self.AV_new

            self.V_cav = self.V_cav + step_size*(self.Qmv - self.Qao);
            self.V_art = self.V_art + step_size*(self.Qao - self.Qper);
            self.V_ven = self.V_ven + step_size*(self.Qper - self.Qmv);

            print "Qmv pressure = ",self.Qmv
            print "Qao pressure = ",self.Qao
            print "Qper pressure = ",self.Qper


            self.output_dict["V_cav"] = self.V_cav
            self.output_dict["p_cav"] = p_cav
            self.output_dict["V_art"] = self.V_art
            self.output_dict["V_ven"] = self.V_ven
            self.output_dict["Pven"] = self.Pven
            self.output_dict["Part"] = self.Part
            self.output_dict["end_systole"] = self.end_systole
            self.output_dict["end_diastole"] = self.end_diastole

        return self.output_dict
