# Install script for directory: /home/fenics/shared/VTK/Filters/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Core/CMakeFiles/vtkFiltersCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/Core/vtkAppendArcLength.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAppendFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAppendPolyData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAppendSelection.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkArrayCalculator.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAssignAttribute.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAttributeDataToFieldDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkBinCellDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCellDataToPointData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCleanPolyData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkClipPolyData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCompositeDataProbeFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkConnectivityFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkContourFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkContourGrid.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkContourHelper.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkContour3DLinearGrid.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDataObjectGenerator.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDataObjectToDataSetFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDataSetEdgeSubdivisionCriterion.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDataSetToDataObjectFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDecimatePolylineFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDecimatePro.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDelaunay2D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkDelaunay3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkElevationFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkExecutionTimer.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkFeatureEdges.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkFieldDataToAttributeDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkFlyingEdges2D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkFlyingEdges3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkFlyingEdgesPlaneCutter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkGlyph2D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkGlyph3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkHedgeHog.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkHull.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkIdFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMarchingCubes.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMarchingSquares.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMaskFields.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMaskPoints.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMaskPolyData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMassProperties.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMergeDataObjectFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMergeFields.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMergeFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMoleculeAppend.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkMultiObjectMassProperties.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkPlaneCutter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkPointDataToCellData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkPolyDataConnectivityFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkPolyDataNormals.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkProbeFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkQuadricClustering.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkQuadricDecimation.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkRearrangeFields.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkRemoveDuplicatePolys.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkResampleToImage.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkResampleWithDataSet.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkReverseSense.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSimpleElevationFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSmoothPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSphereTreeFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStaticCleanPolyData.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStripper.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStructuredGridOutlineFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSynchronizedTemplates2D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSynchronizedTemplates3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkSynchronizedTemplatesCutter3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkTensorGlyph.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkThreshold.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkThresholdPoints.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkTransposeTable.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkTriangleFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkTriangleMeshPointNormals.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkTubeFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkUnstructuredGridQuadricDecimation.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkVectorDot.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkVectorNorm.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkVoronoi2D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkWindowedSincPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCutter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCompositeCutter.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkGridSynchronizedTemplates3D.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkRectilinearSynchronizedTemplates.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkEdgeSubdivisionCriterion.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStreamingTessellator.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkImplicitPolyDataDistance.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStreamerBase.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkCenterOfMass.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkImageAppend.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkStructuredGridAppend.h"
    "/home/fenics/shared/VTK/Filters/Core/vtkAppendCompositeDataLeaves.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/Core/vtkFiltersCoreModule.h"
    )
endif()

