#include <dolfin/common/Array.h>
#include <math.h>
#include <iostream>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_odeiv2.h>
#include "ArtsODE.h"
#include <iostream>


using namespace dolfin;

// Constructor to initialize parameter to their default values
ODEsolver::ODEsolver()
{      //amir: "::" used to define class members outside of the class
	// amir: params is instance of FeniCS' Parameters class
	params.add("Ea", 20.0);
	params.add("v0", 7.5e-3);
	params.add("a6", 2.0);
	params.add("a7", 1.5);
	params.add("Tref", 180.0e3);
	params.add("tr", 75.0);
	params.add("td", 75.0);
	params.add("b", 150.0);
	params.add("ld", -0.4);
	
};

// Destructor
ODEsolver::~ODEsolver() {};


// Getting stress                                  //amir: defining a member function (Get_fiso) of class ODEsolver 
std::vector<double> ODEsolver::Get_fiso() {

	return fiso_vec;

};

// Stepping through the ODE  with initial condition x from time t to next time at t + dt        
std::vector<double> ODEsolver::ODEsolverstep(const Array<double>& x, double dt, double t, const Array<double>& saclen)
{

	// Define parameters for GSL ODE solver, which has to be a struct
	gsl_parameters gsl_params;

	double ee = params["Ea"];
	// here contains of params (FEniCS) assigned to gsl_params structure
	gsl_params.Ea = params["Ea"];
	gsl_params.v0 = params["v0"];
	gsl_params.a6 = params["a6"];
	gsl_params.a7 = params["a7"];
	gsl_params.Tref = params["Tref"];
	gsl_params.tr = params["tr"];
	gsl_params.td = params["td"];
	gsl_params.b = params["b"];
	gsl_params.ld = params["ld"];
	gsl_params.saclen0 = 1.85;

	//FILE *fp;
	//fp = fopen("/home/lclee/Research/test_gsl/test.txt", "w+");
	//fp = fopen("/home/likchuan/Research/test_gsl/test.txt", "w+");

	fiso_vec.clear();
	y2.clear();

	int i;
	for (i = 0; i < x.size(); ++i)       // x is lc, same size as fiso (field variable) or total number of gauss points
	{

		gsl_params.saclen = saclen[i];

		sys = { func, jac, 1, &gsl_params };

		gsl_odeiv2_driver * d = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, 1e-6, 1e-6, 0.0);

		//std::cout << i << std::endl;
		//std::cout << y2.size() << std::endl;
		//std::cout << x.size() << std::endl;
		double y[1] = { x[i] };
		double tt = t;
		double ti = tt + dt;
		int status = gsl_odeiv2_driver_apply(d, &tt, ti, y);

		if (status != GSL_SUCCESS) {
			printf("error, return value=%d\n", status);
		};

		//printf ("%.5e %.5e\n", t, y[0]);

		double fiso_ = fiso(y, &gsl_params);
		double Tref = gsl_params.Tref;
		//double ftwitch_ = ftwitch(t, y,  &gsl_params);
		//double sigma = saclen[i]/gsl_params.saclen0*fiso_*ftwitch_*(saclen[i] - y[0])*gsl_params.Ea;

		//std::cout << fiso_ << " " << y[0] << " " << ftwitch_ << std::endl;

			//fprintf (fp, "%.5e %.5e %.5e %.5e %.5e\n", t, y[0], sigma, fiso_, ftwitch_);
		y2.push_back(y[0]);
		//stress.push_back(sigma);
		fiso_vec.push_back(Tref*fiso_);
		//stress.push_back(Tref*ftwitch_);

		gsl_odeiv2_driver_free(d);

	};
	//fclose(fp);


	//std::cout << y2.size() << std::endl;
	return y2;

};

// func defines f(y,t) in the ODE system dy/dt = f(y,t)
int ODEsolver::func(double t, const double y[], double f[], void *gsl_params)
{
	(void)(t); /* avoid unused parameter warning */
	struct gsl_parameters *gsl_param_ptr = (struct gsl_parameters *) gsl_params;
	double Ea = gsl_param_ptr->Ea;
	double v0 = gsl_param_ptr->v0;
	double saclen = gsl_param_ptr->saclen;


	f[0] = (Ea*(saclen - y[0]) - 1.0)*v0;
	return GSL_SUCCESS;
};

// func defines jacobian df(y,t)/dy in the ODE system dy/dt = f(y,t)
int ODEsolver::jac(double t, const double y[], double *dfdy, double dfdt[], void *gsl_params)
{
	(void)(t); /* avoid unused parameter warning */
	struct gsl_parameters * gsl_param_ptr = (struct gsl_parameters *)gsl_params;
	double Ea = gsl_param_ptr->Ea;
	double v0 = gsl_param_ptr->v0;

	gsl_matrix_view dfdy_mat = gsl_matrix_view_array(dfdy, 1, 1);
	gsl_matrix * m = &dfdy_mat.matrix;

	gsl_matrix_set(m, 0, 0, -Ea * v0);
	dfdt[0] = 0.0;
	return GSL_SUCCESS;
};


// fiso function in the Arts Model
double ODEsolver::fiso(const double y[], void *gsl_params)
{

	struct gsl_parameters * gsl_param_ptr = (struct gsl_parameters *)gsl_params;
	double a6 = gsl_param_ptr->a6;
	double a7 = gsl_param_ptr->a7;


	if (y[0] > a7) {
		return tanh(a6*(y[0] - a7))*tanh(a6*(y[0] - a7));
	}
	else {
		return 0;
	};

};

// ftwitch function in the Arts Model
double ODEsolver::ftwitch(double t, const double y[], void *gsl_params)
{

	struct gsl_parameters * gsl_param_ptr = (struct gsl_parameters *)gsl_params;
	double tr = gsl_param_ptr->tr;
	double td = gsl_param_ptr->td;
	double b = gsl_param_ptr->b;
	double saclen = gsl_param_ptr->saclen;
	double ld = gsl_param_ptr->ld;

	double tmax = b * (saclen - ld);

	double sigmoid_0 = 1.0 / (1.0 + exp(-1.0*t));
	double sigmoid_1 = 1.0 / (1.0 + exp(-1.0*(tmax - t)));


	return tanh((tmax - t) / td)*tanh((tmax - t) / td)*tanh(t / tr)*tanh(t / tr)*sigmoid_0*sigmoid_1;

	//if(t < 0.0){
	//      return 0;
	// }
	// else if(t > 0.0 && t < tmax){
	//      return tanh((tmax - t)/td)*tanh((tmax - t)/td)*tanh(t/tr)*tanh(t/tr);
	// }
	// else{
	//      return 0;
	// };

};