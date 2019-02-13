# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Infovis/Layout
# Build directory: /home/fenics/shared/VTK-build/Infovis/Layout
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInfovisLayout-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Infovis/Layout" "VTKINFOVISLAYOUT_EXPORT")
set_tests_properties(vtkInfovisLayout-HeaderTest PROPERTIES  LABELS "vtkInfovisLayout")
