# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/General
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Imaging/General
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingGeneral-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/General" "VTKIMAGINGGENERAL_EXPORT")
set_tests_properties(vtkImagingGeneral-HeaderTest PROPERTIES  LABELS "vtkImagingGeneral")
