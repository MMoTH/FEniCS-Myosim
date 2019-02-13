set(vtkIOExportOpenGL2_HEADERS_LOADED 1)
set(vtkIOExportOpenGL2_HEADERS "vtkOpenGLGL2PSExporter;vtkIOExportOpenGL2ObjectFactory")

foreach(header ${vtkIOExportOpenGL2_HEADERS})
  set(vtkIOExportOpenGL2_HEADER_${header}_EXISTS 1)
endforeach()
