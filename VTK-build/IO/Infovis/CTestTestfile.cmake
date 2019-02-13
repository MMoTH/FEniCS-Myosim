# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Infovis
# Build directory: /home/fenics/shared/VTK-build/IO/Infovis
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOInfovis-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Infovis" "VTKIOINFOVIS_EXPORT")
set_tests_properties(vtkIOInfovis-HeaderTest PROPERTIES  LABELS "vtkIOInfovis")
