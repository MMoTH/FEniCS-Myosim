# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Morphological/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Imaging/Morphological/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingMorphologicalCxx-TestImageThresholdConnectivity "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkImagingMorphologicalCxxTests" "TestImageThresholdConnectivity" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Imaging/Morphological/Testing/Data/Baseline/TestImageThresholdConnectivity.png")
set_tests_properties(vtkImagingMorphologicalCxx-TestImageThresholdConnectivity PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingMorphological" SKIP_RETURN_CODE "125")
add_test(vtkImagingMorphologicalCxx-TestImageConnectivityFilter "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkImagingMorphologicalCxxTests" "TestImageConnectivityFilter" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Imaging/Morphological/Testing/Data/Baseline/TestImageConnectivityFilter.png")
set_tests_properties(vtkImagingMorphologicalCxx-TestImageConnectivityFilter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingMorphological" SKIP_RETURN_CODE "125")
