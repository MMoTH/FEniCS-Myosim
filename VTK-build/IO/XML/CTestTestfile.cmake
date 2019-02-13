# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/XML
# Build directory: /home/fenics/shared/VTK-build/IO/XML
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOXML-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/XML" "VTKIOXML_EXPORT")
set_tests_properties(vtkIOXML-HeaderTest PROPERTIES  LABELS "vtkIOXML")
