#include<iostream>
#include <string.h>

#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv.h>
#include <gsl/gsl_spline.h>
#include <gsl/gsl_roots.h>
#include <gsl/gsl_rng.h>

#include "hs.h"
#include "mf.h"
#include "Ca.h"
#include "base_parameters.h"
#include "global_definitions.h"

// constructor
mf::mf(dolfin::hs * set_p_hs, Ca * set_p_Ca, base_parameters * set_p_bp)
{
	p_hs = set_p_hs;
	p_Ca = set_p_Ca;
	p_bp = set_p_bp;
};

//destructor
mf::~mf() {};

double mf::generic_rate(int rate_index, double x, int m_isoform)
{
	cb_force = p_hs->p_FE->cb_force;
	passive_force = p_hs->p_FE->passive_force;
	total_force = cb_force + passive_force;

	// Returns a rate value

	// Variables
	int i, j;

	int old_state;
	int new_state;

	double rate = 0;
	double attachment_width;

	double amp1;

	double x_mid;

	double old_extension;
	double new_extension;

	double old_energy;
	double new_energy;
	int reverse_rate_index;
	double reverse_rate;

	double ligand_modulator;

	double * fp;

	double temp;
	double temp_double;

	double cond_rate_mod;
	int cond_rate_copy;

	double cond_fd_rate_mod;
	int cond_fd_rate_copy;
	double cond_fd_rate_factor;

	// Code

	// Create space for the function_parameters
	fp = new double[p_bp->no_of_function_parameters + 1];

	// Allocate the values
	for (i = 1; i <= p_bp->no_of_function_parameters; i++)
	{
		fp[i] = gsl_matrix_get(p_bp->function_parameters[m_isoform], rate_index - 1, i - 1);
	}

	// Adjust for Ca_function_modifications
	if (p_bp->base_Ca_concentration>0.0)
	{
		for (i = 1; i <= p_bp->no_of_function_parameters; i++)
		{
			fp[i] = fp[i] * GSL_MAX(0.0,
				1.0 +
				(gsl_matrix_get(p_bp->Ca_function_modifications, rate_index - 1, i - 1) *
				(p_Ca->initial_Ca - p_bp->base_Ca_concentration) / p_bp->base_Ca_concentration));
		}
	}

	// Adjust for conditions
	for (i = 1; i <= p_bp->no_of_function_parameters; i++)
	{
		cond_rate_copy = (int)(floor(0.5 + gsl_matrix_get(p_bp->cond_rate_copy[condition_number], rate_index - 1, i - 1)));

		if (cond_rate_copy == 0)
		{
			// There's no copy to worry about
			// Just set the cond_rate_mode to the matrix value
			temp_double = gsl_matrix_get(p_bp->cond_rate_mod[condition_number], rate_index - 1, i - 1);
		}
		else
		{
			//printf("cond_rate_copy %i\n",cond_rate_copy);
			// Use the scaling factor for the specified rate
			temp_double = gsl_matrix_get(p_bp->cond_rate_mod[cond_rate_copy - 1], rate_index - 1, i - 1);
		}

		if (temp_double>0.0)
		{
			fp[i] = fp[i] * temp_double;
		}
	}

	// Adjust for current hsl
	for (i = 1; i <= p_bp->no_of_function_parameters; i++)
	{
		temp_double = 1.0 + gsl_matrix_get(p_bp->ld_rate, rate_index - 1, i - 1) *
			((p_hs->hsl - p_bp->initial_hs_length) / p_bp->initial_hs_length);

		if (temp_double<0.0)
			temp_double = 0.0;


		fp[i] = fp[i] * temp_double;
	}

	// Adjust for current force
	for (i = 1; i <= p_bp->no_of_function_parameters; i++)
	{
		// Try to set the cond_fd_rate_factor
		cond_fd_rate_copy = (int)(floor(0.5 + gsl_matrix_get(p_bp->cond_fd_rate_copy[condition_number], rate_index - 1, i - 1)));

		if (cond_fd_rate_copy != 0)
		{
			printf("Ken was here\n");
			exit(1);
		}

		if (cond_fd_rate_copy == 0)
		{
			// There's no copy to worry about
			cond_fd_rate_factor = gsl_matrix_get(p_bp->cond_fd_rate_mod[condition_number], rate_index - 1, i - 1);
		}
		else
		{
			cond_fd_rate_factor = gsl_matrix_get(p_bp->cond_fd_rate_mod[cond_fd_rate_copy - 1], rate_index - 1, i - 1);
		}

		/*
		if ((rate_index==1)&&(i==1))
		printf("force %g  cond_fd_rate_factor :%g\n",actual_forces.total_force,cond_fd_rate_factor);
		*/

		if (gsl_matrix_get(p_bp->fd_rate, rate_index - 1, 12) >= 0.0)
		{
			temp_double = 1.0 + cond_fd_rate_factor * gsl_matrix_get(p_bp->fd_rate, rate_index - 1, i - 1) *
				total_force;
		}
		else
		{
			if (gsl_matrix_get(p_bp->fd_rate, rate_index - 1, 12) == -1.0)
				temp_double = 1.0 + cond_fd_rate_factor * gsl_matrix_get(p_bp->fd_rate, rate_index - 1, i - 1) *
				cb_force;
			else
			{
				temp_double = 1.0 + cond_fd_rate_factor * gsl_matrix_get(p_bp->fd_rate, rate_index - 1, i - 1) *
					passive_force;
				//printf("Here\n");
			}
		}

		if ((gsl_matrix_get(p_bp->fd_coefs, rate_index - 1, 0)>0) || (gsl_matrix_get(p_bp->fd_coefs, rate_index - 1, 0)<0))
		{
			temp_double = 1.0 +
				gsl_matrix_get(p_bp->fd_coefs, rate_index - 1, 0)*
				(1 - exp(-gsl_matrix_get(p_bp->fd_coefs, rate_index - 1, 1)*total_force));
		}

		if (temp_double<0.0)
			temp_double = 0.0;
		/*
		if ((rate_index==1)&&(i==1))
		{
		printf("hs %i force: %g temp_double: %g\n",
		hs_number,
		actual_forces.total_force,
		temp_double);
		}
		*/


		fp[i] = fp[i] * temp_double;
	}

	// Adjust for br_slopes
	for (i = 1; i <= p_bp->no_of_function_parameters; i++)
	{
		fp[i] = fp[i] * GSL_MAX(0.0, return_br_factor(rate_index - 1, i - 1));
	}

	// First scan the scheme to deduce the relevant information
	for (i = 0; i<p_bp->no_of_states; i++)
	{
		for (j = 0; j<MAX_PATHWAYS; j++)
		{
			if (p_bp->state_rate_functions[i][j] == rate_index)
			{
				old_state = i + 1;
				new_state = p_bp->state_transitions[i][j];
			}
		}
	}

	old_extension = gsl_matrix_get(p_bp->cb_extensions, old_state - 1, m_isoform);
	new_extension = gsl_matrix_get(p_bp->cb_extensions, new_state - 1, m_isoform);

	// Set the rates
	//if (strcmp(p_bp->function_type[rate_index - 1], "gaussian") == 0)
	//if (rate_index == 3)
	if (p_bp->function_type[rate_index - 1] == 'g')
	{
		amp1 = fp[1];

		if (x >= 0)
		{
			rate = amp1 * exp((-0.5 * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
				* pow(x + old_extension, 2.0)) /
				(1e18 * K_BOLTZMANN * p_bp->temperature));
		}
		else
		{
			if (fp[4] >= 0)
			{
				rate = amp1 * exp((-0.5 * gsl_vector_get(p_bp->k_cb_neg, m_isoform)
					* pow(x + old_extension, 2.0)) /
					(1e18 * K_BOLTZMANN * p_bp->temperature));
			}
			else
			{
				rate = amp1 * exp((-0.5 * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
					* pow(x + old_extension, 2.0)) /
					(1e18 * K_BOLTZMANN * p_bp->temperature));
			}

			if (fp[5]>0)
			{
				rate = amp1 * exp((-0.5 * fp[5] * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
					* pow(x + old_extension, 2.0)) /
					(1e18 * K_BOLTZMANN * p_bp->temperature));
			}
		}

		// Special cases
		if (fp[3] != 0)
		{
			rate = amp1 * exp((-0.5 * fp[3] * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
				* pow(x + old_extension, 2.0)) /
				(1e18 * K_BOLTZMANN * p_bp->temperature));
		}

		// Special case
		if (fp[6] != 0)
		{
			rate = amp1 * exp((-0.5 * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
				* pow(x + old_extension + fp[6], 2.0)) /
				(1e18 * K_BOLTZMANN * p_bp->temperature));
		}

		if ((fp[3] != 0.0) && (fp[6] != 0.0))
		{
			rate = amp1 * exp((-0.5 * fp[3] * gsl_vector_get(p_bp->k_cb_pos, m_isoform)
				* pow(x + old_extension + fp[6], 2.0)) /
				(1e18 * K_BOLTZMANN * p_bp->temperature));
		}
	}

	//if (strcmp(p_bp->function_type[rate_index - 1], "constant") == 0)
	if (p_bp->function_type[rate_index - 1] == 'c')
	{
		rate = fp[1];
	}

	//if (strcmp(p_bp->function_type[rate_index - 1], "huxley") == 0)
	if (p_bp->function_type[rate_index - 1] == 'h')
	{
		attachment_width = fp[2];

		if (x>0)
		{
			// Limited range
			if (x <= fp[2])
			{
				rate = fp[1] * x;
			}
			else
			{
				// biphasic
				if (x <= fp[2])
				{
					rate = fp[1] * x;
				}
				else
				{
					rate = fp[5];
				}
			}
		}
		else
		{
			rate = fp[3] + fabs(fp[6] * x);
		}

		if (fp[7]>0)
		{
			rate = fp[3] * (1.0 / (1.0 + exp(fp[7] * x)));
			rate = rate + fp[1] * x*
				(-1.0 + (1.0 / (1.0 + exp(fp[7] * (x - fp[2])))) +
				(1.0 / (1.0 + exp(-fp[7] * x))));
		}
	}

	//if (strcmp(p_bp->function_type[rate_index - 1], "square") == 0)
	/*if (p_bp->function_type[rate_index - 1] == 's')
	{
		if (fp[13]<0)
			x_mid = -old_extension;
		else
			x_mid = 0;

		if (x>x_mid)
		{
			if (fp[4] <= 0)
			{
				// Limited range
				if ((x - x_mid)<fp[2])
				{
					rate = fp[1];
				}
				else
				{
					rate = 0.0;
				}
			}
			else
			{
				// biphasic
				if ((x - x_mid) <= fp[2])
				{
					rate = fp[1];
				}
				else
				{
					rate = fp[5];
				}
			}
		}
		else
		{
			rate = fp[3];
		}
	}*/

	//if (strcmp(p_bp->function_type[rate_index - 1], "exponential") == 0)
	if (p_bp->function_type[rate_index - 1] == 'e')
	{
		if (fp[13]>0)
			x_mid = fp[5];
		else
			x_mid = -old_extension;

		x = x - x_mid;

		rate = fp[1];

		if (x>fp[4])
		{
			rate = rate + exp(fp[2] * (x - fp[4])) - 1.0;
		}
		else
		{
			if (fp[12]<0)
				fp[3] = fp[2];

			if (x<-fp[4])
				rate = rate + exp(fp[3] * fabs(x + fp[4])) - 1.0;
		}
	}

//if (strcmp(p_bp->function_type[rate_index - 1], "poly") == 0)
//if (rate_index == 4)
	if (p_bp->function_type[rate_index - 1] == 'p')
	{
		if (fp[13] >= 0)
			x_mid = -old_extension;
		else
			//x_mid = 0.0 + fp[14];
			x_mid = 0.0;

		x = x - x_mid;

		rate = fp[1];

		if (x > fp[2])
			rate = rate + fp[3] * fabs(pow(x - fp[2], fp[4]));
		else
		{
			if (fp[12]<0.0)
			{
				fp[8] = fp[2];
				fp[9] = fp[3];
				fp[10] = fp[4];
			}

			if (x< -fp[8])
			{
				if (fp[11]>0)
				{
					if (fp[11]>1)
						rate = fp[11];
					else
						rate = rate + fp[3] * pow(x - fp[2], fp[4]);
				}
				else
					rate = rate + fp[9] * (pow(fabs(x + fp[8]), fp[10]));
			}
		}
	}

	/*if (strcmp(p_bp->function_type[rate_index - 1], "poly_ligand") == 0)
	{
		x_mid = -old_extension;
		x = x - x_mid;

		// Base line
		rate = fp[1] / fp[6];

		if (x > fp[2])
			rate = rate + fp[3] / fp[7] * pow(x - fp[2], fp[4]);
		else
		{
			rate = rate + fp[9] / fp[13] * pow(fabs(x + fp[8]), fp[10]);
		}
	}*/

	//if (strcmp(p_bp->function_type[rate_index - 1], "wall") == 0)
	if (p_bp->function_type[rate_index - 1] == 'w')
	{
		x_mid = -old_extension;

		// Base line
		rate = fp[1];

		if ((x - x_mid)>fp[2])
		{
			if (fp[3]>0)
				rate = fp[3];
			else
				rate = VERY_HIGH_RATE;
		}

		if ((x - x_mid)<-fp[4])
		{
			if (fp[5]>0)
				rate = fp[5];
			else
				rate = VERY_HIGH_RATE;
		}
	}

	//if (strcmp(p_bp->function_type[rate_index - 1], "bilog") == 0)
	if (p_bp->function_type[rate_index - 1] == 'b')
	{
		if (fp[13] <= 0)
			x_mid = old_extension;
		else
			if (fp[13]>1.0)
				x_mid = old_extension / 2.0;
			else
				x_mid = 0.0;

		double slope = fp[6];

		if (fp[12]<0)
		{
			fp[4] = fp[2];
			fp[5] = fp[3];
		}

		if (x >= -x_mid)
		{
			rate = fp[1] + fp[2] / (1 + exp(-slope * (x + (x_mid - fp[3]))));
		}
		else
		{
			if (fabs(fp[7])>0)
			{
				rate = fp[1] + fp[4] / (1 + exp(fp[7] * (x + (x_mid + fp[5]))));
			}
			else
				rate = fp[1] + fp[4] / (1 + exp(slope*(x + (x_mid + fp[5]))));
		}
	}

	//if (strcmp(p_bp->function_type[rate_index - 1], "sigmoid") == 0)
	if (p_bp->function_type[rate_index - 1] == 's')
	{
		if (fp[4] <= 0)
			x_mid = (old_extension + new_extension) / 2.0;
		else
			x_mid = 0;

		rate = fp[3] + (fp[1] / (1.0 + exp(fp[2] * (x + x_mid + fp[5]))));
	}


	/*if (strcmp(p_bp->function_type[rate_index - 1], "wall_ligand") == 0)
	{
		x_mid = -old_extension;

		// Base line
		rate = fp[1] / fp[6];

		if ((x - x_mid)>fp[2])
			rate = VERY_HIGH_RATE / fp[6];

		if ((x - x_mid)<-fp[3])
			rate = VERY_HIGH_RATE / fp[6];
	}*/

	/*if (strcmp(p_bp->function_type[rate_index - 1], "energy") == 0)
	{
		old_energy = return_cb_energy(old_state - 1, x, m_isoform);
		new_energy = return_cb_energy(new_state - 1, x, m_isoform);

		reverse_rate_index = (int)fp[1];

		reverse_rate = generic_rate(reverse_rate_index, x, m_isoform);

		rate = reverse_rate * exp((old_energy - new_energy) / p_bp->beta);
	}*/

	// Modulate the rate by the ligand
	ligand_modulator = (double)1.0;

	/*if (!strcmp(p_bp->function_ligand[rate_index - 1], "ATP"))
	{
		ligand_modulator = p_Ca->current_ATP_concentration;
	}
	if (!strcmp(p_bp->function_ligand[rate_index - 1], "ADP"))
	{
		ligand_modulator = p_Ca->current_ADP_concentration;
	}
	if (!strcmp(p_bp->function_ligand[rate_index - 1], "Pi"))
	{
		ligand_modulator = p_Ca->current_Pi_concentration;
	}*/

	rate = rate * ligand_modulator;

	// Limit rates
	if (rate>VERY_HIGH_RATE)
		rate = VERY_HIGH_RATE;

	if (rate<0.0)
		rate = 0.0;

	// Tidy up
	delete[] fp;

	// Return
	return rate;
}

double mf::return_br_factor(int i, int j)
{
	double temp;

	temp = 1.0 + gsl_matrix_get(p_bp->br_slope, i, j) *
		(gsl_vector_get(p_bp->initial_dml, condition_number) /
			p_bp->initial_hs_length);

	if (temp<0.0)
		temp = 0.0;

	return temp;
}

double mf::return_cb_energy(int cb_state, double x, int m_isoform)
{
	// Returns the energy of a cb

	// Variables
	double k_link;
	double energy;

	if (p_bp->state_attached[cb_state] == 0)
	{
		// state is detached
		energy = gsl_matrix_get(p_bp->cb_base_energies, cb_state, m_isoform) * p_bp->beta;
	}
	else
	{
		// state is attached
		if (x > -gsl_matrix_get(p_bp->cb_extensions, cb_state, m_isoform))
		{
			k_link = gsl_vector_get(p_bp->k_cb_pos, m_isoform);
		}
		else
		{
			k_link = gsl_vector_get(p_bp->k_cb_neg, m_isoform);
		}

		energy = (gsl_matrix_get(p_bp->cb_base_energies, cb_state, m_isoform) * p_bp->beta) +
			(0.5* k_link * pow((x + gsl_matrix_get(p_bp->cb_extensions, cb_state, m_isoform)), 2.0));
	}

	return energy;
}
