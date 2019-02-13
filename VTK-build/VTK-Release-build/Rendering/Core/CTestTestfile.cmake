# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/Core
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Rendering/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Rendering/Core" "VTKRENDERINGCORE_EXPORT")
set_tests_properties(vtkRenderingCore-HeaderTest PROPERTIES  LABELS "vtkRenderingCore")
