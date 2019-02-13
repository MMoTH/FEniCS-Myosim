# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/CityGML/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/CityGML/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOCityGMLCxx-TestCityGMLReader "/home/fenics/shared/VTK-build/bin/vtkIOCityGMLCxxTests" "TestCityGMLReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/CityGML/Testing/Data/Baseline/TestCityGMLReader.png")
set_tests_properties(vtkIOCityGMLCxx-TestCityGMLReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOCityGML" SKIP_RETURN_CODE "125")
