set(vtkIOWeb_LOADED 1)
set(vtkIOWeb_DEPENDS "vtkCommonCore;vtkCommonCore;vtkCommonDataModel;vtkCommonMisc;vtkIOCore;vtkIOExport;vtksys")
set(vtkIOWeb_LIBRARIES "vtkIOWeb")
set(vtkIOWeb_INCLUDE_DIRS "${VTK_INSTALL_PREFIX}/include/vtk-8.2")
set(vtkIOWeb_LIBRARY_DIRS "")
set(vtkIOWeb_RUNTIME_LIBRARY_DIRS "${VTK_INSTALL_PREFIX}/lib")
set(vtkIOWeb_WRAP_HIERARCHY_FILE "${CMAKE_CURRENT_LIST_DIR}/vtkIOWebHierarchy.txt")
set(vtkIOWeb_KIT "vtkIO")
set(vtkIOWeb_TARGETS_FILE "")


