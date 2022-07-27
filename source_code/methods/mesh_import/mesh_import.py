from dolfin import *
import numpy as np
#import mpi
import mshr
#import vtk_py
import os

## Import the appropriate mesh to mmoth-vent
#
# As of 10/23/2020, choices include unit_cube (single cell sims),
# cylinder, path_to_existing? (exising to just load in mesh from specified path?)
def import_mesh(sim_geometry, options):

    # create a dictionary to pass info for fcn assignments later
    lv_options = {}

    if sim_geometry == "box_mesh":
        print "Creating Box Mesh"

        # setting default values
        box_mesh_specs = {}
        box_mesh_specs["base_corner_x"] = [0.0]
        box_mesh_specs["base_corner_y"] = [0.0]
        box_mesh_specs["base_corner_z"] = [0.0]
        box_mesh_specs["end_x"] = [10.0]
        box_mesh_specs["end_y"] = [1.0]
        box_mesh_specs["end_z"] = [1.0]
        box_mesh_specs["refinement_x"] = [10.0]
        box_mesh_specs["refinement_y"] = [5.0]
        box_mesh_specs["refinement_z"] = [5.0]
        box_mesh_specs.update(options)

        base_corner = Point(box_mesh_specs["base_corner_x"][0],box_mesh_specs["base_corner_y"][0],box_mesh_specs["base_corner_z"][0])
        end_corner = Point(box_mesh_specs["end_x"][0],box_mesh_specs["end_y"][0],box_mesh_specs["end_z"][0])
        mesh = BoxMesh(base_corner,end_corner,box_mesh_specs["refinement_x"][0],box_mesh_specs["refinement_y"][0],box_mesh_specs["refinement_z"][0])

    if sim_geometry == "gmesh_cylinder":
        path_to_mesh = options["mesh_path"][0]
        #mesh = Mesh(path_to_mesh)

        mesh = Mesh()
        f = XDMFFile(mpi_comm_world(), path_to_mesh)
        f.read(mesh)
        f.close()
    if sim_geometry == "cylinder":

        # initialize dictionary
        cylinder_specs = {}

        # default values
        #----------------
        # Center point for end of cylinder
        cylinder_specs["end_x"] = [10.0]
        cylinder_specs["end_y"] = [0.0]
        cylinder_specs["end_z"] = [0.0]

        # Center point for base of cylinder
        cylinder_specs["base_x"] = [0.0]
        cylinder_specs["base_y"] = [0.0]
        cylinder_specs["base_z"] = [0.0]

        # Base radius
        cylinder_specs["base_radius"] = [1.0]
        cylinder_specs["end_radius"] = [1.0]

        # Segments for approximating round shape
        cylinder_specs["segments"] = [20]

        # Refinement of mesh
        cylinder_specs["refinement"] = [30]

        # If user provides any alternate values, update
        # the cylinder_specs dictionary now
        cylinder_specs.update(options)

        cyl_bottom_center = Point(cylinder_specs["base_x"][0],cylinder_specs["base_y"][0],cylinder_specs["base_z"][0])
        cyl_top_center    = Point(cylinder_specs["end_x"][0],cylinder_specs["end_y"][0],cylinder_specs["end_z"][0])

        # Create cylinder geometry
        cylinder_geometry = mshr.Cylinder(cyl_top_center,cyl_bottom_center,cylinder_specs["end_radius"][0],cylinder_specs["base_radius"][0],cylinder_specs["segments"][0])

        # Create mesh
        print "Creating cylinder mesh"
        mesh = mshr.generate_mesh(cylinder_geometry,cylinder_specs["refinement"][0])

    if sim_geometry == "unit_cube":

        # Use built in function
        mesh = UnitCubeMesh(1,1,1)

    if sim_geometry == "ventricle" or sim_geometry == "ellipsoid":
        if "casename" in options:
            casename = options["casename"][0]
            print "assigned casename from input file"
        else:
            if sim_geometry == "ellipsoid":
                casename = "ellipsoid_scaled"
            else:
                casename = "New_mesh" #New_mesh is the default casename in scripts sent from Dr. Lee

        mesh_path = options["mesh_path"][0]

        lv_options["casename"] = casename
        lv_options["mesh_path"] = mesh_path

        # check to see if it exists
        if not os.path.exists(mesh_path):
            print "mesh file not found"
            exit()

        if "hdf5" in mesh_path:

            print "Importing hdf5 mesh"

            mesh = Mesh()
            f = HDF5File(mpi_comm_world(), mesh_path, 'r')
            if "grown_mesh" in options.keys():
              casename = "grown_mesh" 
            if options["scaled"][0] == "True":
              print "using scaled version of mesh"
              casename = "scaled_mesh"
            f.read(mesh, casename, False)
            # had to read casename for scaled mesh. Now switch casename back to original
            # to access all other functions for ellipsoid sim
            print "SIM_GEOMETRY",sim_geometry
            if sim_geometry == "ellipsoid":
                print "CHANGING CASENAME"
                lv_options["casename"] = "ellipsoidal"
            #f.close()

            #ugrid = vtk_py.convertXMLMeshToUGrid(mesh)
            #ugrid = vtk_py.rotateUGrid(ugrid, sx=0.1, sy=0.1, sz=0.1)
            #mesh = vtk_py.convertUGridToXMLMesh(ugrid)

            #f = HDF5File(mpi_comm_world(), mesh_path, 'a')
            #f.write(mesh,"ellipsoid_scaled")
            #f.close()

            lv_options["f"] = f
            #hdf5_file = HDF5File(mpi_comm_world(),'scaled_mesh.hdf5',"w")
            #hdf5_file.write(mesh,"Mesh")



    return mesh,lv_options
