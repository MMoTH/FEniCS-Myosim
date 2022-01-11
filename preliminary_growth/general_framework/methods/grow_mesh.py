# @Author: charlesmann
# @Date:   2022-01-11T10:42:23-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T13:49:39-05:00

from dolfin import *
import diastolic_unloading
import calculate_deviation_function
import calculate_thetas


def grow_mesh(fcn_spaces, functions, uflforms, Ftotal, Jac, Ftotal_growth, Jac_growth, bcs, ref_vol, output_object, sim_state, mesh, input_parameters, growth_iter_counter):

    # unload ventricle
    functions = diastolic_unloading.diastolic_unloading(fcn_spaces, functions, uflforms, Ftotal, Jac, bcs, ref_vol, output_object, sim_state.reference_load_steps)

    # Assign thetas from pre-calculated stimuli
    functions["stimulus_ff"].assign(functions["stimulus_ff_temp"])
    functions["stimulus_ss"].assign(functions["stimulus_ss_temp"])
    functions["stimulus_nn"].assign(functions["stimulus_nn_temp"])

    # Calculate deviation
    functions = calculate_deviation_function.calculate_deviation_function(fcn_spaces,functions)

    # Calculate thetas
    functions = calculate_thetas.calculate_thetas(fcn_spaces,functions,input_parameters)

    solve(Ftotal_growth == 0, functions["w"], bcs, J = Jac_growth, form_compiler_parameters={"representation":"uflacs"})

    (u,p,pendo,c11)   = split(functions["w"])

    # Move mesh to relieve residual stress
    # We need to project u which is in CG2 to CG1 to move the nodes of the tetrahedral mesh
    ALE.move(mesh, project(u, VectorFunctionSpace(mesh, 'CG', 1)))

    growth_iter_counter +=1

    output_object.save_grown_mesh(mesh, growth_iter_counter)

    output_object.total_sol_file.save_pvd_object(functions["w"].sub(0))

    # Reset thetas so Fg is identity
    functions["theta_ff"].vector()[:] = 1.0
    functions["theta_ss"].vector()[:] = 1.0
    functions["theta_nn"].vector()[:] = 1.0

    return functions, mesh, growth_iter_counter
