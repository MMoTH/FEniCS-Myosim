# Install script for directory: /home/fenics/shared/VTK/Filters/Parallel

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
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersParallel-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersParallel-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersParallel-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersParallel-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersParallel-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersParallel-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/fenics/shared/VTK-build/lib:"
           NEW_RPATH "")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Filters/Parallel/CMakeFiles/vtkFiltersParallel.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Parallel/vtkAggregateDataSetFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkAngularPeriodicFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkCollectGraph.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkCollectPolyData.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkCollectTable.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkCutMaterial.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkDuplicatePolyData.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkExtractCTHPart.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkExtractPolyDataPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkExtractUnstructuredGridPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkExtractUserDefinedPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkIntegrateAttributes.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPassThroughFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPCellDataToPointData.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPeriodicFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPExtractDataArraysOverTime.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPExtractSelectedArraysOverTime.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPieceRequestFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPieceScalars.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPipelineSize.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPKdTree.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPLinearExtrusionFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPMaskPoints.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPOutlineCornerFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPOutlineFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPOutlineFilterInternals.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPPolyDataNormals.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPProbeFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPProjectSphereFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPReflectionFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPResampleFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkProcessIdScalars.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPSphereSource.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPYoungsMaterialInterface.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkRectilinearGridOutlineFilter.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkRemoveGhosts.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkTransmitPolyDataPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkTransmitRectilinearGridPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkTransmitStructuredDataPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkTransmitStructuredGridPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkTransmitUnstructuredGridPiece.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkUnstructuredGridGhostCellsGenerator.h"
    "/home/fenics/shared/VTK/Filters/Parallel/vtkPExtractArraysOverTime.h"
    "/home/fenics/shared/VTK-build/Filters/Parallel/vtkFiltersParallelModule.h"
    )
endif()

