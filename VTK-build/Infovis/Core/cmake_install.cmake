# Install script for directory: /home/fenics/shared/VTK/Infovis/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInfovisCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInfovisCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkInfovisCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkInfovisCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInfovisCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInfovisCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Infovis/Core/CMakeFiles/vtkInfovisCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Infovis/Core/vtkAddMembershipArray.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkAdjacencyMatrixToEdgeTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkArrayNorm.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkArrayToTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkCollapseGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkCollapseVerticesByArray.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkContinuousScatterplot.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkDataObjectToTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkDotProductSimilarity.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkExtractSelectedTree.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkEdgeCenters.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkExpandSelectedGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkExtractSelectedGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkGenerateIndexArray.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkGraphHierarchicalBundleEdges.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkGroupLeafVertices.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkMergeColumns.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkMergeGraphs.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkMergeTables.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkMutableGraphHelper.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkNetworkHierarchy.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkPipelineGraphSource.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkPruneTreeFilter.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkRandomGraphSource.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkReduceTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkRemoveIsolatedVertices.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkSparseArrayToTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkStreamGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkStringToCategory.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkStringToNumeric.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTableToArray.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTableToGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTableToSparseArray.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTableToTreeFilter.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkThresholdGraph.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkThresholdTable.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTransferAttributes.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTransposeMatrix.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTreeFieldAggregator.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTreeDifferenceFilter.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkTreeLevelsFilter.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkVertexDegree.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkRemoveHiddenData.h"
    "/home/fenics/shared/VTK/Infovis/Core/vtkKCoreDecomposition.h"
    "/home/fenics/shared/VTK-build/Infovis/Core/vtkInfovisCoreModule.h"
    )
endif()

