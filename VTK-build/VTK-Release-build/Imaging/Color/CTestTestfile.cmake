# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Color
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Imaging/Color
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingColor-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Color" "VTKIMAGINGCOLOR_EXPORT")
set_tests_properties(vtkImagingColor-HeaderTest PROPERTIES  LABELS "vtkImagingColor")
