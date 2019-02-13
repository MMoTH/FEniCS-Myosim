# Install script for directory: /home/fenics/shared/VTK/IO/XML

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOXML-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOXML-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkIOXML-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkIOXML-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOXML-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOXML-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/IO/XML/CMakeFiles/vtkIOXML.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/IO/XML/vtkRTXMLPolyDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLCompositeDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLCompositeDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLDataSetWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLDataObjectWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLFileReadTester.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLGenericDataObjectReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHierarchicalBoxDataFileConverter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHierarchicalBoxDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHierarchicalBoxDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHierarchicalDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHyperTreeGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLHyperTreeGridWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLImageDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLImageDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLMultiBlockDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLMultiBlockDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLMultiGroupDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPDataObjectReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPImageDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPolyDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPolyDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPPolyDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPRectilinearGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPStructuredDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPStructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPTableReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPUnstructuredDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPUnstructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPartitionedDataSetReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPartitionedDataSetWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPartitionedDataSetCollectionReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLPartitionedDataSetCollectionWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLRectilinearGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLRectilinearGridWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLStructuredDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLStructuredDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLStructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLStructuredGridWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLTableReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLTableWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUniformGridAMRReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUniformGridAMRWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUnstructuredDataReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUnstructuredDataWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUnstructuredGridReader.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLUnstructuredGridWriter.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLWriterC.h"
    "/home/fenics/shared/VTK/IO/XML/vtkXMLWriter.h"
    "/home/fenics/shared/VTK-build/IO/XML/vtkIOXMLModule.h"
    )
endif()

