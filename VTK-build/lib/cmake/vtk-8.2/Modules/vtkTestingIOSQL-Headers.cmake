set(vtkTestingIOSQL_HEADERS_LOADED 1)
set(vtkTestingIOSQL_HEADERS "DatabaseSchemaWith2Tables")

foreach(header ${vtkTestingIOSQL_HEADERS})
  set(vtkTestingIOSQL_HEADER_${header}_EXISTS 1)
endforeach()
