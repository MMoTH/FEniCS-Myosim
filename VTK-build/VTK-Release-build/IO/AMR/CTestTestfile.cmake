# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/AMR
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/AMR
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOAMR-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/AMR" "VTKIOAMR_EXPORT")
set_tests_properties(vtkIOAMR-HeaderTest PROPERTIES  LABELS "vtkIOAMR")
