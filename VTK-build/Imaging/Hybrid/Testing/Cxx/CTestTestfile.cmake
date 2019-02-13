# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Hybrid/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Imaging/Hybrid/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingHybridCxx-TestImageToPoints "/home/fenics/shared/VTK-build/bin/vtkImagingHybridCxxTests" "TestImageToPoints" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Imaging/Hybrid/Testing/Data/Baseline/TestImageToPoints.png")
set_tests_properties(vtkImagingHybridCxx-TestImageToPoints PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingHybrid" SKIP_RETURN_CODE "125")
add_test(vtkImagingHybridCxx-TestSampleFunction "/home/fenics/shared/VTK-build/bin/vtkImagingHybridCxxTests" "TestSampleFunction")
set_tests_properties(vtkImagingHybridCxx-TestSampleFunction PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingHybrid" SKIP_RETURN_CODE "125")
