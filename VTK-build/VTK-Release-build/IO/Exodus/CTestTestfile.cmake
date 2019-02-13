# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Exodus
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/Exodus
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOExodus-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Exodus" "VTKIOEXODUS_EXPORT")
set_tests_properties(vtkIOExodus-HeaderTest PROPERTIES  LABELS "vtkIOExodus")
