# Install script for directory: /home/fenics/shared/VTK/Rendering/Context2D

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingContext2D-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingContext2D-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingContext2D-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingContext2D-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingContext2D-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingContext2D-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Rendering/Context2D/CMakeFiles/vtkRenderingContext2D.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkAbstractContextBufferId.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkAbstractContextItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkBlockItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkBrush.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContext2D.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContext3D.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextActor.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextClip.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextDevice2D.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextDevice3D.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextKeyEvent.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextMapper2D.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextMouseEvent.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextScene.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkContextTransform.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkImageItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkMarkerUtilities.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkLabeledContourPolyDataItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkPen.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkPolyDataItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkPropItem.h"
    "/home/fenics/shared/VTK/Rendering/Context2D/vtkTooltipItem.h"
    "/home/fenics/shared/VTK-build/Rendering/Context2D/vtkRenderingContext2DModule.h"
    )
endif()

