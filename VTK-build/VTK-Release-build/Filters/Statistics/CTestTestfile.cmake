# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Statistics
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Statistics
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersStatistics-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Statistics" "VTKFILTERSSTATISTICS_EXPORT")
set_tests_properties(vtkFiltersStatistics-HeaderTest PROPERTIES  LABELS "vtkFiltersStatistics")
