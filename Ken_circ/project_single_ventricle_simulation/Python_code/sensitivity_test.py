# Code runs a simulation of a single ventricle circulation
import os
import numpy as np
import pandas as pd
from xml.etree import ElementTree as et
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

base_xml_file_string = '..\\test_data\\test_model_1_8jan2019.xml'
parameter_strings = ['half_sarcomere/myofilaments/k_1',
                     'half_sarcomere/myofilaments/k_force',
                     'half_sarcomere/myofilaments/k_2',
                     'half_sarcomere/myofilaments/k_3',
                     'half_sarcomere/myofilaments/k_4_0',
                     'half_sarcomere/myofilaments/k_4_1',
                     'half_sarcomere/myofilaments/k_cb',
                     'half_sarcomere/myofilaments/x_ps',
                     'half_sarcomere/myofilaments/k_on',
                     'half_sarcomere/myofilaments/k_off',
                     'half_sarcomere/myofilaments/k_coop',
                     'half_sarcomere/myofilaments/passive_exp_sigma',
                     'half_sarcomere/myofilaments/passive_exp_L',
                     ]

parameter_strings = ['circulation/aorta/resistance',
                     ]
parameter_strings = ['circulation/aorta/compliance',
                     ]
parameter_strings = ['half_sarcomere/membranes/k_leak',
                     'half_sarcomere/membranes/k_act',
                     'half_sarcomere/membranes/k_serca',
                     ]


parameter_multipliers = np.arange(0.5,1.6, 0.1)
base_output_folder = '../output/test_2/'
image_type = 'png'
working_xml_file_string = '..\\working\\model.xml'

#sc.run_simulation_from_xml_file(working_xml_file_string)

def build_xml_string(input_object, current_string, indent):
    
    def indent_string(indent):
        ind_string = ""
        for i in np.arange(0,indent):
            ind_string = ("%s    " % ind_string)
        return ind_string
    
    for child in input_object:
        current_string = ("%s\n%s<%s>" %
                          (current_string, indent_string(indent), child.tag))
        if (len(list(child))>0):
            current_string = build_xml_string(child, current_string, indent+1)
        else:
            current_string = ("%s%s%s" %
                             (current_string, indent_string(0), child.text))
        if (len(list(child))==0):
            current_string = ("%s%s</%s>" %
                              (current_string, indent_string(0), child.tag))
        else:
            current_string = ("%s\n%s</%s>" %
                              (current_string, indent_string(indent), child.tag))
    return current_string

if True:
    
    for i in np.arange(0, len(parameter_strings)):
    
        for j in np.arange(0, len(parameter_multipliers)):
            # Load in the base xml file
            tree = et.parse(base_xml_file_string)
            root = tree.getroot()
            
            # Replace values in file
            parameter_tag = root.findall(parameter_strings[i])
            a = parameter_tag
            parameter_value = np.float(parameter_tag[0].text)
    
            new_value = parameter_value * parameter_multipliers[j]
            parameter_tag[0].text = ("%g" % new_value)
            print("i: %d j: %d v: %g" % (i,j,new_value))
            
            # Create output folders
            parameter_path = parameter_strings[i].replace("/", '_')
            output_data_folder = ("%s/%s/data" %
                                  (base_output_folder, parameter_path))
    
            # Data file
            if not os.path.isdir(output_data_folder):
                os.makedirs(output_data_folder)
    
            tag = root.find('output_parameters/data_file')
            mult_string = ("mult_%.3f" % parameter_multipliers[j])
            mult_string = mult_string.replace(".","pt")
            tag.text = ("%s/data_file_%s.xlsx" %
                        (output_data_folder, mult_string))
            print(tag.text)
    
    
            output_figure_folder = ("%s/%s/figures" %
                                    (base_output_folder, parameter_path))
            if not os.path.isdir(output_figure_folder):
                os.makedirs(output_figure_folder)
    
            tag = root.find('output_parameters/summary_figure')
            tag.text = ("%s/summary_figure_%s.%s" %
                        (output_figure_folder, mult_string, image_type))
    
            tag = root.find('output_parameters/pv_figure')
            tag.text = ("%s/pv_figure_%s.%s" %
                        (output_figure_folder, mult_string, image_type))
    
            tag = root.find('output_parameters/flows_figure')
            tag.text = ("%s/flows_figure_%s.%s" %
                        (output_figure_folder, mult_string, image_type))
    
            tag = root.find('output_parameters/hs_fluxes_figure')
            tag.text = ("%s/hs_fluxes_figure_%s.%s" %
                        (output_figure_folder, mult_string, image_type))
    
            # Create the new model file
            xml_string = build_xml_string(root, "", 0)
            temp_string = "<?xml version=\"1.0\" encoding=\"windows-1252\"?>\n" +\
                            "<single_circulation_simulation>\n"
            temp_string = ("%s\n%s\n</single_circulation_simulation>\n" %
                           (temp_string, xml_string))
            print(temp_string)
            f = open(working_xml_file_string,'w');
            f.write(temp_string)
            f.close()
    
            # Run it
            sc.run_simulation_from_xml_file(working_xml_file_string)
            
#            break
