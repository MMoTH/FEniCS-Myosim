#ifndef BASE_PARAMETERS_H                           
#define BASE_PARAMETERS_H

//#include "atlstr.h"
#include <string.h>
#include "global_definitions.h"

#include "gsl/gsl_vector.h"
#include "gsl/gsl_matrix.h"
#include "gsl/gsl_rng.h"

class base_parameters
{
	public:
		// Constructor and destructor
		base_parameters(char * set_instruction_file_string,
			char * set_output_directory_string);
		~base_parameters(void);

		// Variables
		char instruction_file_string[MAX_STRING_LENGTH];
		char output_dir_string[MAX_STRING_LENGTH];

		int particle_number;
		int check_number;
		int distributions_dump_mode;
		int error_flag;

		int debug_dump_mode;

		int no_of_conditions;
		int no_of_time_points;

		int no_of_half_sarcomeres;
		int no_of_myofibrils;
		int no_of_half_sarcomeres_in_series;
		
		int no_of_x_bins;
		double x_bin_min;
		double x_bin_max;
		double x_bin_increment;

		int no_of_states;
		int no_of_attached_states;
		int no_of_detached_states;

		int no_of_transitions;
		int no_of_function_parameters;

		int ** state_transitions;
		int ** state_rate_functions;
		int ** n_vector_indices;

		int * state_attached;

		//CString * function_type;
		char * function_type;
		char * function_action;
		//CString * function_ligand;
		char * function_ligand;
		gsl_matrix * function_parameters [M_MAX_NO_OF_ISOFORMS];

		gsl_matrix * base_function_values;
		gsl_matrix * Ca_function_modifications;
		gsl_matrix * Ca_function_copy;
		gsl_matrix * function_modifications [M_MAX_NO_OF_ISOFORMS];

		gsl_matrix * thin_function_mod;
		gsl_matrix * thin_function_copy;

		gsl_vector * base_cb_extensions;

		gsl_vector * base_cb_energies;

		gsl_vector * k_cb_pos;
		gsl_vector * k_cb_pos_modifications;
		
		gsl_vector * k_cb_neg;
		gsl_vector * k_cb_neg_modifications;

		gsl_vector * k_cb_multiplier;

		gsl_matrix * cb_extensions;
		gsl_matrix * cb_base_energies;
		
		gsl_matrix * function_copy;

		gsl_vector * base_delta_extensions;
		gsl_vector * base_delta_energies;
		
		gsl_matrix * delta_extensions_modifications;

		gsl_vector * state_extensions_copy;
		gsl_vector * state_delta_extensions_copy;

		gsl_vector * x_bins;

		gsl_vector * Ca_scaling_factor;
		gsl_matrix * cond_scaling_factor;
		gsl_matrix * cond_scaling_copy;

		gsl_vector * ld_slope;
		gsl_matrix * ld_rate;

		gsl_vector * fd_slope;
		gsl_matrix * fd_rate;

		gsl_matrix * fd_coefs;

		gsl_matrix * br_slope;

		gsl_vector * initial_dml;

		gsl_matrix * cond_rate_mod	[MAX_NO_OF_CONDITIONS];
		gsl_matrix * cond_rate_copy	[MAX_NO_OF_CONDITIONS];

		gsl_matrix * rate_multiple [MAX_NO_OF_TRANSITIONS];

		gsl_matrix * cond_fd_rate_mod [MAX_NO_OF_CONDITIONS];
		gsl_matrix * cond_fd_rate_copy [MAX_NO_OF_CONDITIONS];

		gsl_vector * isotonic_off_mode;

		gsl_vector * d_hsl_slack;

		gsl_vector * series_k_vector;
		gsl_vector * series_alpha_vector;
		gsl_vector * series_beta_vector;

		gsl_vector * k_plus_vector;
		gsl_vector * k_minus_vector;

		gsl_vector * N_variability_vector;
		gsl_vector * P_variability_vector;

		int m_no_of_isoforms;
		gsl_matrix * m_isoform_rel_populations;

		// Control arrays
		gsl_vector * time_steps;
		gsl_matrix * hs_increments;
		gsl_matrix * isotonic_forces;
		gsl_matrix * pCa_values;
		gsl_matrix * Pi_concentrations;
		gsl_matrix * ADP_concentrations;
		gsl_matrix * ATP_concentrations;

		// Doubles
		double initial_hs_length;

		double beta;

		// Single adjustable variables

		double temperature;
		double * p_temperature;

		double base_k_cb_pos;
		double * p_base_k_cb_pos;

		double base_k_cb_neg;
		double * p_base_k_cb_neg;

		double a_on_rate;
		double * p_a_on_rate;

		double a_off_rate;
		double * p_a_off_rate;

		double k_plus;
		double * p_k_plus;

		double k_minus;
		double * p_k_minus;

		double k_coop;
		double * p_k_coop;

		double k_recruit_tf;
		double * p_k_recruit_tf;

		double k_recruit_cbf;
		double * p_k_recruit_cbf;

		double k_recruit_pf;
		double * p_k_recruit_pf;

		double passive_force_mode;
		double * p_passive_force_mode;

		double passive_force_linear;
		double * p_passive_force_linear;

		double passive_hsl_slack;
		double * p_passive_hsl_slack;

		double passive_k_linear;
		double * p_passive_k_linear;
		
		double passive_sigma;
		double * p_passive_sigma;
		
		double passive_L;
		double * p_passive_L;

		double passive_L_slack_hsl;
		double * p_passive_L_slack_hsl;

		double passive_L_slack_k;
		double * p_passive_L_slack_k;

		double series_alpha;
		double * p_series_alpha;

		double series_beta;
		double * p_series_beta;

		double series_L0;
		double * p_series_L0;

		double series_F0;
		double * p_series_F0;

		double series_k;
		double * p_series_k;

		double coop_power;
		double * p_coop_power;

		double series_compliance_effect;
		double * p_series_compliance_effect;

		double movement_enhancement;
		double * p_movement_enhancement;

		double filament_compliance_factor;
		double * p_filament_compliance_factor;

		double dN_mode;
		double * p_dN_mode;

		double k_cb_linear;
		double * p_k_cb_linear;

		double viscosity;
		double * p_viscosity;

		double cb_number_density;
		double * p_cb_number_density;

		double hs_k_falloff;
		double * p_hs_k_falloff;

		double hs_thick_filament_length;
		double * p_hs_thick_filament_length;

		double hs_thin_filament_length;
		double * p_hs_thin_filament_length;

		double hs_bare_zone_length;
		double * p_hs_bare_zone_length;

		double ld_slack_hsl;
		double * p_ld_slack_hsl;

		double base_Ca_concentration;
		double * p_base_Ca_concentration;

		double Ca_threshold;
		double * p_Ca_threshold;

		double t_start;
		double * p_t_start;

		// Isotonic modes
		double isotonic_on_mode;
		double * p_isotonic_on_mode;

		double k_windkessel;
		double * p_k_windkessel;

		double d_windkessel;
		double * p_d_windkessel;

		// Progressive_relaxation
		double first_alpha;
		double * p_first_alpha;

		double inter_z_factor;
		double * p_inter_z_factor;

		double inter_thick_factor;
		double * p_inter_thick_factor;

		double inter_hs_factor;
		double * p_inter_hs_factor;

		// Recovery mode
		gsl_vector * ml_recovery_mode;
		gsl_vector * ml_recovery_start;
		gsl_vector * ml_recovery_stop;
		gsl_vector * ml_recovery_flag;

		// Variability
		double N_variability;
		double * p_N_variability;

		double P_variability;
		double * p_P_variability;

		// Random numbers
		const gsl_rng_type * rand_T;
		gsl_rng * rand_r;
		
		// Functions
		void display_base_parameters(void);
		void dump_base_parameters(void);
		void set_base_parameters_from_instruction_file(char * instruction_file_string);
		void load_m_isoform_data(char * instruction_file_string);
		void load_kinetic_scheme(char * instruction_file_string);
		void set_n_vector_indices(void);
		void fill_control_arrays(char * instruction_file_string);
		void set_fixed_parameters_from_file(char * instruction_file_string);
		void set_adjustable_parameters_from_file(char * instruction_file_string);
		double * return_pointer_to_fixed_parameter(char * tag_string);
		double * return_pointer_to_adjustable_parameter(char * tag_string);
		double deduce_adjustable_parameter_value(double p_value,
					double min_value, double max_value);
};
#endif