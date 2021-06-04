from dolfin import *

class growth():

    def __init__(self,growth_params,quad_fcn_space,time_step):

        self.f0_stimulus = growth_params["f0_stimulus"][0]
        self.f0_set_point = growth_params["f0_set_point"][0]
        self.f0_time_constant = growth_params["f0_time_constant"][0]
        self.f0_growth_start = growth_params["f0_growth_start"][0]

        self.s0_stimulus = growth_params["s0_stimulus"][0]
        self.s0_set_point = growth_params["s0_set_point"][0]
        self.s0_time_constant = growth_params["s0_time_constant"][0]
        self.s0_growth_start = growth_params["s0_growth_start"][0]

        self.n0_stimulus = growth_params["n0_stimulus"][0]
        self.n0_set_point = growth_params["n0_set_point"][0]
        self.n0_time_constant = growth_params["n0_time_constant"][0]
        self.n0_growth_start = growth_params["n0_growth_start"][0]

        self.time_step = time_step
        self.fcn_space = quad_fcn_space

        # right now, using one stimulus for all directions
        #self.stim_fcn = Function(quad_fcn_space)

    def grow_mesh(self,S_passive, f0,theta1,theta2,theta3,time):
        print "successfully called grow_mesh"

        if time >= self.f0_growth_start:

            # right now, hard coding in passive stress in f0 direction as stimulus
            stim_fcn = inner(f0,S_passive*f0)
            stim_fcn_projected = project(stim_fcn,self.fcn_space,form_compiler_parameters={"representation":"uflacs"})
            print "stim fcn"
            #print stim_fcn_projected.vector().get_local()
            set_point_fcn = Function(self.fcn_space)
            set_point_fcn.vector()[:] = self.f0_set_point
            #print set_point_fcn.vector().get_local()
            print "assigned stim fcn"

            theta1 += (1./self.f0_time_constant)*((stim_fcn_projected - set_point_fcn)/set_point_fcn)
            #theta2 = 1 + (1./self.f0_time_constant)*((stim_fcn - set_point_fcn)/set_point_fcn)*self.time_step
            #theta3 = 1 + (1./self.f0_time_constant)*((stim_fcn - set_point_fcn)/set_point_fcn)*self.time_step
            theta2 = 1.
            theta3 = theta2

        return theta1,theta2,theta3
