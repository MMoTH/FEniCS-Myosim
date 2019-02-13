# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/VeraOut
# Build directory: /home/fenics/shared/VTK-build/IO/VeraOut
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOVeraOut-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/VeraOut" "VTKIOVERAOUT_EXPORT")
set_tests_properties(vtkIOVeraOut-HeaderTest PROPERTIES  LABELS "vtkIOVeraOut")
