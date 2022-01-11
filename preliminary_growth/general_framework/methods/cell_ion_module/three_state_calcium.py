import numpy as np


## Uses the calcium transient from the three state paper
def init(params):
    model_class = three_state_ca(params)
    return model_class


class three_state_ca():

    def __init__(self,params):

        # Hard coding, have established this transient
        # these could be set in params if needed
        self.t_act = 0.03
        self.cardiac_period = 0.17



    def calculate_concentrations(self,cycle,time):

        # cycle doesn't matter, using cell time instead
        cycle = 0.0
        # Time is passed in as ms, not seconds
        t = float(time)/1000
        # Don't plan on using this transient much, hard coding some stuff
        #t_act = 0.0
        cardiac_period = .17
        t_p = cardiac_period*cycle + self.t_act+0.01
        fCa = 25
        fCa_2 = 2.5
        calcium_value = 0.0
        pCa = 0.0


        if t <= self.t_act:
            pCa = 7
            calcium_value = 10**(-1*pCa)
            #print >>file, 'first if'
        elif ((cardiac_period*cycle+self.t_act) < t) and (t < (t_p)):
            pCa = (t - (cardiac_period*cycle+self.t_act))/0.02
            calcium_value = (1 + 9*np.sin(3.14*pCa))*1E-7
            #print >>file, 'second if'
        elif (t >= t_p):
            pCa = 0.5*np.exp(-np.power((t - t_p)*fCa, fCa_2))
            #print >>file, 'third if'
            calcium_value = (1+9*np.sin(3.14*pCa))*1E-7

        #print >>file, t, calcium_value
        return calcium_value
