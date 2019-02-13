# include <iostream>

#include <dolfin/common/Array.h>

#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv2.h>
#include <gsl/gsl_spline.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_rng.h>

#include "hs.h"
#include "mf.h"
#include "Ca.h"
#include "base_parameters.h"

struct func_params
{
	dolfin::hs * p_hs;
	mf * p_mf;
	Ca * p_Ca;
	base_parameters * p_bp;
};

//constructor
dolfin::hs::hs()
{
	// create instances of classes and FE structure
	// read every time i_t_s or G_c_f_v called in FEniCS
	p_FE = new FE;
	p_bp = new base_parameters("/home/fenics/shared/test_12/instruction_file_FEniCS.txt", "/home/fenics/shared/test_12/");
	p_Ca = new Ca(p_bp);
	p_mf = new mf(this, p_Ca, p_bp);

	//FE_params.add("input_path", "place_holder");
	//p_FE->input_path = FE_params["input_path"];
	
	//FE_params.add("output_path", "place_holder");
	//p_FE->output_path = FE_params["output_path"];
	
	//p_bp = new base_parameters("/home/fenics/shared/instruction_files/instruction_file_FEniCS.txt", "/home/fenics/shared/output_directory/");
	//p_bp = new base_parameters(p_FE->input_path, p_FE->output_path);
	

	FE_params.add("step_size", 0.0);
	Ca_params.add("Ca_flag", 4);
	Ca_params.add("t_act", 0.0);
	Ca_params.add("constant_pCa", 0.0);
	Ca_params.add("time_point", 0);
	Ca_params.add("cell_time", 0.0);

	x_bin_min = p_bp->x_bin_min;
	x_bin_max = p_bp->x_bin_max;
	x_bin_increment = p_bp->x_bin_increment;

	no_of_x_bins = (int)(((x_bin_max - x_bin_min) / x_bin_increment) + 1);
	
	
	// Now create a gsl_vector to hold the bin positions
	x = gsl_vector_alloc(no_of_x_bins);
	// Copy them from the base_parameters
	gsl_vector_memcpy(x, p_bp->x_bins);

	// Work out how many array elements we have
	n_array_length = (p_bp->no_of_attached_states*no_of_x_bins) +
		p_bp->no_of_detached_states + 1;
	// +1 allows for number of binding sites

	/*std::cout << x_bin_min << "\n";
	std::cout << x_bin_max << "\n";
	std::cout << x_bin_increment << "\n";
	std::cout << no_of_x_bins << "\n";
	std::cout << n_array_length << "\n";

	for (int i = 0; i < no_of_x_bins; i++)
		std::cout << gsl_vector_get(x, i) << "\n";*/
}

//destructor
dolfin::hs::~hs()
{
	gsl_vector_free(x);
	
	delete p_FE;
	delete p_bp;
	delete p_Ca;
	delete p_mf;
};

std::vector<double> dolfin::hs::Get_cb_force_vec()
{

	return cb_force_vec;

};
double dolfin::hs::Get_Ca()
{

	return p_Ca->Calcium();

};

std::vector<double> dolfin::hs::apply_time_step(const Array<double>& z, const Array<double>& delta_hsl, const Array<double>& hslen, const Array<double>& p_f, const Array<double>& cb_f)
{
	int i, j, m_counter;
	double temp;

	p_FE->step_size = FE_params["step_size"];
	
	p_Ca->Ca_flag = Ca_params["Ca_flag"];
	p_Ca->t_act = Ca_params["t_act"];
	p_Ca->constant_pCa = Ca_params["constant_pCa"];
	p_Ca->time_point = Ca_params["time_point"];
	p_Ca->cell_time = Ca_params["cell_time"];

	//p_mf = new mf(this, p_Ca, p_bp);

	step_size = p_FE->step_size/1000.0;
		
	y_vec.clear();
	cb_force_vec.clear();

	no_of_int_points = hslen.size();
	
	double y_init[n_array_length];

	for (m_counter = 0; m_counter < p_bp->m_no_of_isoforms; m_counter++)
	{
		m_isoform = m_counter;
		for (i = 0; i < no_of_int_points; i++) // loop over all int_points/sarcomeres
		{
			// assign element-specific parameters 
			hsl = hslen[i];
			p_FE->cb_force = cb_f[i];
			p_FE->passive_force = p_f[i] * beta_value;

			for (j = 0; j < n_array_length; j++)
				y_init[j] = z[m_counter * no_of_int_points * n_array_length + i * n_array_length + j]; // vectorization of 3rd order tensor of isoforms, elements and populations
				//std::cout << y_init[j] << "\n";

			solve_ode(y_init, step_size);
			
			interpolate(m_counter, i, delta_hsl[i]);

			// Ken's Correction block
			//-----------------
			temp = 0.0;
			for (j = 0; j < (n_array_length - 1); j++)
				temp = temp + y_vec[m_counter * no_of_int_points * n_array_length + i * n_array_length + j];
			temp = temp - 1.0;
			y_vec.at(m_counter * no_of_int_points * n_array_length + i * n_array_length) = 
				y_vec[m_counter * no_of_int_points * n_array_length + i * n_array_length] - temp;
			//-----------------

			calculate_cb_force(m_counter, i, delta_hsl[i]);
		}
	}
	//std::cout << "total_force = " << p_mf->total_force;
	//std::cout << "\n";
	return y_vec;
}

void dolfin::hs::solve_ode(double y_init[], double step_size)
{
	struct func_params params = { this, p_mf, p_Ca, p_bp };

	int j;

	double t = 0.0;
	double t1 = step_size;
	double h = step_size;

	double * y = new double[n_array_length];

	// Initialise the populations
	for (j = 0; j < n_array_length; j++)
	{
		y[j] = y_init[j];
		//std::cout << y[j] << "\n";
	}

	const gsl_odeiv_step_type * T = gsl_odeiv_step_rk2;

	gsl_odeiv_step * s = gsl_odeiv_step_alloc(T, n_array_length);
	gsl_odeiv_control * c = gsl_odeiv_control_y_new(POPULATION_ABS_TOLERANCE, POPULATION_REL_TOLERANCE);
	gsl_odeiv_evolve * e = gsl_odeiv_evolve_alloc(n_array_length);
	gsl_odeiv_system sys = { func,jac, n_array_length, &params };

	while (t<t1)
	{
		int status = gsl_odeiv_evolve_apply(e, c, s, &sys, &t, t1, &h, y);
		if (status != GSL_SUCCESS)
		{
			exit(1);
			break;
		}
	}

	// Update
	for (j = 0; j < n_array_length; j++)
	{
		if (y[j] < 0.0)
			y[j] = (double)0.0;
		//std::cout << y[j] << "\n";
		// update all indices of y_vec now; attached state populations will be overwritten after cb shifted
		y_vec.push_back(y[j]);
	}

	// Tidy up
	delete[] y;

	gsl_odeiv_evolve_free(e);
	gsl_odeiv_control_free(c);
	gsl_odeiv_step_free(s);
	
}

void dolfin::hs::interpolate(int m_counter, int i, double delta_hsl)
{
	// This function moves the cb distributions by delta_hsl
	// Populations are shifted by compliance_factor * delta_hsl

	// Cubic spline method is copied from GSL Manual Chapter 26

	// Short-cut if there is no movement 
	if (delta_hsl == (double)0.0)
	{
		//std::cout << "delta_hsl = 0.0" << "\n";
		return;
	}

	// Variables

	int j, k;

	double x_eval;
	double new_y;

	double shift = (p_bp->filament_compliance_factor) * delta_hsl;

	double * xx = new double[no_of_x_bins];
	double * yy = new double[no_of_x_bins];

	gsl_interp_accel * acc;
	gsl_spline * spline;

	// Code

	// Assign the x values
	for (j = 0; j < no_of_x_bins; j++)
		xx[j] = gsl_vector_get(x, j);

	// Cycle through populations
	for (j = 0; j < p_bp->no_of_states; j++)
	{
		if (p_bp->state_attached[j] == 1)
		{
			// We need to move populations
			for (k = 0; k < no_of_x_bins; k++)
				yy[k] = y_vec[m_counter * no_of_int_points * n_array_length + i * n_array_length + p_bp->n_vector_indices[j][0] + k];

			acc = gsl_interp_accel_alloc();
			spline = gsl_spline_alloc(gsl_interp_cspline, no_of_x_bins);
			gsl_spline_init(spline, xx, yy, no_of_x_bins);

			// Assign the new values
			for (k = 0; k < no_of_x_bins; k++)
			{
				x_eval = gsl_vector_get(x, k) - shift;

				if ((x_eval >= gsl_vector_get(x, 0)) &&
					(x_eval <= gsl_vector_get(x, no_of_x_bins - 1)))
				{
					// x_eval is in range
					new_y = gsl_spline_eval(spline, x_eval, acc);
				}
				else
				{
					// Extrapolating beyond range
					new_y = (double)0.0;
				}


				// Prevent negative populations
				if (new_y < 0.0)
					new_y = (double)0.0;

				// attached state populations are overwritten here
				y_vec.at(m_counter * no_of_int_points * n_array_length + i * n_array_length + p_bp->n_vector_indices[j][0] + k) = new_y;
			}
		}
	}

	// Tidy up
	delete[] xx;
	delete[] yy;

	gsl_spline_free(spline);
	gsl_interp_accel_free(acc);
}

void dolfin::hs::calculate_cb_force(int m_counter, int i, double delta_hsl)
{
	int j, k;

	double dx;
	double cb_ext;

	double f_holder;
	double n_holder;

	double n_pop;

	double cb_adjustment = delta_hsl * p_bp->filament_compliance_factor;

	double cb_force = 0;

	// Cycle through the states
	for (j = 0; j < p_bp->no_of_states; j++)
	{
		f_holder = 0.0;
		n_holder = 0.0;
		
		if (p_bp->state_attached[j] == 1)
		{
			cb_ext = gsl_matrix_get(p_bp->cb_extensions, j, m_counter);
			// last was here 
			for (k = 0; k < no_of_x_bins; k++)
			{
				dx = gsl_vector_get(x, k) + cb_adjustment;
				n_pop = y_vec[m_counter * no_of_int_points * n_array_length + i * n_array_length + p_bp->n_vector_indices[j][0] + k];

				if (dx > -cb_ext)
				{
					f_holder = f_holder +
						(n_pop * gsl_vector_get(p_bp->k_cb_multiplier, j) *
							gsl_vector_get(p_bp->k_cb_pos, m_counter) * (dx + cb_ext));
				}
				else
				{
					f_holder = f_holder +
						(n_pop * gsl_vector_get(p_bp->k_cb_multiplier, j) *
							gsl_vector_get(p_bp->k_cb_neg, m_counter) * (dx + cb_ext));
				}
			}

			// Correct for number density,nm units and alpha value
			f_holder = f_holder * p_bp->cb_number_density * 1e-9;

			// Adjust for variability
			f_holder = f_holder * alpha_value;
		}
		// Add in the cb force
		cb_force = cb_force + f_holder;
	}
	//std::cout << "cb_forces:  \n";
	//std::cout << cb_force << "\n";
	cb_force_vec.push_back(cb_force); // length of cb_force_vec: m_no_of_isoform * no_of_int_points
}

int dolfin::hs::func(double t, const double y[], double f[], void *params)
{
	// Returns the derivitives
	// cb_populations are passed in as a vector
	// The code knows about the parent hs object through a pointer
	// that is passed in through params

	// Variables
	int i, j, k;
	int n_array_length;

	int other_state;
	int rate_index;

	int bin_index;

	double n_available;
	double n_bound;
	double n_overlap;

	double rate_constant;

	double k_on_factor;
	double k_off_factor;
	double k_coop_factor;

	// Temps
	int i_temp;
	double d_temp;


	struct func_params *p = (struct func_params *) params; // define pointer p to params

	hs * p_hs = p->p_hs;
	mf * p_mf = p->p_mf;
	Ca * p_Ca = p->p_Ca;
	base_parameters * p_bp = p->p_bp;

	int m_isoform = p_hs->m_isoform;

	n_array_length = p_hs->n_array_length;

	// Set n_available and n_bound
	n_available = y[n_array_length - 1];
	n_bound = p_hs->return_n_bound(y);

	// Zero derivitives
	for (i = 0; i<n_array_length; i++)
		f[i] = 0.0;

	// Now cycle through the states
	for (i = 0; i<p_bp->no_of_states; i++)
	{
		if (p_bp->state_attached[i] == 0)
		{
			// We are in a detached state
			for (j = 0; j<MAX_PATHWAYS; j++)
			{
				other_state = p_bp->state_transitions[i][j];

				if (other_state != 0)
				{
					// We have a transition, find the rate and deduce what to do
					rate_index = p_bp->state_rate_functions[i][j];

					if (p_bp->function_action[rate_index - 1] == 'a')
					{
						// Cross-bridges will increment into multiple elements and decrement from a single element
						i_temp = p_bp->n_vector_indices[i][0];

						// Cycle through the bins
						bin_index = 0;

						for (k = p_bp->n_vector_indices[other_state - 1][0];
							k <= p_bp->n_vector_indices[other_state - 1][1]; k++)
						{
							// Adjust the rate constant for the bin_width
							rate_constant = p_bp->x_bin_increment *
								p_mf->generic_rate(rate_index,
									gsl_vector_get(p_hs->x, bin_index), m_isoform);

							// Calculate the adjustment
							d_temp = rate_constant * (n_available - n_bound) * y[i_temp];

							// These are the increments
							f[k] = f[k] + d_temp;

							// These are the decrements
							f[i_temp] = f[i_temp] - d_temp;

							// Increment
							bin_index++;
						}
					}

					if (p_bp->function_action[rate_index - 1] == 'n')
					{
						// Cross-bridges will increment one element and decrement from a single element
						rate_constant = p_mf->generic_rate(rate_index, 0, m_isoform);

						// Calculate the adjustment
						i_temp = p_bp->n_vector_indices[i][0];
						d_temp = rate_constant * y[i_temp];

						// Increment
						k = p_bp->n_vector_indices[other_state - 1][0];
						f[k] = f[k] + d_temp;

						// Decrement
						f[i_temp] = f[i_temp] - d_temp;
					}
				}
			}
		}
		else
		{
			// We are in an attached state
			for (j = 0; j<MAX_PATHWAYS; j++)
			{
				other_state = p_bp->state_transitions[i][j];

				if (other_state != 0)
				{
					// We have a transition, find the rate and deduce what to do
					rate_index = p_bp->state_rate_functions[i][j];

					if (p_bp->function_action[rate_index - 1] == 'd')
					{
						// Cross-bridges will increment into a single element and
						// decrement from multiple elements

						i_temp = p_bp->n_vector_indices[other_state - 1][0];

						// Cycle through the bins
						bin_index = 0;

						for (k = p_bp->n_vector_indices[i][0];
							k <= p_bp->n_vector_indices[i][1]; k++)
						{
							// Deduce the rate constant
							rate_constant = p_mf->generic_rate(rate_index,
								gsl_vector_get(p_hs->x, bin_index), m_isoform);

							// Calculate the adjustment
							d_temp = rate_constant * y[k];

							// These are the increments
							f[i_temp] = f[i_temp] + d_temp;

							// These are the decrements
							f[k] = f[k] - d_temp;

							// Increment
							bin_index++;
						}
					}

					if (p_bp->function_action[rate_index - 1] == 'n')
					{
						// Cross-bridges will increment and decrement from multiple places

						// Cycle through bins
						bin_index = 0;

						for (k = p_bp->n_vector_indices[i][0];
							k <= p_bp->n_vector_indices[i][1]; k++)
						{
							rate_constant = p_mf->generic_rate(rate_index,
								gsl_vector_get(p_hs->x, bin_index), m_isoform);

							// Calculate the adjustment
							d_temp = rate_constant * y[k];

							// These are the increments
							i_temp = p_bp->n_vector_indices[other_state - 1][0] + bin_index;
							f[i_temp] = f[i_temp] + d_temp;

							// These are the decrements
							f[k] = f[k] - d_temp;

							// Increment counter
							bin_index++;
						}
					}
				}
			}
		}
	}

	// Update n_available
	i_temp = p_hs->n_array_length - 1;
	//p_hs->check_int(i_temp);

	n_overlap = p_hs->return_f_overlap(p_hs->hsl);
	int coop_power = (int)(p_bp->coop_power);

	// Set k_on_factor, determined by 0th element of p_bp->thin_function_mod
	int cond_number = 0;
	int copy_number = (int)gsl_matrix_get(p_bp->thin_function_copy, cond_number, 0);

	if (copy_number>0)
	{
		k_on_factor = gsl_matrix_get(p_bp->thin_function_mod, copy_number - 1, 0);
	}
	else
	{
		k_on_factor = gsl_matrix_get(p_bp->thin_function_mod, cond_number, 0);
	}

	// k_off_factor, determined by 1st element of p_bp->thin_function_mod
	copy_number = (int)gsl_matrix_get(p_bp->thin_function_copy, cond_number, 1);

	if (copy_number>0)
	{
		k_off_factor = gsl_matrix_get(p_bp->thin_function_mod, copy_number - 1, 1);
	}
	else
	{
		k_off_factor = gsl_matrix_get(p_bp->thin_function_mod, cond_number, 1);
	}

	// k_coop_factor, determined by 2nd element of p_bp->thin_function_mod
	copy_number = (int)gsl_matrix_get(p_bp->thin_function_copy, cond_number, 2);

	if (copy_number>0)
	{
		k_coop_factor = gsl_matrix_get(p_bp->thin_function_mod, copy_number - 1, 2);
	}
	else
	{
		k_coop_factor = gsl_matrix_get(p_bp->thin_function_mod, cond_number, 2);
	}

	
	f[i_temp] = k_on_factor * p_bp->a_on_rate * p_Ca->Calcium()*
		(n_overlap - n_available) * (1.0 + (k_coop_factor * p_bp->k_coop) * gsl_pow_int(n_available / n_overlap, coop_power)) -
		k_off_factor * p_bp->a_off_rate * (n_available - n_bound) *
		(1.0 + (k_coop_factor * p_bp->k_coop)*gsl_pow_int((n_overlap - n_available) / n_overlap, coop_power));

	return GSL_SUCCESS;
}

int dolfin::hs::jac(double t, const double y[], double *dfdy, double dfdt[], void *params)
{
	return GSL_SUCCESS;
}

double dolfin::hs::return_n_bound(const double * y)
{
	// Given a vector, returns n_bound, the number of sites that are bound

	// Variables
	int i, j, k;
	double n_bound = 0;

	// Code
	for (i = 0; i < p_bp->m_no_of_isoforms; i++)
	{
		for (j = 0; j < p_bp->no_of_states; j++)
		{
			if (p_bp->state_attached[j])
			{
				for (k = p_bp->n_vector_indices[j][0];
					k <= p_bp->n_vector_indices[j][1]; k++)
				{
					n_bound = n_bound + y[k];
				}
			}
		}
	}

	return n_bound;
}

double dolfin::hs::return_f_overlap(double x)
	{
		// Code returns f_overlap, the proportion of cross-bridges that can bind
		// at half-sarcomere length s

		// Variables
		double x_overlap;
		double x_no_overlap;
		double max_x_overlap;
		double f_overlap;

		// Code
		x_no_overlap = x - p_bp->hs_thick_filament_length;
		x_overlap = p_bp->hs_thin_filament_length - x_no_overlap;
		max_x_overlap = p_bp->hs_thick_filament_length - p_bp->hs_bare_zone_length;

		if (x_overlap < 0.0)
			f_overlap = 0.0;

		if ((x_overlap > 0.0) && (x_overlap <= max_x_overlap))
			f_overlap = x_overlap / max_x_overlap;

		if (x_overlap > max_x_overlap)
			f_overlap = 1.0;

		if (x < p_bp->hs_thin_filament_length)
		{
			f_overlap = 1.0 + (p_bp->hs_k_falloff*(x - p_bp->hs_thin_filament_length));
			if (f_overlap < 0.0)
				f_overlap = 0.0;
		}

		return f_overlap;
	}

double dolfin::hs::dump_rate_constants(int i, int j, int k)
{
	// Code dumps rate constants

	if (j == 0)
		return gsl_vector_get(x, i);
	else
		return p_mf->generic_rate(j, gsl_vector_get(x, i), k);
}

void dolfin::hs::display_bps(void)
{
	p_bp->display_bps();
}