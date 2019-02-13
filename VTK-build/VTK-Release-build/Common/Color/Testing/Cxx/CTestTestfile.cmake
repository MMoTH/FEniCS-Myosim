# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Color/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Common/Color/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonColorCxx-TestCategoricalColors "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonColorCxxTests" "TestCategoricalColors" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkCommonColorCxx-TestCategoricalColors PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonColor" SKIP_RETURN_CODE "125")
add_test(vtkCommonColorCxx-TestColorSeries "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonColorCxxTests" "TestColorSeries" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Common/Color/Testing/Data/Baseline/TestColorSeries.png")
set_tests_properties(vtkCommonColorCxx-TestColorSeries PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonColor" SKIP_RETURN_CODE "125")
add_test(vtkCommonColorCxx-TestColorSeriesLookupTables "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonColorCxxTests" "TestColorSeriesLookupTables" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkCommonColorCxx-TestColorSeriesLookupTables PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonColor" SKIP_RETURN_CODE "125")
add_test(vtkCommonColorCxx-TestNamedColors "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonColorCxxTests" "TestNamedColors" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkCommonColorCxx-TestNamedColors PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonColor" SKIP_RETURN_CODE "125")
