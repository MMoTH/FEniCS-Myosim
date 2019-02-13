# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Video
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/Video
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOVideo-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/Video" "VTKIOVIDEO_EXPORT")
set_tests_properties(vtkIOVideo-HeaderTest PROPERTIES  LABELS "vtkIOVideo")
