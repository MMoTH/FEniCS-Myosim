# @Author: charlesmann
# @Date:   2021-12-28T14:42:09-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-28T15:35:02-05:00


from dolfin import *

def create_boundary_conditions(mesh,fcn_spaces,functions):
    W = fcn_spaces["solution_space"]
    facetboundaries = functions["facetboundaries"]
    topid = 4
    LVendoid = 2
    epiid = 1
    bctop = DirichletBC(W.sub(0).sub(2), Expression(("0.0"), degree = 2), facetboundaries, topid)
    bcs = [bctop]
    functions["LVendoid"] = LVendoid

    return bcs, functions
