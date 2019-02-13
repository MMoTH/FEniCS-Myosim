# Code for displaying single circulation model
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def display_fluxes(data_structure, output_file_string="", t_limits=[], \
                   kinetic_scheme='3state_with_SRX'):
    no_of_rows = 3
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([6, 4.5])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    # Check for t_limits, prune data if necessary
    if t_limits:
        t = data_structure['time']
        vi = np.nonzero((t>=t_limits[0])&(t<=t_limits[1]))
        data_structure = data_structure.iloc[vi]

    if (kinetic_scheme=='3state_with_SRX'):
        
        ax1 = f.add_subplot()
        ax1 = f.add_subplot(spec2[0, 0])
        ax1.plot('time', 'J1', data=data_structure, label='J1')
        ax1.plot('time', 'J2', data=data_structure, label='J2')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Flux')
        ax1.legend(bbox_to_anchor=(1.05, 1))

        ax2 = f.add_subplot()
        ax2 = f.add_subplot(spec2[1, 0])
        ax2.plot('time', 'J3', data=data_structure, label='J3')
        ax2.plot('time', 'J4', data=data_structure, label='J4')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Flux')
        ax2.legend(bbox_to_anchor=(1.05, 1))

        ax3 = f.add_subplot()
        ax3 = f.add_subplot(spec2[2, 0])
        ax3.plot('time', 'Jon', data=data_structure, label='Jon')
        ax3.plot('time', 'Joff', data=data_structure, label='Joff')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Flux')
        ax3.legend(bbox_to_anchor=(1.05, 1))

    if (output_file_string):
        f.savefig(output_file_string)
        plt.close('all')
