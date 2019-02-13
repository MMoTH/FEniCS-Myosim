# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Infovis/Core
# Build directory: /home/fenics/shared/VTK-build/Infovis/Core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkInfovisCore-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Infovis/Core" "VTKINFOVISCORE_EXPORT")
set_tests_properties(vtkInfovisCore-HeaderTest PROPERTIES  LABELS "vtkInfovisCore")
