# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Math
# Build directory: /home/fenics/shared/VTK-build/Common/Math
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonMath-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/Math" "VTKCOMMONMATH_EXPORT")
set_tests_properties(vtkCommonMath-HeaderTest PROPERTIES  LABELS "vtkCommonMath")
