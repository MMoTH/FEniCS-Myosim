# Install script for directory: /home/fenics/shared/VTK/Rendering/Volume

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingVolume-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingVolume-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingVolume-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkRenderingVolume-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingVolume-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingVolume-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Rendering/Volume/CMakeFiles/vtkRenderingVolume.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Rendering/Volume/vtkDirectionEncoder.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkEncodedGradientEstimator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkEncodedGradientShader.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFiniteDifferenceGradientEstimator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointRayCastImage.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastCompositeGOHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastCompositeGOShadeHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastCompositeHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastCompositeShadeHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastMIPHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkFixedPointVolumeRayCastMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkGPUVolumeRayCastMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkMultiVolume.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkOSPRayVolumeInterface.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkProjectedTetrahedraMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkRayCastImageDisplayHelper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkRecursiveSphereDirectionEncoder.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkSphericalDirectionEncoder.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridBunykRayCastFunction.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridHomogeneousRayIntegrator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridLinearRayIntegrator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridPartialPreIntegration.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridPreIntegration.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeRayCastFunction.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeRayCastIterator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeRayCastMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeRayIntegrator.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkUnstructuredGridVolumeZSweepMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkVolumeMapper.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkVolumeOutlineSource.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkVolumePicker.h"
    "/home/fenics/shared/VTK/Rendering/Volume/vtkVolumeRayCastSpaceLeapingImageFilter.h"
    "/home/fenics/shared/VTK-build/Rendering/Volume/vtkRenderingVolumeModule.h"
    )
endif()

