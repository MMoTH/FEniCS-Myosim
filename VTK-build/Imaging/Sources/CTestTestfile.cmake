# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Sources
# Build directory: /home/fenics/shared/VTK-build/Imaging/Sources
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingSources-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Sources" "VTKIMAGINGSOURCES_EXPORT")
set_tests_properties(vtkImagingSources-HeaderTest PROPERTIES  LABELS "vtkImagingSources")
