
#ifndef VTKTESTINGGENERICBRIDGE_EXPORT_H
#define VTKTESTINGGENERICBRIDGE_EXPORT_H

#ifdef VTKTESTINGGENERICBRIDGE_STATIC_DEFINE
#  define VTKTESTINGGENERICBRIDGE_EXPORT
#  define VTKTESTINGGENERICBRIDGE_NO_EXPORT
#else
#  ifndef VTKTESTINGGENERICBRIDGE_EXPORT
#    ifdef vtkTestingGenericBridge_EXPORTS
        /* We are building this library */
#      define VTKTESTINGGENERICBRIDGE_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define VTKTESTINGGENERICBRIDGE_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef VTKTESTINGGENERICBRIDGE_NO_EXPORT
#    define VTKTESTINGGENERICBRIDGE_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef VTKTESTINGGENERICBRIDGE_DEPRECATED
#  define VTKTESTINGGENERICBRIDGE_DEPRECATED __attribute__ ((__deprecated__))
#  define VTKTESTINGGENERICBRIDGE_DEPRECATED_EXPORT VTKTESTINGGENERICBRIDGE_EXPORT __attribute__ ((__deprecated__))
#  define VTKTESTINGGENERICBRIDGE_DEPRECATED_NO_EXPORT VTKTESTINGGENERICBRIDGE_NO_EXPORT __attribute__ ((__deprecated__))
#endif

#define DEFINE_NO_DEPRECATED 0
#if DEFINE_NO_DEPRECATED
# define VTKTESTINGGENERICBRIDGE_NO_DEPRECATED
#endif



#endif
