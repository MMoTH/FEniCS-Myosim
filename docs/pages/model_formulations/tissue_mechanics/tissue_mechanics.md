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
This tissue is modeled as an incompressible, hyperelastic, transversely isotropic material in which the fiber direction f0 is assumed to be stiffer than the s0 and n0 directions. As a hyperelastic material, the PK2 stress   **S** of this material can be obtained by differentiating the sum of two strain energy functions &Psi;<sub>1</sub>[^1] and &Psi;<sub>2</sub>[^2] with respect to the Green-Lagrange strain tensor:  

<center><i>Q<sub>1</sub> = b<sub>ff</sub>(E<sub>ff</sub><sup>2</sup>) + b<sub>fx</sub>(E<sub>ss</sub><sup>2</sup> + E<sub>nn</sub><sup>2</sup> + E<sub>ns</sub><sup>2</sup> + E<sub>sn</sub><sup>2</sup>) + b<sub>xx</sub>(E<sub>fs</sub><sup>2</sup> + E<sub>sf</sub><sup>2</sup> + E<sub>fn</sub><sup>2</sup> + E<sub>nf</sub><sup>2</sup>)</i></center>  
<center><i>Q<sub>2</sub> = C<sub>3</sub>(&alpha;-1)<sup>2</sup></i> for &alpha; > 1</center><center><i> = 0 </i>otherwise    </center><br/><center><i>&Psi;<sub>1</sub> = (<sup>C</sup>&frasl;<sub>2</sub>)(e<sup>Q<sub>1</sub></sup>-1) - p(J-1)</i></center><br/><center><i>&Psi;<sub>2</sub> = C<sub>2</sub>(e<sup>Q<sub>2</sub></sup>-1)</i></center><br/><center> <b>S</b> = <sup>&part;(&Psi;<sub>1</sub>+&Psi;<sub>2</sub>)</sup>&frasl;<sub>&part;<b>E</b></sub></center><br/>where <i>E<sub>ab</sub></i> represent the components of the Green-Lagrange strain tensor in the local coordinate system, <i>C<sub>i</sub></i> and <i>b<sub>ab</sub></i> represent material parameters, <i>&alpha;</i> is myofiber stretch, <i>p</i> is the lagrange multipler to enforce incompressibility (also the hydrostatic pressure), and <i>J</i> is the Jacobian of the deformation gradient.  

[^1]:Guccione, Julius M, Costa, Kevin D, and McCulloch, Andrew D. "Finite Element Stress Analysis of Left Ventricular Mechanics in the Beating Dog Heart." Journal of Biomechanics 28.10 (1995): 1167-177. Web.  

[^2]:Xi C, Kassab GS, Lee LC. Microstructure-based finite element model of left ventricle passive inflation. Acta Biomater. 2019 May;90:241-253. doi: 10.1016/j.actbio.2019.04.016. Epub 2019 Apr 11. PMID: 30980939; PMCID: PMC6677579.
