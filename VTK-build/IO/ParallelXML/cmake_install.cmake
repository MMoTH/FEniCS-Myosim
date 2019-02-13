# Install script for directory: /home/fenics/shared/VTK/IO/ParallelXML

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOParallelXML-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOParallelXML-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkIOParallelXML-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkIOParallelXML-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOParallelXML-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOParallelXML-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/IO/ParallelXML/CMakeFiles/vtkIOParallelXML.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPDataSetWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPDataObjectWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPImageDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPPolyDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPRectilinearGridWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPStructuredDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPStructuredGridWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPTableWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPUnstructuredDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPUnstructuredGridWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPHierarchicalBoxDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPMultiBlockDataWriter.h"
    "/home/fenics/shared/VTK/IO/ParallelXML/vtkXMLPUniformGridAMRWriter.h"
    "/home/fenics/shared/VTK-build/IO/ParallelXML/vtkIOParallelXMLModule.h"
    )
endif()

