from dolfin import *
import sys
#sys.path.append("/mnt/home/f0101140/Desktop/FEniCS-Myosim/dependencies/")
#sys.path.append("/mnt/home/f0101140/Desktop/FEniCS-Myosim/source_code/")
sys.path.append("/home/fenics/shared/dependencies/")
sys.path.append("/home/fenics/shared/source_code/")
from forms import Forms

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


    def grow_ellipsoid(self,mesh,concentric_growth_stimulus,p_cav,expr,bcs,fdataPV,Wp,w,wtest,dx,c11,X,u,dw,displacement_file,uflforms,Pactive,Fmat,v):

        print "called grow_ellipsoid function"

        #pseudo code for now
        # Need mesh passed in, growth stimulus
        # concentric_growth_stimulus = loaded_stimulus
        set_point_stimulus = Function(self.fcn_space)
        # Specific to this simulation:
        assign(set_point_stimulus,concentric_growth_stimulus)
        set_point_stimulus*=0.9
        set_point_stimulus = project(set_point_stimulus,FunctionSpace(mesh,"DG",1))
        #

        # Save current EDP?
        original_edp = p_cav
        # Need boundary conditions passed in?
        # Will need the dictionary of expressions as well
        # Need reference cavity volume saved, initialized as class property?
        # Need fdataPV file pointer

        # Need to unload the ventricle
        #------------------------------------

        # Going to try to incrementally get rid of active stress
        active_stress_copy = 0.5*Pactive


        # First, solve variational problem without active stress
        # Define F1 - F4 but omit active stress term
        #uflforms = Forms()
        F1 = derivative(Wp, w, wtest)*dx
        F2 = inner(Fmat*Pactive, grad(v))*dx

        Wvol = uflforms.LVV0constrainedE()
        F3 = derivative(Wvol, w, wtest)

        # constrain rigid body motion
        L4 = inner(as_vector([c11[0], c11[1], 0.0]), u)*dx + \
    	 inner(as_vector([0.0, 0.0, c11[2]]), cross(X, u))*dx + \
    	 inner(as_vector([c11[3], 0.0, 0.0]), cross(X, u))*dx + \
    	 inner(as_vector([0.0, c11[4], 0.0]), cross(X, u))*dx

        F4 = derivative(L4, w, wtest)

        Ftot = F1 +F2+ F3 + F4
        Jac1 = derivative(F1, w, dw)
        Jac2 = derivative(F2, w, dw)
        Jac3 = derivative(F3, w, dw)
        Jac4 = derivative(F4, w, dw)

        Jac = Jac1 +Jac2+ Jac3 + Jac4

        solve(Ftot == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})



        # Then, unload the LV back to reference volume?
        current_volume = expr["LVCavityvol"].vol
        reference_volume = 0.0969230305108 # hard coded for this ellipsoid mesh
        vol_increment = (current_volume - reference_volume)/10 # 10 is arbitrary
        for i in np.arange(10):
            expr["LVCavityvol"].vol -= vol_increment
            solve(Ftot == 0, w, bcs, J = Jac, form_compiler_parameters={"representation":"uflacs"})
            displacement_file << w.sub(0)

        #    save displacement to view and check it

        # INSTEAD OF UNLOADING, START WITH ORIGINAL UNLOADED MESH? Do we have to rebuild everything after that though?

        # Update theta1, theta2, theta3 in general. Here, just for concentric, update theta2 and theta3
        # Need the current stimulus value (will come from previous cycle for now, end systolic active stress?)
        # stim_value_projected = ...
        #
        # theta2 += (1./self.s0_time_constant)*((stim_fcn_projected - set_point_fcn)/set_point_fcn) # try time constant of one
        # solve()
        # Update Pressure, volume of cavity
        #    save displacement to view and check it

        # Set current displacement as new reference configuration
        # ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))
        # Save displacement to view this?

        # Re load ventricle
        # while pressure < original_EDP:
        #     expr["LVCavityvol"].vol += vol_increment
        #     solve()
        #     save displacement to view and check it
        #     p_cav = uflforms.LVcavitypressure()
        #     V_cav = uflforms.LVcavityvol()
        #     if(MPI.rank(comm) == 0):
        #         print >>fdataPV, 0.0, p_cav*0.0075 , 0.0, 0.0, V_cav, 0.0, 0.0, 0.0

        # Try to solve variational problem with active stress. May be too big of a jump
        # solve()
        # update half-sarcomere length information
        # pass all information back to simulation
        # return ...
