# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Statistics
# Build directory: /home/fenics/shared/VTK-build/Imaging/Statistics
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingStatistics-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Statistics" "VTKIMAGINGSTATISTICS_EXPORT")
set_tests_properties(vtkImagingStatistics-HeaderTest PROPERTIES  LABELS "vtkImagingStatistics")
