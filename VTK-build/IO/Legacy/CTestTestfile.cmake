# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Legacy
# Build directory: /home/fenics/shared/VTK-build/IO/Legacy
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOLegacy-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Legacy" "VTKIOLEGACY_EXPORT")
set_tests_properties(vtkIOLegacy-HeaderTest PROPERTIES  LABELS "vtkIOLegacy")
