# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Web
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/Web
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOWeb-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Web" "VTKIOWEB_EXPORT")
set_tests_properties(vtkIOWeb-HeaderTest PROPERTIES  LABELS "vtkIOWeb")
