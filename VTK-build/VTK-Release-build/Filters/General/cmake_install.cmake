# Install script for directory: /home/fenics/shared/VTK/Filters/General

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeneral-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeneral-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersGeneral-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkFiltersGeneral-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeneral-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkFiltersGeneral-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/General/CMakeFiles/vtkFiltersGeneral.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Filters/General/vtkAnnotationLink.h"
    "/home/fenics/shared/VTK/Filters/General/vtkAppendPoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkApproximatingSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkAreaContourSpectrumFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkAxes.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBlankStructuredGrid.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBlankStructuredGridWithImage.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBlockIdScalars.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBoxClipDataSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBrownianPoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCellCenters.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCellDerivatives.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCellValidator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkClipClosedSurface.h"
    "/home/fenics/shared/VTK/Filters/General/vtkClipConvexPolyData.h"
    "/home/fenics/shared/VTK/Filters/General/vtkClipDataSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkClipVolume.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCoincidentPoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkContourTriangulator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCountFaces.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCountVertices.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCursor2D.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCursor3D.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCurvatures.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDataSetGradient.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDataSetGradientPrecompute.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDataSetTriangleFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDeformPointSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDensifyPolyData.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDicer.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDiscreteFlyingEdges2D.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDiscreteFlyingEdges3D.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDiscreteFlyingEdgesClipper2D.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDiscreteMarchingCubes.h"
    "/home/fenics/shared/VTK/Filters/General/vtkEdgePoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkExtractSelectedFrustum.h"
    "/home/fenics/shared/VTK/Filters/General/vtkExtractSelectionBase.h"
    "/home/fenics/shared/VTK/Filters/General/vtkGradientFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkGraphLayoutFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkGraphToPoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkHierarchicalDataLevelFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkHyperStreamline.h"
    "/home/fenics/shared/VTK/Filters/General/vtkIconGlyphFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkImageMarchingCubes.h"
    "/home/fenics/shared/VTK/Filters/General/vtkInterpolateDataSetAttributes.h"
    "/home/fenics/shared/VTK/Filters/General/vtkInterpolatingSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkLevelIdScalars.h"
    "/home/fenics/shared/VTK/Filters/General/vtkLinkEdgels.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMergeCells.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMultiBlockDataGroupFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMultiBlockFromTimeSeriesFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMultiBlockMergeFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMultiThreshold.h"
    "/home/fenics/shared/VTK/Filters/General/vtkOBBDicer.h"
    "/home/fenics/shared/VTK/Filters/General/vtkOBBTree.h"
    "/home/fenics/shared/VTK/Filters/General/vtkPassThrough.h"
    "/home/fenics/shared/VTK/Filters/General/vtkPointConnectivityFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkPolyDataStreamer.h"
    "/home/fenics/shared/VTK/Filters/General/vtkPolyDataToReebGraphFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkProbePolyhedron.h"
    "/home/fenics/shared/VTK/Filters/General/vtkQuadraturePointInterpolator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkQuadraturePointsGenerator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkQuadratureSchemeDictionaryGenerator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkQuantizePolyDataPoints.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRandomAttributeGenerator.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRectilinearGridClip.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRectilinearGridToTetrahedra.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRecursiveDividingCubes.h"
    "/home/fenics/shared/VTK/Filters/General/vtkReflectionFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRotationFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSampleImplicitFunctionFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkShrinkFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkShrinkPolyData.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSpatialRepresentationFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSplineFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSplitByCellScalarFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSplitField.h"
    "/home/fenics/shared/VTK/Filters/General/vtkStructuredGridClip.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSubdivisionFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSubPixelPositionEdgels.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSynchronizeTimeFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTableBasedClipDataSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTableToPolyData.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTableToStructuredGrid.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTemporalPathLineFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTemporalStatistics.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTessellatorFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTimeSourceExample.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTransformFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkTransformPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkUncertaintyTubeFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkVertexGlyphFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkVolumeContourSpectrumFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkVoxelContoursToSurfaceFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkWarpLens.h"
    "/home/fenics/shared/VTK/Filters/General/vtkWarpScalar.h"
    "/home/fenics/shared/VTK/Filters/General/vtkWarpTo.h"
    "/home/fenics/shared/VTK/Filters/General/vtkWarpVector.h"
    "/home/fenics/shared/VTK/Filters/General/vtkYoungsMaterialInterface.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMarchingContourFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkRectilinearGridToPointSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkGraphWeightEuclideanDistanceFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkGraphWeightFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkImageDataToPointSet.h"
    "/home/fenics/shared/VTK/Filters/General/vtkIntersectionPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkBooleanOperationPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkLoopBooleanPolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkDistancePolyDataFilter.h"
    "/home/fenics/shared/VTK/Filters/General/vtkOverlappingAMRLevelIdScalars.h"
    "/home/fenics/shared/VTK/Filters/General/vtkExtractArray.h"
    "/home/fenics/shared/VTK/Filters/General/vtkMatricizeArray.h"
    "/home/fenics/shared/VTK/Filters/General/vtkNormalizeMatrixVectors.h"
    "/home/fenics/shared/VTK/Filters/General/vtkPassArrays.h"
    "/home/fenics/shared/VTK/Filters/General/vtkSplitColumnComponents.h"
    "/home/fenics/shared/VTK/Filters/General/vtkCellTreeLocator.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Filters/General/vtkFiltersGeneralModule.h"
    )
endif()

