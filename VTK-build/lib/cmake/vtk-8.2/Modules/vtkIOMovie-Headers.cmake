set(vtkIOMovie_HEADERS_LOADED 1)
set(vtkIOMovie_HEADERS "vtkGenericMovieWriter;vtkOggTheoraWriter")

foreach(header ${vtkIOMovie_HEADERS})
  set(vtkIOMovie_HEADER_${header}_EXISTS 1)
endforeach()
