# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Generic
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Generic
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersGeneric-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Generic" "VTKFILTERSGENERIC_EXPORT")
set_tests_properties(vtkFiltersGeneric-HeaderTest PROPERTIES  LABELS "vtkFiltersGeneric")
