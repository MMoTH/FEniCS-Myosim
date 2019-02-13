# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Color
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Common/Color
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonColor-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/Color" "VTKCOMMONCOLOR_EXPORT")
set_tests_properties(vtkCommonColor-HeaderTest PROPERTIES  LABELS "vtkCommonColor")
