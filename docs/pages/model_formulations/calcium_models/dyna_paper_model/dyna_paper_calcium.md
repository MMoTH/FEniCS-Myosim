---
title: Dyna Paper Calcium Transient
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 2
---
Dyna Paper Calcium Transient
----------------------------
The following adapted[^1] equation gives the calcium transient used in the paper "Force-Dependent Recruitment From Myosin OFF-State Increases End-Systolic
Pressure-Volume Relationship in Left Ventricle"[^2].

if t <= self.t_act:
          pCa = 7
          calcium_value = 10**(-1*pCa)
elif ((cardiac_period*cycle+self.t_act) < t) and (t < (t_p)):
          pCa = (t - (cardiac_period*cycle+self.t_act))/0.02
          calcium_value = (1 + 9*np.sin(3.14*pCa))1E-7
elif (t >= t_p):
          pCa = 0.5*np.exp(-np.power((t - t_p)fCa, fCa_2))
          calcium_value = (1+9*np.sin(3.14*pCa))1E-7

This yields the following:

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/calcium_models/dyna_paper_model/dyna_ca.png?raw=true" width="800" height="500">

[^1]: Laurita, K. R., & Singal, A. (2001). Mapping action potentials and calcium transients simultaneously from the intact heart. Am J Physiol Heart Circ Physiol, 280(5), H2053-2060. doi:10.1152/ajpheart.2001.280.5.H2053
[^2]: Mann, C. K., Lee, L. C., Campbell, K. S., & Wenk, J. F. (2020). Force-dependent recruitment from myosin OFF-state increases end-systolic pressure-volume relationship in left ventricle. Biomechanics and modeling in mechanobiology, 19(6), 2683–2692. https://doi.org/10.1007/s10237-020-01331-6
