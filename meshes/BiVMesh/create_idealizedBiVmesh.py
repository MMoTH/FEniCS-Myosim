import sys
sys.path.append("/mnt/home/lclee/")
sys.path.append("/home/fenics/shared/dependencies/")
import vtk
import vtk_py
import os
import dolfin
from mpi4py import MPI as pyMPI
import glob
from vtk.util import numpy_support

def GetSurfaces(directory, filebasename, fieldvariable, isparallel):

	filenames = glob.glob(directory + "/" + filebasename + "*")
	filenames.sort()
	filenames = [filename for filename in filenames if filename[-3:] != "pvd"]

	if(filenames[0][-4:] == "pvtu" and isparallel):
		ugrid = vtk_py.readXMLPUGrid(filenames[0])

	elif(filenames[0][-4:] == ".vtu" and (not isparallel)):
		ugrid = vtk_py.readXMLUGrid(filenames[0])

	Epi = vtk_py.extractUGridBasedOnThreshold(ugrid, fieldvariable, 1)
	Epi  = vtk_py.convertUGridtoPdata(Epi)
	LVendo = vtk_py.extractUGridBasedOnThreshold(ugrid, fieldvariable, 2)
	LVendo  = vtk_py.convertUGridtoPdata(LVendo)
	RVendo = vtk_py.extractUGridBasedOnThreshold(ugrid, fieldvariable, 3)
	RVendo  = vtk_py.convertUGridtoPdata(RVendo)

	return LVendo, RVendo, Epi



comm2 = pyMPI.COMM_WORLD
#gmshcmd = "/mnt/home/lclee/gmsh/gmsh-4.7.1-Linux64/bin/gmsh"
gmshcmd = "gmsh"
#gmshcmd = "/home/fenics/shared/Downloads/gmsh-4.5.6-Linux64/bin/gmsh"

# Normal heart #####################################################
meshname = "biv_idealized2"
directory = "./"
#
## Use gmsh to generate biventricular mesh
#os.system(gmshcmd + " -3 " + meshname + ".geo" + " -o " + meshname+".vtk") kurtis commented out, already generated this file in newer version of gmsh
####################################################################

# Failing heart #####################################################
#meshname = "biv_idealized2_failing"
#directory = "./"

# Use gmsh to generate biventricular mesh
#os.system(gmshcmd + " -3 " + meshname + ".geo" + " -o " + meshname+".vtk")
####################################################################

#stop

# Read in vtk file
ugrid = vtk_py.readUGrid(meshname+".vtk");

# Rotate mesh so that z = 0 at base
ugridrot =  vtk_py.rotateUGrid(ugrid, rx=0.0, ry=-90.0, rz=0.0, sx=1.0, sy=1.0, sz=1.0)
vtk_py.writeUGrid(ugridrot, meshname+"_rot.vtk")

# For some reason vtkPointLocator in extractFenicsBiVFacet will give error if precision is too high
newpts = vtk.vtkPoints()
for p in range(0, ugridrot.GetNumberOfPoints()):
	pt = [ugridrot.GetPoints().GetPoint(p)[0], ugridrot.GetPoints().GetPoint(p)[1], ugridrot.GetPoints().GetPoint(p)[2]]
        newpts.InsertNextPoint([round(pt[k],5) for k in range(0,3)])
ugridrot.SetPoints(newpts)


# Extract fenics mesh
fenics_mesh_ref, fenics_facet_ref, fenics_edge_ref = vtk_py.extractFeNiCsBiVFacet(ugridrot);
dolfin.File("bivmesh.pvd") << fenics_mesh_ref;
dolfin.File("bivfacet.pvd") << fenics_facet_ref;
dolfin.File("bivedge.pvd") << fenics_edge_ref;

X = dolfin.SpatialCoordinate(fenics_mesh_ref)
N = dolfin.FacetNormal (fenics_mesh_ref)
ds = dolfin.ds(subdomain_data = fenics_facet_ref)
lv_vol_form = -dolfin.Constant(1.0/3.0) * dolfin.inner(N, X)*ds(2)
rv_vol_form = -dolfin.Constant(1.0/3.0) * dolfin.inner(N, X)*ds(3)
lv_vol = dolfin.assemble(lv_vol_form, form_compiler_parameters={"representation":"uflacs"})
rv_vol = dolfin.assemble(rv_vol_form, form_compiler_parameters={"representation":"uflacs"})

if(comm2.Get_rank() == 0):
	print "LV cavity vol = ", lv_vol, " ml"
	print "RV cavity vol = ", rv_vol, " ml"



# Set Material Region
matid = dolfin.MeshFunction('size_t', fenics_mesh_ref, 3, fenics_mesh_ref.domains())
LVendo, RVendo, Epi = GetSurfaces("./", "bivfacet000000.vtu", "f", False)
ugrid = vtk_py.readXMLUGrid("bivmesh000000.vtu")
vtk_py.addRegionsToBiV(ugrid, LVendo, RVendo, Epi)
matid_vtk = numpy_support.vtk_to_numpy(ugrid.GetCellData().GetArray("region_id"))
matid.array()[:] = matid_vtk
dolfin.File("matid.pvd") << matid;

# Set BiVFiber
fiber_angle_param = {"mesh": fenics_mesh_ref,\
	 "facetboundaries": fenics_facet_ref,\
	 "LV_fiber_angle": [60,-60], \
	 "LV_sheet_angle": [0.1, -0.1], \
	 "Septum_fiber_angle": [60, -60],\
	 "Septum_sheet_angle": [0.1, -0.1],\
	 "RV_fiber_angle": [60, -60],\
	 "RV_sheet_angle": [0.1, -0.1],\
	 "LV_matid": 0,\
	 "Septum_matid": 1,\
	 "RV_matid": 2,\
	 "matid": matid,\
	 "isrotatept": False,\
	 "isreturn": True,\
	 "outfilename":  meshname,\
	 "outdirectory": directory,\
	 "epiid": 1,\
	 "rvid": 3,\
	 "lvid": 2,\
	 "degree": 4}


print "mesh in param?"
print fiber_angle_param["mesh"]
ef, es, en = vtk_py.SetBiVFiber_Quad_PyQ(fiber_angle_param)

f = dolfin.HDF5File(fenics_mesh_ref.mpi_comm(), directory + meshname+".hdf5", 'w')
f.write(fenics_mesh_ref, meshname)
f.close()

f = dolfin.HDF5File(fenics_mesh_ref.mpi_comm(), directory + meshname+".hdf5", 'a')
f.write(fenics_facet_ref, meshname+"/"+"facetboundaries")
f.write(fenics_edge_ref, meshname+"/"+"edgeboundaries")
f.write(matid, meshname+"/"+"matid")
f.write(ef, meshname+"/"+"eF")
f.write(es, meshname+"/"+"eS")
f.write(en, meshname+"/"+"eN")
f.close()




