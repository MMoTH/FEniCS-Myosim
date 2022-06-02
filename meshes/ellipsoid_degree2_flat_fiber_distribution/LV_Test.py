import sys
sys.path.append("/home/fenics/shared/dependencies/")

import vtk
import os
import vtk_py as vtk_py
import numpy as np
from dolfin import *
from mpi4py import MPI as pyMPI

def pig_lv():
	#print "starting pig_LV"
	casename = "ellipsoidal" #"New_mesh" #"ellipsoidal_from_MRI"
	meshfilename =  casename + ".vtk" #"ellipsoidal.vtk"#

	print meshfilename


	outdir = "./" +casename + "/"
	directory = os.getcwd() + '/' +  casename + "/"
	ugrid = vtk_py.readUGrid(meshfilename)


	#print (ugrid)

	mesh = vtk_py.convertUGridToXMLMesh(ugrid)

	print (mesh)
	comm2 = pyMPI.COMM_WORLD

	fenics_mesh_ref, fenics_facet_ref, fenics_edge_ref = vtk_py.extractFeNiCsBiVFacet(ugrid, geometry = "LV")

	matid = MeshFunction('size_t',fenics_mesh_ref, 3, mesh.domains())


	meshname = casename
	ztop =  max(fenics_mesh_ref.coordinates()[:,2])
	ztrans = Expression(("0.0", "0.0", str(-ztop)), degree = 1)

	if(dolfin.dolfin_version() != '1.6.0'):
		ALE.move(fenics_mesh_ref,ztrans)
	else:
		fenics_mesh_ref.move(ztrans)

	mesh = fenics_mesh_ref

	gdim = mesh.geometry().dim()

	quad_deg = 2
	VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=quad_deg, quad_scheme="default")
	VQuadelem._quad_scheme = 'default'
	fiberFS = FunctionSpace(mesh, VQuadelem)
	Quadelem = FiniteElement("Quadrature", mesh.ufl_cell(), degree=quad_deg, quad_scheme="default")
	Quadelem._quad_scheme = 'default'
	hslFS = FunctionSpace(mesh, Quadelem)
	isepiflip = True
	isendoflip = False
	endo_angle = 10; epi_angle = -10; casedir="./";
	hsl0_endo = 895.0
	hsl0_epi = 955.0

	hsl0, ef, es, en, eC, eL, eR = vtk_py.addLVfiber(mesh, fiberFS, hslFS, "lv", endo_angle, epi_angle, hsl0_endo, hsl0_epi, casedir, isepiflip, isendoflip, isapexflip=False)

	matid_filename = outdir + meshname + "_matid.pvd"
	File(matid_filename) << matid

	f = HDF5File(mesh.mpi_comm(), directory + meshname+".hdf5", 'w')
	f.write(mesh, meshname)
	f.close()

	f = HDF5File(mesh.mpi_comm(), directory + meshname+".hdf5", 'a')
	f.write(fenics_facet_ref, meshname+"/"+"facetboundaries")
	f.write(fenics_edge_ref, meshname+"/"+"edgeboundaries")
	f.write(matid, meshname+"/"+"matid")
	f.write(ef, meshname+"/"+"eF")
	f.write(es, meshname+"/"+"eS")
	f.write(en, meshname+"/"+"eN")
	f.write(eC, meshname+"/"+"eC")
	f.write(eL, meshname+"/"+"eL")
	f.write(eR, meshname+"/"+"eR")
	#print hsl0
	#print eR
	f.write(hsl0, meshname+"/"+"hsl0")

	f.close()


	File(outdir+"_facetboundaries"+".pvd") << fenics_facet_ref
	File(outdir+"_edgeboundaries"+".pvd") << fenics_edge_ref
	File(outdir+"_mesh" + ".pvd") << mesh
	File(outdir+"matid" +".pvd") << matid


	return 0
print "starting lvtest?"
s = pig_lv()
