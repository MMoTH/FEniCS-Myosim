set(vtkFiltersTopology_HEADERS_LOADED 1)
set(vtkFiltersTopology_HEADERS "vtkFiberSurface")

foreach(header ${vtkFiltersTopology_HEADERS})
  set(vtkFiltersTopology_HEADER_${header}_EXISTS 1)
endforeach()
