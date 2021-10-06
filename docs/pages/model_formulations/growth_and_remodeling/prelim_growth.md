---
title: Preliminary Growth
parent: Model Formulations
nav_order: 3
has_children: false
---
Following the volumetric growth theory introduced by Rodriguez et al.[^1], the deformation gradient is multiplicatively split such that  
<p style="text-align: center;"><img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/growth_and_remodeling/decomp.jpeg?raw=true" width="74" height="21">
</p>
For a more thorough review see [here](https://rdcu.be/cv6Wj)[^2]. The growth deformation gradient takes the form
<p style="text-align: center;"><img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/growth_and_remodeling/fg.jpeg?raw=true" width="150" height="68">
</p>  
where each &theta; dictates growth in either the fiber direction (eccentric growth) or the sheet and sheet normal directions (concentric growth).
<p style="text-align: center;"><img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/growth_and_remodeling/theta.jpeg?raw=true" width="87" height="43">
</p>
where s is a function taking on some stimulus value (varies with position) and s<sub>0</sub> is the stimulus value reached after a steady state simulation. <underline>F</underline><sub>g</sub> is updated and the weak form solved in the absence of any active stress or external load, and <underline>F</underline><sub>e</sub> restores compatibility. The reference mesh is updated such that the nodes take on the positions obtained by applying the displacement solved for, thus relieving residual stresses.

[^1]: Rodriguez, E. K., Hoger, A., & McCulloch, A. D. (1994). Stress-dependent finite growth in soft elastic tissues. Journal of biomechanics, 27(4), 455–467. https://doi.org/10.1016/0021-9290(94)90021-3
[^2]: Sharifi, H., Mann, C.K., Rockward, A.L. et al. Multiscale simulations of left ventricular growth and remodeling. Biophys Rev (2021). https://doi.org/10.1007/s12551-021-00826-5
