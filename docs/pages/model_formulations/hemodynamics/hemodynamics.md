---
title: "Circulatory Model"
parent: Model Formulations
nav_order: 3
---

<div class="notice--info">
  <h4>Message</h4>
  <p>This page is under  construction.</p>
</div>

Currently, a simple three compartment circulatory model is used for left-ventricular simulations. Given cavity pressure (solved for at the previous time step when solving the weak form), flows between compartments are calculated by the following system of ODEs and used to update compartment volumes. For this model, there are three compartments: the left ventricle, arteries, and veins. Blood flows from the ventricle to the arteries through the aorta, between the arteries and veins through the peripheral vasculatore, and from the veins back to the ventricle through the mitral valve.

Let Q<sub>ao</sub>, Q<sub>mv</sub>, Q<sub>per</sub> denote the flows through the aorta, mitral valve, and peripheral vasculature respectively. Similarly, C<sub>ao</sub>, C<sub>mv</sub>, C<sub>ven</sub> denote compliances,  R<sub>ao</sub>, R<sub>ven</sub>, R<sub>per</sub> denote resistances, P<sub>art</sub>, P<sub>cav</sub>, P<sub>ven</sub> and V<sub>art</sub>, V<sub>ven</sub>, V<sub>cav</sub> volumes with subscripts containing "0" indicating reference volumes. Then

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/hemodynamics/p_art.jpeg?raw=true" width="199" height="46">  
<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/hemodynamics/p_ven.jpeg?raw=true" width="199" height="46">  

<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/hemodynamics/qao.jpeg?raw=true" width="199" height="46">  
<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/hemodynamics/qmv.jpeg?raw=true" width="199" height="46">  
<img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/hemodynamics/qper.jpeg?raw=true" width="199" height="46">  


This cavity volume is then constrained to this value during the solving of the weak form. This is done by introducing a Lagrange multiplier that ends up taking on the value of the cavity pressure.
