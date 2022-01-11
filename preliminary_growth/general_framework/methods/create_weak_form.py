# @Author: charlesmann
# @Date:   2021-12-28T14:47:31-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T17:06:38-05:00

from dolfin import *
import sys
sys.path.append("/home/fenics/shared/dependencies/")
from forms import Forms

def create_weak_form(mesh,fcn_spaces,functions,arrays_and_values):

    m,k = indices(2)


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
    # temporary active stress
    #Pactive, cbforce = uflforms.TempActiveStress(0.0)

    functions["hsl_old"].vector()[:] = functions["hsl0"].vector()[:]
    functions["hsl_diff_from_reference"] = (functions["hsl_old"] - functions["hsl0"])/functions["hsl0"]
    functions["pseudo_alpha"] = functions["pseudo_old"]*(1.-(arrays_and_values["k_myo_damp"]*(functions["hsl_diff_from_reference"])))
    alpha_f = sqrt(dot(f0, Cmat*f0)) # actual stretch based on deformation gradient
    functions["hsl"] = functions["pseudo_alpha"]*alpha_f*functions["hsl0"]
    functions["delta_hsl"] = functions["hsl"] - functions["hsl_old"]

    cb_force = Constant(0.0)

    y_vec_split = split(functions["y_vec"])

    for jj in range(arrays_and_values["no_of_states"]):
        f_holder = Constant(0.0)
        temp_holder = 0.0

        if arrays_and_values["state_attached"][jj] == 1:
            cb_ext = arrays_and_values["cb_extensions"][jj]

            for kk in range(arrays_and_values["no_of_x_bins"]):
                dxx = arrays_and_values["xx"][kk] + functions["delta_hsl"] * arrays_and_values["filament_compliance_factor"]
                n_pop = y_vec_split[arrays_and_values["n_vector_indices"][jj][0] + kk]
                temp_holder = n_pop * arrays_and_values["k_cb_multiplier"][jj] * (dxx + cb_ext) * conditional(gt(dxx + cb_ext,0.0), arrays_and_values["k_cb_pos"], arrays_and_values["k_cb_neg"])
                f_holder = f_holder + temp_holder

            f_holder = f_holder * dolfin_functions["cb_number_density"][-1] * 1e-9
            f_holder = f_holder * arrays_and_values["alpha_value"]

        cb_force = cb_force + f_holder

    Pactive = cb_force * as_tensor(functions["f0"][m]*functions["f0"][k], (m,k))+ arrays_and_values["xfiber_fraction"]*cb_force * as_tensor(functions["s0"][m]*functions["s0"][k], (m,k))+ arrays_and_values["xfiber_fraction"]*cb_force * as_tensor(functions["n0"][m]*functions["n0"][k], (m,k))

    functions["cb_force"] = cb_force
    arrays_and_values["cb_f_array"] = project(functions["cb_force"], fcn_spaces["quadrature_space"]).vector().get_local()[:]
    arrays_and_values["hsl_array"] = project(functions["hsl"], fcn_spaces["quadrature_space"]).vector().get_local()[:]

    # calculate myofiber passive stress along f0, set negatives to zero (no compressive stress born by fibers)
    total_passive_PK2, functions["Sff"] = uflforms.stress(functions["hsl"])
    temp_DG = project(functions["Sff"], FunctionSpace(mesh, "DG", 1), form_compiler_parameters={"representation":"uflacs"})
    p_f = interpolate(temp_DG, fcn_spaces["quadrature_space"])
    arrays_and_values["p_f_array"] = p_f.vector().get_local()[:]

    functions["Pactive"] = Pactive
    #functions["cbforce"] = cbforce
    F2 = inner(Fmat*Pactive, grad(v))*dx


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

    Ftotal = F1 + F2 + F3 + F4

    Ftotal_growth = F1 + F3_p + F4

    Jac1 = derivative(F1, w, dw)
    Jac2 = derivative(F2, w, dw)
    Jac3 = derivative(F3, w, dw)
    Jac3_p = derivative(F3_p,w,dw)
    Jac4 = derivative(F4, w, dw)

    Jac = Jac1 + Jac2 + Jac3 + Jac4
    Jac_growth = Jac1 + Jac3_p + Jac4

    return Ftotal, Jac, Ftotal_growth, Jac_growth, uflforms, functions, Pactive, arrays_and_values
