# Install script for directory: /home/fenics/shared/VTK/Rendering/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkRenderingCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkRenderingCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/Core/CMakeFiles/vtkRenderingCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Rendering/Core/vtkGPUInfoListArray.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkNoise200x200.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPythagoreanQuadruples.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRayCastStructures.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderingCoreEnums.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTDxMotionEventInfo.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractMapper3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractVolumeMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkActor2DCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkActorCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkActor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAssembly.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAvatar.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkBackgroundColorMonitor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkBillboardTextActor3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCameraActor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCamera.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCameraInterpolator.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCellCenterDepthSort.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCIEDE2000.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkColorTransferFunction.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCompositeDataDisplayAttributes.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCompositeDataDisplayAttributesLegacy.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCompositePolyDataMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCoordinate.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCullerCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCuller.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkDataSetMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkDiscretizableColorTransferFunction.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkDistanceToCamera.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkFollower.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkFrameBufferObjectBase.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkFrustumCoverageCuller.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkFXAAOptions.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGenericRenderWindowInteractor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGenericVertexAttributeMapping.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGlyph3DMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGPUInfo.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGPUInfoList.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGraphicsFactory.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGraphMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkGraphToGlyphs.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkHardwareSelector.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkHierarchicalPolyDataMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageActor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageMapper3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageProperty.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageSlice.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkImageSliceMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkInteractorEventRecorder.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkInteractorObserver.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLabeledContourMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLightActor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLightCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLight.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLightKit.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLogLookupTable.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLookupTableWithEnabling.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkMapArrayValues.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkMapper2D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkMapperCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkObserverMediator.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPointGaussianMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPolyDataMapper2D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPolyDataMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProp3DCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProp3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProp3DFollower.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPropAssembly.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPropCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProp.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProperty2D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkProperty.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRendererCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderer.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRendererDelegate.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRendererSource.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderPass.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderState.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderTimerLog.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderWindowCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderWindow.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderWindowInteractor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderWindowInteractor3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkSelectVisiblePoints.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkShaderDeviceAdapter2.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkSkybox.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextActor.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextActor3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTexture.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTexturedActor2D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTransformCoordinateSystems.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTransformInterpolator.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTupleInterpolator.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkViewDependentErrorMetric.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkViewport.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkVisibilitySort.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkVolumeCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkVolume.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkVolumeProperty.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkWindowLevelLookupTable.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkWindowToImageFilter.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAssemblyNode.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAssemblyPath.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAssemblyPaths.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAreaPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractPropPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPropPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPickingManager.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkLODProp3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkWorldPointPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkCellPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkPointPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderedAreaPicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkScenePicker.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkInteractorStyle.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkInteractorStyleSwitchBase.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkInteractorStyle3D.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTDxInteractorStyle.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTDxInteractorStyleCamera.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTDxInteractorStyleSettings.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkStringToImage.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextMapper.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextProperty.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextPropertyCollection.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkTextRenderer.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractInteractionDevice.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkAbstractRenderDevice.h"
    "/home/fenics/shared/VTK/Rendering/Core/vtkRenderWidget.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/Core/vtkRenderingCoreModule.h"
    )
endif()

