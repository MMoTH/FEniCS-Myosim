# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Imaging/Fourier
# Build directory: /home/fenics/shared/VTK-build/Imaging/Fourier
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkImagingFourier-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Imaging/Fourier" "VTKIMAGINGFOURIER_EXPORT")
set_tests_properties(vtkImagingFourier-HeaderTest PROPERTIES  LABELS "vtkImagingFourier")
