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
    sys.path.append('c:\\ken\\github\\campbellmusclelab\\python\\modules')
    import Python_single_ventricle as sc
    import Python_MyoSim.half_sarcomere as myosim

xml_file_string = '..\\test_data\\test_model2.xml'

#sc.run_simulation_from_xml_file(xml_file_string)
#
from xml.etree import ElementTree as et

tree = et.parse(xml_file_string)
root = tree.getroot()

a = root.findall('simulation_parameters/time_step')
a[0].text = 'ken'



def build_string(input_object, current_string, indent):
    
    def indent_string(indent):
        ind_string = ""
        for i in np.arange(0,indent):
            ind_string = ("%s    " % ind_string)
        return ind_string
    
    for child in input_object:
        current_string = ("%s\n%s<%s>" %
                          (current_string, indent_string(indent), child.tag))
        if (len(list(child))>0):
            current_string = build_string(child, current_string, indent+1)
        else:
            current_string = ("%s\n%s%s" %
                             (current_string, indent_string(indent+1), child.text))
        current_string = ("%s\n%s</%s>" %
                          (current_string, indent_string(indent), child.tag))
    return current_string

#
b = build_string(root,"",0)
print(b)

#print("root")
#print(root)
#print("root.tag")
#print(root.tag)
#for child in root:
#    print(child.tag, child.attrib)
#    for e in child:
#        print(e.tag, e.text)
#
#
#d = ut.parse(xml_file_string)
#print("d")
#print(d)



#sc.run_simulation_from_xml_file(xml_file_string)

#data_file_string = '..\\output\\data\\summary_data.xlsx'
#d = pd.read_excel(data_file_string)
#
#perturbation_time_span = [2,2.9]
#sc.display_pv_loop(d,
#                   output_file_string='..\\output\\figures\\perturbation_pv_loop_figure.png', 
#                   t_limits=perturbation_time_span)
#
#sc.display_simulation(d,
#                      output_file_string='..\\output\\figures\\perturbation_summary_figure.png',
#                      t_limits=perturbation_time_span)
#
#myosim.display_fluxes(d,
#                      output_file_string='..\\output\\figures\\perturbation_hs_fluxes.png',
#                      t_limits=perturbation_time_span)
