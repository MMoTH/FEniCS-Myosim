// base_parameters.cpp
//#include <stdafx.h>
#include <iostream>
#include <stdio.h>
//#include <atlstr.h>
#include <math.h>

#include "base_parameters.h"
#include "global_definitions.h"

#include "gsl/gsl_vector.h"
#include "gsl/gsl_matrix.h"
#include "gsl/gsl_rng.h"

// Variables

// Structure to do with varying parameter values
struct tag_data_struct
{
	int int_1;
	int int_2;
	int int_3;
};
tag_data_struct * set_tag_data(tag_data_struct * p_tag_data,
	char * tag_string, int no_of_parameters);

// Constructor
base_parameters::base_parameters(char * set_instruction_file_string,
	char * set_output_directory_string)
{
	// Constructor
	
	// Variables
	int i;

	// Set the instruction_file_string
	/*sprintf_s(instruction_file_string,MAX_STRING_LENGTH,
		"%s",set_instruction_file_string);*/
	sprintf(instruction_file_string, "%s", set_instruction_file_string);

	// Set the output directory string
	/*sprintf_s(output_dir_string,MAX_STRING_LENGTH,
		"%s",set_output_directory_string);*/
	sprintf(output_dir_string, "%s", set_output_directory_string);

	// Initialise
	debug_dump_mode=0;
	error_flag=0;

	no_of_attached_states=0;
	no_of_detached_states=0;
	
	// Initialise adjustable variables
	temperature = 288.0;
	p_temperature =& temperature;

	a_on_rate = 0.0;
	p_a_on_rate =& a_on_rate;

	a_off_rate=1.0;
	p_a_off_rate =& a_off_rate;

	k_coop = 0.0;
	p_k_coop =& k_coop;

	k_plus=0.0;
	p_k_plus =& k_plus;

	k_minus=0.0;
	p_k_minus =& k_minus;

	k_recruit_tf = 0.0;
	p_k_recruit_tf =& k_recruit_tf;

	k_recruit_cbf = 0.0;
	p_k_recruit_cbf =& k_recruit_cbf;

	k_recruit_pf = 0.0;
	p_k_recruit_pf =& k_recruit_pf;

	passive_force_mode = 0.0;
	p_passive_force_mode =& passive_force_mode;

	passive_force_linear = 0.0;
	p_passive_force_linear =& passive_force_linear;

	passive_hsl_slack = 900;
	p_passive_hsl_slack =& passive_hsl_slack;

	passive_k_linear = 0.0;
	p_passive_k_linear =& passive_k_linear;

	passive_sigma = 0.0;
	p_passive_sigma =& passive_sigma;

	passive_L = 1.0e30;
	p_passive_L =& passive_L;

	passive_L_slack_hsl = 900;
	p_passive_L_slack_hsl =& passive_L_slack_hsl;

	passive_L_slack_k = 10;
	p_passive_L_slack_k =& passive_L_slack_k;

	series_alpha = 1e3;
	p_series_alpha =& series_alpha;

	series_beta = 1e7;
	p_series_beta =& series_beta;

	series_k = 1.0e10;
	p_series_k =& series_k;

	series_L0 = 1500;
	p_series_L0 =& series_L0;

	series_F0 = 1e10;
	p_series_F0 =& series_F0;

	series_compliance_effect = -1.0;
	p_series_compliance_effect =& series_compliance_effect;

	coop_power = 2.0;
	p_coop_power =& coop_power;

	k_cb_linear = 1.0;
	p_k_cb_linear =& k_cb_linear;

	base_k_cb_pos = 0.001;
	p_base_k_cb_pos =& base_k_cb_pos;

	base_k_cb_neg = 0.0;
	p_base_k_cb_neg =& base_k_cb_neg;

	movement_enhancement = 0.0;
	p_movement_enhancement =& movement_enhancement;

	filament_compliance_factor = 1.0;
	p_filament_compliance_factor =& filament_compliance_factor;

	viscosity = 0.0;
	p_viscosity =& viscosity;

	hs_thick_filament_length = 815.0;
	p_hs_thick_filament_length =& hs_thick_filament_length;

	hs_thin_filament_length = 1120.0;
	p_hs_thin_filament_length =& hs_thin_filament_length;

	hs_bare_zone_length = 80.0;
	p_hs_bare_zone_length =& hs_bare_zone_length;

	hs_k_falloff = 0.002;
	p_hs_k_falloff =& hs_k_falloff;

	isotonic_on_mode = 0.0;
	p_isotonic_on_mode =& isotonic_on_mode;

	N_variability = 0.0;
	p_N_variability =& N_variability;

	P_variability = 0.0;
	p_P_variability =& P_variability;

	ld_slack_hsl = 900.0;
	p_ld_slack_hsl =& ld_slack_hsl;

	dN_mode = 1.0;
	p_dN_mode =& dN_mode;

	base_Ca_concentration = -1e-7;
	p_base_Ca_concentration =& base_Ca_concentration;

	Ca_threshold = 0.0;
	p_Ca_threshold =& Ca_threshold;

	t_start = 0.0;
	p_t_start =& t_start;

	k_windkessel = 0.0;
	p_k_windkessel =& k_windkessel;

	d_windkessel = 0.0;
	p_d_windkessel =& d_windkessel;

	// Progressive relaxation
	first_alpha = 1.0;
	p_first_alpha =& first_alpha;

	inter_z_factor = 0.0;
	p_inter_z_factor =& inter_z_factor;

	inter_thick_factor = 0.0;
	p_inter_thick_factor =& inter_thick_factor;

	inter_hs_factor = 0.0;
	p_inter_hs_factor =& inter_hs_factor;

	// Call other initialisation functions
	set_base_parameters_from_instruction_file(instruction_file_string);

	// Work out how many x bins there are
	no_of_x_bins=(int)(((x_bin_max-x_bin_min)/x_bin_increment)+1);

	// Allocate the positions
	x_bins = gsl_vector_alloc(no_of_x_bins);

	for (i=0;i<no_of_x_bins;i++)
	{
		gsl_vector_set(x_bins,i,x_bin_min+((double)i*x_bin_increment));
	}

	// Allocate vectors for parameters that are m_isoform dependent
	if (no_of_conditions>0)
		m_isoform_rel_populations = gsl_matrix_alloc(no_of_conditions,m_no_of_isoforms);
	else
		m_isoform_rel_populations = gsl_matrix_alloc(1,m_no_of_isoforms);
	gsl_matrix_set_zero(m_isoform_rel_populations);

	k_cb_pos = gsl_vector_alloc(m_no_of_isoforms);
	gsl_vector_set_all(k_cb_pos,0.0);
	k_cb_pos_modifications = gsl_vector_alloc(m_no_of_isoforms);
	gsl_vector_set_all(k_cb_pos_modifications,0.0);

	k_cb_neg = gsl_vector_alloc(m_no_of_isoforms);
	gsl_vector_set_all(k_cb_neg,0.0);
	k_cb_neg_modifications = gsl_vector_alloc(m_no_of_isoforms);
	gsl_vector_set_all(k_cb_neg_modifications,0.0);

	// And the rest of the initialisation
	load_kinetic_scheme(instruction_file_string);
	
	load_m_isoform_data(instruction_file_string);

	if (no_of_conditions>0)
	{
		fill_control_arrays(instruction_file_string);
	}

	k_cb_multiplier = gsl_vector_alloc(no_of_states);
	gsl_vector_set_all(k_cb_multiplier,1.0);

	Ca_scaling_factor = gsl_vector_alloc(MAX_NO_OF_SCALING_FACTORS);
	gsl_vector_set_all(Ca_scaling_factor,0.0);

	cond_scaling_factor = gsl_matrix_alloc(no_of_conditions,MAX_NO_OF_SCALING_FACTORS);
	gsl_matrix_set_all(cond_scaling_factor,1.0);

	cond_scaling_copy = gsl_matrix_alloc(no_of_conditions,MAX_NO_OF_SCALING_FACTORS);
	gsl_matrix_set_all(cond_scaling_copy,0.0);

	ld_slope = gsl_vector_alloc(MAX_NO_OF_SCALING_FACTORS);
	gsl_vector_set_all(ld_slope,0.0);

	ld_rate = gsl_matrix_alloc(no_of_transitions,no_of_function_parameters);
	gsl_matrix_set_all(ld_rate,0.0);

	fd_slope = gsl_vector_alloc(MAX_NO_OF_SCALING_FACTORS);
	gsl_vector_set_all(fd_slope,0.0);

	fd_rate = gsl_matrix_alloc(no_of_transitions,no_of_function_parameters);
	gsl_matrix_set_all(fd_rate,0.0);

	fd_coefs = gsl_matrix_alloc(no_of_transitions,no_of_function_parameters);
	gsl_matrix_set_all(fd_coefs,0.0);

	thin_function_mod = gsl_matrix_alloc(no_of_conditions,MAX_NO_OF_SCALING_FACTORS);
	gsl_matrix_set_all(thin_function_mod,1.0);

	thin_function_copy = gsl_matrix_alloc(no_of_conditions,MAX_NO_OF_SCALING_FACTORS);
	gsl_matrix_set_zero(thin_function_copy);

	// Set up recovery mode
	ml_recovery_mode = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(ml_recovery_mode);

	ml_recovery_start = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(ml_recovery_start);

	ml_recovery_stop = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(ml_recovery_stop);

	ml_recovery_flag = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_all(ml_recovery_flag,1.0);



	set_fixed_parameters_from_file(instruction_file_string);
	set_adjustable_parameters_from_file(instruction_file_string);

	// Update beta
	beta = 	K_BOLTZMANN * 1.0e18 * temperature;			// kT in nN nm

	// Initialise the random number generator
	gsl_rng_env_setup();
	rand_T = gsl_rng_default;
	rand_r=gsl_rng_alloc(rand_T);
}

// Destructor
base_parameters::~base_parameters()
{
	// Tidy up

	// Variables
	int i;

	// Code

	delete [] state_attached;

	for (i=0;i<no_of_states;i++)
	{
		delete [] state_transitions[i];
		delete [] state_rate_functions[i];
		delete [] n_vector_indices[i];
	}
	delete [] state_transitions;
	delete [] state_rate_functions;
	delete [] n_vector_indices;

	delete [] function_type;
	delete [] function_action;
	delete [] function_ligand;

	gsl_matrix_free(base_function_values);
	gsl_matrix_free(Ca_function_modifications);
	gsl_matrix_free(Ca_function_copy);

	for (i=0;i<no_of_conditions;i++)
	{
		gsl_matrix_free(cond_rate_mod[i]);
		gsl_matrix_free(cond_rate_copy[i]);
	}

	for (i=0;i<no_of_transitions;i++)
	{
		gsl_matrix_free(rate_multiple[i]);
	}

	for (i=0;i<no_of_conditions;i++)
	{
		gsl_matrix_free(cond_fd_rate_mod[i]);
		gsl_matrix_free(cond_fd_rate_copy[i]);
	}

	for (i=0;i<m_no_of_isoforms;i++)
	{
		gsl_matrix_free(function_parameters[i]);
		gsl_matrix_free(function_modifications[i]);
	}

	gsl_matrix_free(function_copy);
	gsl_matrix_free(cb_extensions);
	gsl_matrix_free(cb_base_energies);

	gsl_vector_free(base_delta_extensions);
	gsl_matrix_free(delta_extensions_modifications);

	gsl_vector_free(base_delta_energies);

	gsl_vector_free(state_extensions_copy);
	gsl_vector_free(state_delta_extensions_copy);
	
	gsl_vector_free(x_bins);

	gsl_matrix_free(m_isoform_rel_populations);

	gsl_vector_free(base_cb_extensions);

	gsl_vector_free(k_cb_pos);
	gsl_vector_free(k_cb_pos_modifications);

	gsl_vector_free(k_cb_neg);
	gsl_vector_free(k_cb_neg_modifications);

	gsl_vector_free(k_cb_multiplier);

	gsl_vector_free(Ca_scaling_factor);
	gsl_matrix_free(cond_scaling_factor);
	gsl_matrix_free(cond_scaling_copy);

	gsl_vector_free(ld_slope);
	gsl_matrix_free(ld_rate);

	gsl_vector_free(fd_slope);
	gsl_matrix_free(fd_rate);

	gsl_matrix_free(fd_coefs);

	gsl_matrix_free(br_slope);

	gsl_vector_free(initial_dml);

	gsl_vector_free(isotonic_off_mode);

	gsl_vector_free(ml_recovery_mode);
	gsl_vector_free(ml_recovery_start);
	gsl_vector_free(ml_recovery_stop);
	gsl_vector_free(ml_recovery_flag);

	gsl_vector_free(d_hsl_slack);

	gsl_vector_free(series_k_vector);
	gsl_vector_free(series_alpha_vector);
	gsl_vector_free(series_beta_vector);
	gsl_vector_free(k_plus_vector);
	gsl_vector_free(k_minus_vector);
	gsl_vector_free(N_variability_vector);
	gsl_vector_free(P_variability_vector);

	gsl_vector_free(time_steps);
	gsl_matrix_free(hs_increments);
	gsl_matrix_free(isotonic_forces);
	gsl_matrix_free(pCa_values);
	gsl_matrix_free(Pi_concentrations);
	gsl_matrix_free(ADP_concentrations);
	gsl_matrix_free(ATP_concentrations);

	gsl_matrix_free(thin_function_mod);
	gsl_matrix_free(thin_function_copy);

	gsl_rng_free(rand_r);
}

void base_parameters::display_bps(void)
{
	printf("n_vector_indices\n");
	for (int i = 0; i<no_of_states; i++)
	{
		printf("State[%i]\t", i);
		printf("%i\t%i\n", n_vector_indices[i][0], n_vector_indices[i][1]);
	}
}
// Display status
void base_parameters::display_base_parameters(void)
{
	// Function displays base_parameters

	// Variables
	int m_counter;
	int i,j,k;

	// Code
	printf("base_parameters::display_base_parameters()\n");
	printf("particle_number: %i\n",particle_number);
	printf("check_number: %i\n",check_number);

	printf("//MYOSIM\n");
	printf("no_of_conditions: %i\n",no_of_conditions);
	printf("debug_dump_mode: %i\n",debug_dump_mode);
	printf("distributions_dump_mode: %i\n",distributions_dump_mode);

	printf("//MUSCLE\n");
	printf("no_of_half_sarcomeres: %i\n",no_of_half_sarcomeres);
	printf("no_of_myofibrils: %i\n",no_of_myofibrils);
	printf("no_of_half_sarcomeres_in_series: %i\n",no_of_half_sarcomeres_in_series);
	printf("cb_number_density: %g\n",cb_number_density);

	printf("//DISTRIBUTIONS\n");
	printf("no_of_bins: %i\n",no_of_x_bins);
	printf("x_bin_min: %g\n",x_bin_min);
	printf("x_bin_max: %g\n",x_bin_max);
	printf("x_bin_increment: %g\n",x_bin_increment);

	printf("//KINETICS\n");
	printf("no_of_states: %i\n",no_of_states);
	printf("no_of_transitions: %i\n",no_of_transitions);
	printf("no_of_function_parameters: %i\n",no_of_function_parameters);
	printf("no_of_attached_states: %i\n",no_of_attached_states);
	printf("no_of_detached_states: %i\n",no_of_detached_states);
	printf("state_attached:\t");
	for (i=0;i<no_of_states;i++)
	{
		printf("%i\t",state_attached[i]);
	}
	printf("\n");
	printf("state_transitions\n");
	for (i=0;i<no_of_states;i++)
	{
		printf("State[%i]\t",i);
		for (j=0;j<MAX_PATHWAYS;j++)
			printf("%i\t",state_transitions[i][j]);
		printf("\n");
	}
	printf("state_rate_functions\n");
	for (i=0;i<no_of_states;i++)
	{
		printf("State[%i]\t",i);
		for (j=0;j<MAX_PATHWAYS;j++)
			printf("%i\t",state_rate_functions[i][j]);
		printf("\n");
	}
	printf("state_extensions\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		printf("m_isoform: %i\n",m_counter);
		for (i=0;i<no_of_states;i++)
		{
			printf("State[%i]\t Extension: %g\n",i,
				gsl_matrix_get(cb_extensions,i,m_counter));
		}
	}
	printf("Base_delta_extensions\n");
	for (i=0;i<no_of_states;i++)
	{
		printf("State[%i]\t Delta_extension: %g\n",i,
			gsl_vector_get(base_delta_extensions,i));
	}

	printf("Extension_modifications\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		printf("m_isoform[%i]\n",m_counter);
		for (i=0;i<no_of_states;i++)
		{
			printf("State[%i]\tModifier: %g\n",
				i,gsl_matrix_get(delta_extensions_modifications,i,m_counter));
		}
	}

	printf("state_base_energies\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		printf("m_isoform: %i\n",m_counter);
		for (i=0;i<no_of_states;i++)
		{
			printf("State[%i]\t cb_base_energy: %g\n",i,
				gsl_matrix_get(cb_base_energies,i,m_counter));
		}
	}

	printf("function_parameters\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		printf("m_isoform[%i]\n",m_counter);
		for (i=0;i<no_of_transitions;i++)
		{
			printf("Transition[%i]\t",i+1);
			printf("%s\t",function_type[i]);
			printf("%c\t",function_action[i]);
			printf("%s\t",function_ligand[i]);
			for (j=0;j<no_of_function_parameters;j++)
				printf("%5.3g\t",gsl_matrix_get(function_parameters[m_counter],i,j));
			printf("\n");
		}
	}

//exit(1);


	printf("function_modifications\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		printf("m_isoform[%i]\n",m_counter);
		for (i=0;i<no_of_transitions;i++)
		{
			for (j=0;j<no_of_function_parameters;j++)
				printf("%5.3g\t",gsl_matrix_get(function_modifications[m_counter],i,j));
			printf("\n");
		}
	}

	printf("Ca_function_modifications\n");
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
			printf("%5.3g\t",gsl_matrix_get(Ca_function_modifications,i,j));
		printf("\n");
	}

	printf("function_copy\n");
	for (i=0;i<no_of_transitions;i++)
	{
		printf("[%i]\t",i);
		for (j=0;j<no_of_function_parameters;j++)
		{
			printf("%.0f\t",gsl_matrix_get(function_copy,i,j));
		}
		printf("\n");
	}

	printf("Ca_scaling_factors\n");
	for (i=0;i<MAX_NO_OF_SCALING_FACTORS;i++)
	{
		printf("[%i] %g\t",i,gsl_vector_get(Ca_scaling_factor,i));
	}
	printf("\n");

	printf("Condition_scaling_factors\n");
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<MAX_NO_OF_SCALING_FACTORS;j++)
		{
			printf("[%i] %g\t",j,gsl_matrix_get(cond_scaling_factor,i,j));
		}
		printf("\n");
	}

	printf("Condition_rate_mod\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("Condition %i\n",i);
		for (j=0;j<no_of_transitions;j++)
		{
			printf("[%i]\t",j);
			for (k=0;k<no_of_function_parameters;k++)
			{
				printf("%g\t",gsl_matrix_get(cond_rate_mod[i],j,k));
			}
			printf("\n");
		}
	}

	printf("Condition_rate_copy\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("Condition %i\n",i);
		for (j=0;j<no_of_transitions;j++)
		{
			printf("[%i]\t",j);
			for (k=0;k<no_of_function_parameters;k++)
			{
				printf("%g\t",gsl_matrix_get(cond_rate_copy[i],j,k));
			}
			printf("\n");
		}
	}

	printf("Condition_fd_rate_mod\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("Condition %i\n",i);
		for (j=0;j<no_of_transitions;j++)
		{
			printf("[%i]\t",j);
			for (k=0;k<no_of_function_parameters;k++)
			{
				printf("%g\t",gsl_matrix_get(cond_fd_rate_mod[i],j,k));
			}
			printf("\n");
		}
	}

	printf("Condition_fd_rate_copy\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("Condition %i\n",i);
		for (j=0;j<no_of_transitions;j++)
		{
			printf("[%i]\t",j);
			for (k=0;k<no_of_function_parameters;k++)
			{
				printf("%g\t",gsl_matrix_get(cond_fd_rate_copy[i],j,k));
			}
			printf("\n");
		}
	}


	printf("Thin_function_mod\n");
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<MAX_NO_OF_SCALING_FACTORS;j++)
		{
			printf("[%i] %g\t",j,gsl_matrix_get(thin_function_mod,i,j));
		}
		printf("\n");
	}

	printf("Thin_function_copy\n");
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<MAX_NO_OF_SCALING_FACTORS;j++)
		{
			printf("[%i] %g\t",j,gsl_matrix_get(thin_function_copy,i,j));
		}
		printf("\n");
	}


	printf("n_vector_indices\n");
	for (i=0;i<no_of_states;i++)
	{
		printf("State[%i]\t",i);
		printf("%i\t%i\n",n_vector_indices[i][0],n_vector_indices[i][1]);
	}
	printf("m_no_of_isoforms: %i\n",m_no_of_isoforms);
	printf("m_isoform_rel_populations\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("[%i]\t",i);
		for (j=0;j<m_no_of_isoforms;j++)
		{
			printf("%.2f\t",gsl_matrix_get(m_isoform_rel_populations,i,j));
		}
		printf("\n");
	}

	printf("br_slope\n");
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			printf("[%i][%i]: %g\n",i,j,gsl_matrix_get(br_slope,i,j));
		}
	}

	printf("ld_slope\n");
	for (i=0;i<MAX_NO_OF_SCALING_FACTORS;i++)
	{
		printf("[%i] %g\t",i+1,gsl_vector_get(ld_slope,i));
	}
	printf("\n");

	printf("ld_rate\n");
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			printf("[%i][%i]: %g\n",i,j,gsl_matrix_get(ld_rate,i,j));
		}
	}

	printf("fd_coefs\n");
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			printf("[%i][%i]: %g\n",i,j,gsl_matrix_get(fd_coefs,i,j));
		}
	}

	printf("initial_dml\n");
	for (i=0;i<no_of_conditions;i++)
	{
		printf("[%i]: %g\n",i,gsl_vector_get(initial_dml,i));
	}

	printf("\nControl_arrays - first line\n");
	printf("Time_step: %g\n",gsl_vector_get(time_steps,0));
	for (i=0;i<no_of_conditions;i++)
	{
		printf("hs_inc: %g\tiso_for: %g\tpCa: %g\tPi: %g\tADP: %g\tATP: %g\n",
			gsl_matrix_get(hs_increments,0,i),
			gsl_matrix_get(isotonic_forces,0,i),
			gsl_matrix_get(pCa_values,0,i),
			gsl_matrix_get(Pi_concentrations,0,i),
			gsl_matrix_get(ADP_concentrations,0,i),
			gsl_matrix_get(ATP_concentrations,0,i));
	}
	printf("Control_arrays - last line [%i]\n",no_of_time_points);
	printf("Time_step: %g\n",gsl_vector_get(time_steps,no_of_time_points-1));
	for (i=0;i<no_of_conditions;i++)
	{
		printf("hs_inc: %g\tiso_for: %g\tpCa: %g\tPi: %g\tADP: %g\tATP: %g\n",
			gsl_matrix_get(hs_increments,no_of_time_points-1,i),
			gsl_matrix_get(isotonic_forces,no_of_time_points-1,i),
			gsl_matrix_get(pCa_values,no_of_time_points-1,i),
			gsl_matrix_get(Pi_concentrations,no_of_time_points-1,i),
			gsl_matrix_get(ADP_concentrations,no_of_time_points-1,i),
			gsl_matrix_get(ATP_concentrations,no_of_time_points-1,i));
	}
	printf("//ADJUSTABLE_PARAMETERS\n");
	printf("a_on_rate: %g\n",a_on_rate);
	printf("a_off_rate: %g\n",a_off_rate);
	printf("k_plus: %g\n",k_plus);
	printf("k_minus: %g\n",k_minus);
	printf("base_k_cb_pos: %g\n",base_k_cb_pos);
	printf("k_cb_pos\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
		printf("[%i]: %g\t",m_counter,gsl_vector_get(k_cb_pos,m_counter));
	printf("\n");
	printf("k_cb_neg\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
		printf("[%i]: %g\t",m_counter,gsl_vector_get(k_cb_neg,m_counter));
	printf("\n");
	printf("k_cb_mult\n");
	for (i=0;i<no_of_states;i++)
		printf("[%i]: %g\t",i,gsl_vector_get(k_cb_multiplier,i));
	printf("\n");
	printf("filament_compliance_factor: %g\n",filament_compliance_factor);
	printf("passive_hsl_slack: %g\n",passive_hsl_slack);
	printf("passive_k_linear: %g\n",passive_k_linear);
	printf("passive_sigma: %g\n",passive_sigma);
	printf("passive_L: %g\n",passive_L);
	printf("viscosity: %g\n",viscosity);
	
	// Fixed parameters
	printf("//FIXED PARAMETERS\n");
	printf("temperature: %g\n",temperature);
	printf("passive_force_linear: %g\n",passive_force_linear);
	printf("movement_enhancement: %g\n",movement_enhancement);
	printf("series_compliance_effect: %i\n",(int)series_compliance_effect);
	printf("hs_thick_filament_length: %g\n",hs_thick_filament_length);
	printf("hs_thin_filament_length: %g\n",hs_thin_filament_length);
	printf("hs_bare_zone_length: %g\n",hs_bare_zone_length);
	printf("hs_k_falloff: %g\n",hs_k_falloff);
	printf("isotonic_on_mode: %i\n",isotonic_on_mode);
	for (i=0;i<no_of_conditions;i++)
		printf("isotonic_off_mode[%i]: %f\n",i,gsl_vector_get(isotonic_off_mode,i));
	for (i=0;i<no_of_conditions;i++)
		printf("series_k_vector[%i]: %g\n",i,gsl_vector_get(series_k_vector,i));
	printf("end of display_base_parameters()\n\n");
}

void base_parameters::dump_base_parameters(void)
{
	// Code dumps base_parameters to file

	// Variables
	int m_counter;
	int s_counter;
	int t_counter;
	int c_counter;
	int i;

	char dump_file_string[MAX_STRING_LENGTH];

	// Code

	FILE * dump_file;

	// Deduce the file name
	if (strlen(output_dir_string)>0)
	{
		/*sprintf_s(dump_file_string,"%s\\%s.txt",
			output_dir_string,
			PARAMETERS_FILE_STRING);*/
		sprintf(dump_file_string, "%s\\%s.txt", output_dir_string, PARAMETERS_FILE_STRING);
	}
	else
	{
		/*sprintf_s(dump_file_string,"%s.txt",
			PARAMETERS_FILE_STRING);*/
		sprintf(dump_file_string, "%s.txt", PARAMETERS_FILE_STRING);
	}

	//fopen_s(&dump_file,dump_file_string,"w");
	dump_file = fopen(dump_file_string, "w");
	if (dump_file==NULL)
	{
		printf("base_parameters::dump_base_parameters\nDump file: %s\ncould not be opened\nNow finishing\n",
			dump_file_string);
		exit(1);
	}

	// Dump
	fprintf(dump_file,"\nThin filament\n");
	fprintf(dump_file,"a_on_rate: %g\n",a_on_rate);
	fprintf(dump_file,"a_off_rate: %g\n",a_off_rate);
	fprintf(dump_file,"k_coop: %g\n",k_coop);

	fprintf(dump_file,"\nPassive force\n");
	fprintf(dump_file,"passive_force_mode: %i\n",(int)passive_force_mode);
	fprintf(dump_file,"passive_hsl_slack: %g\n",passive_hsl_slack);
	fprintf(dump_file,"passive_k_linear: %g\n",passive_k_linear);
	fprintf(dump_file,"passive_L: %g\n",passive_L);

	fprintf(dump_file,"\nSeries compliance\n");
	fprintf(dump_file,"series_compliance_effect: %g\n",series_compliance_effect);
	fprintf(dump_file,"series_L0: %g\n",series_L0);
	fprintf(dump_file,"series_F0: %g\n",series_F0);
	fprintf(dump_file,"series_k: %g\n",series_k);
	fprintf(dump_file,"series_alpha: %g\n",series_alpha);


	fprintf(dump_file,"cb_number_density %g\n",cb_number_density);
	fprintf(dump_file,"m_no_of_isoforms %i\n",m_no_of_isoforms);
	fprintf(dump_file,"no_of_states %i\n",no_of_states);
	fprintf(dump_file,"no_of_attached_states %i\n",no_of_attached_states);
	fprintf(dump_file,"attached_states");
	for (s_counter=0;s_counter<no_of_states;s_counter++)
	{
		if (state_attached[s_counter]>0)
			fprintf(dump_file,"\t%i",s_counter+1);
	}
	fprintf(dump_file,"\n");

	fprintf(dump_file,"k_cb_pos\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		fprintf(dump_file,"m_%i: %g",m_counter+1,gsl_vector_get(k_cb_pos,m_counter));
		if (m_counter==(m_no_of_isoforms-1))
			fprintf(dump_file,"\n");
		else
			fprintf(dump_file,"\t");
	}

	fprintf(dump_file,"k_cb_neg\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		fprintf(dump_file,"m_%i: %g",m_counter+1,gsl_vector_get(k_cb_neg,m_counter));
		if (m_counter==(m_no_of_isoforms-1))
			fprintf(dump_file,"\n");
		else
			fprintf(dump_file,"\t");
	}

	fprintf(dump_file,"state_extensions\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		for (s_counter=0;s_counter<no_of_states;s_counter++)
		{
			fprintf(dump_file,"m%i_s%i %g",m_counter+1,s_counter+1,
				gsl_matrix_get(cb_extensions,s_counter,m_counter));

			if (s_counter==(no_of_states-1))
				fprintf(dump_file,"\n");
			else
				fprintf(dump_file,"\t");
		}
	}
	
	fprintf(dump_file,"\nrate_parameters\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		fprintf(dump_file,"m_isoform: %i\n",m_counter+1);
		for (t_counter=0;t_counter<no_of_transitions;t_counter++)
		{
			for (i=0;i<no_of_function_parameters;i++)
			{
				fprintf(dump_file,"[%i,%i]: %f\t",
					t_counter+1,i+1,gsl_matrix_get(function_parameters[m_counter],t_counter,i));
			}
			fprintf(dump_file,"\n");
		}
	}

	fprintf(dump_file,"\ncond_rate_mod\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		fprintf(dump_file,"m_isoform: %i\n",m_counter+1);
		for (c_counter=0;c_counter<no_of_conditions;c_counter++)
		{
			fprintf(dump_file,"Condition: %i\n",c_counter+1);
			for (t_counter=0;t_counter<no_of_transitions;t_counter++)
			{
				for (i=0;i<no_of_function_parameters;i++)
				{
					fprintf(dump_file,"[%i,%i]: %f\t",
						t_counter+1,i+1,gsl_matrix_get(cond_rate_mod[c_counter],t_counter,i));
				}
				fprintf(dump_file,"\n");
			}
		}
	}

	fprintf(dump_file,"\ncond_rate_copy\n");
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		fprintf(dump_file,"m_isoform: %i\n",m_counter+1);
		for (c_counter=0;c_counter<no_of_conditions;c_counter++)
		{
			fprintf(dump_file,"Condition: %i\n",c_counter+1);
			for (t_counter=0;t_counter<no_of_transitions;t_counter++)
			{
				for (i=0;i<no_of_function_parameters;i++)
				{
					fprintf(dump_file,"[%i,%i]: %f\t",
						t_counter+1,i+1,gsl_matrix_get(cond_rate_copy[c_counter],t_counter,i));
				}
				fprintf(dump_file,"\n");
			}
		}
	}

	fprintf(dump_file,"\nfd_rate\n");
		for (t_counter=0;t_counter<no_of_transitions;t_counter++)
		{
			for (i=0;i<no_of_function_parameters;i++)
			{
				fprintf(dump_file,"[%i,%i]: %f\t",
					t_counter+1,i+1,gsl_matrix_get(fd_rate,t_counter,i));
			}
			fprintf(dump_file,"\n");
		}
	// Tidy up
	fclose(dump_file);
}

void base_parameters::set_base_parameters_from_instruction_file(char * instruction_file_string)
{
	// Code sets the base parameters

	// Variables
	float temp_float;

	char temp_string[MAX_STRING_LENGTH];

	char myosim_tag[] = MYOSIM_TAG;
	char muscle_tag[] = MUSCLE_TAG;
	char distributions_tag[] = DISTRIBUTIONS_TAG;

	// Code

	// Open the instruction file
	FILE * instruction_file;
	//fopen_s(&instruction_file,instruction_file_string,"r");
	instruction_file = fopen(instruction_file_string, "r");

	if (instruction_file==NULL)
	{
		printf("base_parameters::set_base_parameters_from_instruction_file\n");
		printf("Instruction file: %s\ncould not be opened\n",
			instruction_file_string);
		printf("Now finishing\n");
		exit(1);
	}

	// Check that the first string is correct
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	if (strcmp(temp_string,myosim_tag)!=0)
	{
		printf("Instruction file\n%s\ndoes not start with\n%s\n and is invalid\n",
			instruction_file_string,
			myosim_tag);
		printf("Now exiting\n");
		exit(1);
	}

	// File appears valid - read the rest of the MYOSIM parameters

	// Now the no_of_conditions
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_conditions);
	fscanf(instruction_file, "%i", &no_of_conditions);

	// Initialize the isotonic_off_mode
	isotonic_off_mode = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(isotonic_off_mode);

	// d_hsl_slack
	d_hsl_slack = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(d_hsl_slack);

	// Initialize the series_vectors;
	series_k_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(series_k_vector);

	series_alpha_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(series_alpha_vector);

	series_beta_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(series_beta_vector);

	// Initalize the cooperativity vectors
	k_plus_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(k_plus_vector);

	k_minus_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(k_minus_vector);

	initial_dml = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(initial_dml);

	// Initialize the variability vectors
	N_variability_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(N_variability_vector);

	P_variability_vector = gsl_vector_alloc(no_of_conditions);
	gsl_vector_set_zero(P_variability_vector);

	// Debug dump mode
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&debug_dump_mode);
	fscanf(instruction_file, "%i", &debug_dump_mode);

	// Read the distributions dump mode
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&distributions_dump_mode);
	fscanf(instruction_file, "%i", &distributions_dump_mode);

	// Correct this parameter for the zero offset
	distributions_dump_mode=distributions_dump_mode-1;

	// Skip the closing tag
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);

/*
	// Skip the exe name
	fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	// Read the particle number
	fscanf_s(instruction_file,"%i",&particle_number);
	// Read the check number
	fscanf_s(instruction_file,"%i",&check_number);

	// Skip other stuff
	for (i=1;i<=5;i++)
		fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
*/

	// Read in the MUSCLE, DISTRIBUTIONS, and KINETICS sections in order

	// Scan the file until we get to the MUSCLE tag
	//sprintf_s(temp_string,"",MAX_STRING_LENGTH);
	sprintf(temp_string, "");
	while ((strcmp(temp_string,muscle_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("base_parameters, %s tag not found\nNow finishing\n",
				muscle_tag);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Read no_of_half_sarcomeres
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_half_sarcomeres);
	fscanf(instruction_file, "%i", &no_of_half_sarcomeres);

	// Read no_of_myofibrils
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_myofibrils);
	fscanf(instruction_file, "%i", &no_of_myofibrils);

	// Set the no_of_half-sarcomeres_in_series
	no_of_half_sarcomeres_in_series = no_of_half_sarcomeres/no_of_myofibrils;

	// Set the initial_hs_length
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%f",&temp_float);
	fscanf(instruction_file, "%f", &temp_float);
	initial_hs_length = (double)temp_float;

	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&m_no_of_isoforms);
	fscanf(instruction_file, "%i", &m_no_of_isoforms);

	// Read in the cb number density
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%f",&temp_float);
	fscanf(instruction_file, "%f", &temp_float);
	cb_number_density = (double)temp_float;

	// Skip the //END_MUSCLE tag
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);


	// Scan the file until we get to the //DISTRIBUTIONS tag
	//sprintf_s(temp_string,"",MAX_STRING_LENGTH);
	sprintf(temp_string, "");
	while ((strcmp(temp_string,distributions_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("base_parameters, %s tag not found\nNow finishing\n",
				distributions_tag);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Deduce the bin parameters
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%f",&temp_float);
	fscanf(instruction_file, "%f", &temp_float);
	x_bin_min = (double)temp_float;

	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%f",&temp_float);
	fscanf(instruction_file, "%f", &temp_float);
	x_bin_max = (double)temp_float;
	
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%f",&temp_float);
	fscanf(instruction_file, "%f", &temp_float);
	x_bin_increment = (double)temp_float;
	

	// Skip the closing tag
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);

	// Tidy up
	fclose(instruction_file);
}

void base_parameters::load_m_isoform_data(char * instruction_file_string)
{
	// Code sets the m_isoform data
	// If there is only 1 isoform, this can be done forthwith
	// If there are more than one isoforms, the data needs to be read from file

	// Variables
	int i,j;

	float temp_float;

	char temp_string[MAX_STRING_LENGTH];
	char myosin_isoform_tag[] = MYOSIN_ISOFORM_TAG;

	// Code

	// Is there more than one isoform?
	if (m_no_of_isoforms==1)
	{
		// We can set this to one
		gsl_matrix_set_all(m_isoform_rel_populations,(double)1.0);
		return;
	}

	// More than one isoform - read the data from file
	
	FILE * instruction_file;
	//fopen_s(&instruction_file,instruction_file_string,"r");
	instruction_file = fopen(instruction_file_string, "r");
	if (instruction_file==NULL)
	{
		printf("base_parameters::load_m_isoform_data::Instruction file: %s\ncould not be opened\nNow finishing\n",
			instruction_file_string);
		exit(1);
	}

	// Scan the file until we get to the myosin
	//sprintf_s(temp_string,"",MAX_STRING_LENGTH);
	sprintf(temp_string, "");
	while ((strcmp(temp_string,MYOSIN_ISOFORM_TAG)!=0))
	{
		if (feof(instruction_file))
		{
			printf("base_parameters::myosin_isoform_tag::%s not found\nNow finishing\n",
				myosin_isoform_tag);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Fill the matrix
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<m_no_of_isoforms;j++)
		{
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(m_isoform_rel_populations,
				i,j,(double)temp_float);
		}
	}

	// Tidy up
	fclose(instruction_file);
}

void base_parameters::load_kinetic_scheme(char * instruction_file_string)
{
	// Code loads the kinetic scheme from the specified instruction file

	// Variables
	int m_counter;
	int i,j;
	int temp_int;

	float temp_float;

	char temp_string[MAX_STRING_LENGTH];
	char kinetics_tag[] = KINETICS_TAG;

	// Code
	
	FILE *instruction_file;
	//fopen_s(&instruction_file,instruction_file_string,"r");
	instruction_file = fopen(instruction_file_string, "r");
	if (instruction_file==NULL)
	{
		printf("base_parameters::load_kinetic_scheme::Instruction file: %s\ncould not be opened\nNow finishing\n",
			instruction_file_string);
		exit(1);
	}

	// Scan the file until we get to the kinetic scheme
	//sprintf_s(temp_string,"",MAX_STRING_LENGTH);
	sprintf(temp_string, "");
	while ((strcmp(temp_string,kinetics_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("base_parameters::load_kinetic_scheme::%s not found\nNow finishing\n",
				kinetics_tag);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Parse the data
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_states);
	fscanf(instruction_file, "%i", &no_of_states);
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_transitions);
	fscanf(instruction_file, "%i", &no_of_transitions);
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	//fscanf_s(instruction_file,"%i",&no_of_function_parameters);
	fscanf(instruction_file, "%i", &no_of_function_parameters);

	// Reserve space for the vector and matrices
	state_attached = new int [no_of_states];

	state_transitions = new int * [no_of_states];
	state_rate_functions = new int * [no_of_states];
	n_vector_indices = new int * [no_of_states];
	for (i=0;i<no_of_states;i++)
	{
		state_transitions[i] = new int [MAX_PATHWAYS];
		state_rate_functions[i] = new int [MAX_PATHWAYS];
		n_vector_indices[i] = new int [2];
	}

	base_cb_extensions = gsl_vector_alloc(no_of_states);
	gsl_vector_set_zero(base_cb_extensions);

	base_cb_energies = gsl_vector_alloc(no_of_states);
	gsl_vector_set_zero(base_cb_energies);

	cb_extensions = gsl_matrix_alloc(no_of_states,m_no_of_isoforms);
	gsl_matrix_set_zero(cb_extensions);
	cb_base_energies = gsl_matrix_alloc(no_of_states,m_no_of_isoforms);
	gsl_matrix_set_zero(cb_base_energies);

	// Now read the kinetic scheme
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);
	for (i=0;i<no_of_states;i++)
	{
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		
		// Deduce the type of state
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		if (!strcmp(temp_string,"A"))
		{
			state_attached[i]=1;
			no_of_attached_states++;
		}
		else
		{
			state_attached[i]=0;
			no_of_detached_states++;
		}

		// Scan the potential pathways
		for (j=0;j<MAX_PATHWAYS;j++)
		{
			//fscanf_s(instruction_file,"%i",&temp_int);
			fscanf(instruction_file, "%i", &temp_int);
			state_transitions[i][j]=temp_int;
		}

		// Skip the divider
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);

		// Scan the potential pathways
		for (j=0;j<MAX_PATHWAYS;j++)
		{
			//fscanf_s(instruction_file,"%i",&temp_int);
			fscanf(instruction_file, "%i", &temp_int);
			state_rate_functions[i][j]=temp_int;
		}

		// Read the base energies
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		//fscanf_s(instruction_file,"%f",&temp_float);
		fscanf(instruction_file, "%f", &temp_float);
		gsl_vector_set(base_cb_energies,i,(double)temp_float);

		// Read the extensions
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		//fscanf_s(instruction_file,"%f",&temp_float);
		fscanf(instruction_file, "%f", &temp_float);
		gsl_vector_set(base_cb_extensions,i,(double)temp_float);
		//for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
			//gsl_matrix_set(base_cb_extensions,i,m_counter,(double)temp_float);
	}

	// Skip the dividers
	for (i=0;i<2;i++)
	{
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Now read the rates

	// First of all reserve space
	//function_type = new CString [no_of_transitions];
	function_type = new char[no_of_transitions];
	function_action = new char [no_of_transitions];
	//function_ligand = new CString [no_of_transitions];
	function_ligand = new char[no_of_transitions];
	base_function_values = gsl_matrix_alloc(no_of_transitions,
		MAX_RATE_FUNCTION_PARAMETERS);
	Ca_function_modifications = gsl_matrix_alloc(no_of_transitions,
		MAX_RATE_FUNCTION_PARAMETERS);
	Ca_function_copy = gsl_matrix_alloc(no_of_transitions,
		MAX_RATE_FUNCTION_PARAMETERS);

	for (i=0;i<no_of_conditions;i++)
	{
		cond_rate_mod[i] = gsl_matrix_alloc(no_of_transitions,
			no_of_function_parameters);
		cond_rate_copy[i] = gsl_matrix_alloc(no_of_transitions,
			no_of_function_parameters);
	}

	for (i=0;i<no_of_conditions;i++)
	{
		cond_fd_rate_mod[i] = gsl_matrix_alloc(no_of_transitions,
			no_of_function_parameters);
		cond_fd_rate_copy[i] = gsl_matrix_alloc(no_of_transitions,
			no_of_function_parameters);
	}

	for (i=0;i<m_no_of_isoforms;i++)
	{
		function_parameters[i] = gsl_matrix_alloc(no_of_transitions,
			MAX_RATE_FUNCTION_PARAMETERS);
		function_modifications[i] = gsl_matrix_alloc(no_of_transitions,
			MAX_RATE_FUNCTION_PARAMETERS);
	}

	function_copy = gsl_matrix_alloc(no_of_transitions,
		MAX_RATE_FUNCTION_PARAMETERS);

	// Allocate and zero rate_multiple arrays
	for (i=0;i<no_of_transitions;i++)
	{
		rate_multiple[i] = gsl_matrix_alloc(no_of_transitions,
			MAX_RATE_FUNCTION_PARAMETERS);

		gsl_matrix_set_zero(rate_multiple[i]);
	}

	base_delta_extensions = gsl_vector_alloc(no_of_states);

	base_delta_energies = gsl_vector_alloc(no_of_states);

	state_extensions_copy = gsl_vector_alloc(no_of_states);
	state_delta_extensions_copy = gsl_vector_alloc(no_of_states);

	br_slope = gsl_matrix_alloc(no_of_transitions,MAX_RATE_FUNCTION_PARAMETERS);
	gsl_matrix_set_all(br_slope,0.0);

	// Set matrices
	gsl_matrix_set_zero(base_function_values);
	gsl_matrix_set_zero(Ca_function_modifications);
	gsl_matrix_set_zero(Ca_function_copy);

	for (i=0;i<no_of_conditions;i++)
	{
		gsl_matrix_set_zero(cond_rate_mod[i]);
		gsl_matrix_set_zero(cond_rate_copy[i]);
	}

	for (i=0;i<no_of_conditions;i++)
	{
		gsl_matrix_set_all(cond_fd_rate_mod[i],1.0);
		gsl_matrix_set_zero(cond_fd_rate_copy[i]);
	}

	for (i=0;i<m_no_of_isoforms;i++)
	{
		gsl_matrix_set_zero(function_parameters[i]);
		gsl_matrix_set_zero(function_modifications[i]);
	}

	gsl_matrix_set_zero(function_copy);
	gsl_vector_set_zero(state_extensions_copy);
	gsl_vector_set_all(base_delta_extensions,DEFAULT_DELTA_PARAMETER_VALUE);
	gsl_vector_set_zero(state_delta_extensions_copy);
	gsl_vector_set_all(base_delta_energies,DEFAULT_DELTA_PARAMETER_VALUE);

	// Delta extensions modifications
	delta_extensions_modifications = gsl_matrix_alloc(no_of_states,m_no_of_isoforms);
	gsl_matrix_set_all(delta_extensions_modifications,1.0);
	
	for (i=0;i<no_of_transitions;i++)
	{
		// Skip the transition number
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);

		// Function type
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		function_type[i] = temp_string[0];

		// Function action
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		function_action[i]=temp_string[0];

		// Function ligand
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
		function_ligand[i] = temp_string[0];

		// Function parameters - copy them to every isoform
		for (j=0;j<no_of_function_parameters;j++)
		{
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
			{
				gsl_matrix_set(function_parameters[m_counter],i,j,(double)temp_float);
			}
		}
	}

	// Set the n_vector_indices
	set_n_vector_indices();

	// Tidy up
	fclose(instruction_file);
}

void base_parameters::set_n_vector_indices(void)
{
	// Code sets the start and stop indices for each state in the n_vector

	// Variables
	int i;
	int counter=0;
	
	// Code
	for (i=0;i<no_of_states;i++)
	{
		if (state_attached[i]==0)
		{
			n_vector_indices[i][0]=counter;
			n_vector_indices[i][1]=counter;
		}
		else
		{
			n_vector_indices[i][0]=counter;
			n_vector_indices[i][1]=counter+no_of_x_bins-1;
		}

		counter=n_vector_indices[i][1]+1;
	}
}

void base_parameters::fill_control_arrays(char * instruction_file_string)
{
	// Code fills the control arrays

	// Variables
	int i,j;

	int temp_int;
	int holder;
	int keep_going;

	float temp_float;

	char protocol_tag[] = PROTOCOL_TAG;
	char temp_string[MAX_STRING_LENGTH];

	// Code

	// Open the file
	FILE * instruction_file;
	//if (fopen_s(&instruction_file,instruction_file_string,"r")!=0)
	instruction_file = fopen(instruction_file_string, "r");
	if (instruction_file==NULL)
	{
		printf("Instruction file:\n\t%s\ncould not be opened\nNow finishing...",
			instruction_file_string);
		exit(1);
	}
	// Scan file for the control arrays
	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	while ((strcmp(temp_string,protocol_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("%s not found in %s\n",protocol_tag,instruction_file_string);
			printf("Now exiting\n");
			exit(1);
		}

		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Now count the text entries
	// Skip the header line
	for (i=1;i<=(1+(no_of_conditions*NO_OF_CONDITION_PARAMETERS));i++)
		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);
	// Read the values
	holder=0;
	keep_going=1;
	while (keep_going)
	{
		//temp_int=fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		temp_int = fscanf(instruction_file, "%s", temp_string);
		if ((temp_int!=0)&&(temp_int!=EOF))
		{
			keep_going=1;
			holder++;
		}
		else
		{
			keep_going=0;
		}
	}
	no_of_time_points=int((holder-1)/(1.0+((double)no_of_conditions*NO_OF_CONDITION_PARAMETERS)));

	// Allocate control arrays
	time_steps=gsl_vector_alloc(no_of_time_points);
	hs_increments=gsl_matrix_alloc(no_of_time_points,no_of_conditions);
	isotonic_forces=gsl_matrix_alloc(no_of_time_points,no_of_conditions);
	pCa_values=gsl_matrix_alloc(no_of_time_points,no_of_conditions);
	Pi_concentrations=gsl_matrix_alloc(no_of_time_points,no_of_conditions);
	ADP_concentrations=gsl_matrix_alloc(no_of_time_points,no_of_conditions);
	ATP_concentrations=gsl_matrix_alloc(no_of_time_points,no_of_conditions);

	// Rewind and rescan
	rewind(instruction_file);

	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	while ((strcmp(temp_string,protocol_tag)!=0)&&(!feof(instruction_file)))
	{
		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);
	}
	// Skip the header line
	for (i=1;i<=(1+(no_of_conditions*NO_OF_CONDITION_PARAMETERS));i++)
		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);

	// Read the data
	for (i=0;i<no_of_time_points;i++)
	{
		//fscanf_s(instruction_file,"%f",&temp_float);
		fscanf(instruction_file, "%f", &temp_float);
		gsl_vector_set(time_steps,i,(double)temp_float);

		for (j=0;j<no_of_conditions;j++)
		{
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(hs_increments,i,j,(double)temp_float);

			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(isotonic_forces,i,j,(double)temp_float);

			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(pCa_values,i,j,(double)temp_float);

			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(Pi_concentrations,i,j,(double)temp_float);

			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(ADP_concentrations,i,j,(double)temp_float);

			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			gsl_matrix_set(ATP_concentrations,i,j,(double)temp_float);
		}
	}

	// Tidy up
	fclose(instruction_file);
}

double * base_parameters::return_pointer_to_fixed_parameter(char * tag_string)
{
	// Code returns a pointer to a fixed parameter

	// Variables
	double * p_double;

	tag_data_struct tag_data;
	tag_data_struct * p_tag_data =& tag_data;


	// Code

	// Possibilities
	if (strcmp(tag_string,"k_cb_linear")==0)
		return p_k_cb_linear;

	if (strcmp(tag_string,"temperature")==0)
		return p_temperature;

	if (strcmp(tag_string,"passive_force_mode")==0)
		return p_passive_force_mode;

	if (strcmp(tag_string,"passive_force_linear")==0)
		return p_passive_force_linear;

	if (strcmp(tag_string,"movement_enhancement")==0)
		return p_movement_enhancement;

	if (strcmp(tag_string,"hs_thick_filament_length")==0)
		return p_hs_thick_filament_length;

	if (strcmp(tag_string,"hs_thin_filament_length")==0)
		return p_hs_thin_filament_length;

	if (strcmp(tag_string,"hs_bare_zone_length")==0)
		return p_hs_bare_zone_length;

	if (strcmp(tag_string,"isotonic_on_mode")==0)
		return p_isotonic_on_mode;

	if (strcmp(tag_string,"filament_compliance_factor")==0)
		return p_filament_compliance_factor;

	if (strcmp(tag_string,"N_variability")==0)
		return p_N_variability;

	if (strcmp(tag_string,"P_variability")==0)
		return p_P_variability;

	if (strcmp(tag_string,"series_compliance_effect")==0)
		return p_series_compliance_effect;

	if (strcmp(tag_string,"coop_power")==0)
		return p_coop_power;

	if (strcmp(tag_string,"dN_mode")==0)
		return p_dN_mode;

	if (strncmp(tag_string,"isotonic_off_mode",17)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& isotonic_off_mode->data[(p_tag_data->int_1-1)*
						isotonic_off_mode->stride];

		return p_double;
	}

	if (strncmp(tag_string,"ml_recovery_start",17)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& ml_recovery_start->data[(p_tag_data->int_1-1)*
						isotonic_off_mode->stride];

		return p_double;
	}

	if (strncmp(tag_string,"ml_recovery_stop",16)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& ml_recovery_stop->data[(p_tag_data->int_1-1)*
						isotonic_off_mode->stride];

		return p_double;
	}


	if (strncmp(tag_string,"series_k_vector",15)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& series_k_vector->data[(p_tag_data->int_1-1)*
				series_k_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"series_alpha_vector",19)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& series_alpha_vector->data[(p_tag_data->int_1-1)*
				series_alpha_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"series_beta_vector",18)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& series_beta_vector->data[(p_tag_data->int_1-1)*
				series_beta_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"k_plus_vector",13)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& k_plus_vector->data[(p_tag_data->int_1-1)*
				k_plus_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"k_minus_vector",13)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& k_minus_vector->data[(p_tag_data->int_1-1)*
				k_minus_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"N_variability_vector",20)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& N_variability_vector->data[(p_tag_data->int_1-1)*
				N_variability_vector->stride];

		return p_double;
	}

	if (strncmp(tag_string,"P_variability_vector",20)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& P_variability_vector->data[(p_tag_data->int_1-1)*
				P_variability_vector->stride];

		return p_double;
	}
	
	if (strncmp(tag_string,"initial_dml",11)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& initial_dml->data[(p_tag_data->int_1-1)*
				initial_dml->stride];

		return p_double;
	}
	
	// Fall through
	return NULL;
}

double * base_parameters::return_pointer_to_adjustable_parameter(char * tag_string)
{
	// Code returns a pointer to an adjustable parameter

	// Variables
	double * p_double;

	tag_data_struct tag_data;
	tag_data_struct * p_tag_data =& tag_data;
	
	// Code

	// Possibilities
	if (strcmp(tag_string,"hs_k_falloff")==0)
		return p_hs_k_falloff;

	if (strcmp(tag_string,"passive_hsl_slack")==0)
		return p_passive_hsl_slack;

	if (strcmp(tag_string,"passive_k_linear")==0)
		return p_passive_k_linear;

	if (strcmp(tag_string,"passive_sigma")==0)
		return p_passive_sigma;

	if (strcmp(tag_string,"passive_L")==0)
		return p_passive_L;

	if (strcmp(tag_string,"passive_L_slack_hsl")==0)
		return p_passive_L_slack_hsl;

	if (strcmp(tag_string,"series_alpha")==0)
		return p_series_alpha;

	if (strcmp(tag_string,"series_beta")==0)
		return p_series_beta;

	if (strcmp(tag_string,"series_L0")==0)
		return p_series_L0;

	if (strcmp(tag_string,"series_F0")==0)
		return p_series_F0;
	
	if (strcmp(tag_string,"series_k")==0)
		return p_series_k;

	if (strcmp(tag_string,"a_on_rate")==0)
		return p_a_on_rate;

	if (strcmp(tag_string,"a_off_rate")==0)
		return p_a_off_rate;

	if (strcmp(tag_string,"k_plus")==0)
		return p_k_plus;

	if (strcmp(tag_string,"k_minus")==0)
		return p_k_minus;

	if (strcmp(tag_string,"k_coop")==0)
		return p_k_coop;

	if (strcmp(tag_string,"k_recruit_tf")==0)
		return p_k_recruit_tf;

	if (strcmp(tag_string,"k_recruit_cbf")==0)
		return p_k_recruit_cbf;

	if (strcmp(tag_string,"k_recruit_pf")==0)
		return p_k_recruit_pf;
	
	if (strcmp(tag_string,"base_k_cb_pos")==0)
		return p_base_k_cb_pos;

	if (strcmp(tag_string,"base_k_cb_neg")==0)
		return p_base_k_cb_neg;

	if (strcmp(tag_string,"viscosity")==0)
		return p_viscosity;

	if (strcmp(tag_string,"ld_slack_hsl")==0)
		return p_ld_slack_hsl;

	if (strcmp(tag_string,"N_variability")==0)
		return p_N_variability;

	if (strcmp(tag_string,"base_Ca_concentration")==0)
		return p_base_Ca_concentration;

	if (strcmp(tag_string,"Ca_threshold")==0)
		return p_Ca_threshold;

	if (strcmp(tag_string,"t_start")==0)
		return p_t_start;

	if (strcmp(tag_string,"k_windkessel")==0)
		return p_k_windkessel;

	if (strcmp(tag_string,"d_windkessel")==0)
		return p_d_windkessel;

	// Progressive relaxation
	if (strcmp(tag_string,"first_alpha")==0)
		return p_first_alpha;

	if (strcmp(tag_string,"inter_z_factor")==0)
		return p_inter_z_factor;

	if (strcmp(tag_string,"inter_thick_factor")==0)
		return p_inter_thick_factor;

	if (strcmp(tag_string,"inter_hs_factor")==0)
		return p_inter_hs_factor;


	// More complicated things
	if (strncmp(tag_string,"base_rates",10)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& base_function_values->data[((p_tag_data->int_1-1) * 
				base_function_values->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"cond_rate_mod",13)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& cond_rate_mod[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					cond_rate_mod[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"cond_rate_copy",14)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& cond_rate_copy[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					cond_rate_copy[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"cond_fd_rate_mod",16)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& cond_fd_rate_mod[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					cond_fd_rate_mod[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"cond_fd_rate_copy",17)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& cond_fd_rate_copy[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					cond_fd_rate_copy[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"Ca_rate_mod",11)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& Ca_function_modifications->data[((p_tag_data->int_1-1) * 
				Ca_function_modifications->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"Ca_rate_copy",12)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& Ca_function_copy->data[((p_tag_data->int_1-1) * 
				Ca_function_copy->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"rate_copy",9)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& function_copy->data[((p_tag_data->int_1-1) * 
				function_copy->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"thin_function_mod",17)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& thin_function_mod->data[((p_tag_data->int_1-1) *
				thin_function_mod->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"thin_function_copy",18)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& thin_function_copy->data[((p_tag_data->int_1-1) *
				thin_function_copy->tda) + p_tag_data->int_2-1];

		return p_double;
	}
	
	if (strncmp(tag_string,"cond_scale",10)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& cond_scaling_factor->data[((p_tag_data->int_1-1) *
			cond_scaling_factor->tda) + p_tag_data->int_2-1];
		
		return p_double;
	}

	if (strncmp(tag_string,"cond_copy",9)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& cond_scaling_copy->data[((p_tag_data->int_1-1) *
					cond_scaling_copy->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"rate_mod",8)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& function_modifications[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					function_modifications[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"rate_multiple",13)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,3);

		p_double =& rate_multiple[p_tag_data->int_3-1]->
						data[((p_tag_data->int_1-1) *
					rate_multiple[p_tag_data->int_3-1]->tda) +
						p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"k_cb_pos_mod",12)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& k_cb_pos_modifications->data[(p_tag_data->int_1-1)*
						k_cb_pos_modifications->stride];

		return p_double;
	}

	if (strncmp(tag_string,"k_cb_mult",9)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& k_cb_multiplier->data[(p_tag_data->int_1-1)*
						k_cb_multiplier->stride];

		return p_double;
	}

	if (strncmp(tag_string,"base_cb_ext",11)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& base_cb_extensions->data[(p_tag_data->int_1-1)*
						base_cb_extensions->stride];

		return p_double;
	}

	if (strncmp(tag_string,"base_cb_energy",14)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& base_cb_energies->data[(p_tag_data->int_1-1)*
						base_cb_energies->stride];

		return p_double;
	}

	if (strncmp(tag_string,"base_delta_ext",14)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& base_delta_extensions->data[(p_tag_data->int_1-1)*
						base_delta_extensions->stride];

		return p_double;
	}

	if (strncmp(tag_string,"d_hsl_slack",11)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& d_hsl_slack->data[(p_tag_data->int_1-1) *
						d_hsl_slack->stride];

		return p_double;
	}

	if (strncmp(tag_string,"delta_ext_mod",13)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& delta_extensions_modifications->data[((p_tag_data->int_1-1) * 
				delta_extensions_modifications->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"base_delta_energy",17)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& base_delta_energies->data[(p_tag_data->int_1-1)*
						base_delta_energies->stride];

		return p_double;
	}

	if (strncmp(tag_string,"Ca_scale_factor",15)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& Ca_scaling_factor->data[(p_tag_data->int_1-1)*
						Ca_scaling_factor->stride];

		return p_double;
	}

	if (strncmp(tag_string,"ld_slope",8)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& ld_slope->data[(p_tag_data->int_1-1)*
						ld_slope->stride];

		return p_double;
	}

	if (strncmp(tag_string,"ld_rate",7)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& ld_rate->data[((p_tag_data->int_1-1) *
			ld_rate->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"fd_slope",8)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,1);

		p_double =& fd_slope->data[(p_tag_data->int_1-1) *
						fd_slope->stride];

		return p_double;
	}

	if (strncmp(tag_string,"fd_rate",7)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& fd_rate->data[((p_tag_data->int_1-1) *
			fd_rate->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"fd_coefs",8)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& fd_coefs->data[((p_tag_data->int_1-1) *
			fd_coefs->tda) + p_tag_data->int_2-1];

		return p_double;
	}

	if (strncmp(tag_string,"br_slope",8)==0)
	{
		p_tag_data = set_tag_data(p_tag_data,tag_string,2);

		p_double =& br_slope->data[((p_tag_data->int_1-1) *
			br_slope->tda) + p_tag_data->int_2-1];

		return p_double;
	}
	
	// Default
	return NULL;
}

tag_data_struct * set_tag_data(tag_data_struct * p_tag_data,
	char * tag_string, int no_of_parameters)
{
	// Code sets the int values for the tag_string
	// This is used in deducing adjustable parameter values

	// Variables
	int i,j;
	int start;
	int stop;
	int place;
	int temp_int;

	char * p_char;
	char temp_string[MAX_STRING_LENGTH];

	// Code
	for (i=1;i<=no_of_parameters;i++)
	{
		if (no_of_parameters==1)
		{
			p_char = strrchr(tag_string,'_');
			place=(int)(p_char-tag_string+1);

			temp_int=0;
			for (j=place;j<=(int)strlen(tag_string);j++)
			{
				temp_string[temp_int]=tag_string[j];
				temp_int++;
			}
			temp_string[temp_int]='\0';
		}
		else
		{
			if (i==1)
			{
				p_char = strrchr(tag_string,'_');
				start=(int)(p_char-tag_string+1);
				p_char = strrchr(tag_string,'@');
				stop=(int)(p_char-tag_string-1);
			}
			else
			{
				if (no_of_parameters==2)
				{
					if (i==2)
					{
						p_char = strrchr(tag_string,'@');
						start=(int)(p_char-tag_string+1);
						stop=(int)strlen(tag_string);
					}
				}
				else
				{
					if (i==2)
					{
						p_char = strrchr(tag_string,'@');
						start=(int)(p_char-tag_string+1);
						p_char = strrchr(tag_string,'#');
						stop=(int)(p_char-tag_string-1);
					}

					if (i==3)
					{
						p_char = strrchr(tag_string,'#');
						start=(int)(p_char-tag_string+1);
						stop=(int)strlen(tag_string);
					}
				}
			}
		
			temp_int=0;
			for (place=start;place<=stop;place++)
			{
				temp_string[temp_int]=tag_string[place];
				temp_int++;
			}
			temp_string[temp_int]='\0';
		}

		if (i==1)
			p_tag_data->int_1 = atoi(temp_string);
		if (i==2)
			p_tag_data->int_2 = atoi(temp_string);
		if (i==3)
			p_tag_data->int_3 = atoi(temp_string);
	}

	return p_tag_data;
}

void base_parameters::set_fixed_parameters_from_file(char * instruction_file_string)
{
	// Code updates the values of fixed parameters

	// Variables
	float temp_float;

	double * p_double;

	char temp_string[MAX_STRING_LENGTH];
	char fixed_tag[] = FIXED_TAG;
	char end_tag[MAX_STRING_LENGTH];

	// Code
	FILE * instruction_file;
	//fopen_s(&instruction_file,instruction_file_string,"r");
	instruction_file = fopen(instruction_file_string, "r");
	if (instruction_file==NULL)
	{
		printf("base_parameters::set_fixed_parameters_from_file...\n");
		printf("file %s could not be opened\n",instruction_file_string);
		printf("Now exiting\n");
		exit(1);
	}

	// Scan file for the fixed parameters
	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	while ((strcmp(temp_string,fixed_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("%s not found in:\n\t%s\nNow finishing...\n",
				fixed_tag,
				instruction_file_string);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Now read parameters until you get to the end tag

	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	printf("\nNow reading fixed parameters\n");

	// Deduce the end_tag
	//sprintf_s(end_tag,"//END_",MAX_STRING_LENGTH);
	sprintf(end_tag, "//END_");
	//sprintf_s(end_tag,"%s%s",end_tag,fixed_tag+2,MAX_STRING_LENGTH);
	sprintf(end_tag, "%s%s", end_tag, fixed_tag + 2);

	// Read the next value
	//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
	fscanf(instruction_file, "%s", temp_string);

	while ((strcmp(temp_string,end_tag)!=0))
	{
		// Get the pointer
		p_double=return_pointer_to_fixed_parameter(temp_string);

		if (p_double!=NULL)
		{
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);

			// Set the variable value
			*p_double = (double)temp_float;
		}

		// Display
		printf("Fixed parameter: %s = %g\n",temp_string,(double)temp_float);

		// Read the next value
		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Tidy up
	fclose(instruction_file);
}

void base_parameters::set_adjustable_parameters_from_file(char * instruction_file_string)
{
	// Code updates the values of adjustable parameters

	// Variables
	int i,j,k;
	int m_counter;
	int adjustable;
	int temp_int;

	char temp_string[MAX_STRING_LENGTH];
	char mode_string[MAX_STRING_LENGTH];

	char adjustable_tag[] = ADJUSTABLE_TAG;
	char end_tag[MAX_STRING_LENGTH];

	float temp_float;

	double p_value;
	double temp_value;
	double min_value;
	double max_value;

	double * p_double;

	// Code
	FILE * instruction_file;
	//fopen_s(&instruction_file,instruction_file_string,"r");
	instruction_file = fopen(instruction_file_string, "r");
	if (instruction_file==NULL)
	{
		printf("base_parameters::set_adjustable_parameters_from_file...\n");
		printf("file %s could not be opened\n",instruction_file_string);
		printf("Now exiting\n");
		exit(1);
	}

	// Scan file for the adjustable parameters
	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	while ((strcmp(temp_string,adjustable_tag)!=0))
	{
		if (feof(instruction_file))
		{
			printf("%s not found in:\n\t%s\nNow finishing...\n",
				adjustable_tag,
				instruction_file_string);
			exit(1);
		}
		//fscanf_s(instruction_file,"%s",temp_string,_MAX_PATH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Now read parameters until you get to the end tag

	//sprintf_s(temp_string,"");
	sprintf(temp_string, "");
	printf("\nNow reading adjustable parameters\n");

	// Deduce the end_tag
	//sprintf_s(end_tag,"//END_",MAX_STRING_LENGTH);
	sprintf(end_tag, "//END_");
	//sprintf_s(end_tag,"%s%s",end_tag,adjustable_tag+2,MAX_STRING_LENGTH);
	sprintf(end_tag, "%s%s", end_tag, adjustable_tag + 2);

	while ((strcmp(temp_string,end_tag)!=0))
	{
		if (strcmp(temp_string,"")!=0)
		{
			printf("%s\n",temp_string);
		}

		p_double=return_pointer_to_adjustable_parameter(temp_string);

		if (p_double!=NULL)
		{
			//fscanf_s(instruction_file,"%i",&adjustable);
			fscanf(instruction_file, "%i", &adjustable);
			//fscanf_s(instruction_file,"%s",&mode_string,MAX_STRING_LENGTH);
			fscanf(instruction_file, "%s", &mode_string);
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			p_value=(double)temp_float;
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			min_value=(double)temp_float;
			//fscanf_s(instruction_file,"%f",&temp_float);
			fscanf(instruction_file, "%f", &temp_float);
			max_value=(double)temp_float;

			temp_value = deduce_adjustable_parameter_value(
				p_value,min_value,max_value);

			// Adjust for log or linear mode
			if (strcmp(mode_string,"lin")==0)
				*p_double = temp_value;
			else
			{
				if (strcmp(mode_string,"log")==0)
				{
					// Positive value
					*p_double = pow(10,temp_value);
				}
				else
				{
					// Negative value
					*p_double = -pow(10,temp_value);
				}
			}

			printf("Tag %s  Value %g\n",temp_string,*p_double);
		}

		//fscanf_s(instruction_file,"%s",temp_string,MAX_STRING_LENGTH);
		fscanf(instruction_file, "%s", temp_string);
	}

	// Look for base_function_values != 0
	// These change the values for every isoform


	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			temp_value = gsl_matrix_get(base_function_values,i,j);
			if (temp_value!=0.0)
			{
				// Update the value for all the isoforms
				for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
				{
					gsl_matrix_set(function_parameters[m_counter],i,j,temp_value);
				}
			}
		}
	}

	// Now look for modifications
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		for (i=0;i<no_of_transitions;i++)
		{
			for (j=0;j<no_of_function_parameters;j++)
			{
				temp_value = gsl_matrix_get(function_modifications[m_counter],i,j);
				// Update by multiplying the value for the first isoform
				if (temp_value!=0.0)
				{
					gsl_matrix_set(function_parameters[m_counter],i,j,
						temp_value * gsl_matrix_get(function_parameters[0],i,j));
				}
			}
		}
	}

	// Look for rate copies
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			// Produces an integer
			temp_value = gsl_matrix_get(function_copy,i,j);
			
			// If the integer is not zero, copy the jth function parameter of transition temp_int
			// to the jth function parameter of transition i for every m_isoform

			temp_int = (int)(floor(fabs(gsl_matrix_get(function_copy,i,j))+0.5));
			if (temp_int>0)
			{
				for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
				{
					gsl_matrix_set(function_parameters[m_counter],i,j,
						gsl_matrix_get(function_parameters[m_counter],temp_int-1,j));
				}
			}
		}
	}

	// Look for cond_Ca_copies
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<MAX_NO_OF_SCALING_FACTORS;j++)
		{
			// Produces an integer
			temp_int = (int)(floor(fabs(gsl_matrix_get(cond_scaling_copy,i,j))+0.5));

			// If the integer is not zero, copy the ith cond_scaling_factor
			if (temp_int>0)
			{
				gsl_matrix_set(cond_scaling_factor,i,j,
					gsl_matrix_get(cond_scaling_factor,temp_int-1,j));
			}
		}
	}

	// Look for Ca_function_copies
	for (i=0;i<no_of_transitions;i++)
	{
		for (j=0;j<no_of_function_parameters;j++)
		{
			// Produces an integer
			temp_int = (int)(floor(fabs(gsl_matrix_get(Ca_function_copy,i,j))+0.5));

			// If the integer is not zero, copy the jth Ca_function copy
			if (temp_int>0)
			{
				gsl_matrix_set(Ca_function_modifications,i,j,
					gsl_matrix_get(Ca_function_modifications,temp_int-1,j));
			}
		}
	}
/*
	// Look for cond_rate_copies
	for (i=0;i<no_of_conditions;i++)
	{
		for (j=0;j<no_of_transitions;j++)
		{
			for (k=0;k<no_of_function_parameters;k++)
			{
				// Produces an integer
				temp_int = (int)(floor(fabs(gsl_matrix_get(cond_rate_copy[i],j,k))+0.5));

				// If the integer is not zero, copy the jth cond_rate_mod
				if (temp_int>0)
				{
					gsl_matrix_set(cond_rate_mod[i],j,k,
						gsl_matrix_get(cond_rate_mod[temp_int-1],j,k));
				}
			}
		}
	}
*/

	// Set the k_cb_pos which is equal to the base value multiplied by any non-zero modification
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		gsl_vector_set(k_cb_pos,m_counter,base_k_cb_pos);

		temp_value = gsl_vector_get(k_cb_pos_modifications,m_counter);
		if (temp_value!=0.0)
			gsl_vector_set(k_cb_pos,m_counter,base_k_cb_pos * temp_value);
	}

	// Similary for k_cb_neg
	for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
	{
		gsl_vector_set(k_cb_neg,m_counter,base_k_cb_neg);

		temp_value = gsl_vector_get(k_cb_neg_modifications,m_counter);
		if (temp_value!=0.0)
			gsl_vector_set(k_cb_neg,m_counter,base_k_cb_neg * temp_value);
	}

	// Force updates if the system is linear
	if (k_cb_linear>0.5)
	{
		for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
		{
			gsl_vector_set(k_cb_neg,m_counter,gsl_vector_get(k_cb_pos,m_counter));
		}
	}

	// Set the cb_extensions which are the base values multiplied by any non-zero
	// modifications
	for (i=0;i<no_of_states;i++)
	{
		for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
		{
			gsl_matrix_set(cb_extensions,i,m_counter,
				gsl_vector_get(base_cb_extensions,i));
		}
	}

	// Look for delta_extensions
	for (i=1;i<no_of_states;i++)
	{
		temp_value=gsl_vector_get(base_delta_extensions,i);

		if (temp_value!=DEFAULT_DELTA_PARAMETER_VALUE)
		{
			for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
			{
				// Set the extension allowing for a modifier
				gsl_matrix_set(cb_extensions,i,m_counter,
					gsl_matrix_get(cb_extensions,i-1,m_counter)+
						temp_value * gsl_matrix_get(delta_extensions_modifications,
										i-1,m_counter));
			}
		}
	}

	// Set the cb_base_energies
	for (i=0;i<no_of_states;i++)
	{
		for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
		{
			gsl_matrix_set(cb_base_energies,i,m_counter,
				gsl_vector_get(base_cb_energies,i));
		}
	}

	// Look for delta_cb_energies
	for (i=1;i<no_of_states;i++)
	{
		temp_value = gsl_vector_get(base_delta_energies,i);

		if (temp_value!=DEFAULT_DELTA_PARAMETER_VALUE)
		{
			for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
			{
				gsl_matrix_set(cb_base_energies,i,m_counter,
					gsl_matrix_get(cb_base_energies,i-1,m_counter) +
						temp_value);
			}
		}
	}

	// Look for rate_multiples
	for (i=1;i<=no_of_transitions;i++)
	{
		for (j=1;j<=no_of_transitions;j++)
		{
			for (k=1;k<=MAX_RATE_FUNCTION_PARAMETERS;k++)
			{
				temp_value = gsl_matrix_get(rate_multiple[i-1],j-1,k-1);
				
				if ((temp_value > 0.0) || (temp_value < 0.0))
				{
					for (m_counter=0;m_counter<m_no_of_isoforms;m_counter++)
					{
						gsl_matrix_set(function_parameters[m_counter],i-1,k-1,
							temp_value * gsl_matrix_get(function_parameters[m_counter],j-1,k-1));
					}
				}
			}
		}
	}

	// Tidy up
	fclose(instruction_file);
}

double base_parameters::deduce_adjustable_parameter_value(double p_value,
	double min_value, double max_value)
{
	double temp;

	temp=fmod(fabs(p_value),2.0);

	if (temp<1.0)
	{
		return min_value+temp*(max_value-min_value);
	}
	else
	{
		return max_value-(temp-1.0)*(max_value-min_value);
	}
}
