# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/ParallelXML
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/ParallelXML
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOParallelXML-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/ParallelXML" "VTKIOPARALLELXML_EXPORT")
set_tests_properties(vtkIOParallelXML-HeaderTest PROPERTIES  LABELS "vtkIOParallelXML")
