# Code runs a simulation of a single ventricle circulation
import numpy as np
import pandas as pd
try:
    import Python_single_ventricle as sc
    import Python_MyoSim.half_sarcomere as myosim
    import untangle as ut
except:
    import sys
    print(sys.path)
    sys.path.append('/home/fenics/shared/Ken_circ')
    import Python_single_ventricle as sc
    import Python_MyoSim.half_sarcomere as myosim

xml_file_string = '..\\test_data\\test_model_mouse.xml'

sc.run_simulation_from_xml_file(xml_file_string)
