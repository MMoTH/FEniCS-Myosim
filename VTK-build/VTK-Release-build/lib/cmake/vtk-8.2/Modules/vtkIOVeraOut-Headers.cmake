set(vtkIOVeraOut_HEADERS_LOADED 1)
set(vtkIOVeraOut_HEADERS "vtkVeraOutReader")

foreach(header ${vtkIOVeraOut_HEADERS})
  set(vtkIOVeraOut_HEADER_${header}_EXISTS 1)
endforeach()
