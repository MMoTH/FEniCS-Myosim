set(vtkIOSegY_HEADERS_LOADED 1)
set(vtkIOSegY_HEADERS "vtkSegYReader;vtkSegYIOUtils;vtkSegYReaderInternal;vtkSegYTraceReader")

foreach(header ${vtkIOSegY_HEADERS})
  set(vtkIOSegY_HEADER_${header}_EXISTS 1)
endforeach()
