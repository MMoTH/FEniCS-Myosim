# Install script for directory: /home/fenics/shared/VTK/Common/Transforms

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonTransforms-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonTransforms-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkCommonTransforms-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkCommonTransforms-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonTransforms-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonTransforms-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Common/Transforms/CMakeFiles/vtkCommonTransforms.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Common/Transforms/vtkAbstractTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkCylindricalTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkGeneralTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkHomogeneousTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkIdentityTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkLinearTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkMatrixToHomogeneousTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkMatrixToLinearTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkPerspectiveTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkSphericalTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkThinPlateSplineTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkTransform2D.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkTransformCollection.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkWarpTransform.h"
    "/home/fenics/shared/VTK/Common/Transforms/vtkLandmarkTransform.h"
    "/home/fenics/shared/VTK-build/Common/Transforms/vtkCommonTransformsModule.h"
    )
endif()

