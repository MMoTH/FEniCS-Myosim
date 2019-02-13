# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Extraction
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Extraction
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersExtraction-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Extraction" "VTKFILTERSEXTRACTION_EXPORT")
set_tests_properties(vtkFiltersExtraction-HeaderTest PROPERTIES  LABELS "vtkFiltersExtraction")
