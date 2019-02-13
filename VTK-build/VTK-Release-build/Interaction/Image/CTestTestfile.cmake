# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Interaction/Image
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Interaction/Image
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInteractionImage-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Interaction/Image" "VTKINTERACTIONIMAGE_EXPORT")
set_tests_properties(vtkInteractionImage-HeaderTest PROPERTIES  LABELS "vtkInteractionImage")
