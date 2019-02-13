# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Points/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Points/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersPointsCxx-UnitTestKernels "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersPointsCxxTests" "UnitTestKernels" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersPointsCxx-UnitTestKernels PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersPoints" SKIP_RETURN_CODE "125")
add_test(vtkFiltersPointsCxx-TestSPHKernels "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersPointsCxxTests" "TestSPHKernels" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersPointsCxx-TestSPHKernels PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersPoints" SKIP_RETURN_CODE "125")
add_test(vtkFiltersPointsCxx-PlotSPHKernels "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersPointsCxxTests" "PlotSPHKernels" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Filters/Points/Testing/Data/Baseline/PlotSPHKernels.png")
set_tests_properties(vtkFiltersPointsCxx-PlotSPHKernels PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersPoints" SKIP_RETURN_CODE "125")
add_test(vtkFiltersPointsCxx-TestPointCloudFilterArrays "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersPointsCxxTests" "TestPointCloudFilterArrays" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersPointsCxx-TestPointCloudFilterArrays PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersPoints" SKIP_RETURN_CODE "125")
