# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Texture/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Filters/Texture/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersTextureCxx-TestScalarsToTexture "/home/fenics/shared/VTK-build/bin/vtkFiltersTextureCxxTests" "TestScalarsToTexture" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Filters/Texture/Testing/Data/Baseline/TestScalarsToTexture.png")
set_tests_properties(vtkFiltersTextureCxx-TestScalarsToTexture PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersTexture" SKIP_RETURN_CODE "125")
