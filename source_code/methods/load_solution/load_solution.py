from dolfin import *
import pandas as pd
import numpy as np

def load_solution(load_solution_dir,sim_geometry,sim_protocol,n_array_length):

    f = HDF5File(mpi_comm_world(),load_solution_dir + 'solution.hdf5','r')
    df = pd.read_csv(load_solution_dir+'sol_df.csv')

    df_tonpy = df.to_numpy()


    # Read in and set expressions from csv file
    LVCavityvol = Expression(("vol"), vol=0.0, degree=2)
    u_top = Expression(("u_top"), u_top = 0.0, degree = 0)
    u_front = Expression(("u_front"), u_front = 0.0, degree = 0)
    u_D = Expression(("u_D"), u_D = 0.0, degree = 0)
    # traction boundary condition for end of cell/fiber, could use this to apply
    # a traction to epicardium or something
    Press = Expression(("P"), P=0.0, degree=0)

    LVCavityvol.vol = df.LVCavityvol[0]
    u_top.u_top = df.u_top[0]
    u_front.u_front = df.u_front[0]
    u_D.u_D = df.u_D[0]
    Press.P = df.Press[0]
    #cb_f_array = df.cb_f_array[:]
    #p_f_array = df.p_f_array[:]
    cb_f_array = np.load(load_solution_dir+'cb_f_array.npy')
    p_f_array = np.load(load_solution_dir+'p_f_array.npy')

    expressions = {
        "LVCavityvol":LVCavityvol,
        "u_top":u_top,
        "u_front":u_front,
        "u_D":u_D,
        "Press":Press,
        "cb_force_loaded": cb_f_array,
        "p_force_loaded": p_f_array
        }

    mesh = Mesh()

    f.read(mesh,"/mesh",False)

    VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=2, quad_scheme="default")
    VQuadelem._quad_scheme = 'default'

    # General quadrature element whose points we will evaluate myosim at
    Quadelem = FiniteElement("Quadrature", tetrahedron, degree=2, quad_scheme="default")
    Quadelem._quad_scheme = 'default'

    # Vector element for displacement
    Velem = VectorElement("CG", mesh.ufl_cell(), 2, quad_scheme="default")
    Velem._quad_scheme = 'default'

    # Quadrature element for pressure
    Qelem = FiniteElement("CG", mesh.ufl_cell(), 1, quad_scheme="default")
    Qelem._quad_scheme = 'default'

    # Real element for rigid body motion boundary condition
    Relem = FiniteElement("Real", mesh.ufl_cell(), 0, quad_scheme="default")
    Relem._quad_scheme = 'default'

    VRelem = MixedElement([Relem, Relem, Relem, Relem, Relem])



    fiberFS = FunctionSpace(mesh, VQuadelem)
    f0 = Function(fiberFS)
    s0 = Function(fiberFS)
    n0 = Function(fiberFS)

    f.read(f0,"f0")
    f.read(s0,"s0")
    f.read(n0,"n0")

    facetboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-1)
    edgeboundaries = MeshFunction('size_t', mesh, mesh.topology().dim()-2)
    subdomains = MeshFunction('int', mesh, 3)

    f.read(facetboundaries,"facetboundaries")
    f.read(edgeboundaries,"edgeboundaries")
    f.read(subdomains,"subdomains")

    dg = FunctionSpace(mesh,"DG",1)
    concentric_growth_stimulus = Function(dg)
    eccentric_growth_stimulus = Function(dg)

    f.read(concentric_growth_stimulus,"concentric_growth_stimulus")
    f.read(eccentric_growth_stimulus,"eccentric_growth_stimulus")

    if sim_geometry == "cylinder" or sim_geometry == "unit_cube" or sim_geometry == "box_mesh" or sim_geometry == "gmesh_cylinder":
        if sim_protocol["simulation_type"][0] == "ramp_and_hold_simple_shear":
            print "implementing periodic boundary condition"
            W = FunctionSpace(mesh, MixedElement([Velem,Qelem]),constrained_domain=PeriodicBoundary())
        else:
            #W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem]))
            W = FunctionSpace(mesh, MixedElement([Velem,Qelem]))
        x_dofs = W.sub(0).sub(0).dofmap().dofs() # will use this for x rxn forces later
        print "assigned W"
    else:
        W = FunctionSpace(mesh, MixedElement([Velem,Qelem,Relem,VRelem]))

    w = Function(W)

    f.read(w,"w")
    #f.read(W,"W")

    Quad = FunctionSpace(mesh, Quadelem)
    Quad_vectorized_Fspace = FunctionSpace(mesh, MixedElement(n_array_length*[Quadelem]))


    hsl0 = Function(Quad)

    y_vec = Function(Quad_vectorized_Fspace)

    f.read(hsl0,"hsl")
    f.read(y_vec,"y_vec")

    functions = {
        "mesh": mesh,
        "f0": f0,
        "s0": s0,
        "n0": n0,
        "facetboundaries": facetboundaries,
        "edgeboundaries":edgeboundaries,
        "subdomains":subdomains,
        "concentric_growth_stimulus":concentric_growth_stimulus,
        "eccentric_growth_stimulus":eccentric_growth_stimulus,
        "W":W,
        "w":w,
        "hsl0":hsl0,
        "y_vec":y_vec
    }
    wk_params = {}
    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        # load in more windkessel parameters
        """df_wk = pd.read_csv(load_solution_dir+'sol_df_wk.csv')
        wk_params["V_ven"] = df_wk.V_ven[0]
        wk_params["V_art"] = df_wk.V_art[0]
        wk_params["Part"] = df_wk.Part[0]
        wk_params["Pven"] = df_wk.Pven[0]
        wk_params["PLV"] = df_wk.PLV[0]"""
	fdataPV = np.loadtxt(load_solution_dir+"PV_.txt")
        wk_params["PLV"] = fdataPV[-1,1]
        wk_params["Part"] = fdataPV[-1,2]
        wk_params["Pven"] = fdataPV[-1,3]
        wk_params["V_ven"] = fdataPV[-1,5]
        wk_params["V_art"] = fdataPV[-1,6]






    return expressions, functions, wk_params
