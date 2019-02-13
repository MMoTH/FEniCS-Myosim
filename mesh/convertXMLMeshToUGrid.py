########################################################################

import vtk
import dolfin



########################################################################

def convertXMLMeshToUGrid(mesh):

	connectivity =  mesh.cells()
	coords =  mesh.coordinates()

	points = vtk.vtkPoints()
	for coord in coords:
		points.InsertNextPoint(coord[0], coord[1], coord[2])
	
	cellarray = vtk.vtkCellArray()
	for cell in connectivity:
		tetra = vtk.vtkTetra()
		tetra.GetPointIds().SetId(0, cell[0])
		tetra.GetPointIds().SetId(1, cell[1])
		tetra.GetPointIds().SetId(2, cell[2])
		tetra.GetPointIds().SetId(3, cell[3])

		cellarray.InsertNextCell(tetra)

	ugrid = vtk.vtkUnstructuredGrid()
	ugrid.SetPoints(points)
	ugrid.SetCells(tetra.GetCellType(), cellarray)

	return ugrid	
	



