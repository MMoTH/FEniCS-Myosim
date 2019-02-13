# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/LOD
# Build directory: /home/fenics/shared/VTK-build/Rendering/LOD
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingLOD-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Rendering/LOD" "VTKRENDERINGLOD_EXPORT")
set_tests_properties(vtkRenderingLOD-HeaderTest PROPERTIES  LABELS "vtkRenderingLOD")
