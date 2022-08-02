from dolfin import *
from numpy import random as r
import numpy as np
import math

def assign_local_coordinate_system(lv_options,coord_params,sim_params):

    # Set random seed
    if "rseed" in sim_params.keys():
        rseed = sim_params["rseed"][0]
        r.seed(rseed)

    # initialization
    marker_space = coord_params["marker_space"]
    fiberFS      = coord_params["fiberFS"]
    sim_geometry = coord_params["sim_geometry"]
    geo_options  = coord_params["geo_options"]
    geo_options["fiberFS"] = fiberFS
    no_of_int_points = coord_params["no_of_int_points"]
    #geo_options = coord_params["geo_options"]

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
    """m_x = 1.0/sqrt(2.)
    m_y = 1./sqrt(2.)
    m_z = 0.0"""



    if (sim_geometry == "ventricle") or (sim_geometry == "ellipsoid"):
        casename = lv_options["casename"]
        f        = lv_options["f"]
        # assign local coordinate system at each gauss point
        if sim_params["fiber_orientation"]["load_fibers"][0] > 0.0:
            # loading in fibers from a previous simulation
            fnew = HDF5File(mpi_comm_world(),sim_params["fiber_orientation"]["load_fibers"][1],'r')
            fnew.read(f0,"f0")
            fnew.read(s0,"s0")
            fnew.read(n0,"n0")
            fnew.close()
            f.read(facetboundaries, casename+"/"+"facetboundaries")
            f.read(edgeboundaries, casename+"/"+"edgeboundaries")
        else:
            f.read(facetboundaries, casename+"/"+"facetboundaries")
            f.read(edgeboundaries, casename+"/"+"edgeboundaries")
            f.read(f0, casename + "/" + "eF")
            f.read(s0, casename + "/" + "eS")
            f.read(n0, casename + "/" + "eN")
        f.close()

    if (sim_geometry == "cylinder") or sim_geometry == "gmesh_cylinder":

        theta = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["theta"][0])
        phi   = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["phi"][0])
        width = sim_params["fiber_orientation"]["fiber_randomness"][0]

        # Convert fiber angles into Cartesian coordinates with radius 1
        m_x = sin(phi)*cos(theta)
        m_y = sin(phi)*sin(theta)
        m_z = cos(phi)

        # Functions that are useful in unit cube and cylinder for calculating
        # fibrous area, or the long (x) axis to assign local coordinate systems
        test_marker_fcn = Function(marker_space)
        z_axis       = Function(fiberFS)

        if sim_geometry == "cylinder":
            radius = geo_options["base_radius"][0]
        if sim_geometry == "gmesh_cylinder":
            radius = 1.0
        else:
            radius = 0.5
        # Create a simple expression to test if x_coord is > 9.0 or < 1.0
        # making last 10% of cylinder spring elements
        end_marker = Expression("x[0]",degree=1)
        y_marker = Expression("x[1]", degree=1)
        point_radius = Expression("sqrt(pow(x[1],2)+pow(x[2],2))",degree=1)

        # Project the expression onto the mesh
        end_marker_values = project(end_marker,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
        y_values = project(y_marker,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})
        point_rad_values = project(point_radius,FunctionSpace(mesh,"DG",1),form_compiler_parameters={"representation":"uflacs"})

        # Interpolate onto the FunctionSpace for quadrature points
        end_marker_on_mesh = interpolate(end_marker_values,Quad)
        y_marker_on_mesh = interpolate(y_values,Quad)
        point_rad = interpolate(point_rad_values,Quad)

        # Create array of the expression values
        end_marker_array = end_marker_on_mesh.vector().get_local()
        y_marker_array = y_marker_on_mesh.vector().get_local()
        point_rad_array = point_rad.vector().get_local()

        # Updating geometry options to save end_marker_array to assign heterogeneous parameters later
        geo_options["end_marker_array"] = end_marker_array
        dm = fiberFS.dofmap()
        local_range = dm.ownership_range()
        local_dim = local_range[1]-local_range[0]
        assign_array_f0 = np.zeros(np.shape(f0.vector().get_local()))

        for jj in np.arange(int(local_dim/3)):

            if sim_geometry == "box_mesh":
                start_end_compliance = 2./3.
                end_beginning_compliance = 0.
            else:
                start_end_compliance = 9.0
                end_beginning_compliance = 1.0

            #if (temp_tester_array[jj] < dig_array[jj]) or (temp_tester_array[jj] > -dig_array[jj] + 10.0):
            if (end_marker_array[jj] > start_end_compliance) or (end_marker_array[jj] < end_beginning_compliance):
                #print "assigning end fibers"
                
                # inside left end
                #f0.vector()[jj*3] = 1.0
                #f0.vector()[jj*3+1] = 0.0
                #f0.vector()[jj*3+2] = 0.0
                assign_array_f0[jj*3] = 1.0
                assign_array_f0[jj*3+1] = 0.0
                assign_array_f0[jj*3+2] = 0.0

            else:
                if sim_geometry == "gmesh_cylinder" or sim_geometry == "cylinder":
                    # In middle region, assign fiber vector
                    # find radius of point
                    temp_radius = point_rad_array[jj]
                    if np.abs(temp_radius - radius) < 0.01:
                        temp_width = 0.0
                    else:
                        temp_width = np.abs(width*(1.0-(temp_radius*temp_radius/(radius*radius))))
                    #f0.vector()[jj*3] = r.normal(m_x,temp_width,1)[0]
                    #f0.vector()[jj*3+1] = r.normal(m_y,temp_width,1)[0]
                    #f0.vector()[jj*3+2] = r.normal(m_z,temp_width,1)[0]
                    assign_array_f0[jj*3] = r.normal(m_x, temp_width, 1)[0]
                    assign_array_f0[jj*3+1] = r.normal(m_y, temp_width, 1)[0]
                    assign_array_f0[jj*3+2] = r.normal(m_z, temp_width, 1)[0]
                else:
                    # coding in a test case for box mesh
                    if y_marker_array[jj] >= 0.5:
                      f0.vector()[jj*3] = 1.0 #0.965925826289068 # 0.707106781186548
                      f0.vector()[jj*3+1] = 0.0 #0.258819045102521 #0.707106781186548
                      f0.vector()[jj*3+2] = 0.0
                    else:
                      f0.vector()[jj*3] = 1.0 #0.965925826289068 #0.707106781186548
                      f0.vector()[jj*3+1] = 0.0 #-0.258819045102521 #-0.707106781186548
                      f0.vector()[jj*3+2] = 0.0

            #f0.vector()[jj*3] = r.normal(m_x,width,1)[0]
            #f0.vector()[jj*3+1] = r.normal(m_y,width,1)[0]
            #f0.vector()[jj*3+2] = r.normal(m_z,width,1)[0]
            f0.vector().set_local(assign_array_f0)
            as_backend_type(f0.vector()).update_ghost_values()
        # normalize f0
        f0 /= sqrt(inner(f0,f0))
       
        # Need a z-axis function
        s0 = cross(Constant((0.0,0.0,1.0)),f0)
        n0 = cross(f0, s0)
        """f0_holder = f0.vector().array()[jj*3:jj*3+3]
        f0_holder /= sqrt(np.inner(f0_holder,f0_holder))
        for kk in range(3):
            f0.vector()[jj*3+kk] = f0_holder[kk]

        z_axis.vector()[jj*3] = 0.0
        z_axis.vector()[jj*3+1] = 0.0
        z_axis.vector()[jj*3+2] = 1.0

        s0_holder = np.cross(z_axis.vector().array()[jj*3:jj*3+3],f0_holder)

        s0_holder /= sqrt(np.inner(s0_holder,s0_holder))
        for kk in range(3):
            s0.vector()[jj*3+kk] = s0_holder[kk]

        n0_holder = np.cross(f0.vector().array()[jj*3:jj*3+3],s0.vector().array()[jj*3:jj*3+3])

        n0_holder /= sqrt(np.inner(n0_holder,n0_holder))
        for kk in range(3):
            n0.vector()[jj*3+kk] = n0_holder[kk]"""

    if sim_geometry == "box_mesh":

        theta = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["theta"][0])
        phi   = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["phi"][0])
        width = sim_params["fiber_orientation"]["fiber_randomness"][0]

        # Convert fiber angles into Cartesian coordinates with radius 1
        m_x = sin(phi)*cos(theta)
        m_y = sin(phi)*sin(theta)
        m_z = cos(phi)

        # Functions that are useful in unit cube and cylinder for calculating
        # fibrous area, or the long (x) axis to assign local coordinate systems
        test_marker_fcn = Function(marker_space)
        z_axis       = Function(fiberFS)

        x_marker = Expression("x[0]",degree=1)
        y_marker = Expression("x[1]",degree=1)
        z_marker = Expression("x[2]",degree=1)

        # Project the expression onto the mesh
        x_marker_values = project(x_marker,FunctionSpace(mesh,"DG",0),form_compiler_parameters={"representation":"uflacs"})
        y_marker_values = project(y_marker,FunctionSpace(mesh,"DG",0),form_compiler_parameters={"representation":"uflacs"})
        z_marker_values = project(z_marker,FunctionSpace(mesh,"DG",0),form_compiler_parameters={"representation":"uflacs"})

        """# Interpolate onto the FunctionSpace for quadrature points
        x_marker_on_mesh = interpolate(x_marker_values,Quad)
        y_marker_on_mesh = interpolate(y_marker_values,Quad)
        z_marker_on_mesh = interpolate(z_marker_values,Quad)

        # Create array of the expression values
        x_marker_array = x_marker_on_mesh.vector().get_local()
        y_marker_array = y_marker_on_mesh.vector().get_local()
        z_marker_array = z_marker_on_mesh.vector().get_local()"""

        x_marker_array = x_marker_values.vector().get_local()
        y_marker_array = y_marker_values.vector().get_local()
        z_marker_array = z_marker_values.vector().get_local()

        # Updating geometry options to save end_marker_array to assign heterogeneous parameters later
        geo_options["x_marker_array"] = x_marker_array
        geo_options["y_marker_array"] = y_marker_array
        geo_options["z_marker_array"] = z_marker_array
        geo_options["end_marker_array"] = x_marker_array

        for jj in np.arange(no_of_int_points):

            f0.vector()[jj*3] = r.normal(m_x,width,1)[0]
            f0.vector()[jj*3+1] = r.normal(m_y,width,1)[0]
            f0.vector()[jj*3+2] = r.normal(m_z,width,1)[0]

            f0_holder = f0.vector().array()[jj*3:jj*3+3]
            f0_holder /= sqrt(np.inner(f0_holder,f0_holder))
            for kk in range(3):
                f0.vector()[jj*3+kk] = f0_holder[kk]

            z_axis.vector()[jj*3] = 0.0
            z_axis.vector()[jj*3+1] = 0.0
            z_axis.vector()[jj*3+2] = 1.0

            s0_holder = np.cross(z_axis.vector().array()[jj*3:jj*3+3],f0_holder)

            s0_holder /= sqrt(np.inner(s0_holder,s0_holder))
            for kk in range(3):
                s0.vector()[jj*3+kk] = s0_holder[kk]

            n0_holder = np.cross(f0.vector().array()[jj*3:jj*3+3],s0.vector().array()[jj*3:jj*3+3])

            n0_holder /= sqrt(np.inner(n0_holder,n0_holder))
            for kk in range(3):
                n0.vector()[jj*3+kk] = n0_holder[kk]

    if (sim_geometry == "unit_cube"):

        theta = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["theta"][0])
        phi   = math.radians(sim_params["fiber_orientation"]["fiber_direction"]["phi"][0])
        width = sim_params["fiber_orientation"]["fiber_randomness"][0]

        # Convert fiber angles into Cartesian coordinates with radius 1
        m_x = sin(phi)*cos(theta)
        m_y = sin(phi)*sin(theta)
        m_z = cos(phi)

        # Functions that are useful in unit cube and cylinder for calculating
        # fibrous area, or the long (x) axis to assign local coordinate systems
        test_marker_fcn = Function(marker_space)
        z_axis       = Function(fiberFS)

        dm = fiberFS.dofmap()
        local_range = dm.ownership_range()
        local_dim = local_range[1] - local_range[0]
        for jj in np.arange(int(local_dim/3)):

            f0.vector()[jj*3] = r.normal(m_x,width,1)[0]
            f0.vector()[jj*3+1] = r.normal(m_y,width,1)[0]
            f0.vector()[jj*3+2] = r.normal(m_z,width,1)[0]

            f0_holder = f0.vector().array()[jj*3:jj*3+3]
            f0_holder /= sqrt(np.inner(f0_holder,f0_holder))
            for kk in range(3):
                f0.vector()[jj*3+kk] = f0_holder[kk]

            z_axis.vector()[jj*3] = 0.0
            z_axis.vector()[jj*3+1] = 0.0
            z_axis.vector()[jj*3+2] = 1.0

            s0_holder = np.cross(z_axis.vector().array()[jj*3:jj*3+3],f0_holder)

            s0_holder /= sqrt(np.inner(s0_holder,s0_holder))
            for kk in range(3):
                s0.vector()[jj*3+kk] = s0_holder[kk]

            n0_holder = np.cross(f0.vector().array()[jj*3:jj*3+3],s0.vector().array()[jj*3:jj*3+3])

            n0_holder /= sqrt(np.inner(n0_holder,n0_holder))
            for kk in range(3):
                n0.vector()[jj*3+kk] = n0_holder[kk]

    # Kurtis adding this in for a quick test
    #f0.vector()[(no_of_int_points-1)*3] = 0.0
    #f0.vector()[(no_of_int_points-1)*3+1] = 1.0
    #f0.vector()[(no_of_int_points-1)*3+2] = 0.0

    return f0,s0,n0,geo_options

def update_local_coordinate_system(fiber_direction,coord_params):

    f0 = coord_params["f0"]
    print "update local cs"
    s0 = coord_params["s0"]
    n0 = coord_params["n0"]
    no_of_int_points = coord_params["no_of_int_points"]
    fiberFS = coord_params["fiberFS"]
    z_axis = Function(fiberFS)
    dm = fiberFS.dofmap()
    local_range = dm.ownership_range()
    local_dim = local_range[1] - local_range[0]

    for jj in np.arange(int(local_dim/3)):

        f0_holder = f0.vector().array()[jj*3:jj*3+3]
        f0_holder /= sqrt(np.inner(f0_holder,f0_holder))
        for kk in range(3):
            f0.vector()[jj*3+kk] = f0_holder[kk]

        z_axis.vector()[jj*3] = 0.0
        z_axis.vector()[jj*3+1] = 0.0
        z_axis.vector()[jj*3+2] = 1.0

        s0_holder = np.cross(z_axis.vector().array()[jj*3:jj*3+3],f0_holder)

        s0_holder /= sqrt(np.inner(s0_holder,s0_holder))
        for kk in range(3):
            s0.vector()[jj*3+kk] = s0_holder[kk]

        n0_holder = np.cross(f0.vector().array()[jj*3:jj*3+3],s0.vector().array()[jj*3:jj*3+3])

        n0_holder /= sqrt(np.inner(n0_holder,n0_holder))
        for kk in range(3):
            n0.vector()[jj*3+kk] = n0_holder[kk]


    return s0, n0
