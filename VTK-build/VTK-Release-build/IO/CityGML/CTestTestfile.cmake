# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/CityGML
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/CityGML
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOCityGML-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/CityGML" "VTKIOCITYGML_EXPORT")
set_tests_properties(vtkIOCityGML-HeaderTest PROPERTIES  LABELS "vtkIOCityGML")
