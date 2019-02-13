# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Parallel/Core/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Parallel/Core/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkParallelCoreCxx-TestFieldDataSerialization "/home/fenics/shared/VTK-build/bin/vtkParallelCoreCxxTests" "TestFieldDataSerialization")
set_tests_properties(vtkParallelCoreCxx-TestFieldDataSerialization PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkParallelCore" SKIP_RETURN_CODE "125")
add_test(vtkParallelCore-TestSocketCommunicator "/usr/bin/python2" "/home/fenics/shared/VTK/CMake/vtkTestDriver.py" "--process" "/home/fenics/shared/VTK-build/bin/vtkParallelCore-TestSocketCommunicator" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "--server" "--process" "/home/fenics/shared/VTK-build/bin/vtkParallelCore-TestSocketCommunicator" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
