# Install script for directory: /home/fenics/shared/VTK/Imaging/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkImagingCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkImagingCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkImagingCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Imaging/Core/CMakeFiles/vtkImagingCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Imaging/Core/vtkExtractVOI.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageAppendComponents.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageBlend.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageCacheFilter.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageCast.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageChangeInformation.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageClip.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageConstantPad.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageDataStreamer.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageDecomposeFilter.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageDifference.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageExtractComponents.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageFlip.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageIterateFilter.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageMagnify.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageMapToColors.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageMask.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageMirrorPad.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImagePadFilter.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImagePermute.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImagePointDataIterator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImagePointIterator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageResample.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageReslice.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageResliceToColors.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageShiftScale.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageShrink3D.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageStencilIterator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageThreshold.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageTranslateExtent.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageWrapPad.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkRTAnalyticSource.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageResize.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageBSplineCoefficients.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageStencilData.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageStencilAlgorithm.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkAbstractImageInterpolator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageBSplineInternals.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageBSplineInterpolator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageSincInterpolator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageInterpolator.h"
    "/home/fenics/shared/VTK/Imaging/Core/vtkImageStencilSource.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Imaging/Core/vtkImagingCoreModule.h"
    )
endif()

