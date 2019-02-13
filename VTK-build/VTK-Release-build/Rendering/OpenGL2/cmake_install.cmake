# Install script for directory: /home/fenics/shared/VTK/Rendering/OpenGL2

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingOpenGL2-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingOpenGL2-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkRenderingOpenGL2-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkRenderingOpenGL2-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingOpenGL2-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkRenderingOpenGL2-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/CMakeFiles/vtkRenderingOpenGL2.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGL.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkStateStorage.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/vtkTDxConfigure.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/vtkOpenGLError.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/vtkRenderingOpenGLConfigure.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/vtkRenderingOpenGL2ObjectFactory.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkCameraPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkClearRGBPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkClearZPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkCompositePolyDataMapper2.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDefaultPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDepthOfFieldPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDepthImageProcessingPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDepthPeelingPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDualDepthPeelingPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkEDLShading.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkFramebufferPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkGaussianBlurPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkGenericOpenGLRenderWindow.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkHiddenLineRemovalPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkImageProcessingPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkLightingMapPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkLightsPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpaquePass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLActor.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLBillboardTextActor3D.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLBufferObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLCamera.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLFXAAFilter.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLFramebufferObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLGL2PSHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLGlyph3DHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLGlyph3DMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLHardwareSelector.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLImageAlgorithmHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLImageMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLImageSliceMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLIndexBufferObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLInstanceCulling.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLLabeledContourMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLLight.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLPointGaussianMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLPolyDataMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLPolyDataMapper2D.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLProperty.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLQuadHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderTimer.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderTimerLog.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderUtilities.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderWindow.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLRenderer.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLShaderCache.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLSkybox.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLSphereMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLState.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLStickMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLTextActor.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLTextActor3D.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLTextMapper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLTexture.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLVertexArrayObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLVertexBufferObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLVertexBufferObjectCache.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOpenGLVertexBufferObjectGroup.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOrderIndependentTranslucentPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkOverlayPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkPanoramicProjectionPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkPixelBufferObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkPointFillPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkRenderPassCollection.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkRenderStepsPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkRenderbuffer.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkSSAAPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkSequencePass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkShader.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkShaderProgram.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkShadowMapBakerPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkShadowMapPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkSimpleMotionBlurPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkSobelGradientMagnitudePass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkTextureObject.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkTextureUnitManager.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkToneMappingPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkTransformFeedback.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkTranslucentPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkValuePass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkVolumetricPass.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDataTransferHelper.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkDummyGPUInfoList.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkXRenderWindowInteractor.h"
    "/home/fenics/shared/VTK/Rendering/OpenGL2/vtkXOpenGLRenderWindow.h"
    "/home/fenics/shared/VTK-build/VTK-Release-build/Rendering/OpenGL2/vtkRenderingOpenGL2Module.h"
    )
endif()

