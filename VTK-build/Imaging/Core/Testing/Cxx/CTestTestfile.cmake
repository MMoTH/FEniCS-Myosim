# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Core/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Imaging/Core/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingCoreCxx-FastSplatter "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "FastSplatter" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/FastSplatter.png")
set_tests_properties(vtkImagingCoreCxx-FastSplatter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageAccumulate "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageAccumulate" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-ImageAccumulate PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageAccumulateLarge "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageAccumulateLarge" "32")
set_tests_properties(vtkImagingCoreCxx-ImageAccumulateLarge PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageAutoRange "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageAutoRange" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageAutoRange.png")
set_tests_properties(vtkImagingCoreCxx-ImageAutoRange PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageBSplineCoefficients "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageBSplineCoefficients" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageBSplineCoefficients.png")
set_tests_properties(vtkImagingCoreCxx-ImageBSplineCoefficients PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageHistogram "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageHistogram" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageHistogram.png")
set_tests_properties(vtkImagingCoreCxx-ImageHistogram PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageHistogramStatistics "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageHistogramStatistics" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-ImageHistogramStatistics PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageInterpolateSlidingWindow2D "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageInterpolateSlidingWindow2D" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageInterpolateSlidingWindow2D.png")
set_tests_properties(vtkImagingCoreCxx-ImageInterpolateSlidingWindow2D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageInterpolateSlidingWindow3D "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageInterpolateSlidingWindow3D" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageInterpolateSlidingWindow3D.png")
set_tests_properties(vtkImagingCoreCxx-ImageInterpolateSlidingWindow3D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageResize "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageResize" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageResize.png")
set_tests_properties(vtkImagingCoreCxx-ImageResize PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageResize3D "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageResize3D" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageResize3D.png")
set_tests_properties(vtkImagingCoreCxx-ImageResize3D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageResizeCropping "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageResizeCropping" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageResizeCropping.png")
set_tests_properties(vtkImagingCoreCxx-ImageResizeCropping PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageReslice "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageReslice" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/ImageReslice.png")
set_tests_properties(vtkImagingCoreCxx-ImageReslice PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImageWeightedSum "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImageWeightedSum" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-ImageWeightedSum PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-ImportExport "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "ImportExport" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-ImportExport PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestBSplineWarp "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestBSplineWarp" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestBSplineWarp.png")
set_tests_properties(vtkImagingCoreCxx-TestBSplineWarp PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestImageStencilDataMethods "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestImageStencilDataMethods" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-TestImageStencilDataMethods PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestImageStencilIterator "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestImageStencilIterator" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-TestImageStencilIterator PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestStencilWithLasso "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestStencilWithLasso" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestStencilWithLasso.png")
set_tests_properties(vtkImagingCoreCxx-TestStencilWithLasso PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestStencilWithPolyDataContour "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestStencilWithPolyDataContour" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestStencilWithPolyDataContour.png")
set_tests_properties(vtkImagingCoreCxx-TestStencilWithPolyDataContour PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestStencilWithPolyDataSurface "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestStencilWithPolyDataSurface" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestStencilWithPolyDataSurface.png")
set_tests_properties(vtkImagingCoreCxx-TestStencilWithPolyDataSurface PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-TestUpdateExtentReset "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestUpdateExtentReset" "32" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingCoreCxx-TestUpdateExtentReset PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingCore" SKIP_RETURN_CODE "125")
add_test(vtkImagingCoreCxx-AddStencilData "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestImageStencilData" "1" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestAddStencilData.png")
add_test(vtkImagingCoreCxx-SubtractStencilData "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestImageStencilData" "2" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestSubtractStencilData.png")
add_test(vtkImagingCoreCxx-ClipStencilData "/home/fenics/shared/VTK-build/bin/vtkImagingCoreCxxTests" "TestImageStencilData" "3" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Core/Testing/Data/Baseline/TestClipStencilData.png")
