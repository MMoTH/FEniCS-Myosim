#ifndef MF_H                           
#define MF_H

namespace dolfin
{
	class hs;
}
//class hs;
class Ca;
class base_parameters;


class mf
{
public:

	//constructor
	mf(dolfin::hs * set_p_hs, Ca * set_p_Ca, base_parameters * set_p_bp);

	//destructor
	~mf();

	int condition_number = 0;

	double cb_force;
	double passive_force;
	double total_force;

	dolfin::hs * p_hs;
	Ca * p_Ca;
	base_parameters * p_bp;

	double generic_rate(int rate_index, double x, int m_isoform);

	double return_br_factor(int i, int j);

	double return_cb_energy(int cb_state, double x, int m_isoform);

};


#endif