# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Infovis/Layout/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Infovis/Layout/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInfovisLayoutCxx-TestChacoGraphReader "/home/fenics/shared/VTK-build/bin/vtkInfovisLayoutCxxTests" "TestChacoGraphReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Infovis/Layout/Testing/Data/Baseline/TestChacoGraphReader.png")
set_tests_properties(vtkInfovisLayoutCxx-TestChacoGraphReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkInfovisLayout" SKIP_RETURN_CODE "125")
add_test(vtkInfovisLayoutCxx-TestCirclePackLayoutStrategy "/home/fenics/shared/VTK-build/bin/vtkInfovisLayoutCxxTests" "TestCirclePackLayoutStrategy" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Infovis/Layout/Testing/Data/Baseline/TestCirclePackLayoutStrategy.png")
set_tests_properties(vtkInfovisLayoutCxx-TestCirclePackLayoutStrategy PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkInfovisLayout" SKIP_RETURN_CODE "125")
add_test(vtkInfovisLayoutCxx-TestGraphLayoutStrategy "/home/fenics/shared/VTK-build/bin/vtkInfovisLayoutCxxTests" "TestGraphLayoutStrategy" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkInfovisLayoutCxx-TestGraphLayoutStrategy PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkInfovisLayout" SKIP_RETURN_CODE "125")
add_test(vtkInfovisLayoutCxx-TestIncrementalForceLayout "/home/fenics/shared/VTK-build/bin/vtkInfovisLayoutCxxTests" "TestIncrementalForceLayout" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkInfovisLayoutCxx-TestIncrementalForceLayout PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkInfovisLayout" SKIP_RETURN_CODE "125")
add_test(vtkInfovisLayoutCxx-TestTreeMapLayoutStrategy "/home/fenics/shared/VTK-build/bin/vtkInfovisLayoutCxxTests" "TestTreeMapLayoutStrategy" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Infovis/Layout/Testing/Data/Baseline/TestTreeMapLayoutStrategy.png")
set_tests_properties(vtkInfovisLayoutCxx-TestTreeMapLayoutStrategy PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkInfovisLayout" SKIP_RETURN_CODE "125")
