# Install script for directory: /home/fenics/shared/VTK/Common/ComputationalGeometry

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonComputationalGeometry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonComputationalGeometry-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkCommonComputationalGeometry-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkCommonComputationalGeometry-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonComputationalGeometry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonComputationalGeometry-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Common/ComputationalGeometry/CMakeFiles/vtkCommonComputationalGeometry.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkCardinalSpline.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkKochanekSpline.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricBoy.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricConicSpiral.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricCrossCap.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricDini.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricEllipsoid.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricEnneper.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricFigure8Klein.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricFunction.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricKlein.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricMobius.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricRandomHills.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricRoman.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricSpline.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricSuperEllipsoid.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricSuperToroid.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricTorus.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricKuen.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricPseudosphere.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricBohemianDome.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricHenneberg.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricCatalanMinimal.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricBour.h"
    "/home/fenics/shared/VTK/Common/ComputationalGeometry/vtkParametricPluckerConoid.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Common/ComputationalGeometry/vtkCommonComputationalGeometryModule.h"
    )
endif()

