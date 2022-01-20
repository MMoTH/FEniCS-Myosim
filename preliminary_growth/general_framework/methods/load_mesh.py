# @Author: charlesmann
# @Date:   2021-12-28T14:02:32-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T17:10:23-05:00
import sys
sys.path.append('/home/fenics/shared/dependencies/')
sys.path.append('/mnt/home/f0101140/Desktop/test_myosim_fix/FEniCS-Myosim/dependencies/')
import recode_dictionary
import json
from dolfin import *


def load_mesh(input_file):

    # This needs to be re-worked a bit to be more general, and a more consistent
    # case name (rather than "ellipsoid_scaled") needs to be used
    print "Loading mesh from input file"
    with open(input_file, 'r') as json_input:
      input_parameters = json.load(json_input)

    # We recursively iterate through the instruction file to make sure we
    # have all json strings instead of unicode
    recode_dictionary.recode(input_parameters)

    # Get the simulation parameters and geometry options
    #sim_params = input_parameters["simulation_parameters"]
    #geo_options = sim_params["geometry_options"]
    #esh_path = geo_options["mesh_path"][0]
    mesh_path = input_parameters["geometry"]["mesh_path"][0]

    # Create a dolfin mesh object
    mesh = Mesh()

    # Read the mesh into the mesh object
    f = HDF5File(mpi_comm_world(), mesh_path, 'r')
    f.read(mesh,"ellipsoid_scaled",False)
    #f.close()
    # don't close the file yet, we will need to read in the fiber coordinate system later
    # Save the reference mesh
    #File('./output/reference_mesh.pvd') << mesh

    return mesh, f, input_parameters
