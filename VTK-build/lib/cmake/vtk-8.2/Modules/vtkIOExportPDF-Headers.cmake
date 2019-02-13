set(vtkIOExportPDF_HEADERS_LOADED 1)
set(vtkIOExportPDF_HEADERS "vtkPDFContextDevice2D;vtkPDFExporter;vtkIOExportPDFObjectFactory")

foreach(header ${vtkIOExportPDF_HEADERS})
  set(vtkIOExportPDF_HEADER_${header}_EXISTS 1)
endforeach()
