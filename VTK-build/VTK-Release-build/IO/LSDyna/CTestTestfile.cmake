# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/LSDyna
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/LSDyna
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOLSDyna-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/LSDyna" "VTKIOLSDYNA_EXPORT")
set_tests_properties(vtkIOLSDyna-HeaderTest PROPERTIES  LABELS "vtkIOLSDyna")
