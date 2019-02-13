# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Parallel
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Parallel
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersParallel-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Parallel" "VTKFILTERSPARALLEL_EXPORT")
set_tests_properties(vtkFiltersParallel-HeaderTest PROPERTIES  LABELS "vtkFiltersParallel")
