# Install script for directory: /home/fenics/shared/VTK/Interaction/Widgets

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInteractionWidgets-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInteractionWidgets-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkInteractionWidgets-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkInteractionWidgets-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInteractionWidgets-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkInteractionWidgets-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Interaction/Widgets/CMakeFiles/vtkInteractionWidgets.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Interaction/Widgets/vtk3DWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAbstractPolygonalHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAbstractWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAffineRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAffineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAffineWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAngleRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAngleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAngleRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAngleWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAxesTransformRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkAxesTransformWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBalloonRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBalloonWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBezierContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBiDimensionalRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBiDimensionalRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBiDimensionalWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBorderRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBorderWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBoundedPlanePointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBoxRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBoxWidget2.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBoxWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkBrokenLineWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkButtonRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkButtonWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCameraRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCameraWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCaptionRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCaptionWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCellCentersPointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCenteredSliderRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCenteredSliderWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCheckerboardRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCheckerboardWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkClosedSurfacePointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkConstrainedPointHandleRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkContinuousValueWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkContinuousValueWidgetRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkContourRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkContourWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkCurveRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkDijkstraImageContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkDistanceRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkDistanceRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkDistanceRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkDistanceWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkEllipsoidTensorProbeRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkEvent.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkFinitePlaneRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkFinitePlaneWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkFixedSizeHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkFocalPlaneContourRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkFocalPlanePointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkHandleRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkHandleWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkHoverWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImageActorPointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImageCroppingRegionsWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImageOrthoPlanes.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImagePlaneWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImageTracerWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImplicitCylinderRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImplicitCylinderWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImplicitPlaneRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImplicitPlaneWidget2.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkImplicitPlaneWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLinearContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLineWidget2.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLineWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLogoRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkLogoWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkMeasurementCubeHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkOrientationMarkerWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkOrientedGlyphContourRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkOrientedGlyphFocalPlaneContourRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkOrientedPolygonalHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkParallelopipedRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkParallelopipedWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPlaneWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPlaybackRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPlaybackWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPointHandleRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPointHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPointWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolyDataContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolyDataPointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolyDataSourceWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolyLineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolyLineWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolygonalHandleRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolygonalSurfaceContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkPolygonalSurfacePointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkProgressBarRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkProgressBarWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkProp3DButtonRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkRectilinearWipeRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkRectilinearWipeWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkScalarBarRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkScalarBarWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSeedRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSeedWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSliderRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSliderRepresentation3D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSliderRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSliderWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSphereHandleRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSphereRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSphereWidget2.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSphereWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSplineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSplineWidget2.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkSplineWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTensorProbeRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTensorProbeWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTerrainContourLineInterpolator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTerrainDataPointPlacer.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTextRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTexturedButtonRepresentation2D.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTexturedButtonRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkTextWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkWidgetCallbackMapper.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkWidgetEvent.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkWidgetEventTranslator.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkWidgetRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkWidgetSet.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkXYPlotWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorLineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorThickLineRepresentation.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorWidget.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorActor.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorPicker.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursor.h"
    "/home/fenics/shared/VTK/Interaction/Widgets/vtkResliceCursorPolyDataAlgorithm.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Interaction/Widgets/vtkInteractionWidgetsModule.h"
    )
endif()

