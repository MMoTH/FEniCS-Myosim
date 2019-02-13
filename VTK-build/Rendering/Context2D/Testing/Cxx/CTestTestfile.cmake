# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Rendering/Context2D/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Rendering/Context2D/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkRenderingContext2DCxx-TestContext2D "/home/fenics/shared/VTK-build/bin/vtkRenderingContext2DCxxTests" "TestContext2D" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkRenderingContext2DCxx-TestContext2D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkRenderingContext2D" SKIP_RETURN_CODE "125")
add_test(vtkRenderingContext2DCxx-TestPolyDataToContext "/home/fenics/shared/VTK-build/bin/vtkRenderingContext2DCxxTests" "TestPolyDataToContext" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Rendering/Context2D/Testing/Data/Baseline/TestPolyDataToContext.png")
set_tests_properties(vtkRenderingContext2DCxx-TestPolyDataToContext PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkRenderingContext2D" SKIP_RETURN_CODE "125")
