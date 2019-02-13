# Install script for directory: /home/fenics/shared/VTK/Filters/Extraction

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "RuntimeLibraries")
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersExtraction-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersExtraction-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersExtraction-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersExtraction-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersExtraction-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersExtraction-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/fenics/shared/VTK-build/VTK-Release-build/lib:"
           NEW_RPATH "")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Extraction/CMakeFiles/vtkFiltersExtraction.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Extraction/vtkBlockSelector.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkConvertSelection.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractBlock.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractCells.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractCellsByType.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractDataArraysOverTime.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractDataOverTime.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractDataSets.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractEdges.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractGeometry.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractGrid.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractLevel.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractPolyDataGeometry.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractRectilinearGrid.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedArraysOverTime.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedBlock.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedIds.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedLocations.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedPolyDataIds.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedRows.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectedThresholds.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelection.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractTemporalFieldData.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractTensorComponents.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractTimeSteps.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractUnstructuredGrid.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractVectorComponents.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkFrustumSelector.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkHierarchicalDataExtractDataSets.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkHierarchicalDataExtractLevel.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkLocationSelector.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkProbeSelectedLocations.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkSelector.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkValueSelector.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractArraysOverTime.h"
    "/home/fenics/shared/VTK/Filters/Extraction/vtkExtractSelectionLegacy.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Extraction/vtkFiltersExtractionModule.h"
    )
endif()

