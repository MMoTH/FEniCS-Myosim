# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Charts/Core
# Build directory: /home/fenics/shared/VTK-build/Charts/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkChartsCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Charts/Core" "VTKCHARTSCORE_EXPORT")
set_tests_properties(vtkChartsCore-HeaderTest PROPERTIES  LABELS "vtkChartsCore")
