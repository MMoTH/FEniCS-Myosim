# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/Misc
# Build directory: /home/fenics/shared/VTK-build/Common/Misc
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonMisc-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/Misc" "VTKCOMMONMISC_EXPORT")
set_tests_properties(vtkCommonMisc-HeaderTest PROPERTIES  LABELS "vtkCommonMisc")
