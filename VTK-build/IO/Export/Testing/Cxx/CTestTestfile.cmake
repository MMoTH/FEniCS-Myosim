# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Export/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/Export/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOExportCxx-X3DTest "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "X3DTest" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-X3DTest PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
add_test(vtkIOExportCxx-TestOBJExporter "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "TestOBJExporter" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-TestOBJExporter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
add_test(vtkIOExportCxx-TestGLTFExporter "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "TestGLTFExporter" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-TestGLTFExporter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
add_test(vtkIOExportCxx-TestSingleVTPExporter "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "TestSingleVTPExporter" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-TestSingleVTPExporter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
add_test(vtkIOExportCxx-TestRIBExporter "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "TestRIBExporter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-TestRIBExporter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
add_test(vtkIOExportCxx-UnitTestRIB "/home/fenics/shared/VTK-build/bin/vtkIOExportCxxTests" "UnitTestRIB" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary")
set_tests_properties(vtkIOExportCxx-UnitTestRIB PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExport" SKIP_RETURN_CODE "125")
