# Install script for directory: /home/fenics/shared/VTK/Rendering/Annotation

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingAnnotation-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingAnnotation-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingAnnotation-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingAnnotation-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingAnnotation-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingAnnotation-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Rendering/Annotation/CMakeFiles/vtkRenderingAnnotation.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkScalarBarActorInternal.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkAnnotatedCubeActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkArcPlotter.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkAxesActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkAxisActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkAxisActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkAxisFollower.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkBarChartActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkCaptionActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkConvexHull2D.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkCornerAnnotation.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkCubeAxesActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkCubeAxesActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkGraphAnnotationLayersFilter.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkLeaderActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkLegendBoxActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkLegendScaleActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkParallelCoordinatesActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkPieChartActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkPolarAxesActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkProp3DAxisFollower.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkScalarBarActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkSpiderPlotActor.h"
    "/home/fenics/shared/VTK/Rendering/Annotation/vtkXYPlotActor.h"
    "/home/fenics/shared/VTK-build/Rendering/Annotation/vtkRenderingAnnotationModule.h"
    )
endif()

