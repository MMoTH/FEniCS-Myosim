---
title: "Tissue Mechanics"
parent: Model Formulations
nav_order: 2
---

<div class="notice--info">
  <h4>Message</h4>
  <p>This page is under  construction.</p>
</div>

Consider a representative element of contractile tissue (Insert basic cell with local coordinate system image).
This tissue is modeled as an incompressible, hyperelastic, transversely isotropic material in which the fiber direction f0 is assumed to be stiffer than the s0 and n0 directions. As a hyperelastic material, the PK2 stress   **S** of this material can be obtained by differentiating a strain energy function &Psi; with respect to the Green-Lagrange strain tensor:  

<center><i>Q<sub>1</sub> = bff(Eff<sup>2</sup>) + bfx(Ess<sup>2</sup> + Enn<sup>2</sup> + Ens<sup>2</sup> + Esn<sup>2</sup>) + bxx(Efs<sup>2</sup> + Esf<sup>2</sup> + Efn<sup>2</sup> + Enf<sup>2</sup>)</i></center>  

<center><i>Q<sub>2</sub> = C<sub>3</sub>(&alpha;-1)<sup>2</sup></i> for &alpha; > 1</center>  

<center><i> = 0 </i>otherwise</center>  

<center><i>&Psi;<sub>1</sub> = (<sup>C</sup>&frasl;<sub>2</sub>)(e<sup>Q</sup>-1) - p(J-1)</i></center>  

<center><i>&Psi;<sub>2</sub> = C<sub>2</sub>(e<sup>Q<sub>2</sub></sup>-1)</i></center>  

<center> <b>S</b> = <sup>&part;(&Psi;<sub>1</sub>+&Psi;<sub>2</sub>)</sup>&frasl;<sub>&part;<b>E</b></sub></center>  

Trying a table to align equal signs:  

| | |  
|:---|:----|  
|test1 | test2 |

Cite the humphrey book, Guccione paper, Xi paper?
