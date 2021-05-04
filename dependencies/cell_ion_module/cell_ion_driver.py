# So far these are only needed to test standalone
import sys
import numpy as np
sys.path.append("/home/fenics/shared/dependencies/cell_ion_module")
from scipy.integrate import solve_ivp

#sys.path.append("/Users/charlesmann/Academic/UK/fenics/source_code/dependencies/cell_ion_module")

## Class for cell ion models
#
#calculate calcium concentration (and other concentrations depending on the model) and ion voltage
class cell_ion_driver():

    def __init__(self,params,timestep_size,duration):

        # Specify model to be ran
        self.model_name = params["model"][0]
        self.model_params = params["model_inputs"]
        self.timestep = timestep_size

        #base_dir = "cell_ion_module"
        #model_name = base_dir + temp
        #model_name = "three_state_calcium"

        if self.model_name == "file_input":
            self.ca = np.load(self.model_params["path_to_calcium"][0])
            self.counter = 0

        if self.model_name == "three_state_calcium":
            self.t_act = 0.00
            self.cardiac_period = 0.17

        if self.model_name == "two_compartment":
            self.Ca_content = float(self.model_params["Ca_content"][0])
            self.k_leak = float(self.model_params["k_leak"][0])
            self.k_act = float(self.model_params["k_act"][0])
            self.k_serca = float(self.model_params["k_serca"][0])
            self.activation = np.zeros(int(duration/timestep_size))
            #self.activation[31:40]=1.0
            # user specifies activation start and stop
            act_start = self.model_params["act_start"][0]
            print 'act_start: ', act_start
            act_end = self.model_params["act_end"][0]
            act_open = self.model_params["act_open"][0]
            #self.activation[int(act_start/self.timestep):int(()/self.timestep)] = 1.0
            # For cyclical activation
            period = self.model_params["act_period"][0]
            for i in range(int((duration-act_start)/(period*self.timestep))+1):
                self.activation[int((i*period+act_start)/self.timestep):int((i*period+act_start+act_open)/self.timestep)] = 1.0
            print 'activation array: ', self.activation
            self.y = np.zeros(2)
            self.y[1] = self.Ca_content
            self.y[0] = 1e-7
            #self.y[0] = 0.0
            self.myofilament_Ca_conc = self.y[0]

        if self.model_name == "constant_calcium":
            self.basal_ca = self.model_params["basal_ca"][0]
            self.active_ca = self.model_params["active_ca"][0]
            self.t_act = self.model_params["t_act"][0]


        # Import the model
        #self.model = __import__(model_name)
        #self.model_class = self.model.init(model_params)


    def calculate_concentrations(self,time_step,l):

        if self.model_name == "file_input":

            calcium_value = self.ca[self.counter]
            self.counter+=1
            print "cell time = " + str(time)
            #return calcium_value

        if self.model_name == "three_state_calcium":
            cycle = 0.0
            # Time is passed in as ms, not seconds
            t = float(l)/1000
            print "calcium time is = " + str(t)
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

        if self.model_name == "two_compartment":
            y = self.y
            time_step = time_step*(1e-3)

            def derivs(t, y):
                dy = np.zeros(np.size(y))
                dy[0] = (self.k_leak + self.activation[l] * self.k_act) * y[1] - \
                        self.k_serca * y[0]
                dy[1] = -dy[0]
                return dy

            # Evolve
            sol = solve_ivp(derivs, [0, time_step], y, method = 'RK23')
            self.y = sol.y[:, -1]
            calcium_value = self.y[0]

        if self.model_name == "constant_calcium":

            if l < self.t_act:
                calcium_value = self.basal_ca
            else:
                calcium_value = self.active_ca

        return calcium_value
