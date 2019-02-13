# Install script for directory: /home/fenics/shared/VTK/Filters/Modeling

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersModeling-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersModeling-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersModeling-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersModeling-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersModeling-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersModeling-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Modeling/CMakeFiles/vtkFiltersModeling.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Modeling/vtkAdaptiveSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkBandedPolyDataContourFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkButterflySubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkContourLoopExtraction.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkCookieCutter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkDijkstraGraphGeodesicPath.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkDijkstraImageGeodesicPath.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkFitToHeightMapFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkFillHolesFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkGeodesicPath.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkGraphGeodesicPath.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkLinearExtrusionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkLinearSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkLoopSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkOutlineFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkPolyDataPointSampler.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkProjectedTexture.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkQuadRotationalExtrusionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkRibbonFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkRotationalExtrusionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkRuledSurfaceFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSectorSource.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSelectEnclosedPoints.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSelectPolyData.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSpherePuzzleArrows.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSpherePuzzle.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkSubdivideTetra.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkTrimmedExtrusionFilter.h"
    "/home/fenics/shared/VTK/Filters/Modeling/vtkVolumeOfRevolutionFilter.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Modeling/vtkFiltersModelingModule.h"
    )
endif()

