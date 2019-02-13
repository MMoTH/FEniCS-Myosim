# Install script for directory: /home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkfreetype-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkfreetype-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkfreetype-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkfreetype-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkfreetype-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkfreetype-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2/vtkfreetype/include" TYPE FILE FILES
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/ft2build.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/vtk_freetype_mangle.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/vtk_ftmodule.h"
    "/home/fenics/shared/VTK-build/ThirdParty/freetype/vtkfreetype/include/vtkFreeTypeConfig.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2/vtkfreetype/include/freetype" TYPE FILE FILES
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftmodapi.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftcid.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/t1tables.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftmac.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftsizes.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ttnameid.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/tttags.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftbitmap.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftsystem.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftxf86.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/fttypes.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftmoderr.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/fterrdef.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftgzip.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftincrem.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftstroke.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftlcdfil.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftbbox.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftgxval.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftsnames.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftgasp.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/fttrigon.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftbdf.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/tttables.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftwinfnt.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftsynth.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftpfr.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftcache.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftimage.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftlist.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftlzw.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftchapters.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftrender.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftglyph.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftotval.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/freetype.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftoutln.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ttunpat.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftadvanc.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftbzip2.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/ftmm.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/fterrors.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2/vtkfreetype/include/freetype/config" TYPE FILE FILES
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/config/ftoption.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/config/ftstdlib.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/config/ftheader.h"
    "/home/fenics/shared/VTK/ThirdParty/freetype/vtkfreetype/include/freetype/config/ftmodule.h"
    "/home/fenics/shared/VTK-build/ThirdParty/freetype/vtkfreetype/include/freetype/config/ftconfig.h"
    )
endif()

