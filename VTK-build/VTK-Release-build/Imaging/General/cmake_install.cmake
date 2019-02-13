# Install script for directory: /home/fenics/shared/VTK/Imaging/General

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingGeneral-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingGeneral-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkImagingGeneral-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkImagingGeneral-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingGeneral-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingGeneral-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Imaging/General/CMakeFiles/vtkImagingGeneral.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Imaging/General/vtkImageAnisotropicDiffusion2D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageAnisotropicDiffusion3D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageCheckerboard.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageCityBlockDistance.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageConvolve.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageCorrelation.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageEuclideanDistance.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageEuclideanToPolar.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageGaussianSmooth.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageGradient.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageGradientMagnitude.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageHybridMedian2D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageLaplacian.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageMedian3D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageNormalize.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageRange3D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSeparableConvolution.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSobel2D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSobel3D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSpatialAlgorithm.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageVariance3D.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkSimpleImageFilterExample.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSlab.h"
    "/home/fenics/shared/VTK/Imaging/General/vtkImageSlabReslice.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Imaging/General/vtkImagingGeneralModule.h"
    )
endif()

