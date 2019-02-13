# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Views/Infovis
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Views/Infovis
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkViewsInfovis-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Views/Infovis" "VTKVIEWSINFOVIS_EXPORT")
set_tests_properties(vtkViewsInfovis-HeaderTest PROPERTIES  LABELS "vtkViewsInfovis")
