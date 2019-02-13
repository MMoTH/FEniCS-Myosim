# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/EnSight
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/EnSight
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOEnSight-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/EnSight" "VTKIOENSIGHT_EXPORT")
set_tests_properties(vtkIOEnSight-HeaderTest PROPERTIES  LABELS "vtkIOEnSight")
