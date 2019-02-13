set(vtkIOPLY_HEADERS_LOADED 1)
set(vtkIOPLY_HEADERS "vtkPLY;vtkPLYReader;vtkPLYWriter")

foreach(header ${vtkIOPLY_HEADERS})
  set(vtkIOPLY_HEADER_${header}_EXISTS 1)
endforeach()
