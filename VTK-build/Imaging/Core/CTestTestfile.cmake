# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Core
# Build directory: /home/fenics/shared/VTK-build/Imaging/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Core" "VTKIMAGINGCORE_EXPORT")
set_tests_properties(vtkImagingCore-HeaderTest PROPERTIES  LABELS "vtkImagingCore")
