# Install script for directory: /home/fenics/shared/VTK/Domains/Chemistry

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkDomainsChemistry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkDomainsChemistry-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkDomainsChemistry-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkDomainsChemistry-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkDomainsChemistry-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkDomainsChemistry-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Domains/Chemistry/CMakeFiles/vtkDomainsChemistry.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkBlueObeliskData.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkBlueObeliskDataInternal.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkBlueObeliskDataParser.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkCMLMoleculeReader.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkGaussianCubeReader2.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkMoleculeMapper.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkMoleculeToAtomBallFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkMoleculeToBondStickFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkMoleculeToLinesFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkMoleculeToPolyDataFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkPeriodicTable.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkPointSetToMoleculeFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkProgrammableElectronicData.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkProteinRibbonFilter.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkSimpleBondPerceiver.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkVASPAnimationReader.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkVASPTessellationReader.h"
    "/home/fenics/shared/VTK/Domains/Chemistry/vtkXYZMolReader2.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Domains/Chemistry/vtkDomainsChemistryModule.h"
    )
endif()

