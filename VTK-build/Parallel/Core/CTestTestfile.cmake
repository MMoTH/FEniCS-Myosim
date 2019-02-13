# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Parallel/Core
# Build directory: /home/fenics/shared/VTK-build/Parallel/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkParallelCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Parallel/Core" "VTKPARALLELCORE_EXPORT")
set_tests_properties(vtkParallelCore-HeaderTest PROPERTIES  LABELS "vtkParallelCore")
