# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:55:42 2019

@author: ani228
"""
from scipy.integrate import solve_ivp
#from scipy.integrate import RK45

def exponential_decay(t, y): return -0.5 * y

sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
#sol = RK45(exponential_decay, [0, 10], [2, 4, 8])

print(sol.t)