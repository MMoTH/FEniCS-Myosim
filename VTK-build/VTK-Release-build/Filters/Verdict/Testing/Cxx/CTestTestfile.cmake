# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Verdict/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Verdict/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersVerdictCxx-CellSizeFilter "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersVerdictCxxTests" "CellSizeFilter" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersVerdictCxx-CellSizeFilter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersVerdict" SKIP_RETURN_CODE "125")
add_test(vtkFiltersVerdictCxx-MeshQuality "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersVerdictCxxTests" "MeshQuality" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersVerdictCxx-MeshQuality PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersVerdict" SKIP_RETURN_CODE "125")
