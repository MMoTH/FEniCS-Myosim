#ifndef CA_H
#define CA_H

class base_parameters;

class Ca
{
public:
	// constructor
	Ca(base_parameters * set_p_bp);

	//destructor
	~Ca();

	base_parameters * p_bp;

	int Ca_flag;
	int time_point;

	int condition_number = 0;

	double t_act;
	double t_p;
	double cell_time;
	double constant_pCa;
	double pCa;
	double pCa_dia;
	double pCa_amp;
	double beta;
	double tau_1;
	double tau_2;
	double fCa = 23.5;
	double fCa_2 = 2.35;

	double Cal;

	double initial_Ca;

	double current_pCa;
	double current_Pi_concentration;
	double current_ADP_concentration;
	double current_ATP_concentration;

	//double Calcium(int set_Ca_flag, double set_cell_time);
	double Calcium(void);

};
#endif
