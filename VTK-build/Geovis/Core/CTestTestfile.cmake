# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Geovis/Core
# Build directory: /home/fenics/shared/VTK-build/Geovis/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkGeovisCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Geovis/Core" "VTKGEOVISCORE_EXPORT")
set_tests_properties(vtkGeovisCore-HeaderTest PROPERTIES  LABELS "vtkGeovisCore")
