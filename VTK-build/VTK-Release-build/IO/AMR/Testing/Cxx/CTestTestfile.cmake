# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/AMR/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/AMR/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOAMRCxx-TestAMReXParticlesReader "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOAMRCxxTests" "TestAMReXParticlesReader" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing")
set_tests_properties(vtkIOAMRCxx-TestAMReXParticlesReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOAMR" SKIP_RETURN_CODE "125")
add_test(vtkIOAMRCxx-TestEnzoReader "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOAMRCxxTests" "TestEnzoReader" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing")
set_tests_properties(vtkIOAMRCxx-TestEnzoReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOAMR" SKIP_RETURN_CODE "125")
