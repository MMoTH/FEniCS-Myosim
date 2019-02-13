# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:16:38 2019

@author: kscamp3
"""

import pandas as pd

try:
    import Python_single_ventricle as sc
except:
    import sys
    print(sys.path)
    sys.path.append('c:\\ken\\github\\campbellmusclelab\\python\\modules')
    import Python_single_ventricle as sc
    

fs = 'C:\\ken\\GitHub\\CampbellMuscleLab\\Projects\\Single_ventricle_simulation\\output\\test_2\\half_sarcomere_myofilaments_k_1\\data\\data_file_mult_1pt000.xlsx'

ds = pd.read_excel(fs,'Data')

sc.display_simulation(ds,
                      t_limits =[0, 10],
                      output_file_string = 'temp.png',
                      dpi=200)