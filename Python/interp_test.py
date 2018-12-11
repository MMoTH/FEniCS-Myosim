# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:43:18 2018

@author: ani228
"""

from dolfin import *
import dolfin
import os as os
import numpy as np
from petsc4py import PETSc
from forms import Forms
from nsolver import NSolver as NSolver

def interp(x, xp, fp, left, right):
    
    if x < xp[0]:
    if conditional(x - xp[0] < 0.0, 1, 0):
    #if lt(x,xp[0]):
 
        return left
    
    elif x == xp[-1]:
        
        return fp[-1]
    
    elif x > xp[-1]:
    #elif conditional(x - xp[-1] > 0.0, 1, 0):
        
        return right
        
    else:
        
        for i in range(len(xp)-1):
     
            if x == xp[i]:
            
                return fp[i]
        
            elif x > xp[i] and x < xp[i+1]:
            #elif conditional(x - xp[i] > 0.0, 1, 0) and conditional(x - xp[i+1] < 0.0, 1, 0):
                icopy = i
                
                break
            
        slope = (fp[icopy+1] - fp[icopy])/(xp[icopy+1] - xp[icopy])
        
        y = fp[icopy] + slope * (x-xp[icopy])
        
        return y
    
xp = [1,2,3]
fp = [10,20,30]

print(interp(1.5,xp,fp,0,0))