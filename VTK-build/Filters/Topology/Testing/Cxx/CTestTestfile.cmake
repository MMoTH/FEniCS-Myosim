# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Topology/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Filters/Topology/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersTopologyCxx-TestFiberSurface "/home/fenics/shared/VTK-build/bin/vtkFiltersTopologyCxxTests" "TestFiberSurface" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkFiltersTopologyCxx-TestFiberSurface PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersTopology" SKIP_RETURN_CODE "125")
