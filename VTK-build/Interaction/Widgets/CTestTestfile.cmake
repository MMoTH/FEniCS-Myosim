# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Interaction/Widgets
# Build directory: /home/fenics/shared/VTK-build/Interaction/Widgets
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInteractionWidgets-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Interaction/Widgets" "VTKINTERACTIONWIDGETS_EXPORT")
set_tests_properties(vtkInteractionWidgets-HeaderTest PROPERTIES  LABELS "vtkInteractionWidgets")
