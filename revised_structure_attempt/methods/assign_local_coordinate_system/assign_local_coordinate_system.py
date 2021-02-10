from dolfin import *
from numpy import random as r
import numpy as np

def assign_local_coordinate_system(lv_options,coord_params,sim_params):

    # initialization
    marker_space = coord_params["marker_space"]
    fiberFS      = coord_params["fiberFS"]
    sim_geometry = coord_params["sim_geometry"]
    geo_options  = coord_params["geo_options"]
    no_of_int_points = coord_params["no_of_int_points"]
    geo_options = coord_params["geo_options"]

    mesh = coord_params["mesh"]
    Quad = coord_params["Quad"]
    f0   = coord_params["f0"]
    s0   = coord_params["s0"]
    n0   = coord_params["n0"]
    facetboundaries = coord_params["facetboundaries"]
    edgeboundaries = coord_params["edgeboundaries"]
    # mean values for gaussian for fiber orientation
    #m_x = 0.342020143325669
    #m_y = 0.939692620785908
    m_x = 1.0
    m_y = 0.
    m_z = 0.0
    width = sim_params["fiber_randomness"][0]

    # Functions that are useful in unit cube and cylinder for calculating
    # fibrous area, or the long (x) axis to assign local coordinate systems
    test_marker_fcn = Function(marker_space)
    z_axis       = Function(fiberFS)

    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        casename = lv_options["casename"]
        f        = lv_options["f"]
        # assign local coordinate system at each gauss point
        f.read(facetboundaries, casename+"/"+"facetboundaries")
        f.read(edgeboundaries, casename+"/"+"edgeboundaries")
        f.read(f0, casename + "/" + "eF")
        f.read(s0, casename + "/" + "eS")
        f.read(n0, casename + "/" + "eN")
        f.close()

    elif (sim_geometry == "cylinder") or (sim_geometry == "box_mesh")or sim_geometry == "gmesh_cylinder":

        if sim_geometry == "cylinder":
            radius = geo_options["base_radius"][0]
        if sim_geometry == "gmesh_cylinder":
            radius = 1.0
        else:
            radius = 0.5
        # Create a simple expression to test if x_coord is > 9.0 or < 1.0
        # making last 10% of cylinder spring elements
        end_marker = Expression("x[0]",degree=1)
        point_radius = Expression("sqrt(pow(x[1],2)+pow(x[2],2))",degree=1)

        # Project the expression onto the mesh
        end_marker_values = project(end_marker,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
        point_rad_values = project(point_radius,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})

        # Interpolate onto the FunctionSpace for quadrature points
        end_marker_on_mesh = interpolate(end_marker_values,Quad)
        point_rad = interpolate(point_rad_values,Quad)

        # Create array of the expression values
        end_marker_array = end_marker_on_mesh.vector().get_local()
        point_rad_array = point_rad.vector().get_local()

        # Updating geometry options to save end_marker_array to assign heterogeneous parameters later
        geo_options["end_marker_array"] = end_marker_array

        for jj in np.arange(no_of_int_points):

            #if (temp_tester_array[jj] < dig_array[jj]) or (temp_tester_array[jj] > -dig_array[jj] + 10.0):
            if (end_marker_array[jj] > 9.0) or (end_marker_array[jj] < 1.0):
                # inside left end
                f0.vector()[jj*3] = 1.0
                f0.vector()[jj*3+1] = 0.0
                f0.vector()[jj*3+2] = 0.0

            else:
                # In middle region, assign fiber vector
                # find radius of point
                temp_radius = point_rad_array[jj]
                if np.abs(temp_radius - radius) < 0.01:
                    temp_width = 0.0
                else:
                    temp_width = np.abs(width*(1.0-(temp_radius*temp_radius/(radius*radius))))
                f0.vector()[jj*3] = r.normal(m_x,temp_width,1)[0]
                f0.vector()[jj*3+1] = r.normal(m_y,temp_width,1)[0]
                f0.vector()[jj*3+2] = r.normal(m_z,temp_width,1)[0]

        f0 = f0/sqrt(inner(f0,f0))

        for nn in np.arange(no_of_int_points):
            z_axis.vector()[nn*3] = 0.0
            z_axis.vector()[nn*3+1] = 0.0
            z_axis.vector()[nn*3+2] = 1.0

        s0 = cross(f0,z_axis)
        s0 = s0/sqrt(inner(s0,s0))

        n0 = project(cross(s0,f0),VectorFunctionSpace(mesh, "DG", 0))
        n0 = n0/sqrt(inner(n0,n0))

    elif (sim_geometry == "unit_cube"):

        for jj in np.arange(no_of_int_points):

            f0.vector()[jj*3] = r.normal(m_x,width,1)[0]
            f0.vector()[jj*3+1] = r.normal(m_y,width,1)[0]
            f0.vector()[jj*3+2] = r.normal(m_z,width,1)[0]

        f0 = f0/sqrt(inner(f0,f0))

        for nn in np.arange(no_of_int_points):
            z_axis.vector()[nn*3] = 0.0
            z_axis.vector()[nn*3+1] = 0.0
            z_axis.vector()[nn*3+2] = 1.0

        s0 = cross(z_axis,f0)
        s0 = s0/sqrt(inner(s0,s0))

        n0 = cross(f0,s0)
        #n0 = project(cross(f0,s0),VectorFunctionSpace(mesh, "DG", 0))
        n0 = n0/sqrt(inner(n0,n0))

    return f0,s0,n0,geo_options
