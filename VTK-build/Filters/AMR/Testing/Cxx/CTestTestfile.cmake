# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/AMR/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/Filters/AMR/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersAMRCxx-TestAMRGhostLayerStripping "/home/fenics/shared/VTK-build/bin/vtkFiltersAMRCxxTests" "TestAMRGhostLayerStripping" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkFiltersAMRCxx-TestAMRGhostLayerStripping PROPERTIES  FAIL_REGULAR_EXPRESSION "Error" LABELS "vtkFiltersAMR" SKIP_RETURN_CODE "125")
add_test(vtkFiltersAMRCxx-TestAMRBlanking "/home/fenics/shared/VTK-build/bin/vtkFiltersAMRCxxTests" "TestAMRBlanking" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkFiltersAMRCxx-TestAMRBlanking PROPERTIES  FAIL_REGULAR_EXPRESSION "Error" LABELS "vtkFiltersAMR" SKIP_RETURN_CODE "125")
add_test(vtkFiltersAMRCxx-TestAMRIterator "/home/fenics/shared/VTK-build/bin/vtkFiltersAMRCxxTests" "TestAMRIterator" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkFiltersAMRCxx-TestAMRIterator PROPERTIES  FAIL_REGULAR_EXPRESSION "Error" LABELS "vtkFiltersAMR" SKIP_RETURN_CODE "125")
add_test(vtkFiltersAMRCxx-TestImageToAMR "/home/fenics/shared/VTK-build/bin/vtkFiltersAMRCxxTests" "TestImageToAMR" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkFiltersAMRCxx-TestImageToAMR PROPERTIES  FAIL_REGULAR_EXPRESSION "Error" LABELS "vtkFiltersAMR" SKIP_RETURN_CODE "125")
