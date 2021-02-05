---
title: Two Compartment Calcium Model
parent: Calcium Models
grand_parent: Model Formulations
nav_order: 1
---
Two Compartment Calcium
-----------------------
Testing typing equations:
h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x
dy[0] = (self.k_leak + self.activation[l] * self.k_act) * y[1] - \
                self.k_serca * y[0]
        dy[1] = -dy[0]

Let y be a vector of length 2 such that y[0] represents intracellular calcium that binds to the thin filament, and y[1] represents sarcoplasmic reticulum calcium. Then the rate of change of calcium between these two compartments can be described by the following system of ODEs:
dy[0]&fracdt = (k<sub>leak</sub> + activation*k<sub>act</sub>) * y[1] - k<sub>serca</sub> * y[0]
dy[1]&fracdt = -dy[0]
