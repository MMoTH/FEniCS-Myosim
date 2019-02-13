# Install script for directory: /home/fenics/shared/VTK/Filters/Points

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersPoints-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersPoints-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersPoints-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkFiltersPoints-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersPoints-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersPoints-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Filters/Points/CMakeFiles/vtkFiltersPoints.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Points/vtkBoundedPointSource.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkConnectedPointsFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkDensifyPointCloudFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkEllipsoidalGaussianKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkEuclideanClusterExtraction.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkExtractHierarchicalBins.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkExtractEnclosedPoints.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkExtractPointCloudPiece.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkExtractPoints.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkExtractSurface.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkFitImplicitFunction.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkGaussianKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkGeneralizedKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkHierarchicalBinningFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkInterpolationKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkLinearKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkMaskPointsFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPCACurvatureEstimation.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPCANormalEstimation.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPointCloudFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPointDensityFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPointInterpolator.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPointInterpolator2D.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkPointOccupancyFilter.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkProbabilisticVoronoiKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkRadiusOutlierRemoval.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSPHInterpolator.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSPHCubicKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSPHKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSPHQuarticKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSPHQuinticKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkShepardKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkSignedDistance.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkStatisticalOutlierRemoval.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkUnsignedDistance.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkVoxelGrid.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkVoronoiKernel.h"
    "/home/fenics/shared/VTK/Filters/Points/vtkWendlandQuinticKernel.h"
    "/home/fenics/shared/VTK-build/Filters/Points/vtkFiltersPointsModule.h"
    )
endif()

