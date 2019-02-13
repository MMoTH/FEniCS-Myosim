# Sensitivity analysis
import os
try:
    import Python_single_ventricle.analysis.analysis as an
except:
    import sys
    print(sys.path)
    sys.path.append('c:\\ken\\github\\campbellmusclelab\\python\\modules')
    import Python_single_ventricle.analysis.analysis as an


analysis_data = dict()
analysis_data['root_folder'] = os.path.dirname(os.path.abspath(__file__))
analysis_data['base_sim_data_folder'] = '../output/test_2'
analysis_data['data_folder'] = 'data'
analysis_data['data_file_extension'] = 'xlsx'
analysis_data['steady_state_beat_t_span'] = [9, 10]
analysis_data['espvr_t_span'] = [10, 15]
analysis_data['fig_folder'] = 'figures'
analysis_data['fig_extension'] = 'png'
analysis_data['sensitivity_figure_folder'] = 'sensitivity_images'
analysis_data['sensitivity_results_file'] = 'sensitivity_results.xlsx'

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
                     'circulation/aorta/compliance',
                     'circulation/arteries/resistance',
                     'circulation/arteries/compliance',
                     ]

parameter_strings = ['circulation/aorta/compliance',
                     ]

parameter_strings = ['half_sarcomere/membranes/k_leak',
                     'half_sarcomere/membranes/k_act',
                     'half_sarcomere/membranes/k_serca',
                     ]

an.sensitivity_analysis(analysis_data, parameter_strings)

an.create_sensitivity_plot(analysis_data,"")


