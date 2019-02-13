# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/Filters/SMP/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/Filters/SMP/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkFiltersSMPCxx-TestSMPContour "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersSMPCxxTests" "TestSMPContour" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersSMPCxx-TestSMPContour PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersSMP" SKIP_RETURN_CODE "125")
add_test(vtkFiltersSMPCxx-TestThreadedSynchronizedTemplates3D "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersSMPCxxTests" "TestThreadedSynchronizedTemplates3D" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersSMPCxx-TestThreadedSynchronizedTemplates3D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersSMP" SKIP_RETURN_CODE "125")
add_test(vtkFiltersSMPCxx-TestThreadedSynchronizedTemplatesCutter3D "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersSMPCxxTests" "TestThreadedSynchronizedTemplatesCutter3D" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersSMPCxx-TestThreadedSynchronizedTemplatesCutter3D PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersSMP" SKIP_RETURN_CODE "125")
add_test(vtkFiltersSMPCxx-TestSMPTransform "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersSMPCxxTests" "TestSMPTransform" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersSMPCxx-TestSMPTransform PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersSMP" SKIP_RETURN_CODE "125")
add_test(vtkFiltersSMPCxx-TestSMPWarp "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkFiltersSMPCxxTests" "TestSMPWarp" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkFiltersSMPCxx-TestSMPWarp PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkFiltersSMP" SKIP_RETURN_CODE "125")
