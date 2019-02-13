# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Transforms
# Build directory: /home/fenics/shared/VTK-build/Common/Transforms
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonTransforms-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/Transforms" "VTKCOMMONTRANSFORMS_EXPORT")
set_tests_properties(vtkCommonTransforms-HeaderTest PROPERTIES  LABELS "vtkCommonTransforms")
