set(vtkIOLSDyna_HEADERS_LOADED 1)
set(vtkIOLSDyna_HEADERS "vtkLSDynaPart;vtkLSDynaPartCollection;vtkLSDynaReader;vtkLSDynaSummaryParser;LSDynaMetaData;LSDynaFamily")

foreach(header ${vtkIOLSDyna_HEADERS})
  set(vtkIOLSDyna_HEADER_${header}_EXISTS 1)
endforeach()
