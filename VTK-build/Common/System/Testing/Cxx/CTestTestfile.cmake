# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/System/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Common/System/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonSystemCxx-TestDirectory "/home/fenics/shared/VTK-build/bin/vtkCommonSystemCxxTests" "TestDirectory")
set_tests_properties(vtkCommonSystemCxx-TestDirectory PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonSystem" SKIP_RETURN_CODE "125")
add_test(vtkCommonSystemCxx-otherTimerLog "/home/fenics/shared/VTK-build/bin/vtkCommonSystemCxxTests" "otherTimerLog")
set_tests_properties(vtkCommonSystemCxx-otherTimerLog PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonSystem" SKIP_RETURN_CODE "125")
