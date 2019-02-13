# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/System
# Build directory: /home/fenics/shared/VTK-build/Common/System
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonSystem-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/System" "VTKCOMMONSYSTEM_EXPORT")
set_tests_properties(vtkCommonSystem-HeaderTest PROPERTIES  LABELS "vtkCommonSystem")
