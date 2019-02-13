# Install script for directory: /home/fenics/shared/VTK/IO/Legacy

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOLegacy-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOLegacy-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkIOLegacy-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkIOLegacy-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOLegacy-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOLegacy-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/IO/Legacy/CMakeFiles/vtkIOLegacy.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/IO/Legacy/vtkCompositeDataReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkCompositeDataWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataObjectReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataObjectWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataSetReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataSetWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkDataWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkGenericDataObjectReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkGenericDataObjectWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkGraphReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkGraphWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkPixelExtentIO.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkPolyDataReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkPolyDataWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkRectilinearGridReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkRectilinearGridWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkSimplePointsReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkSimplePointsWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkStructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkStructuredGridWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkStructuredPointsReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkStructuredPointsWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkTableReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkTableWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkTreeReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkTreeWriter.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkUnstructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/Legacy/vtkUnstructuredGridWriter.h"
    "/home/fenics/shared/VTK-build/IO/Legacy/vtkIOLegacyModule.h"
    )
endif()

