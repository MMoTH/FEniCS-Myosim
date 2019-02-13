# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/Image
# Build directory: /home/fenics/shared/VTK-build/Rendering/Image
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingImage-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Rendering/Image" "VTKRENDERINGIMAGE_EXPORT")
set_tests_properties(vtkRenderingImage-HeaderTest PROPERTIES  LABELS "vtkRenderingImage")
