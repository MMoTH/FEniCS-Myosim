# Install script for directory: /home/fenics/shared/VTK/Common/Core

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonCore-8.2.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/fenics/shared/VTK-build/lib/libvtkCommonCore-8.2.so.1"
    "/home/fenics/shared/VTK-build/lib/libvtkCommonCore-8.2.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonCore-8.2.so.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libvtkCommonCore-8.2.so"
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/vtk-8.2/Modules" TYPE FILE FILES "/home/fenics/shared/VTK-build/Common/Core/CMakeFiles/vtkCommonCore.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vtk-8.2" TYPE FILE FILES
    "/home/fenics/shared/VTK/Common/Core/vtkABI.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayDispatch.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayDispatch.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayInterpolate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayInterpolate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayIteratorIncludes.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayIteratorTemplateImplicit.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayPrint.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayPrint.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkAssume.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAtomicTypeConcepts.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAtomicTypes.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAutoInit.h"
    "/home/fenics/shared/VTK/Common/Core/vtkBuffer.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayAccessor.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayIteratorMacro.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayMeta.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayRange.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayTupleRange_AOS.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayTupleRange_Generic.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayValueRange_AOS.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayValueRange_Generic.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayTemplate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkGenericDataArrayLookupHelper.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIOStream.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIOStreamFwd.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationInternals.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMappedDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMathUtilities.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMersenneTwister.h"
    "/home/fenics/shared/VTK/Common/Core/vtkNew.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSOADataArrayTemplate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkSetGet.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSmartPointer.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTemplateAliasMacro.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTestDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypeList.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypeList.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkTypeTraits.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedDataArrayIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariantCast.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariantCreate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariantExtract.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariantInlineOperators.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWeakPointer.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWeakReference.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWin32Header.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWindows.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkAtomic.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkSMPThreadLocal.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkSMPToolsInternal.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSMPTools.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSMPThreadLocalObject.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkArrayDispatchArrayList.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkToolkits.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeListMacros.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAOSDataArrayTemplate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkAOSDataArrayTemplate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAbstractArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkAnimationCue.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayCoordinates.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayExtents.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayExtentsList.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayIteratorTemplate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayIteratorTemplate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayRange.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArraySort.h"
    "/home/fenics/shared/VTK/Common/Core/vtkArrayWeights.h"
    "/home/fenics/shared/VTK/Common/Core/vtkBitArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkBitArrayIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkBoxMuellerRandomSequence.h"
    "/home/fenics/shared/VTK/Common/Core/vtkBreakPoint.h"
    "/home/fenics/shared/VTK/Common/Core/vtkByteSwap.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCallbackCommand.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCharArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCollection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCollectionIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCommand.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCommonInformationKeyManager.h"
    "/home/fenics/shared/VTK/Common/Core/vtkConditionVariable.h"
    "/home/fenics/shared/VTK/Common/Core/vtkCriticalSection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayCollection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayCollectionIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArrayPrivate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkDataArraySelection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDebugLeaks.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDebugLeaksManager.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDenseArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkDenseArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDoubleArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkDynamicLoader.h"
    "/home/fenics/shared/VTK/Common/Core/vtkEventForwarderCommand.h"
    "/home/fenics/shared/VTK/Common/Core/vtkFileOutputWindow.h"
    "/home/fenics/shared/VTK/Common/Core/vtkFloatArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkFloatingPointExceptions.h"
    "/home/fenics/shared/VTK/Common/Core/vtkGarbageCollector.h"
    "/home/fenics/shared/VTK/Common/Core/vtkGarbageCollectorManager.h"
    "/home/fenics/shared/VTK/Common/Core/vtkGaussianRandomSequence.h"
    "/home/fenics/shared/VTK/Common/Core/vtkGenericDataArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkGenericDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIdList.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIdListCollection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIdTypeArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIndent.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformation.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationDataObjectKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationDoubleKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationDoubleVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationIdTypeKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationInformationKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationInformationVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationIntegerKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationIntegerPointerKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationIntegerVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationIterator.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationKeyLookup.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationKeyVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationObjectBaseKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationObjectBaseVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationRequestKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationStringKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationStringVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationUnsignedLongKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationVariantKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationVariantVectorKey.h"
    "/home/fenics/shared/VTK/Common/Core/vtkInformationVector.h"
    "/home/fenics/shared/VTK/Common/Core/vtkIntArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkLargeInteger.h"
    "/home/fenics/shared/VTK/Common/Core/vtkLongArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkLongLongArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkLookupTable.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMappedDataArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkMappedDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMath.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMersenneTwister.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMinimalStandardRandomSequence.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMultiThreader.h"
    "/home/fenics/shared/VTK/Common/Core/vtkMutexLock.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOStrStreamWrapper.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOStreamWrapper.h"
    "/home/fenics/shared/VTK/Common/Core/vtkObject.h"
    "/home/fenics/shared/VTK/Common/Core/vtkObjectBase.h"
    "/home/fenics/shared/VTK/Common/Core/vtkObjectFactory.h"
    "/home/fenics/shared/VTK/Common/Core/vtkObjectFactoryCollection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOldStyleCallbackCommand.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOutputWindow.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOverrideInformation.h"
    "/home/fenics/shared/VTK/Common/Core/vtkOverrideInformationCollection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkPoints.h"
    "/home/fenics/shared/VTK/Common/Core/vtkPoints2D.h"
    "/home/fenics/shared/VTK/Common/Core/vtkPriorityQueue.h"
    "/home/fenics/shared/VTK/Common/Core/vtkRandomPool.h"
    "/home/fenics/shared/VTK/Common/Core/vtkRandomSequence.h"
    "/home/fenics/shared/VTK/Common/Core/vtkReferenceCount.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSOADataArrayTemplate.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkSOADataArrayTemplate.h"
    "/home/fenics/shared/VTK/Common/Core/vtkScalarsToColors.h"
    "/home/fenics/shared/VTK/Common/Core/vtkShortArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSignedCharArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSimpleCriticalSection.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSmartPointerBase.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSortDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSparseArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkSparseArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkStdString.h"
    "/home/fenics/shared/VTK/Common/Core/vtkStringArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkStringOutputWindow.h"
    "/home/fenics/shared/VTK/Common/Core/vtkSystemIncludes.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTimePointUtility.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTimeStamp.h"
    "/home/fenics/shared/VTK/Common/Core/vtkType.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedDataArray.txx"
    "/home/fenics/shared/VTK/Common/Core/vtkTypedDataArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnicodeString.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnicodeStringArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnsignedCharArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnsignedIntArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnsignedLongArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnsignedLongLongArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkUnsignedShortArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariant.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVariantArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVersion.h"
    "/home/fenics/shared/VTK/Common/Core/vtkVoidArray.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWeakPointerBase.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWeakReference.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWindow.h"
    "/home/fenics/shared/VTK/Common/Core/vtkWrappingHints.h"
    "/home/fenics/shared/VTK/Common/Core/vtkXMLFileOutputWindow.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkConfigure.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkMathConfigure.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkVersionMacros.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeInt8Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeInt16Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeInt32Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeInt64Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeUInt8Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeUInt16Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeUInt32Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeUInt64Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeFloat32Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkTypeFloat64Array.h"
    "/home/fenics/shared/VTK-build/Common/Core/vtkCommonCoreModule.h"
    )
endif()

