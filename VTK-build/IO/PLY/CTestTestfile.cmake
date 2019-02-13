# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/PLY
# Build directory: /home/fenics/shared/VTK-build/IO/PLY
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOPLY-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/PLY" "VTKIOPLY_EXPORT")
set_tests_properties(vtkIOPLY-HeaderTest PROPERTIES  LABELS "vtkIOPLY")
