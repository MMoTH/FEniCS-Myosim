# @Author: charlesmann
# @Date:   2021-09-20T19:22:52-04:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-10-20T13:18:50-04:00



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
            self.cardiac_period = 0.2

        if self.model_name == "two_compartment_demo":
            self.Ca_content = float(self.model_params["Ca_content"][0])
            self.k_leak = float(self.model_params["k_leak"][0])
            self.k_act = float(self.model_params["k_act"][0])
            self.k_serca = float(self.model_params["k_serca"][0])
            self.activation = np.zeros(710)
            self.activation[91:100]=1.0
            #for jj in np.arange(30):
            #    self.activation[400+(12*jj+6):400+(12*jj+11)] = 1.0

            self.y = np.zeros(2)
            self.y[1] = self.Ca_content
            #self.y[0] = 1e-7
            self.y[0] = 0.0
            self.myofilament_Ca_conc = self.y[0]
            #self.model_name = "two_compartment"

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
            self.t_end = self.model_params["t_end"][0]

        if self.model_name == "rice_fit":
            self.diastolic_ca = self.model_params["diastolic_ca"][0]
            self.peak_ca = self.model_params["peak_ca"][0]
            self.tau_1 = self.model_params["tau_1"][0]
            self.tau_2 = self.model_params["tau_2"][0]
            self.t_act = self.model_params["t_act"][0]
            self.period = self.model_params["cardiac_period"][0]

        if self.model_name == "porcine_spline":
            self.breaks = [0.0,0.1,0.2,0.31,0.49,0.6] #times to switch to different splines in s
            self.period = 600 #ms
            self.coefs = np.zeros((5,4))
            self.coefs[0,0] = 0.46100006687048
            self.coefs[0,1] = -0.163627006687048
            self.coefs[0,2] = 0.0190527
            self.coefs[0,3] = 0.00027
            self.coefs[1,0] = 0.091539799388559
            self.coefs[1,1] = -0.025326986625904
            self.coefs[1,2] = 0.000157300668705
            self.coefs[1,3] = 0.001
            self.coefs[2,0] = -0.005276964220075
            self.coefs[2,1] = 0.002134953190664
            self.coefs[2,2] = -0.002161902674819
            self.coefs[2,3] = 0.000854
            self.coefs[3,0] = 0.005885946055328
            self.coefs[3,1] = 0.000393554998039
            self.coefs[3,2] = -0.001883766774062
            self.coefs[3,3] = 0.000635
            self.coefs[4,0] = 0.009373587527503
            self.coefs[4,1] = 0.003571965867916
            self.coefs[4,2] = -0.001169973018190
            self.coefs[4,3] = 0.000343
            self.coefs = self.coefs*(1e-4)
            self.spline_counter = 0


        # Import the model
        #self.model = __import__(model_name)
        #self.model_class = self.model.init(model_params)


    def calculate_concentrations(self,time_step,l,ind):

        if self.model_name == "file_input":

            calcium_value = self.ca[self.counter]
            self.counter+=1
            print "cell time = " + str(time)
            #return calcium_value

        if self.model_name == "three_state_calcium":
            cycle = 0.0
            # Time is passed in as ms, not seconds
            t = l%200
            t = float(t)/1000
            print "calcium time is = " + str(t)
            # Don't plan on using this transient much, hard coding some stuff
            #t_act = 0.0
            cardiac_period = .18
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

        if self.model_name == "two_compartment" or self.model_name == "two_compartment_demo":
            y = self.y
            time_step = time_step*(1e-3)

            def derivs(t, y):
                dy = np.zeros(np.size(y))
                dy[0] = (self.k_leak + self.activation[ind] * self.k_act) * y[1] - \
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
            elif self.t_act <= l and l < self.t_end:
                calcium_value = self.active_ca
            else:
                calcium_value = self.basal_ca

        if self.model_name == "rice_fit":
            print "l",l
            t = l%self.period
            t = float(t)/1000
            tau1 = self.tau_1
            tau2 = self.tau_2
            beta = (tau1/tau2)**(-1./((tau1/tau2)-1.))-(tau1/tau2)**(-1/(1-tau2/tau1))
            print "beta",beta
            if t < self.t_act:
                calcium_value = self.diastolic_ca
            else:
                calcium_value = self.diastolic_ca+((self.peak_ca-self.diastolic_ca)/beta)*(np.exp(-(t-self.t_act)/tau1)-np.exp(-(t-self.t_act)/tau2))

        if self.model_name == "porcine_spline":

            t = l%self.period

            if t < time_step:
                # started a new cycle, reset the spline counter
                self.spline_counter = 0

            t = float(t)/1000 # convert time to seconds


            if t < self.breaks[self.spline_counter+1]:
                # do nothing
                print "not updating spline counter"
            else:
                self.spline_counter +=1

            calcium_value = self.coefs[self.spline_counter,0]*((t-self.breaks[self.spline_counter])**3) + \
                        self.coefs[self.spline_counter,1]*((t-self.breaks[self.spline_counter])**2) + \
                        self.coefs[self.spline_counter,2]*(t-self.breaks[self.spline_counter]) + \
                        self.coefs[self.spline_counter,3]



        return calcium_value
