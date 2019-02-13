import sys
sys.path.append("/home/fenics/shared/")

import vtk
import os
import numpy as np
from dolfin import *
from mpi4py import MPI as pyMPI
from create_ellipsoidal_LV import create_ellipsoidal_LV
from convertUGridToXMLMesh import convertUGridToXMLMesh
from extractFeNiCsLVFacet import extractFeNiCsLVFacet
from addLVfiber import addLVfiber
def pig_lv():
	
	casename = "ellipsoidal"

	outdir = "./" +casename + "/"
	directory = os.getcwd() + '/' +  casename + "/"
	ugrid = create_ellipsoidal_LV(casename, meshsize=0.3, gmshcmd="gmsh", iswritemesh=False, verbose=True)
	

	
	mesh = convertUGridToXMLMesh(ugrid)
	fenics_mesh_ref, fenics_facet_ref, fenics_edge_ref = extractFeNiCsLVFacet(ugrid, geometry = "LV")
	print (mesh)



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

	quad_deg = 4
	VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=quad_deg, quad_scheme="default")
	VQuadelem._quad_scheme = 'default'
	fiberFS = FunctionSpace(mesh, VQuadelem)
	isepiflip = True #True
	isendoflip = True #True
	endo_angle = 60; epi_angle = -60; casedir="./";  
	
	ef, es, en = addLVfiber(mesh, fiberFS, "lv", endo_angle, epi_angle, casedir, isepiflip, isendoflip, isapexflip=False)


	f = HDF5File(mesh.mpi_comm(), directory + casename+".hdf5", 'w')
	f.write(mesh, casename)
	f.close()

	f = HDF5File(mesh.mpi_comm(), directory + casename+".hdf5", 'a') 
	f.write(fenics_facet_ref, casename+"/"+"facetboundaries") 
	f.write(fenics_edge_ref, casename+"/"+"edgeboundaries") 
	f.write(ef, meshname+"/"+"eF") 
	f.write(es, meshname+"/"+"eS") 
	f.write(en, meshname+"/"+"eN")
	f.close()

	File(outdir+"_mesh" + ".pvd") << mesh


	#Hdf5 file reading
	mesh = Mesh()
	f = HDF5File(mpi_comm_world(), directory + casename+".hdf5", 'r')
	f.read(mesh, casename, False)

	facetboundaries = MeshFunction("size_t", mesh, 2)
	f.read(facetboundaries, casename+"/"+"facetboundaries")

	VQuadelem = VectorElement("Quadrature", mesh.ufl_cell(), degree=4, quad_scheme="default")
	VQuadelem._quad_scheme = 'default'
	fiberFS = FunctionSpace(mesh, VQuadelem)

	f0 = Function(fiberFS)
	s0 = Function(fiberFS)
	n0 = Function(fiberFS)

	f.read(f0, casename+"/"+"eF")
	f.read(s0, casename+"/"+"eS")
	f.read(n0, casename+"/"+"eN")

	f.close()

	return 0
	
s = pig_lv()
