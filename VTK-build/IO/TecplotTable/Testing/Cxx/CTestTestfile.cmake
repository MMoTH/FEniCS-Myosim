# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/TecplotTable/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/TecplotTable/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOTecplotTableCxx-TestTecplotTableReader "/home/fenics/shared/VTK-build/bin/vtkIOTecplotTableCxxTests" "TestTecplotTableReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOTecplotTableCxx-TestTecplotTableReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOTecplotTable" SKIP_RETURN_CODE "125")
add_test(TestTecplotTableReader "/home/fenics/shared/VTK-build/bin/vtkIOTecplotTableCxxTests" "TestTecplotTableReader" "-D" "/home/fenics/shared/VTK-build/ExternalData/IO/TecplotTable/Testing/Data/residuals.dat")
