set(vtkCommonMisc_HEADERS_LOADED 1)
set(vtkCommonMisc_HEADERS "vtkContourValues;vtkErrorCode;vtkFunctionParser;vtkHeap;vtkPolygonBuilder;vtkResourceFileLocator")

foreach(header ${vtkCommonMisc_HEADERS})
  set(vtkCommonMisc_HEADER_${header}_EXISTS 1)
endforeach()
