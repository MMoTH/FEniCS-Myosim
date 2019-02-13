set(vtkIOAMR_HEADERS_LOADED 1)
set(vtkIOAMR_HEADERS "vtkAMRBaseParticlesReader;vtkAMRBaseReader;vtkAMRDataSetCache;vtkAMREnzoParticlesReader;vtkAMREnzoReader;vtkAMREnzoReaderInternal;vtkAMReXParticlesReader;vtkAMRFlashParticlesReader;vtkAMRFlashReader;vtkAMRFlashReaderInternal")

foreach(header ${vtkIOAMR_HEADERS})
  set(vtkIOAMR_HEADER_${header}_EXISTS 1)
endforeach()
