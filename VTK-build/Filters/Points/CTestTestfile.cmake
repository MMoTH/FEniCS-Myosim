# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Points
# Build directory: /home/fenics/shared/VTK-build/Filters/Points
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersPoints-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Points" "VTKFILTERSPOINTS_EXPORT")
set_tests_properties(vtkFiltersPoints-HeaderTest PROPERTIES  LABELS "vtkFiltersPoints")
