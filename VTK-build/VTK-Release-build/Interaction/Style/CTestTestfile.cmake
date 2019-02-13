# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Interaction/Style
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Interaction/Style
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInteractionStyle-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Interaction/Style" "VTKINTERACTIONSTYLE_EXPORT")
set_tests_properties(vtkInteractionStyle-HeaderTest PROPERTIES  LABELS "vtkInteractionStyle")
