# Install script for directory: /home/fenics/shared/VTK/Filters/Statistics

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersStatistics-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersStatistics-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersStatistics-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersStatistics-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersStatistics-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersStatistics-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Filters/Statistics/CMakeFiles/vtkFiltersStatistics.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Statistics/vtkAutoCorrelativeStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkBivariateLinearTableThreshold.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkComputeQuartiles.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkContingencyStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkCorrelativeStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkDescriptiveStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkHighestDensityRegionsStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkExtractFunctionalBagPlot.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkKMeansDistanceFunctorCalculator.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkKMeansDistanceFunctor.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkKMeansStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkMultiCorrelativeStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkOrderStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkPCAStatistics.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkStatisticsAlgorithm.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkStrahlerMetric.h"
    "/home/fenics/shared/VTK/Filters/Statistics/vtkStreamingStatistics.h"
    "/home/fenics/shared/VTK-build/Filters/Statistics/vtkFiltersStatisticsModule.h"
    )
endif()

