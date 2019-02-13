set(vtkDomainsChemistryOpenGL2_HEADERS_LOADED 1)
set(vtkDomainsChemistryOpenGL2_HEADERS "vtkOpenGLMoleculeMapper;vtkDomainsChemistryOpenGL2ObjectFactory")

foreach(header ${vtkDomainsChemistryOpenGL2_HEADERS})
  set(vtkDomainsChemistryOpenGL2_HEADER_${header}_EXISTS 1)
endforeach()
