# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Transforms/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Common/Transforms/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonTransformsCxx-TestTransform "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonTransformsCxxTests" "TestTransform")
set_tests_properties(vtkCommonTransformsCxx-TestTransform PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonTransforms" SKIP_RETURN_CODE "125")
add_test(vtkCommonTransformsCxx-TestLandmarkTransform "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonTransformsCxxTests" "TestLandmarkTransform")
set_tests_properties(vtkCommonTransformsCxx-TestLandmarkTransform PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonTransforms" SKIP_RETURN_CODE "125")
