set(vtkIOParallel_HEADERS_LOADED 1)
set(vtkIOParallel_HEADERS "vtkEnSightWriter;vtkMultiBlockPLOT3DReader;vtkMultiBlockPLOT3DReaderInternals;vtkPlot3DMetaReader;vtkPChacoReader;vtkPDataSetReader;vtkPDataSetWriter;vtkPImageWriter;vtkPOpenFOAMReader;vtkPSLACReader")

foreach(header ${vtkIOParallel_HEADERS})
  set(vtkIOParallel_HEADER_${header}_EXISTS 1)
endforeach()
