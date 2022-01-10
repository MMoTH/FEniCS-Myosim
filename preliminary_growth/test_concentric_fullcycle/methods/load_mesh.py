# @Author: charlesmann
# @Date:   2021-12-28T14:02:32-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2021-12-28T15:24:40-05:00
import sys
sys.path.append('/home/fenics/shared/dependencies/')
import recode_dictionary
import json
from dolfin import *


def load_mesh(input_file):
    print "loading mesh from input file"
    with open(input_file, 'r') as json_input:
      input_parameters = json.load(json_input)

    # We recursively iterate through the instruction file to make sure we
    # have all json strings instead of unicode
    recode_dictionary.recode(input_parameters)

    # Get the simulation parameters and geometry options
    sim_params = input_parameters["simulation_parameters"]
    geo_options = sim_params["geometry_options"]
    mesh_path = geo_options["mesh_path"][0]

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
