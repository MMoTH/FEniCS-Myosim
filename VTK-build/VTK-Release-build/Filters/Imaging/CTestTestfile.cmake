# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Imaging
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Imaging
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersImaging-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Imaging" "VTKFILTERSIMAGING_EXPORT")
set_tests_properties(vtkFiltersImaging-HeaderTest PROPERTIES  LABELS "vtkFiltersImaging")
