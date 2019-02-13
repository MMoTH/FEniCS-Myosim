# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/MINC
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/MINC
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOMINC-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/MINC" "VTKIOMINC_EXPORT")
set_tests_properties(vtkIOMINC-HeaderTest PROPERTIES  LABELS "vtkIOMINC")
