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
<p style="text-align: center;"><img src="https://github.com/MMoTH/FEniCS-Myosim/blob/master/docs/pages/model_formulations/growth_and_remodeling/theta.jpeg?raw=true" width="87" height="43">
</p>

[^1]: Rodriguez, E. K., Hoger, A., & McCulloch, A. D. (1994). Stress-dependent finite growth in soft elastic tissues. Journal of biomechanics, 27(4), 455–467. https://doi.org/10.1016/0021-9290(94)90021-3
[^2]: Sharifi, H., Mann, C.K., Rockward, A.L. et al. Multiscale simulations of left ventricular growth and remodeling. Biophys Rev (2021). https://doi.org/10.1007/s12551-021-00826-5
