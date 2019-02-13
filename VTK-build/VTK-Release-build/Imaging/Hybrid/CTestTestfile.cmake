# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Hybrid
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Imaging/Hybrid
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingHybrid-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Hybrid" "VTKIMAGINGHYBRID_EXPORT")
set_tests_properties(vtkImagingHybrid-HeaderTest PROPERTIES  LABELS "vtkImagingHybrid")
