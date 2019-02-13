# Install script for directory: /home/fenics/shared/VTK/Filters/Sources

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersSources-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersSources-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersSources-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersSources-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersSources-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersSources-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Sources/CMakeFiles/vtkFiltersSources.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Sources/vtkArcSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkArrowSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkButtonSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkCellTypeSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkConeSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkCubeSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkCylinderSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkDiskSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkEllipseArcSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkEllipticalButtonSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkFrustumSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkGlyphSource2D.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkHyperTreeGridSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkLineSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkOutlineCornerFilter.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkOutlineCornerSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkOutlineSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkParametricFunctionSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkPlaneSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkPlatonicSolidSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkPointSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkPolyLineSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkProgrammableDataObjectSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkProgrammableSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkRandomHyperTreeGridSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkRectangularButtonSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkRegularPolygonSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkSelectionSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkSphereSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkSuperquadricSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkTessellatedBoxSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkTextSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkTexturedSphereSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkUniformHyperTreeGridSource.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkGraphToPolyData.h"
    "/home/fenics/shared/VTK/Filters/Sources/vtkDiagonalMatrixSource.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Sources/vtkFiltersSourcesModule.h"
    )
endif()

