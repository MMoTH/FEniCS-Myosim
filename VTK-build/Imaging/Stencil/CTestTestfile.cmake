# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Stencil
# Build directory: /home/fenics/shared/VTK-build/Imaging/Stencil
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingStencil-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Stencil" "VTKIMAGINGSTENCIL_EXPORT")
set_tests_properties(vtkImagingStencil-HeaderTest PROPERTIES  LABELS "vtkImagingStencil")
