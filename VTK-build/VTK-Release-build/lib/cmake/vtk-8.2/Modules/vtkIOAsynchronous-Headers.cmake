set(vtkIOAsynchronous_HEADERS_LOADED 1)
set(vtkIOAsynchronous_HEADERS "vtkThreadedImageWriter")

foreach(header ${vtkIOAsynchronous_HEADERS})
  set(vtkIOAsynchronous_HEADER_${header}_EXISTS 1)
endforeach()
