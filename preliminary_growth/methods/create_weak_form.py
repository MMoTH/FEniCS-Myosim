# @Author: charlesmann
# @Date:   2021-12-28T14:47:31-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-04T11:34:18-05:00

from dolfin import *
import sys
sys.path.append("/home/fenics/shared/dependencies/")
from forms import Forms

def create_weak_form(mesh,fcn_spaces,functions):


    # Need to set up the strain energy functions and cavity volume info
    # from the forms file:

    # Load in all of our relevant functions and function spaces
    facetboundaries = functions["facetboundaries"]
    subdomains = MeshFunction('int', mesh, 3)
    X = SpatialCoordinate (mesh)
    N = FacetNormal (mesh)
    W = fcn_spaces["solution_space"]
    w = functions["w"]
    u = functions["u"]
    v = functions["v"]
    p = functions["p"]
    f0 = functions["f0"]
    s0 = functions["s0"]
    n0 = functions["n0"]
    c11 = functions["c11"]
    wtest = functions["wtest"]
    dw = functions["dw"]

    # Don't really need this yet
    hsl0 = 950

    Fg = functions["Fg"]
    M1ij = functions["M1ij"]
    M2ij = functions["M2ij"]
    M3ij = functions["M3ij"]
    TF = fcn_spaces["growth_tensor_space"]
    dolfin_functions = functions["dolfin_functions"]
    pendo = functions["pendo"]
    LVendoid = functions["LVendoid"]
    print "LVendoid"
    print LVendoid

    isincomp = True

    # Define some parameters
    params= {"mesh": mesh,
             "facetboundaries": facetboundaries,
             "facet_normal": N,
             "mixedfunctionspace": W,
             "mixedfunction": w,
             "displacement_variable": u,
             "pressure_variable": p,
             "fiber": f0,
             "sheet": s0,
             "sheet-normal": n0,
             "incompressible": isincomp,
             "hsl0": hsl0,
             "Kappa":Constant(1e5),
             "growth_tensor": Fg,
             "M1": M1ij,
             "M2": M2ij,
             "M3": M3ij,
             "TF": TF}

    # update with the passive parameter functions
    params.update(dolfin_functions["passive_params"])

    # Need to tack on some other stuff, including an expression to keep track of
    # and manipulate the cavity volume
    LVCavityvol = Expression(("vol"), vol=0.0, degree=2)
    Press = Expression(("P"),P=0.0,degree=0)
    functions["LVCavityvol"] = LVCavityvol
    functions["Press"] = Press
    ventricle_params  = {
        "lv_volconst_variable": pendo,
        "lv_constrained_vol":LVCavityvol,
        "LVendoid": LVendoid,
        "LVendo_comp": 2,
    }
    params.update(ventricle_params)

    uflforms = Forms(params)
    print "uflforms mesh"
    print uflforms.parameters["mesh"]

    # Now that the forms file is initialized, initialize specific forms

    #-------------------------------
    # This is needed for the forms file, but not for what we are doing yet
    # I don't want to change the base functionality of anything, so I'm defining
    # this here
    # (there exists the capability to have hsl return to its reference length in
    # an attempt to incorporate some visoelasticity)
    d = u.ufl_domain().geometric_dimension()
    I = Identity(d)
    Fmat = I + grad(u)
    J = det(Fmat)
    Cmat = Fmat.T*Fmat
    alpha_f = sqrt(dot(f0, Cmat*f0))
    hsl = alpha_f*hsl0
    functions["hsl"] = hsl
    n = J*inv(Fmat.T)*N
    #----------------------------------

    # Passive stress contribution
    Wp = uflforms.PassiveMatSEF(hsl)

    # passive material contribution
    F1 = derivative(Wp, w, wtest)*dx

    # active stress contribution (Pactive is PK2, transform to PK1)
    #F2 = inner(Fmat*Pactive, grad(v))*dx
    # Going to make Pactive from a simple expression later when testing concentric growth

    # LV volume increase
    Wvol = uflforms.LVV0constrainedE()
    F3 = derivative(Wvol, w, wtest)

    # For pressure on endo instead of volume bdry condition
    F3_p = Press*inner(n,v)*ds(LVendoid)


    # constrain rigid body motion
    L4 = inner(as_vector([c11[0], c11[1], 0.0]), u)*dx + \
	 inner(as_vector([0.0, 0.0, c11[2]]), cross(X, u))*dx + \
	 inner(as_vector([c11[3], 0.0, 0.0]), cross(X, u))*dx + \
	 inner(as_vector([0.0, c11[4], 0.0]), cross(X, u))*dx

    F4 = derivative(L4, w, wtest)

    Ftotal = F1 + F3 + F4

    Ftotal_growth = F1 + F3_p + F4

    Jac1 = derivative(F1, w, dw)
    #Jac2 = derivative(F2, w, dw)
    Jac3 = derivative(F3, w, dw)
    Jac3_p = derivative(F3_p,w,dw)
    Jac4 = derivative(F4, w, dw)

    Jac = Jac1 + Jac3 + Jac4
    Jac_growth = Jac1 + Jac3_p + Jac4

    return Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions
