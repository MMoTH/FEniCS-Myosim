# Install script for directory: /home/fenics/shared/VTK/Charts/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkChartsCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkChartsCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkChartsCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkChartsCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkChartsCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkChartsCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Charts/Core/CMakeFiles/vtkChartsCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Charts/Core/vtkAxis.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkAxisExtended.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkCategoryLegend.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChart.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartBox.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartHistogram2D.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartLegend.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartMatrix.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartParallelCoordinates.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartPie.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartXY.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkChartXYZ.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkColorLegend.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkColorTransferControlPointsItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkColorTransferFunctionItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkCompositeControlPointsItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkCompositeTransferFunctionItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkContextArea.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkContextPolygon.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkControlPointsItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkInteractiveArea.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkLookupTableItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPiecewiseControlPointsItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPiecewiseFunctionItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPiecewisePointHandleItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlot.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlot3D.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotArea.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotBag.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotBar.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotBox.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotFunctionalBag.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotGrid.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotHistogram2D.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotLine.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotLine3D.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotParallelCoordinates.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotPie.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotPoints.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotPoints3D.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotStacked.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkPlotSurface.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkScalarsToColorsItem.h"
    "/home/fenics/shared/VTK/Charts/Core/vtkScatterPlotMatrix.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Charts/Core/vtkChartsCoreModule.h"
    )
endif()

