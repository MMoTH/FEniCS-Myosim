# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/XML/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/XML/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOXMLCxx-TestAMRXMLIO "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestAMRXMLIO" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestAMRXMLIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestDataObjectXMLIO "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestDataObjectXMLIO" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestDataObjectXMLIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestMultiBlockXMLIOWithPartialArrays "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestMultiBlockXMLIOWithPartialArrays" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestMultiBlockXMLIOWithPartialArrays PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestReadDuplicateDataArrayNames "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestReadDuplicateDataArrayNames" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestReadDuplicateDataArrayNames PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXML "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXML" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/sample.xml")
set_tests_properties(vtkIOXMLCxx-TestXML PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLGhostCellsImport "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLGhostCellsImport" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/XML/Testing/Data/Baseline/TestXMLGhostCellsImport.png")
set_tests_properties(vtkIOXMLCxx-TestXMLGhostCellsImport PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLHierarchicalBoxDataFileConverter "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLHierarchicalBoxDataFileConverter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestXMLHierarchicalBoxDataFileConverter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLHyperTreeGridIO "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLHyperTreeGridIO" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestXMLHyperTreeGridIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLMappedUnstructuredGridIO "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLMappedUnstructuredGridIO" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestXMLMappedUnstructuredGridIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLToString "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLToString")
set_tests_properties(vtkIOXMLCxx-TestXMLToString PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLUnstructuredGridReader "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLUnstructuredGridReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/XML/Testing/Data/Baseline/TestXMLUnstructuredGridReader.png")
set_tests_properties(vtkIOXMLCxx-TestXMLUnstructuredGridReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLWriterWithDataArrayFallback "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLWriterWithDataArrayFallback" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestXMLWriterWithDataArrayFallback PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLWriteRead "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLWriteRead" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOXMLCxx-TestXMLWriteRead PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLCompositeDataReaderDistribution "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLCompositeDataReaderDistribution" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/distTest.vtm" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLCompositeDataReaderDistribution PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLReaderBadImageData "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLReaderBadData" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/badImageData.xml" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLReaderBadImageData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLReaderBadPolyData "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLReaderBadData" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/badPolyData.xml" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLReaderBadPolyData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLReaderBadRectilinearGridData "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLReaderBadData" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/badRectilinearGridData.xml" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLReaderBadRectilinearGridData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLReaderBadUnstucturedGridData "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLReaderBadData" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/badUnstructuredGridData.xml" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLReaderBadUnstucturedGridData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(vtkIOXMLCxx-TestXMLReaderBadUniformGridData "/home/fenics/shared/VTK-build/bin/vtkIOXMLCxxTests" "TestXMLReaderBadData" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/badUniformGridData.xml" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOXMLCxx-TestXMLReaderBadUniformGridData PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOXML" SKIP_RETURN_CODE "125")
add_test(TestXMLCInterface "/home/fenics/shared/VTK-build/bin/TestXMLCInterface")
