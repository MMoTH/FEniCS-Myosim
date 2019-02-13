# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Programmable
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Programmable
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersProgrammable-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Programmable" "VTKFILTERSPROGRAMMABLE_EXPORT")
set_tests_properties(vtkFiltersProgrammable-HeaderTest PROPERTIES  LABELS "vtkFiltersProgrammable")
