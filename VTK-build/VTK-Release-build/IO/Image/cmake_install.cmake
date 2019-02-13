# Install script for directory: /home/fenics/shared/VTK/IO/Image

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOImage-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOImage-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkIOImage-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkIOImage-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOImage-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOImage-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/IO/Image/CMakeFiles/vtkIOImage.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/IO/Image/vtkBMPReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkBMPWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkDEMReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkDICOMImageReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkGESignaReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageExport.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageImport.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageImportExecutive.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageReader2.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageReader2Collection.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageReader2Factory.h"
    "/home/fenics/shared/VTK/IO/Image/vtkImageWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkJPEGReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkJPEGWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkJSONImageWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkMedicalImageProperties.h"
    "/home/fenics/shared/VTK/IO/Image/vtkMedicalImageReader2.h"
    "/home/fenics/shared/VTK/IO/Image/vtkMetaImageReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkMetaImageWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkMRCReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkNIFTIImageHeader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkNIFTIImageReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkNIFTIImageWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkNrrdReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkPNGReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkPNGWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkPNMReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkPNMWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkPostScriptWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkSEPReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkSLCReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkTIFFReader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkTIFFWriter.h"
    "/home/fenics/shared/VTK/IO/Image/vtkVolume16Reader.h"
    "/home/fenics/shared/VTK/IO/Image/vtkVolumeReader.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/IO/Image/vtkIOImageModule.h"
    )
endif()

