# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/NetCDF
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/NetCDF
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIONetCDF-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/NetCDF" "VTKIONETCDF_EXPORT")
set_tests_properties(vtkIONetCDF-HeaderTest PROPERTIES  LABELS "vtkIONetCDF")
