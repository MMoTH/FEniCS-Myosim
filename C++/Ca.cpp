#include <iostream>
#include <math.h>

#include "Ca.h"
#include "base_parameters.h"

// constructor
Ca::Ca(base_parameters * set_p_bp) 
{
	p_bp = set_p_bp;

	/*
	if (p_bp->no_of_conditions>0)
	{
		// Initialise if there is data
		current_pCa = gsl_matrix_get(p_bp->pCa_values, 0, condition_number);
		current_Pi_concentration = gsl_matrix_get(p_bp->Pi_concentrations, 0, condition_number);
		current_ADP_concentration = gsl_matrix_get(p_bp->ADP_concentrations, 0, condition_number);
		current_ATP_concentration = gsl_matrix_get(p_bp->ATP_concentrations, 0, condition_number);
	}
	*/
	// Set some defaults
	/*current_pCa = 9.0;
	current_Pi_concentration = 0.0;
	current_ADP_concentration = 0.0;
	current_ATP_concentration = 0.0;*/

	initial_Ca = pow(10, -current_pCa);
	
};

//destructor
Ca::~Ca() {};

//double Ca::Calcium(int set_Ca_flag, double set_cell_time)
double Ca::Calcium(void)
{
	//Ca_flag = set_Ca_flag;
	//cell_time = set_cell_time;

	// constant calcium
	if (Ca_flag == 1)
	{
		pCa = current_pCa; 
		Cal = pow(10.0, -pCa);
	}
	// XZ's modified calcium curve from May 2016. Ca in M
	else if (Ca_flag == 2)
	{
		t_p = t_act + 0.01;

		if (cell_time >= t_p)
			pCa = 0.5*exp(-pow((cell_time - t_p)*fCa, fCa_2));
		else
			pCa = (cell_time - t_act) / 0.02;

		Cal = (0.1 + 1000 * sin(3.14*pCa)) * 1E-9;
	}
	//  Calcium transient for rabbit trabeculae using parameters to fit Ca from Jeremy Rice Paper
	else if (Ca_flag == 3)
	{
		if (cell_time < t_act)
			Cal = pow(10, -pCa_dia);
		else
		{
			double Ca1 = (pow(10, -pCa_amp) - pow(10, -pCa_dia)) / beta;
			double Ca2 = exp(-(cell_time - t_act) / tau_1);
			double Ca3 = exp(-(cell_time - t_act) / tau_2);
			double Ca4 = Ca2 - Ca3;
			Cal = Ca1 * Ca4 + pow(10, -pCa_dia);
		}
	}
	else if (Ca_flag == 4)
	{
		pCa = gsl_matrix_get(p_bp->pCa_values,time_point,condition_number);
		Cal = pow(10.0, -pCa);
		//std::cout << "pCa = " << pCa;
		//std::cout << "\n";
	}
	return Cal;
}


