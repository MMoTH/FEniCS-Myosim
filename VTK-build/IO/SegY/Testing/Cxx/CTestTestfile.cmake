# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/SegY/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/SegY/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOSegYCxx-TestSegY2DReader "/home/fenics/shared/VTK-build/bin/vtkIOSegYCxxTests" "TestSegY2DReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/SegY/Testing/Data/Baseline/TestSegY2DReader.png")
set_tests_properties(vtkIOSegYCxx-TestSegY2DReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSegY" SKIP_RETURN_CODE "125")
add_test(vtkIOSegYCxx-TestSegY2DReaderZoom "/home/fenics/shared/VTK-build/bin/vtkIOSegYCxxTests" "TestSegY2DReaderZoom" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/SegY/Testing/Data/Baseline/TestSegY2DReaderZoom.png")
set_tests_properties(vtkIOSegYCxx-TestSegY2DReaderZoom PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSegY" SKIP_RETURN_CODE "125")
add_test(vtkIOSegYCxx-TestSegY3DReader "/home/fenics/shared/VTK-build/bin/vtkIOSegYCxxTests" "TestSegY3DReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/SegY/Testing/Data/Baseline/TestSegY3DReader.png")
set_tests_properties(vtkIOSegYCxx-TestSegY3DReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSegY" SKIP_RETURN_CODE "125")
