# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/Extraction/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/Extraction/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersExtractionCxx-TestConvertSelection "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestConvertSelection" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestConvertSelection PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractBlock "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractBlock" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractBlock PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractDataArraysOverTime "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractDataArraysOverTime" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractDataArraysOverTime PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractThresholdsMultiBlock "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractThresholdsMultiBlock" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractThresholdsMultiBlock PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtraction "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtraction" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Filters/Extraction/Testing/Data/Baseline/TestExtraction.png")
set_tests_properties(vtkFiltersExtractionCxx-TestExtraction PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractionExpression "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractionExpression" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Filters/Extraction/Testing/Data/Baseline/TestExtractionExpression.png")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractionExpression PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractRectilinearGrid "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractRectilinearGrid" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractRectilinearGrid PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractRows "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractRows" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractRows PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractSelectedArraysOverTime "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractSelectedArraysOverTime" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractSelectedArraysOverTime PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractSelection "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractSelection" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/Filters/Extraction/Testing/Data/Baseline/TestExtractSelection.png")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractSelection PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
add_test(vtkFiltersExtractionCxx-TestExtractTimeSteps "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersExtractionCxxTests" "TestExtractTimeSteps" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersExtractionCxx-TestExtractTimeSteps PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersExtraction" SKIP_RETURN_CODE "125")
