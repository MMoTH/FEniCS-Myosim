# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Views/Core
# Build directory: /home/fenics/shared/VTK-build/Views/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkViewsCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Views/Core" "VTKVIEWSCORE_EXPORT")
set_tests_properties(vtkViewsCore-HeaderTest PROPERTIES  LABELS "vtkViewsCore")
