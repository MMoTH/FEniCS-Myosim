# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Domains/ChemistryOpenGL2/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Domains/ChemistryOpenGL2/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickShadows "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkDomainsChemistryOpenGL2CxxTests" "TestPDBBallAndStickShadows" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Domains/ChemistryOpenGL2/Testing/Data/Baseline/TestPDBBallAndStickShadows.png")
set_tests_properties(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickShadows PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistryOpenGL2" RUN_SERIAL "ON" SKIP_RETURN_CODE "125" TIMEOUT "360")
add_test(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickShadowsDOFSSAA "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkDomainsChemistryOpenGL2CxxTests" "TestPDBBallAndStickShadowsDOFSSAA" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Domains/ChemistryOpenGL2/Testing/Data/Baseline/TestPDBBallAndStickShadowsDOFSSAA.png")
set_tests_properties(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickShadowsDOFSSAA PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistryOpenGL2" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickTranslucent "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkDomainsChemistryOpenGL2CxxTests" "TestPDBBallAndStickTranslucent" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Domains/ChemistryOpenGL2/Testing/Data/Baseline/TestPDBBallAndStickTranslucent.png")
set_tests_properties(vtkDomainsChemistryOpenGL2Cxx-TestPDBBallAndStickTranslucent PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistryOpenGL2" SKIP_RETURN_CODE "125")
