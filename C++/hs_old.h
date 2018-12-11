#ifndef HS_H                           
#define HS_H

#include <iostream>
#include <dolfin/parameter/Parameters.h>
#include <vector>

#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv.h>
#include <gsl/gsl_spline.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_rng.h>

class mf; 

class Ca; 

class base_parameters;

namespace dolfin
{
	//defining class template "Array" which FEniCS needs for import/export vectors from/to C++ module
	template<typename T> class Array;

	class hs // sarcomere related parameters and functions
	{
	public:
		
		// constructor
		hs();
		
		// destructor
		~hs();

		// cb_force_vec is vector of cb_force for all isoforms-elements
		std::vector<double> cb_force_vec;

		// vector of ODE solutions for all isoforms-elements
		std::vector<double> y_vec;
		
		mf * p_mf;
		Ca * p_Ca;
		base_parameters * p_bp;

		struct FE
		{
			double cb_force;        // used in mf::generic_rate
			double passive_force;   // used in mf::generic_rate

			double step_size;       // used in hs::implement_time_step
			double cell_time;       // used in Ca::Calcium
			double t_act;           // used in Ca::Calcium
			//char * input_path;
			//char * output_path;
		};
		
		FE * p_FE;

		// after a python script reads XML instruction file to a python dictionary,
		// dolfin "Parameters" class used to pass parameters from python to C++

		// create instances of dolfin "Parameters" class
	

		Parameters FE_params;     // "FEniCS_params" transfers FE-parameters from FEniCS to "FE" structure defined above
		//Parameters hs_params;	  // "hs_params" transfers hs-parameters from FEniCS to "hs" class
		//Parameters mf_params;     //"mf_params" transfers mf - parameters from FEniCS to "mf" class
		Parameters Ca_params;     //"Ca_params" transfers Ca - parameters from FEniCS to "Ca" class
	
		

		double t;
		double step_size;
		double hsl; // used in hs::derivs

		int m_isoform;
		int no_of_int_points;

		// alpha and beta - builds variability into forces
		double alpha_value = 1.0;
		double beta_value = 1.0;

		int no_of_states;
		int no_of_attached_states;
		int no_of_detached_states;
		double x_bin_min;
		double x_bin_max;
		double x_bin_increment;
		int no_of_x_bins;
		int n_array_length;
		int no_of_transitions;

		int * state_attached;

		int ** state_transitions;
		int ** state_rate_functions;
		int ** n_vector_indices;

		char * function_type;
		char * function_action;
		char * function_ligand;

		gsl_vector * x;
		
		gsl_odeiv_system sys;

		// LCL
		// function to call calculated cb_force_vec in implement_time_step from FEniCS
		std::vector<double> Get_cb_force_vec();
		double Get_Ca();
	
		// function to evolve_kinetics, shift_cb_distributions and calculate cb_force one time step forward for all isoforms-elements, returns y_vec
		// z is y_vec of previous time step passed to C++ module for ODE initialization in new time step
		// hsl and delta_hsl are vectors of current hsl and current minus previous time step hsl lengths for all isoforms-elements
		//std::vector<double> implement_time_step(const Array<double>& z, const Array<double>& delta_hsl, const Array<double>& hsl, const Array<double>& p_f, const Array<double>& cb_f);
		std::vector<double> apply_time_step(const Array<double>& z, const Array<double>& delta_hsl, const Array<double>& hslen, const Array<double>& p_f, const Array<double>& cb_f);

		void solve_ode(double y_init[], double step_size);

		void interpolate(int m_counter, int i, double delta_hsl);

		void calculate_cb_force(int m_counter, int i, double delta_hsl);

		double dump_rate_constants(int i, int j, int k);
		
		// GSL ode solver functions
		static int func(double t, const double y[], double f[], void *params);
		static int jac(double t, const double y[], double *dfdy, double dfdt[], void *params);

		double return_n_bound(const double * y);

		double return_f_overlap(double x);
	};
};
#endif
