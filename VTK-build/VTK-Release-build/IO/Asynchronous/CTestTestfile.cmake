# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Asynchronous
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/Asynchronous
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOAsynchronous-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Asynchronous" "VTKIOASYNCHRONOUS_EXPORT")
set_tests_properties(vtkIOAsynchronous-HeaderTest PROPERTIES  LABELS "vtkIOAsynchronous")
