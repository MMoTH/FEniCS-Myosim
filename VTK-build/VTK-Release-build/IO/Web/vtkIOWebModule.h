
#ifndef VTKIOWEB_EXPORT_H
#define VTKIOWEB_EXPORT_H

#ifdef VTKIOWEB_STATIC_DEFINE
#  define VTKIOWEB_EXPORT
#  define VTKIOWEB_NO_EXPORT
#else
#  ifndef VTKIOWEB_EXPORT
#    ifdef vtkIOWeb_EXPORTS
        /* We are building this library */
#      define VTKIOWEB_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define VTKIOWEB_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef VTKIOWEB_NO_EXPORT
#    define VTKIOWEB_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef VTKIOWEB_DEPRECATED
#  define VTKIOWEB_DEPRECATED __attribute__ ((__deprecated__))
#  define VTKIOWEB_DEPRECATED_EXPORT VTKIOWEB_EXPORT __attribute__ ((__deprecated__))
#  define VTKIOWEB_DEPRECATED_NO_EXPORT VTKIOWEB_NO_EXPORT __attribute__ ((__deprecated__))
#endif

#define DEFINE_NO_DEPRECATED 0
#if DEFINE_NO_DEPRECATED
# define VTKIOWEB_NO_DEPRECATED
#endif

/* AutoInit dependencies.  */
#include "vtkIOExportModule.h"

#endif
