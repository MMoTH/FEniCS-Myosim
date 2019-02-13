# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/SegY
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/SegY
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOSegY-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/SegY" "VTKIOSEGY_EXPORT")
set_tests_properties(vtkIOSegY-HeaderTest PROPERTIES  LABELS "vtkIOSegY")
