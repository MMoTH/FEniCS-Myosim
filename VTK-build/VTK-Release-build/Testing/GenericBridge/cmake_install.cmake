# Install script for directory: /home/fenics/shared/VTK/Testing/GenericBridge

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkTestingGenericBridge-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkTestingGenericBridge-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkTestingGenericBridge-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkTestingGenericBridge-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkTestingGenericBridge-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkTestingGenericBridge-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/GenericBridge/CMakeFiles/vtkTestingGenericBridge.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeAttribute.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCell.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIterator.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIteratorOnCellBoundaries.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIteratorOnCellList.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIteratorOnDataSet.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIteratorOne.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeCellIteratorStrategy.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeDataSet.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgeExport.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgePointIterator.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgePointIteratorOnCell.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgePointIteratorOnDataSet.h"
    "/home/fenics/shared/VTK/Testing/GenericBridge/vtkBridgePointIteratorOne.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/GenericBridge/vtkTestingGenericBridgeModule.h"
    )
endif()

