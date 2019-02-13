# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Import
# Build directory: /home/fenics/shared/VTK-build/IO/Import
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOImport-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Import" "VTKIOIMPORT_EXPORT")
set_tests_properties(vtkIOImport-HeaderTest PROPERTIES  LABELS "vtkIOImport")
