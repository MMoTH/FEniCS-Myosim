set(vtkIOCityGML_HEADERS_LOADED 1)
set(vtkIOCityGML_HEADERS "vtkCityGMLReader")

foreach(header ${vtkIOCityGML_HEADERS})
  set(vtkIOCityGML_HEADER_${header}_EXISTS 1)
endforeach()
