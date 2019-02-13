# Install script for directory: /home/fenics/shared/VTK/IO/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkIOCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkIOCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkIOCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/IO/Core/CMakeFiles/vtkIOCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/IO/Core/vtkAbstractParticleWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkArrayReader.h"
    "/home/fenics/shared/VTK/IO/Core/vtkArrayWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkASCIITextCodec.h"
    "/home/fenics/shared/VTK/IO/Core/vtkBase64InputStream.h"
    "/home/fenics/shared/VTK/IO/Core/vtkBase64OutputStream.h"
    "/home/fenics/shared/VTK/IO/Core/vtkBase64Utilities.h"
    "/home/fenics/shared/VTK/IO/Core/vtkDataCompressor.h"
    "/home/fenics/shared/VTK/IO/Core/vtkDelimitedTextWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkGlobFileNames.h"
    "/home/fenics/shared/VTK/IO/Core/vtkInputStream.h"
    "/home/fenics/shared/VTK/IO/Core/vtkJavaScriptDataWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkLZ4DataCompressor.h"
    "/home/fenics/shared/VTK/IO/Core/vtkOutputStream.h"
    "/home/fenics/shared/VTK/IO/Core/vtkSortFileNames.h"
    "/home/fenics/shared/VTK/IO/Core/vtkTextCodec.h"
    "/home/fenics/shared/VTK/IO/Core/vtkTextCodecFactory.h"
    "/home/fenics/shared/VTK/IO/Core/vtkUTF16TextCodec.h"
    "/home/fenics/shared/VTK/IO/Core/vtkUTF8TextCodec.h"
    "/home/fenics/shared/VTK/IO/Core/vtkAbstractPolyDataReader.h"
    "/home/fenics/shared/VTK/IO/Core/vtkWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkZLibDataCompressor.h"
    "/home/fenics/shared/VTK/IO/Core/vtkArrayDataReader.h"
    "/home/fenics/shared/VTK/IO/Core/vtkArrayDataWriter.h"
    "/home/fenics/shared/VTK/IO/Core/vtkLZMADataCompressor.h"
    "/home/fenics/shared/VTK/IO/Core/vtkNumberToString.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/IO/Core/vtkIOCoreModule.h"
    )
endif()

