# Install script for directory: /home/fenics/shared/VTK/Filters/Hybrid

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersHybrid-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersHybrid-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersHybrid-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersHybrid-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersHybrid-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersHybrid-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Hybrid/CMakeFiles/vtkFiltersHybrid.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkAdaptiveDataSetSurfaceFilter.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkBSplineTransform.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkDepthSortPolyData.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkDSPFilterDefinition.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkDSPFilterGroup.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkEarthSource.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkFacetReader.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkForceTime.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkGreedyTerrainDecimation.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkGridTransform.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkImageToPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkImplicitModeller.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkPCAAnalysisFilter.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkPolyDataSilhouette.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkProcrustesAlignmentFilter.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkProjectedTerrainPath.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkRenderLargeImage.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalArrayOperatorFilter.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalDataSetCache.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalFractal.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalInterpolator.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalShiftScale.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTemporalSnapToTimeStep.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkTransformToGrid.h"
    "/home/fenics/shared/VTK/Filters/Hybrid/vtkWeightedTransformFilter.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Hybrid/vtkFiltersHybridModule.h"
    )
endif()

