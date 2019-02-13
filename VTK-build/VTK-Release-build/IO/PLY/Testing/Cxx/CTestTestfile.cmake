# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/PLY/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/PLY/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOPLYCxx-TestPLYReader "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYReader" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYReader.png")
set_tests_properties(vtkIOPLYCxx-TestPLYReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYReaderIntensity "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYReaderIntensity" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYReaderIntensity.png")
set_tests_properties(vtkIOPLYCxx-TestPLYReaderIntensity PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYReaderPointCloud "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYReaderPointCloud" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYReaderPointCloud.png")
set_tests_properties(vtkIOPLYCxx-TestPLYReaderPointCloud PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYWriterAlpha "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYWriterAlpha" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYWriterAlpha.png")
set_tests_properties(vtkIOPLYCxx-TestPLYWriterAlpha PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYWriter "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYWriter" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkIOPLYCxx-TestPLYWriter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYReaderTextureUVPoints "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYReaderTextureUV" "squareTextured.ply" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYReaderTextureUVPoints.png")
set_tests_properties(vtkIOPLYCxx-TestPLYReaderTextureUVPoints PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
add_test(vtkIOPLYCxx-TestPLYReaderTextureUVFaces "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOPLYCxxTests" "TestPLYReaderTextureUV" "squareTexturedFaces.ply" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/PLY/Testing/Data/Baseline/TestPLYReaderTextureUVFaces.png")
set_tests_properties(vtkIOPLYCxx-TestPLYReaderTextureUVFaces PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOPLY" SKIP_RETURN_CODE "125")
