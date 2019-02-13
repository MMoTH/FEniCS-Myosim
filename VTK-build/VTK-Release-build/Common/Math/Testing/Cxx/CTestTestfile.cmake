# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Math/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Common/Math/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonMathCxx-TestAmoebaMinimizer "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonMathCxxTests" "TestAmoebaMinimizer")
set_tests_properties(vtkCommonMathCxx-TestAmoebaMinimizer PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonMath" SKIP_RETURN_CODE "125")
add_test(vtkCommonMathCxx-TestMatrix3x3 "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonMathCxxTests" "TestMatrix3x3")
set_tests_properties(vtkCommonMathCxx-TestMatrix3x3 PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonMath" SKIP_RETURN_CODE "125")
add_test(vtkCommonMathCxx-TestPolynomialSolversUnivariate "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonMathCxxTests" "TestPolynomialSolversUnivariate")
set_tests_properties(vtkCommonMathCxx-TestPolynomialSolversUnivariate PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonMath" SKIP_RETURN_CODE "125")
add_test(vtkCommonMathCxx-TestQuaternion "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkCommonMathCxxTests" "TestQuaternion")
set_tests_properties(vtkCommonMathCxx-TestQuaternion PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkCommonMath" SKIP_RETURN_CODE "125")
