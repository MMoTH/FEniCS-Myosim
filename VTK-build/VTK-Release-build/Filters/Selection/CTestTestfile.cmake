# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Selection
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Selection
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersSelection-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Selection" "VTKFILTERSSELECTION_EXPORT")
set_tests_properties(vtkFiltersSelection-HeaderTest PROPERTIES  LABELS "vtkFiltersSelection")
