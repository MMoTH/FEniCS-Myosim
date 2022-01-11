# @Author: charlesmann
# @Date:   2021-06-22T12:00:19-04:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T15:40:57-05:00



from dolfin import *


def assign_initial_hsl(lv_options,hs_params,sim_geometry,hsl0):

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        # assign transmural hsl from mesh file
        lv_options["f"].read(hsl0, lv_options["casename"] + "/" + "hsl0")
    else:
        # assign all half-sarcomeres to initial user-specified value
        hsl0.vector()[:] = hs_params["initial_hs_length"][0]
    return hsl0
