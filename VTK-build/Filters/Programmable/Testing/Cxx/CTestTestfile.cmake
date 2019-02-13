# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Programmable/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Filters/Programmable/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersProgrammableCxx-TestProgrammableFilter "/home/fenics/shared/VTK-build/bin/vtkFiltersProgrammableCxxTests" "TestProgrammableFilter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkFiltersProgrammableCxx-TestProgrammableFilter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersProgrammable" SKIP_RETURN_CODE "125")
add_test(vtkFiltersProgrammableCxx-TestProgrammableGlyph "/home/fenics/shared/VTK-build/bin/vtkFiltersProgrammableCxxTests" "TestProgrammableGlyph" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Filters/Programmable/Testing/Data/Baseline/TestProgrammableGlyph.png")
set_tests_properties(vtkFiltersProgrammableCxx-TestProgrammableGlyph PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersProgrammable" SKIP_RETURN_CODE "125")
