# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Color/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Imaging/Color/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingColorCxx-ImageQuantizeToIndex "/home/fenics/shared/VTK-build/bin/vtkImagingColorCxxTests" "ImageQuantizeToIndex" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkImagingColorCxx-ImageQuantizeToIndex PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkImagingColor" SKIP_RETURN_CODE "125")
