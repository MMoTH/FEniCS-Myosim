# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Common/ExecutionModel
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Common/ExecutionModel
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkCommonExecutionModel-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/Common/ExecutionModel" "VTKCOMMONEXECUTIONMODEL_EXPORT")
set_tests_properties(vtkCommonExecutionModel-HeaderTest PROPERTIES  LABELS "vtkCommonExecutionModel")
