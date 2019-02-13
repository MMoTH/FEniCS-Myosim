# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Legacy/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/Legacy/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOLegacyCxx-TestLegacyCompositeDataReaderWriter "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOLegacyCxxTests" "TestLegacyCompositeDataReaderWriter" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkIOLegacyCxx-TestLegacyCompositeDataReaderWriter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOLegacy" SKIP_RETURN_CODE "125")
add_test(vtkIOLegacyCxx-TestLegacyGhostCellsImport "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOLegacyCxxTests" "TestLegacyGhostCellsImport" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/Legacy/Testing/Data/Baseline/TestLegacyGhostCellsImport.png")
set_tests_properties(vtkIOLegacyCxx-TestLegacyGhostCellsImport PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOLegacy" SKIP_RETURN_CODE "125")
add_test(vtkIOLegacyCxx-TestLegacyArrayMetaData "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOLegacyCxxTests" "TestLegacyArrayMetaData" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkIOLegacyCxx-TestLegacyArrayMetaData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOLegacy" SKIP_RETURN_CODE "125")
