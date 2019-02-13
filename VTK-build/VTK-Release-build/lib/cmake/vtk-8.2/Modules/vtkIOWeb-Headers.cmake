set(vtkIOWeb_HEADERS_LOADED 1)
set(vtkIOWeb_HEADERS "vtkDataArrayHelper;vtkHttpDataSetWriter;vtkHttpSceneExporter")

foreach(header ${vtkIOWeb_HEADERS})
  set(vtkIOWeb_HEADER_${header}_EXISTS 1)
endforeach()
