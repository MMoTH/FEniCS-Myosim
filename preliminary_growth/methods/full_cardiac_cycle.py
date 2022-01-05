# @Author: charlesmann
# @Date:   2022-01-05T12:39:33-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-05T13:51:34-05:00
from dolfin import *
from methods import diastolic_filling
from methods import circulatory_system


def full_cycle():

    # initialize circulatory system

    # diastolic loading to a prescribed EDV (keeping it the same as the last
    # cycle from previous simulation, or the initial prescribed. Assumption is
    # the total blood volume is constant)

    # cycle through time

    #    update wk compartments, return end_diastole or end_systole

    #    update active stress

    #    solve weak form

    #    update necessary quantities
    
    #    if end_diastole or end_systole:
    #        calculate stimulus value

    return functions
