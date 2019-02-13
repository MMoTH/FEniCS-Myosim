# Install script for directory: /home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkhdf5-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkhdf5-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkhdf5-8.2.so.1"
    "/home/fenics/shared/VTK-build/VTK-Release-build/lib/libvtkhdf5-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkhdf5-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkhdf5-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2/vtkhdf5/src" TYPE FILE FILES
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/hdf5.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5api_adpt.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5public.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/vtk_hdf5_mangle.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Apkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Apublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5ACpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5ACpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Bpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Bpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5B2pkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5B2public.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Cpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Cpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Dpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Dpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Epkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Epublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5EApkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Fpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Fpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FApkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDcore.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDdirect.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDfamily.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDlog.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDmpi.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDmpio.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDmulti.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDsec2.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDstdio.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FDwindows.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FSpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5FSpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Gpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Gpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HFpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HFpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HGpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HGpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HLpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5HLpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Ipkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Ipublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Lpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Lpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5MMpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5MPpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Opkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Opublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Oshared.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Ppkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Ppublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5PBpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5PLextern.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5PLpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5PLpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Rpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Rpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Spkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Spublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5SMpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Tpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Tpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Zpkg.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Zpublic.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/vtk_hdf5_mangle.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Edefin.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Einit.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Epubgen.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5Eterm.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5version.h"
    "/home/fenics/shared/VTK/ThirdParty/hdf5/vtkhdf5/src/H5overflow.h"
    )
endif()

