import sys
import json
import os
sys.path.append("/home/fenics/shared/source_code/pso")
sys.path.append("/home/fenics/shared/source_code/fenics_cases")
import fenicsParticle
import matplotlib.pyplot as plt
import numpy as np
import generate_initial_position as g
import objective_functions
from objective_functions import objective_driver
import copy
#import objective_functions as obj_funcs

## Call this from fenics_driver? Pass in parameters?
def particle_swarm_optimization(pso_params,sim_params,file_inputs,output_params,passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params,fenics_script):

    # Get particles for simulations
    # Generalize this
    params = [sim_params, file_inputs, output_params, passive_params,hs_params,cell_ion_params,monodomain_params,windkessel_params]

    base_output_dir = output_params["output_path"][0]

    # Assign optimization parameters
    max_iterations = pso_params["max_iterations"][0]
    convergence_threshold = pso_params["convergence_threshold"][0] # use a relative error??
    num_particles = pso_params["num_particles"][0]
    dimensionality = pso_params["num_variables"][0]
    variables_and_bounds = pso_params["variables_and_bounds"] # dictionary of variables and their bounds
    w = pso_params["w"][0] # Velocity inertial parameter
    c1 = pso_params["c1"][0] # Weight for particle position
    c2 = pso_params["c2"][0] # Weight for best swarm position
    point_generation_scheme = pso_params["point_generation"][0] # goal is to have different init schemes
    objective_function_file = pso_params["objective_fcn_file"][0]
    objective_function = objective_driver.objective_driver(objective_function_file)
    #obj_func_class = objective_function.objFunc_class()

    # initalize data holders
    particle_errors = np.zeros((max_iterations,num_particles))
    opt_history = { \
    "global_error_history": [],
    "best_particle_and_iter":[] \
    }
    best_global_error = -1
    best_global_position = variables_and_bounds
    particle_output = {}
    opt_hist_datafile = open('optimization_history.txt','w')

    # Create instance of class to generate initial position
    pos_gen = g.positionGenerator(num_particles, point_generation_scheme,variables_and_bounds)
    #init_positions = pos_gen.generate_initial_positions()


    num_particles = pos_gen.refinement**pos_gen.num_vars
    print "number of particles = " + str(num_particles)
    # Initialize swarm
    swarm = []
    #initialized_vars_dict= []
    for i in range(0,num_particles):

        # Initialize parameter choices for this particle
        initialized_vars_dict =pos_gen.generate_initial_positions(i,variables_and_bounds)
        print "particle " + str(i)
        print initialized_vars_dict

        params_input = copy.copy(params)
        swarm.append(fenicsParticle.fenicsParticle(dimensionality, initialized_vars_dict, params_input))
#        initialized_vars_dict = g.positionGenerator.generate_initial_position(i,point_generation_scheme,variables_and_bounds,num_particles)


    #print swarm[0].__dict__
    #print swarm[1].__dict__
        # Let user know initial variables for this particle
        #print 'particle ' + str(i) + ' ' + str(initialized_vars_dict) + '\n'

        # Initialize particle and append to swarm
        #swarm.append(fenicsParticle.fenicsParticle(dimensionality, initialized_vars_dict, params))
        #print swarm[0].working_dict

        #print swarm[i].hs_params["myofilament_parameters"]["k_3"]
        #print swarm[0].hs_params["myofilament_parameters"]["k_3"]
        #print swarm[i].hs_params["myofilament_parameters"]["k_4_0"]
        #swarm.append(temp_particle)
        #swarm[i] = temp_particle
        #print swarm[i].hs_params["myofilament_parameters"]["k_3"]
        #print "particle " + str(i) + " initialized. HS Params are:"

        #print swarm[0].all_fenics_params

    #print swarm[0]
    #print swarm[0].hs_params
    #print swarm[1].hs_params
    ## Begin optimization
    iter = 0
    print "out of init loop"

    # Initialize figure
    fig, ax = plt.subplots()

    # set x range
    xdata = np.arange(max_iterations)

    print "iter " + str(iter) + "max_iterations " + str(max_iterations)
    print "best_global_error" + str(best_global_error) + "threshold" + str(convergence_threshold)
    while iter < max_iterations and (best_global_error > convergence_threshold or best_global_error==-1):

        print "iteration # " + str(iter)
        print "current minimum objective " + str(best_global_error)
        print best_global_position

        ## Iterate through swarm
        for j in range(0,num_particles):

            print "particle " + str(j) + "in iteration"
            #print swarm[j].hs_params
            #swarm[j].evaluate_objective(fenics_script,obj_func)

            # Update the error for this particle for visualizing on the fly?
            #particle_errors[iter,j] = swarm[j].current_error

            # Run particle simulation
            particle_output = swarm[j].run_simulation(fenics_script,iter,j,base_output_dir,1)
            particle_errors[iter,j] = objective_function.objFunc_class.evaluate(swarm[j].output_params["output_path"][0],iter,j)
            swarm[j].update_particle_errors(particle_errors[iter,j])

            #plot particle errors?
            ax.plot(xdata[0:iter],particle_errors[0:iter])
            ax.set(xlabel='Iteration', ylabel='Particle Error', title='Error for each iteration')
            ax.grid()
            fig.savefig(output_params["output_path"][0]+"test.png")

            #plt.show()
            #plt.get_current_fig_manager().full_screen_toggle()
            #plt.show()
            #fig.canvas.flush_events()
            #time.sleep(1)


            # Determine if this is the best particle
            if swarm[j].current_error < best_global_error or best_global_error == -1:
                best_global_position = swarm[j].working_dict
                best_global_error = float(swarm[j].current_error)
                best_particle_and_iter = [j,iter]
                #output_dictionary = swarm[j].output_dict

            """print "current directory at end of sim = " + str(os.getcwd())
            os.chdir('../')"""

        opt_history["global_error_history"].append(best_global_error)
        opt_history["best_particle_and_iter"].append(best_particle_and_iter)

        print opt_history["global_error_history"]

        ## Update velocities and position (start new loop to make sure
        # we are using the best global position after objective is evaluated for
        # entire swarm)
        for j in range(0,num_particles):
            swarm[j].update_particle_velocity(w,c1,c2,best_global_position)
            swarm[j].update_particle_position()
            print j
            print iter
            print particle_errors[iter, j]
            opt_hist_datafile.write("Error for particle " + str(j) + " in iteration " + str(iter) + " = " + str(particle_errors[iter,j])+"\n")

        opt_hist_datafile.write("------------------------------------------------------------\n")
        opt_hist_datafile.write("Best global error = " + str(opt_history["global_error_history"][0])+"\n")
        # fix this
        opt_hist_datafile.write("Best position is from: iteration " + str(opt_history["best_particle_and_iter"][0][1]) + ", particle " +str(opt_history["best_particle_and_iter"][0][1])+"\n")



        iter += 1

    ## Map components of position back to input keys, get "final_inputs"
    # The best location will have been "found", don't want to re-run.

    #def calculate_particle_error():


    opt_hist_datafile.close()
    return(best_global_position,opt_history)
