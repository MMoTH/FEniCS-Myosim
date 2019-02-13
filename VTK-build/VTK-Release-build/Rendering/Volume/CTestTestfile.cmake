# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/Volume
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Rendering/Volume
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingVolume-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Rendering/Volume" "VTKRENDERINGVOLUME_EXPORT")
set_tests_properties(vtkRenderingVolume-HeaderTest PROPERTIES  LABELS "vtkRenderingVolume")
