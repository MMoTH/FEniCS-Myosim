# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:42:01 2018

@author: ani228
"""
xp = [1,2,3]
fp = [10,20,30]

print(interp(1,xp,fp,-10,10))

def interp(x, xp, fp, left, right):
    
    if x < xp[0]:
 
        return left
    
    elif x == xp[-1]:
        
        return fp[-1]
    
    elif x > xp[-1]:
        
        return right
        
    else:
        
        for i in range(len(xp)-1):
     
            if x == xp[i]:
            
                return fp[i]
        
            elif x > xp[i] and x < xp[i+1]:
        
                icopy = i
                
                break
            
        slope = (fp[icopy+1] - fp[icopy])/(xp[icopy+1] - xp[icopy])
        
        y = fp[icopy] + slope * (x-xp[icopy])
        
        return y

