# Install script for directory: /home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu

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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2/vtklibharu/include" TYPE FILE FILES
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_types.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_consts.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_version.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_annotation.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_catalog.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_conf.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_destination.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_doc.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_encoder.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_encrypt.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_encryptdict.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_error.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_ext_gstate.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_font.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_fontdef.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_gstate.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_image.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_info.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_list.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_mmgr.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_objects.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_outline.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_pages.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_page_label.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_streams.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_u3d.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_utils.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_pdfa.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_3dmeasure.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/hpdf_exdata.h"
    "/home/fenics/shared/VTK/ThirdParty/libharu/vtklibharu/include/vtk_haru_mangle.h"
    "/home/fenics/shared/VTK-build/ThirdParty/libharu/vtklibharu/include/hpdf_config.h"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/fenics/shared/VTK-build/ThirdParty/libharu/vtklibharu/src/cmake_install.cmake")

endif()

