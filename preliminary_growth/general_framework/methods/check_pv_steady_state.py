# @Author: charlesmann
# @Date: 2022-01-24
# @Last modified by:  charlesmann
# @Last modified time: 2022-01-24

import numpy as np

def check_pv_steady_state(v1,p1,v2,p2):
    
    # This function takes in volume and pressure traces for two cardiac cycles, and compares them to see if they are within some tolerance of one another.
    v_tol = np.amax(v1)/150
    p_tol = np.amax(p1)/70
    check_within = np.nan*np.ones(np.shape(v2)[0])
    for i in np.arange(np.shape(v2)[0]):
        v_int = [v1[i]-v_tol,v1[i]+v_tol]
        p_int = [p1[i]-p_tol,p1[i]+p_tol]
        if (v2[i] > v_int[0]) and (v2[i] < v_int[1]):
            if (p2[i] > p_int[0]) and (p2[i] < p_int[1]):
                check_within[i] = True
            else:
                check_within[i] = False
        else:
            check_within[i] = False
    if check_within.all() == True:
        print("Steady-state reached")
        ss = True
    else:
        ss = False
        print("Steady-state not reached")
     # plt.fill_betweenx(p1,v1-v_tol,v1+v_tol,alpha=0.15)
     # plt.fill_between(v1,p1-p_tol,p1+p_tol,alpha=0.15#)
     # plt.plot(v1,p1)
     # plt.plot(v2,p2,'--')
     # plt.plot(v2[check_within==False],p2[check_within==False],'o')
     # plt.show()
    return ss
