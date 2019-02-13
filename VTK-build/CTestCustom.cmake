SET(CTEST_CUSTOM_MEMCHECK_IGNORE
  ${CTEST_CUSTOM_MEMCHECK_IGNORE}
  Example-vtkLocal
  Example-vtkMy

  # These tests do not run any VTK code
  vtkAcceleratorsVTKm-HeaderTest
  vtkAcceleratorsVTKm-Test-Cxx-HeaderTest
  vtkInfovisBoostGraphAlgorithms-HeaderTest
  vtkInfovisBoostGraphAlgorithms-Test-Cxx-HeaderTest
  vtkInfovisLayout-HeaderTest
  vtkInfovisLayout-Test-Cxx-HeaderTest
  vtkInfovisCore-HeaderTest
  vtkInfovisCore-Test-Cxx-HeaderTest
  vtkInfovisBoost-HeaderTest
  vtkInfovisBoost-Test-Cxx-HeaderTest
  vtkWebPython-HeaderTest
  vtkWebGLExporter-HeaderTest
  vtkWebCore-HeaderTest
  vtkRenderingSceneGraph-HeaderTest
  vtkRenderingSceneGraph-Test-Cxx-HeaderTest
  vtkRenderingImage-HeaderTest
  vtkRenderingImage-Test-Cxx-HeaderTest
  vtkRenderingVolume-HeaderTest
  vtkRenderingVolume-Test-Cxx-HeaderTest
  vtkRenderingOSPRay-HeaderTest
  vtkRenderingOSPRay-Test-Cxx-HeaderTest
  vtkRenderingTk-HeaderTest
  vtkRenderingOpenGL2-HeaderTest
  vtkRenderingOpenGL2-Test-Cxx-HeaderTest
  vtkRenderingOpenVR-HeaderTest
  vtkRenderingOpenVR-Test-Cxx-HeaderTest
  vtkRenderingGL2PSOpenGL2-HeaderTest
  vtkRenderingGL2PSOpenGL2-Test-Cxx-HeaderTest
  vtkRenderingParallel-HeaderTest
  vtkRenderingParallel-Test-Cxx-HeaderTest
  vtkRenderingParallelLIC-HeaderTest
  vtkRenderingLOD-HeaderTest
  vtkRenderingLOD-Test-Cxx-HeaderTest
  vtkRenderingOptiX-HeaderTest
  vtkRenderingOptiX-Test-Cxx-HeaderTest
  vtkRenderingLICOpenGL2-HeaderTest
  vtkRenderingLICOpenGL2-Test-Cxx-HeaderTest
  vtkRenderingFreeTypeFontConfig-HeaderTest
  vtkRenderingFreeTypeFontConfig-Test-Cxx-HeaderTest
  vtkRenderingContext2D-HeaderTest
  vtkRenderingContext2D-Test-Cxx-HeaderTest
  vtkRenderingQt-HeaderTest
  vtkRenderingFreeType-HeaderTest
  vtkRenderingFreeType-Test-Cxx-HeaderTest
  vtkRenderingExternal-HeaderTest
  vtkRenderingExternal-Test-Cxx-HeaderTest
  vtkRenderingAnnotation-HeaderTest
  vtkRenderingAnnotation-Test-Cxx-HeaderTest
  vtkRenderingContextOpenGL2-HeaderTest
  vtkRenderingCore-HeaderTest
  vtkRenderingCore-Test-Cxx-HeaderTest
  vtkRenderingVolumeAMR-HeaderTest
  vtkRenderingLabel-HeaderTest
  vtkRenderingLabel-Test-Cxx-HeaderTest
  vtkRenderingVolumeOpenGL2-HeaderTest
  vtkRenderingVolumeOpenGL2-Test-Cxx-HeaderTest
  vtkRenderingMatplotlib-HeaderTest
  vtkRenderingMatplotlib-Test-Cxx-HeaderTest
  vtkFiltersHybrid-HeaderTest
  vtkFiltersHybrid-Test-Cxx-HeaderTest
  vtkFiltersGeneral-HeaderTest
  vtkFiltersGeneral-Test-Cxx-HeaderTest
  vtkFiltersAMR-HeaderTest
  vtkFiltersAMR-Test-Cxx-HeaderTest
  vtkFiltersModeling-HeaderTest
  vtkFiltersModeling-Test-Cxx-HeaderTest
  vtkFiltersGeometry-HeaderTest
  vtkFiltersGeometry-Test-Cxx-HeaderTest
  vtkFiltersSMP-HeaderTest
  vtkFiltersSMP-Test-Cxx-HeaderTest
  vtkFiltersParallelDIY2-HeaderTest
  vtkFiltersParallelDIY2-Test-Cxx-HeaderTest
  vtkFiltersTopology-HeaderTest
  vtkFiltersTopology-Test-Cxx-HeaderTest
  vtkFiltersReebGraph-HeaderTest
  vtkFiltersReebGraph-Test-Cxx-HeaderTest
  vtkFiltersParallel-HeaderTest
  vtkFiltersParallel-Test-Cxx-HeaderTest
  vtkFiltersParallelVerdict-HeaderTest
  vtkFiltersParallelVerdict-Test-Cxx-HeaderTest
  vtkFiltersVerdict-HeaderTest
  vtkFiltersVerdict-Test-Cxx-HeaderTest
  vtkFiltersExtraction-HeaderTest
  vtkFiltersExtraction-Test-Cxx-HeaderTest
  vtkFiltersFlowPaths-HeaderTest
  vtkFiltersFlowPaths-Test-Cxx-HeaderTest
  vtkFiltersImaging-HeaderTest
  vtkFiltersTexture-HeaderTest
  vtkFiltersTexture-Test-Cxx-HeaderTest
  vtkFiltersParallelGeometry-HeaderTest
  vtkFiltersParallelGeometry-Test-Cxx-HeaderTest
  vtkFiltersParallelImaging-HeaderTest
  vtkFiltersStatistics-HeaderTest
  vtkFiltersStatistics-Test-Cxx-HeaderTest
  vtkFiltersSources-HeaderTest
  vtkFiltersSources-Test-Cxx-HeaderTest
  vtkFiltersParallelMPI-HeaderTest
  vtkFiltersParallelMPI-Test-Cxx-HeaderTest
  vtkFiltersHyperTree-HeaderTest
  vtkFiltersHyperTree-Test-Cxx-HeaderTest
  vtkFiltersGeneric-HeaderTest
  vtkFiltersGeneric-Test-Cxx-HeaderTest
  vtkFiltersProgrammable-HeaderTest
  vtkFiltersProgrammable-Test-Cxx-HeaderTest
  vtkFiltersCore-HeaderTest
  vtkFiltersCore-Test-Cxx-HeaderTest
  vtkFiltersSelection-HeaderTest
  vtkFiltersSelection-Test-Cxx-HeaderTest
  vtkFiltersParallelFlowPaths-HeaderTest
  vtkFiltersParallelFlowPaths-Test-Cxx-HeaderTest
  vtkFiltersOpenTurns-HeaderTest
  vtkFiltersOpenTurns-Test-Cxx-HeaderTest
  vtkFiltersPoints-HeaderTest
  vtkFiltersPoints-Test-Cxx-HeaderTest
  vtkFiltersParallelStatistics-HeaderTest
  vtkFiltersParallelStatistics-Test-Cxx-HeaderTest
  vtkParallelMPI-HeaderTest
  vtkParallelMPI-Test-Cxx-HeaderTest
  vtkParallelCore-HeaderTest
  vtkParallelCore-Test-Cxx-HeaderTest
  vtkViewsInfovis-HeaderTest
  vtkViewsInfovis-Test-Cxx-HeaderTest
  vtkViewsGeovis-HeaderTest
  vtkViewsContext2D-HeaderTest
  vtkViewsQt-HeaderTest
  vtkViewsCore-HeaderTest
  vtkChartsCore-HeaderTest
  vtkChartsCore-Test-Cxx-HeaderTest
  vtkGeovisGDAL-HeaderTest
  vtkGeovisGDAL-Test-Cxx-HeaderTest
  vtkGeovisCore-HeaderTest
  vtkGeovisCore-Test-Cxx-HeaderTest
  vtkImagingHybrid-HeaderTest
  vtkImagingHybrid-Test-Cxx-HeaderTest
  vtkImagingGeneral-HeaderTest
  vtkImagingFourier-HeaderTest
  vtkImagingOpenGL2-HeaderTest
  vtkImagingOpenGL2-Test-Cxx-HeaderTest
  vtkImagingColor-HeaderTest
  vtkImagingColor-Test-Cxx-HeaderTest
  vtkImagingStatistics-HeaderTest
  vtkImagingMath-HeaderTest
  vtkImagingStencil-HeaderTest
  vtkImagingSources-HeaderTest
  vtkImagingMorphological-HeaderTest
  vtkImagingMorphological-Test-Cxx-HeaderTest
  vtkImagingCore-HeaderTest
  vtkImagingCore-Test-Cxx-HeaderTest
  vtkTestingIOSQL-HeaderTest
  vtkTestingRendering-HeaderTest
  vtkTestingGenericBridge-HeaderTest
  vtkTestingCore-HeaderTest
  vtkCommonDataModel-HeaderTest
  vtkCommonDataModel-Test-Cxx-HeaderTest
  vtkCommonTransforms-HeaderTest
  vtkCommonTransforms-Test-Cxx-HeaderTest
  vtkCommonColor-HeaderTest
  vtkCommonColor-Test-Cxx-HeaderTest
  vtkCommonMath-HeaderTest
  vtkCommonMath-Test-Cxx-HeaderTest
  vtkCommonExecutionModel-HeaderTest
  vtkCommonExecutionModel-Test-Cxx-HeaderTest
  vtkCommonCore-HeaderTest
  vtkCommonCore-Test-Cxx-HeaderTest
  vtkCommonSystem-HeaderTest
  vtkCommonSystem-Test-Cxx-HeaderTest
  vtkCommonMisc-HeaderTest
  vtkCommonMisc-Test-Cxx-HeaderTest
  vtkCommonComputationalGeometry-HeaderTest
  vtkCommonComputationalGeometry-Test-Cxx-HeaderTest
  vtkWrappingTools-HeaderTest
  vtkWrappingJava-HeaderTest
  vtkWrappingPythonCore-HeaderTest
  vtkIOFFMPEG-HeaderTest
  vtkIOFFMPEG-Test-Cxx-HeaderTest
  vtkIOImport-HeaderTest
  vtkIOImport-Test-Cxx-HeaderTest
  vtkIOGDAL-HeaderTest
  vtkIOGDAL-Test-Cxx-HeaderTest
  vtkIOInfovis-HeaderTest
  vtkIOInfovis-Test-Cxx-HeaderTest
  vtkIOAMR-HeaderTest
  vtkIOAMR-Test-Cxx-HeaderTest
  vtkIOImage-HeaderTest
  vtkIOImage-Test-Cxx-HeaderTest
  vtkIOLegacy-HeaderTest
  vtkIOLegacy-Test-Cxx-HeaderTest
  vtkIOGeometry-HeaderTest
  vtkIOGeometry-Test-Cxx-HeaderTest
  vtkIOWeb-HeaderTest
  vtkIOMINC-HeaderTest
  vtkIOExport-HeaderTest
  vtkIOExport-Test-Cxx-HeaderTest
  vtkIOParallelXdmf3-HeaderTest
  vtkIOParallelXdmf3-Test-Cxx-HeaderTest
  vtkIOParallelLSDyna-HeaderTest
  vtkIOParallelLSDyna-Test-Cxx-HeaderTest
  vtkIOExodus-HeaderTest
  vtkIOExodus-Test-Cxx-HeaderTest
  vtkIOVPIC-HeaderTest
  vtkIOVPIC-Test-Cxx-HeaderTest
  vtkIOPostgreSQL-HeaderTest
  vtkIOPostgreSQL-Test-Cxx-HeaderTest
  vtkIOXML-HeaderTest
  vtkIOXML-Test-Cxx-HeaderTest
  vtkIONetCDF-HeaderTest
  vtkIONetCDF-Test-Cxx-HeaderTest
  vtkIOParallel-HeaderTest
  vtkIOParallel-Test-Cxx-HeaderTest
  vtkIOEnSight-HeaderTest
  vtkIOTecplotTable-HeaderTest
  vtkIOTecplotTable-Test-Cxx-HeaderTest
  vtkIOPLY-HeaderTest
  vtkIOPLY-Test-Cxx-HeaderTest
  vtkIOXdmf3-HeaderTest
  vtkIOODBC-HeaderTest
  vtkIOODBC-Test-Cxx-HeaderTest
  vtkIOVideo-HeaderTest
  vtkIOSQL-HeaderTest
  vtkIOSQL-Test-Cxx-HeaderTest
  vtkIOParallelExodus-HeaderTest
  vtkIOParallelExodus-Test-Cxx-HeaderTest
  vtkIOXMLParser-HeaderTest
  vtkIOADIOS-HeaderTest
  vtkIOADIOS-Test-Cxx-HeaderTest
  vtkIOMovie-HeaderTest
  vtkIOMovie-Test-Cxx-HeaderTest
  vtkIOAsynchronous-HeaderTest
  vtkIOSegY-HeaderTest
  vtkIOSegY-Test-Cxx-HeaderTest
  vtkIOGeoJSON-HeaderTest
  vtkIOParallelXML-HeaderTest
  vtkIOParallelXML-Test-Cxx-HeaderTest
  vtkIOExportOpenGL2-HeaderTest
  vtkIOExportOpenGL2-Test-Cxx-HeaderTest
  vtkIOVeraOut-HeaderTest
  vtkIOMPIParallel-HeaderTest
  vtkIOMPIParallel-Test-Cxx-HeaderTest
  vtkIOMotionFX-HeaderTest
  vtkIOMotionFX-Test-Cxx-HeaderTest
  vtkIOPDAL-HeaderTest
  vtkIOPDAL-Test-Cxx-HeaderTest
  vtkIOXdmf2-HeaderTest
  vtkIOXdmf2-Test-Cxx-HeaderTest
  vtkIOParallelNetCDF-HeaderTest
  vtkIOParallelNetCDF-Test-Cxx-HeaderTest
  vtkIOLSDyna-HeaderTest
  vtkIOLSDyna-Test-Cxx-HeaderTest
  vtkIOCore-HeaderTest
  vtkIOCore-Test-Cxx-HeaderTest
  vtkIOMySQL-HeaderTest
  vtkIOMySQL-Test-Cxx-HeaderTest
  vtkIOExportPDF-HeaderTest
  vtkIOExportPDF-Test-Cxx-HeaderTest
  vtkIOLAS-HeaderTest
  vtkIOLAS-Test-Cxx-HeaderTest
  vtkIOMPIImage-HeaderTest
  vtkIOMPIImage-Test-Cxx-HeaderTest
  vtkIOCityGML-HeaderTest
  vtkIOCityGML-Test-Cxx-HeaderTest
  vtkIOTRUCHAS-HeaderTest
  vtkIOTRUCHAS-Test-Cxx-HeaderTest
  vtkGUISupportQtSQL-HeaderTest
  vtkGUISupportQtSQL-Test-Cxx-HeaderTest
  vtkGUISupportQt-HeaderTest
  vtkGUISupportQt-Test-Cxx-HeaderTest
  vtkGUISupportQtOpenGL-HeaderTest
  vtkGUISupportQtOpenGL-Test-Cxx-HeaderTest
  vtkdiy2-HeaderTest
  vtkutf8-HeaderTest
  vtkpegtl-HeaderTest
  vtkgl2ps-HeaderTest
  vtkxdmf2-HeaderTest
  vtktiff-HeaderTest
  vtkzlib-HeaderTest
  vtkVPIC-HeaderTest
  vtklibharu-HeaderTest
  vtkVTKm-HeaderTest
  vtklz4-HeaderTest
  vtkhdf5-HeaderTest
  vtkmpi4py-HeaderTest
  vtkpugixml-HeaderTest
  vtkjsoncpp-HeaderTest
  vtkglew-HeaderTest
  vtkeigen-HeaderTest
  vtkkissfft-HeaderTest
  vtkxdmf3-HeaderTest
  vtkfreetype-HeaderTest
  vtkverdict-HeaderTest
  vtklibxml2-HeaderTest
  vtkzfp-HeaderTest
  vtkexpat-HeaderTest
  vtksqlite-HeaderTest
  vtklzma-HeaderTest
  vtkjpeg-HeaderTest
  vtktheora-HeaderTest
  vtknetcdf-HeaderTest
  vtkdoubleconversion-HeaderTest
  vtkogg-HeaderTest
  vtkexodusII-HeaderTest
  vtkpng-HeaderTest
  vtklibproj-HeaderTest
  vtkDomainsMicroscopy-HeaderTest
  vtkDomainsMicroscopy-Test-Cxx-HeaderTest
  vtkDomainsParallelChemistry-HeaderTest
  vtkDomainsParallelChemistry-Test-Cxx-HeaderTest
  vtkDomainsChemistryOpenGL2-HeaderTest
  vtkDomainsChemistryOpenGL2-Test-Cxx-HeaderTest
  vtkDomainsChemistry-HeaderTest
  vtkDomainsChemistry-Test-Cxx-HeaderTest
  vtkPython-HeaderTest
  vtkDICOMParser-HeaderTest
  vtkPythonInterpreter-HeaderTest
  vtkMetaIO-HeaderTest
  vtksys-HeaderTest
  vtkUtilitiesBenchmarks-HeaderTest
  vtkkwiml-HeaderTest
  vtkInteractionImage-HeaderTest
  vtkInteractionStyle-HeaderTest
  vtkInteractionWidgets-HeaderTest
  vtkInteractionWidgets-Test-Cxx-HeaderTest


  PrintSelf-Charts
  PrintSelf-Common
  PrintSelf-Filtering
  PrintSelf-GenericFiltering
  PrintSelf-Geovis
  PrintSelf-Graphics
  PrintSelf-Hybrid
  PrintSelf-Imaging
  PrintSelf-Infovis
  PrintSelf-IO
  PrintSelf-Parallel
  PrintSelf-Rendering
  PrintSelf-Views
  PrintSelf-VolumeRendering
  PrintSelf-Widgets

  TestSetObjectMacro-Charts
  TestSetObjectMacro-Common
  TestSetObjectMacro-Filtering
  TestSetObjectMacro-GenericFiltering
  TestSetObjectMacro-Geovis
  TestSetObjectMacro-Graphics
  TestSetObjectMacro-Hybrid
  TestSetObjectMacro-Imaging
  TestSetObjectMacro-Infovis
  TestSetObjectMacro-IO
  TestSetObjectMacro-Parallel
  TestSetObjectMacro-Rendering
  TestSetObjectMacro-Views
  TestSetObjectMacro-VolumeRendering
  TestSetObjectMacro-Widgets

  # this one runs python which then runs two program so no memory checking there
  Sockets-image
  )


#####################################################
# Be aware CMake currently warns on all the following
#
# "([^ :]+):([0-9]+): warning:",
#  "([^ :]+):([0-9]+): note:",
#  "^cc[^C]*CC: WARNING File = ([^,]+), Line = ([0-9]+)",
#  "^ld([^:])*:([ \\t])*WARNING([^:])*:",
#  "([^:]+): warning ([0-9]+):",
#  "^\"[^\"]+\", line [0-9]+: [Ww](arning|arnung)",
#  "([^:]+): warning[ \\t]*[0-9]+[ \\t]*:",
#  "^(Warning|Warnung) ([0-9]+):",
#  "^(Warning|Warnung)[ :]",
#  "WARNING: ",
#  "([^ :]+) : warning",
#  "([^:]+): warning",
#  "\", line [0-9]+\\.[0-9]+: [0-9]+-[0-9]+ \\([WI]\\)",
#  "^cxx: Warning:",
#  ".*file: .* has no symbols",
#  "([^ :]+):([0-9]+): (Warning|Warnung)",
#  "\\([0-9]*\\): remark #[0-9]*",
#  "\".*\", line [0-9]+: remark\\([0-9]*\\):",
#  "cc-[0-9]* CC: REMARK File = .*, Line = [0-9]*",
#  "^CMake Warning.*:",
#  "^\\[WARNING\\]",

SET(CTEST_CUSTOM_WARNING_MATCH
  ${CTEST_CUSTOM_WARNING_MATCH}
  "{standard input}:[0-9][0-9]*: Warning: "
  )

# Removing this because it somehow matches normal build output lines
# on several platforms.  Perhaps there is a bug in the custom match
# support.
#
#  SET(CTEST_CUSTOM_ERROR_MATCH
#    ${CTEST_CUSTOM_ERROR_MATCH}
#    "\\", line [0-9]+, in "
#    )

IF(CMAKE_SYSTEM MATCHES "OSF")
  SET(CTEST_CUSTOM_WARNING_EXCEPTION
    ${CTEST_CUSTOM_WARNING_EXCEPTION}
    "vtkKWApplication"
    "vtkKWObject"
    )
ENDIF()

SET(CTEST_CUSTOM_WARNING_EXCEPTION
  ${CTEST_CUSTOM_WARNING_EXCEPTION}
  "vcruntime_exception.h\\(43\\): note: see declaration"
  "json/json"
  "shadows a member of 'OGRRawPoint'"
  "list.[0-9]+. : warning C4702: unreachable code"
  "xtree.[0-9]+. : warning C4702: unreachable code"
  "vector.[0-9]+. : warning C4702: unreachable code"
  "warning LNK4221"
  "variable .var_args[2]*. is used before its value is set"
  "jobserver unavailable"
  "warning: \\(Long double usage is reported only once for each file"
  "warning: To disable this warning use"
  "warning: .+ might be clobbered by .longjmp. or .vfork."
  "(ranlib|libtool):.*file: .+ has no symbols"
  "could not be inlined"
  "ld: warning prebinding disabled because \\((__TEXT|__DATA|__LINKEDIT) segment \\(address = 0x[a-f0-9]+ size = 0x[a-f0-9]+\\) of (.*) overlaps with (__LINKEDIT|__TEXT|__DATA) segment \\(address = 0x[a-f0-9]+ size = 0x[a-f0-9]+\\) of (.*)"
  "ld: warning prebinding disabled because dependent library: (.*).dylib is not prebound"
  "warning: duplicate dylib"

  # MPI uses c++ but may have been built with a different c++ compiler.
  # It seems to work anyway so let's ignore it to make it easier to
  # test more compilers.
  "ld: warning: libstdc.*, needed by .*, may conflict with libstdc.*"

  # Does *anyone* have an STL implementation that compiles without warnings...?
  "cc-1116 CC: WARNING File = /usr/include/CC/stl_alloc.h, Line = 175"

  # vtkfreetype needs to be updated to get rid of warnings that occur during
  # 64-bit compiles... for now, mask them out of dashboard results:
  "vtkfreetype.*warning C4"
  "vtkfreetype.*warning: dereferencing type-punned pointer"
  "vtkfreetype.*warning: conversion to .* from .* may change the sign of the result"
  "vtkfreetype.*warning: passing argument .* of .* as .*signed due to prototype"
  "vtkfreetype.*warning: passing argument .* of .* with different width due to prototype"
  "vtkfreetype.*warning: conversion to .* from .* may alter its value"
  "vtkfreetype.*warning: conversion of unsigned constant value to negative integer"
  "vtkfreetype.*warning: suggest braces around empty body in 'do' statement"
  "vtkfreetype.*warning: negative integer implicitly converted to unsigned type"
  "vtkfreetype.*warning: dereferencing pointer .* does break strict-aliasing rules"
  "vtkfreetype.*note: initialized from here"
  "vtkfreetype.*warning: .* may be used uninitialized in this function"
  "vtkfreetype.*note: .* was declared here"
  "vtkfreetype/.*warning: .* set but not used"
  "vtkfreetype/.*warning: .* defined but not used"
  "WARNING: While resolving call to function .*FTC_GNode_Compare.* arguments were dropped!"
  # vtknetcdf occasionally has warnings for things that are not a problem.
  "vtknetcdf.*warning: dereferencing type-punned pointer"
  "vtknetcdf.*warning: passing argument .* of .* as .*signed due to prototype"
  "vtknetcdf.*warning: conversion to .* from .* may change the sign of the result"
  "vtknetcdf.*warning: conversion to .* from .* may alter its value"
  "vtknetcdf.*warning: dereferencing pointer .* does break strict-aliasing rules"
  "vtknetcdf.*note: initialized from here"
  # Some VTK dashboards include building bits of Qt which produce lots of
  # the following warnings when built with the MS compilers. Qt guys should
  # fix their code. Until they do, keep the Qt chatter off the VTK dashboard
  # results:
  "[Qq]t([Cc]ore|[Gg]ui).*(warning|note)"
  "[Qq]t.*h.*warning.*declaration of .* shadows a member of .this"
  "[Qq]t.*h.*warning.*(copy constructor|assignment operator) could not be generated"
  "warning C4244: 'initializing' : conversion from 'qint64' to 'int', possible loss of data"
  # gcc -Wstric-aliasing
  "[Qq]t.*q.*h.*warning: dereferencing pointer .* does break strict-aliasing rules"
  "[Qq]t.*q.*h.*note: initialized from here"
  "[Qq]t.*q.*h.*note: while compiling"
  "[Qq]t.*q.*h.*note: see reference"
  "[Qq]t.*ui_"
  "[Qq]t.*note: see reference"
  "[Qq]t.*warning C4714"

  # Specifically for HP compiler, mask out
  "Filtering.vtkImageMultiple(Input|InputOutput)Filter.cxx.*warning.*more strictly aligned type"
  "IO.vtkJPEG(Reader|Writer).cxx.*warning.*more strictly aligned type"
  ".*warning.*relational operator.*always evaluates to.*"
  ".*warning.*controlling expression is constant"
  "[Qq]t.*h.*warning.*types cannot be declared in anonymous unions"

  # QT on HP-UX uses -ldl while VTK uses -dldl.
  "aCC: warning 983: The -ldl library specified on the command line is also added automatically by the compiler driver."

  # This test is made to discover compiler warnings, therefore the emitted
  # warnings are irrelevant in a dashboard submission
  "TestCxxFeatures.cxx.*warning.*type qualifiers ignored on function return type"

  # File generated by lex/yacc flex/bison, cannot fix the warnings.
  "vtkParse.y.*passing argument 1 of 'preSig' discards qualifiers from pointer target type"
  "vtkParse.y.*passing argument 1 of 'postSig' discards qualifiers from pointer target type"
  "vtkParse.l.*warning: ignoring return value of 'fwrite', declared with attribute warn_unused_result"
  "vtkParse.l.*warning: passing argument .* of .* as .* due to prototype"
  "lex.yy.c.*warning: passing argument .* of .* as .* due to prototype"

  # Java lint warnings
  "Note: .* uses? or overrides a deprecated API"
  "Note: .* uses? unchecked or unsafe operations"
  "Note: Recompile with -Xlint:.* for details"

  # warnings from some Open MPI headers/libs, cannot fix:
  "/openmpi/.*request_inln.h.*warning: declaration .struct MPI::Grequest_intercept_t. does not declare anything"
  "openmpi.*comm_inln.h.*warning: unused parameter"
  "openmpi.*/cxx/op_inln.h.*warning: cast between incompatible function types from"

  # remove the next line once this class is removed probably VTK 9.1
  "vtkExtractArraysOverTime"

  # warnings from some Eigen headers:
  #
  # Eigin has so many warnings using individual suppressions
  # does not work. So many will be suppressed that it exceeds
  # the limit ctest will show making it difficult to see
  # the specifics of an unsuppressed warning unless you have
  # access to the raw build logs. So we suppress everything
  # that has eigin in the path. The old suppressions are left
  # commented below should they be needed.
  "[Ee]igen/src/.* note:"
  "[Ee]igen/src/.* warning:"
  "vtkeigen::"

  # "[Ee]igen/src/.* note: \\(skipping"
  # "[Ee]igen/src/.* note: expanded from macro"
  # "[Ee]igen/src/.* note: implicit copy constructor for"
  # "[Ee]igen/src/.* note: in expansion of macro"
  # "[Ee]igen/src/.* note: in implicit copy constructor for"
  # "[Ee]igen/src/.* note: in implicit move constructor for"
  # "[Ee]igen/src/.* note: in instantiation of member function"
  # "[Ee]igen/src/.* note: previous declaration is here"
  # "[Ee]igen/src/.* note: shadowed declaration is here"
  # "[Ee]igen/src/.* warning: cast from"
  # "[Ee]igen/src/.* warning: 'm_maxThreads' was marked unused but was used"
  # "[Ee]igen/src/.* warning: declaration of '.*' shadows"
  # "[Ee]igen/src/.* warning: declaration shadows a typedef in"
  # "[Ee]igen/src/.* warning: definition of implicit copy constructor for"
  # "[Ee]igen/src/.* warning: enum constant in boolean context"
  # "note: in instantiation of member function 'vtkeigen::"
  # "note: in instantiation of function template specialization 'vtkeigen::"

  # nested from an eigen macro
  "include/assert.h.* note: expanded from macro 'assert'"

  # warnings from some python headers/libs, cannot fix:
  "warning: the use of .tmpnam_r. is dangerous, better use .mkstemp."
  "warning: the use of .tempnam. is dangerous, better use .mkstemp."
  "pyconfig.h.*warning: ._XOPEN_SOURCE. redefined"
  "features.h.*warning: this is the location of the previous definition"

  #boost
  "boost.*warning.*assignment operator could not be generated"
  "boost.*warning.*type name first seen using .* now seen using .*"
  "boost.*warning.*default constructor could not be generated"
  "boost.*warning.*can never be instantiated - user defined constructor required"
  "boost.*warning.*unreferenced formal parameter"
  "boost.*warning.*signed/unsigned mismatch"
  "boost.*warning.*conversion from .* to .*, possible loss of data"
  "boost.*warning.*declaration of .* shadows a member of"
  "boost.*warning.*unused parameter"
  "boost.*warning.*comparison between signed and unsigned integer expressions"
  "TestBoostAdapter.*warning.*edge_property.*may be used uninitialized"

  # bogus unreachable code warning in hashtable in kwsys
  "hashtable.hxx.*warning C4702: unreachable code"

  # Qt Designer related warning
  "QtDesigner/extension.*warning: unused parameter"

  # Strange Arch warning
  "cc1plus: warning: assuming signed overflow does not occur when assuming that .* is always true"

  # Unused dll when building Examples/AMR/Cxx with VS 7.1, Release configuration
  "warning LNK4089: all references to .vtkIOXML-.*dll. discarded by /OPT:REF"

  # Ignore clang's summary warning, assuming prior text has matched some
  # other warning expression:
  "[0-9,]+ warnings? generated."

  #ignore clangs documentation warnings from libxml, which uses gtk-doc natively, not doxygen
  "vtklibxml2.*warning: unknown command tag name"

  # Ignore warnings about inheriting std::exception when the dll-interface
  # doesn't match. There's no other way to really do exceptions properly.
  "warning C4275: non dll-interface class 'std::exception' used as base"

  # This warning occurs when building Java with -source x.y with compiler a.b's
  # runtime library (rt.jar). It also emits a line with "1 warning"
  # which matches ctests regex as well
  "bootstrap class path not set in conjunction with -source"
  "1 warning"

  # diy warnings
  "vtkmdiy/io/utils.hpp\\(84\\): warning: result of call is not used"

  # stephen and matt should be working on these. Suppress until they fix
  # upstream and we update. Todo: check after Sept 1 2018 with Stephen and
  # Matt if these are fixed.
  #
  "vtkmetaio/metaImage.cxx"
  "vtkmetaio/metaArray.cxx"

  # 3-rd party warnings from double-conversion
  "vtkdoubleconversion.*unused function"

  # warnings from ospray include.
  "ospray/ospcommon"

  # warnings as part of the doxygen documentation build
  "no documentation block in"
  "Utilities/Doxygen"
  "Consider increasing DOT_GRAPH_MAX_NODES"
  "based on cache misses the ideal setting for LOOKUP_CACHE_SIZE"

  )

IF(APPLE)
SET(CTEST_CUSTOM_WARNING_EXCEPTION
  ${CTEST_CUSTOM_WARNING_EXCEPTION}
  "warning -.: directory name .* does not exist"
  )
ENDIF()

SET(CTEST_CUSTOM_COVERAGE_EXCLUDE
  ${CTEST_CUSTOM_COVERAGE_EXCLUDE}
  "vtk[^\\.]+(Java|Python).cxx"
  ".*vtkOpenGLState.*" # debugging class
  ".*Testing.Cxx.*cxx"
  ".*Testing.Cxx.*h"
  ".*moc_.*cxx"
  # Generated files
  ".*/Rendering/OpenGL/vtkgl.*"

  # Exclude files from the Utilities directories
  ".*/Utilities/.*"
  ".*/ThirdParty/.*"

  # Exclude vtkOpenGLPolyDataMapper since the class is deprecated since VTK 6.2.
  ".*vtkOpenGLPolyDataMapper.*"
  )

IF(CMAKE_COMPILER_IS_GNUCXX)
SET(CTEST_CUSTOM_WARNING_EXCEPTION
  ${CTEST_CUSTOM_WARNING_EXCEPTION}
  # GCC 4.2 has a bug where it has Unnecessary anonymous namespace warnings
  # you can find the full bug on GNU Bugzilla with bug number 29365
  "warning: .* has a field .* whose type uses the anonymous namespace"
  )
ENDIF()

# If VTK_LEGACY_REMOVE is not set, then we're expecting code to use deprecated
# API. Hence ignore all deprecation warnings.
IF(NOT VTK_LEGACY_REMOVE AND NOT VTK_LEGACY_SILENT)
SET(CTEST_CUSTOM_WARNING_EXCEPTION
  ${CTEST_CUSTOM_WARNING_EXCEPTION}
  ".*[W|w]arning:.* deprecated"
  "[N|n]ote: expanded from macro"
  "[N|n]ote:.* deprecated"
  )
ENDIF()
# Temporarily: to show us *all* the remaining warnings on the
# 64-bit Windows builds on one result page...
#
SET(CTEST_CUSTOM_MAXIMUM_NUMBER_OF_WARNINGS 222)
