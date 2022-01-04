# @Author: charlesmann
# @Date:   2021-12-29T13:32:08-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-29T13:46:20-05:00



from dolfin import *

def calculate_stimulus_function(fcn_spaces,functions,forms):

    # Sff is the passive component from the myofiber SEF
    # total_passive_PK2 is contributions from guccione SEF, Xi SEF, and incompressibility
    # in the global coordinate system. Note, f0 is stored in the global coordinate system as well,
    # so having this tensor act on f0 is consistent
    total_passive_PK2, Sff = forms.stress(functions["hsl"])

    ed_passive_along_f0 = inner(functions["f0"],total_passive_PK2*functions["f0"])

    # project onto stimulus function space?

    temp_stimulus = project(ed_passive_along_f0,fcn_spaces["stimulusFS"],form_compiler_parameters={"representation":"uflacs"})

    return temp_stimulus
