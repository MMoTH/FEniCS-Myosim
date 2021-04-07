from dolfin import *


def assign_initial_hsl(lv_options,hs_params,sim_geometry,hsl0):

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        # assign transmural hsl from mesh file
        lv_options["f"].read(hsl0, lv_options["casename"] + "/" + "hsl0")
    else:
        # assign all half-sarcomeres to initial user-specified value
        hsl0.vector()[:] = hs_params["initial_hs_length"][0]
    return hsl0
