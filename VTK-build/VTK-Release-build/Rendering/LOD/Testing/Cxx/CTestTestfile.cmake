# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/LOD/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Rendering/LOD/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingLODCxx-TestLODActor "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkRenderingLODCxxTests" "TestLODActor" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkRenderingLODCxx-TestLODActor PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkRenderingLOD" SKIP_RETURN_CODE "125")
