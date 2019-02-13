# Install script for directory: /home/fenics/shared/VTK/Filters/Geometry

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeometry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeometry-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersGeometry-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersGeometry-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeometry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeometry-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Geometry/CMakeFiles/vtkFiltersGeometry.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Geometry/vtkCompositeDataGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkHierarchicalDataSetGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkImageDataGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkImageDataToUniformGrid.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkLinearToQuadraticCellsFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkProjectSphereFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkRectilinearGridGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredGridGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredPointsGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkUnstructuredGridGeometryFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkDataSetSurfaceFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkDataSetRegionSurfaceFilter.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkAbstractGridConnectivity.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkDataSetGhostGenerator.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkRectilinearGridPartitioner.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredAMRNeighbor.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredAMRGridConnectivity.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredGridConnectivity.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredGridGhostDataGenerator.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredGridPartitioner.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkStructuredNeighbor.h"
    "/home/fenics/shared/VTK/Filters/Geometry/vtkUniformGridGhostDataGenerator.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Geometry/vtkFiltersGeometryModule.h"
    )
endif()

