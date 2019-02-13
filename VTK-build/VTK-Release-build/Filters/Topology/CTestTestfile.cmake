# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Topology
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Topology
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersTopology-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Filters/Topology" "VTKFILTERSTOPOLOGY_EXPORT")
set_tests_properties(vtkFiltersTopology-HeaderTest PROPERTIES  LABELS "vtkFiltersTopology")
