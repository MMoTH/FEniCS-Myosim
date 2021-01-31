import sys
sys.path.append("/home/fenics/shared/source_code/dependencies/")

import vtk_py as vtk_py
import os
import numpy as np
#from pyquaternion import Quaternion

######################################################################################
# Import stuff from json file
input_file_name = sys.argv[1]

with open(input_file_name, 'r') as f:
  mesh_params = json.load(f)

inputfile_info = mesh_params["input_files"]
clip_info = mesh_params["volume_clip_info"]
output_info = mesh_params["output_info"]

base_input_path = inputfile_info["input_directory"]
endofilename = base_input_path + inputfile_info["endo_surface"]
epifilename = base_input_path + inputfile_info["epi_surface"]

output_dir = output_info["output_dir"]

###################################################################
# Info for clipping top of volumes
#Laxis = np.array([-0.0760398272351652, -0.0945530105122101, 0.992611541781136])
Laxis = clip_info["Laxis"]
zoffset = clip_info["z_offset"]
###################################################################



#zoffset = 1.0
angle = np.arccos(Laxis[2])
raxis = np.cross(Laxis, np.array([0,0,1]))
raxis = raxis / np.linalg.norm(raxis)


#endofilename = 'ENDO-LV' + '.stl'
endopdata = vtk_py.readSTL(endofilename)

#epifilename = 'EPI-LV' + '.stl'
epipdata = vtk_py.readSTL(epifilename)

rotatedepipdata = vtk_py.rotatePData_w_axis(epipdata, angle, raxis)
rotatedendopdata = vtk_py.rotatePData_w_axis(endopdata, angle, raxis)

height =  min(rotatedendopdata.GetBounds()[5], rotatedepipdata.GetBounds()[5]) - zoffset

clipped_endo, clipped_epi = vtk_py.clipSurfacesForCutLVMesh(rotatedendopdata, rotatedepipdata, height, verbose=True)



#vtk_py.writeSTL(clipped_epi, "clipped_epi_tmp.stl")
vtk_py.writeSTL(clipped_epi, output_dir + "clipped_epi_tmp.stl")

#vtk_py.writeSTL(clipped_endo, "clipped_endo_tmp.stl")
vtk_py.writeSTL(clipped_endo, output_dir +  "clipped_endo_tmp.stl")


#filename = 'New_mesh'
filename = output_info["mesh_name"]

vtk_py.createLVmesh(filename, 0.5, "clipped_epi_tmp.stl", "clipped_endo_tmp.stl")#(filename, 0.45, "clipped_epi_tmp.stl", "clipped_endo_tmp.stl") #



#os.remove("clipped_epi_tmp.stl")

#os.remove("clipped_endo_tmp.stl")
#os.remove("LVtemp.geo.bak")

ugridfilename = output_dir + filename + '.vtk'
pdatafilename = output_dir + filename + '.vtp'
ugrid = vtk_py.readUGrid(ugridfilename)
