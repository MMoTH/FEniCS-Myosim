# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/General
# Build directory: /home/fenics/shared/VTK-build/Filters/General
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersGeneral-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/General" "VTKFILTERSGENERAL_EXPORT")
set_tests_properties(vtkFiltersGeneral-HeaderTest PROPERTIES  LABELS "vtkFiltersGeneral")
