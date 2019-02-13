set(vtkIOExport_HEADERS_LOADED 1)
set(vtkIOExport_HEADERS "vtkExporter;vtkGL2PSExporter;vtkGLTFExporter;vtkIVExporter;vtkOBJExporter;vtkOOGLExporter;vtkPOVExporter;vtkRIBExporter;vtkRIBLight;vtkRIBProperty;vtkSVGContextDevice2D;vtkSVGExporter;vtkSingleVTPExporter;vtkVRMLExporter;vtkX3D;vtkX3DExporter;vtkX3DExporterFIWriter;vtkX3DExporterWriter;vtkX3DExporterXMLWriter")

foreach(header ${vtkIOExport_HEADERS})
  set(vtkIOExport_HEADER_${header}_EXISTS 1)
endforeach()
