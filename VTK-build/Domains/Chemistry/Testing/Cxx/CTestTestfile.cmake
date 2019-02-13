# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Domains/Chemistry/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Domains/Chemistry/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkDomainsChemistryCxx-TestBallAndStick "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestBallAndStick" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestBallAndStick.png")
set_tests_properties(vtkDomainsChemistryCxx-TestBallAndStick PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestPDBBallAndStick "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestPDBBallAndStick" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestPDBBallAndStick.png")
set_tests_properties(vtkDomainsChemistryCxx-TestPDBBallAndStick PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" RUN_SERIAL "ON" SKIP_RETURN_CODE "125" TIMEOUT "360")
add_test(vtkDomainsChemistryCxx-TestBondColorModeDiscreteByAtom "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestBondColorModeDiscreteByAtom" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestBondColorModeDiscreteByAtom.png")
set_tests_properties(vtkDomainsChemistryCxx-TestBondColorModeDiscreteByAtom PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestBondColorModeSingleColor "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestBondColorModeSingleColor" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestBondColorModeSingleColor.png")
set_tests_properties(vtkDomainsChemistryCxx-TestBondColorModeSingleColor PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestCompositeRender "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestCompositeRender" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestCompositeRender.png")
set_tests_properties(vtkDomainsChemistryCxx-TestCompositeRender PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestCustomArrayRadius "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestCustomArrayRadius" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestCustomArrayRadius.png")
set_tests_properties(vtkDomainsChemistryCxx-TestCustomArrayRadius PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestFastRender "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestFastRender" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestFastRender.png")
set_tests_properties(vtkDomainsChemistryCxx-TestFastRender PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestLiquoriceSticks "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestLiquoriceSticks" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestLiquoriceSticks.png")
set_tests_properties(vtkDomainsChemistryCxx-TestLiquoriceSticks PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMolecule "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMolecule" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestMolecule PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMoleculeIOLegacy "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMoleculeIOLegacy" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestMoleculeIOLegacy.png")
set_tests_properties(vtkDomainsChemistryCxx-TestMoleculeIOLegacy PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMoleculeSelection "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMoleculeSelection" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestMoleculeSelection PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMoleculeMapperPropertyUpdate "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMoleculeMapperPropertyUpdate" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestMoleculeMapperPropertyUpdate.png")
set_tests_properties(vtkDomainsChemistryCxx-TestMoleculeMapperPropertyUpdate PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMoleculeToLines "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMoleculeToLines" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestMoleculeToLines PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMultiCylinderOn "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMultiCylinderOn" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestMultiCylinderOn.png")
set_tests_properties(vtkDomainsChemistryCxx-TestMultiCylinderOn PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestMultiCylinderOff "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestMultiCylinderOff" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestMultiCylinderOff.png")
set_tests_properties(vtkDomainsChemistryCxx-TestMultiCylinderOff PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestPeriodicTable "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestPeriodicTable" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestPeriodicTable PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestPointSetToMoleculeFilter "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestPointSetToMoleculeFilter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestPointSetToMoleculeFilter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestProgrammableElectronicData "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestProgrammableElectronicData" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestProgrammableElectronicData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestProteinRibbon "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestProteinRibbon" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestProteinRibbon.png")
set_tests_properties(vtkDomainsChemistryCxx-TestProteinRibbon PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestSimpleBondPerceiver "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestSimpleBondPerceiver" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkDomainsChemistryCxx-TestSimpleBondPerceiver PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestVASPAnimationReader "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestVASPAnimationReader" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/VASP/NPT_Z_ANIMATE.out" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestVASPAnimationReader.png")
set_tests_properties(vtkDomainsChemistryCxx-TestVASPAnimationReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestVASPTessellationReader "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestVASPTessellationReader" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/VASP/NPT_Z_TESSELLATE.out" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestVASPTessellationReader.png")
set_tests_properties(vtkDomainsChemistryCxx-TestVASPTessellationReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestVDWSpheres "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestVDWSpheres" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestVDWSpheres.png")
set_tests_properties(vtkDomainsChemistryCxx-TestVDWSpheres PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
add_test(vtkDomainsChemistryCxx-TestCMLMoleculeReader "/home/fenics/shared/VTK-build/bin/vtkDomainsChemistryCxxTests" "TestCMLMoleculeReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/Domains/Chemistry/Testing/Data/Baseline/TestCMLMoleculeReader.png")
set_tests_properties(vtkDomainsChemistryCxx-TestCMLMoleculeReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkDomainsChemistry" SKIP_RETURN_CODE "125")
