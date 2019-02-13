# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Movie/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/Movie/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOMovieCxx-TestOggTheoraWriter "/home/fenics/shared/VTK-build/bin/vtkIOMovieCxxTests" "TestOggTheoraWriter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOMovieCxx-TestOggTheoraWriter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOMovie" SKIP_RETURN_CODE "125")
