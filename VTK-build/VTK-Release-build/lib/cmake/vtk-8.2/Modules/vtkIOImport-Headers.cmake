set(vtkIOImport_HEADERS_LOADED 1)
set(vtkIOImport_HEADERS "vtk3DSImporter;vtkImporter;vtkVRMLImporter;vtkOBJImporter;vtkOBJImporterInternals")

foreach(header ${vtkIOImport_HEADERS})
  set(vtkIOImport_HEADER_${header}_EXISTS 1)
endforeach()
