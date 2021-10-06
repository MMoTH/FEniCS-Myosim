---
title: "Circulatory Model"
parent: Model Formulations
nav_order: 3
---

<div class="notice--info">
  <h4>Message</h4>
  <p>This page is under  construction.</p>
</div>

Currently, a simple three compartment circulatory model is used for left-ventricular simulations. Given cavity pressure (solved for at the previous time step when solving the weak form), flows between compartments are calculated by the following system of ODEs and used to update compartment volumes.

Let Q<sub>ao</sub>, Q<sub>mv</sub>, Q<sub>per</sub> denote the flows through the aorta, mitral valve, and peripheral vasculature respectively. Similarly, C<sub>ao</sub>, C<sub>mv</sub>, C<sub>per</sub> denote compliances,  R<sub>ao</sub>, R<sub>mv</sub>, R<sub>per</sub> denote resistances, P<sub>ao</sub>, P<sub>mv</sub>, P<sub>per</sub> and V<sub>ao</sub>, V<sub>mv</sub>, V<sub>per</sub> volumes. Then

self.Part = 1.0/self.Cao*(self.V_art - self.Vart0);
self.Pven = 1.0/self.Cven*(self.V_ven - self.Vven0);
self.PLV = p_cav;

self.Qao = 1.0/self.Rao*(self.PLV - self.Part);
self.Qmv = 1.0/self.Rven*(self.Pven - self.PLV);
self.Qper = 1.0/self.Rper*(self.Part - self.Pven);

This cavity volume is then constrained to this value during the solving of the weak form. This is done by introducing a Lagrange multiplier that ends up taking on the value of the cavity pressure.
