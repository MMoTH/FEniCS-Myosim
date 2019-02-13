# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/SQL/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/VTK-Release-build/IO/SQL/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOSQLCxx-TestSQLDatabaseSchema "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOSQLCxxTests" "TestSQLDatabaseSchema" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkIOSQLCxx-TestSQLDatabaseSchema PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSQL" RUN_SERIAL "1" SKIP_RETURN_CODE "125")
add_test(vtkIOSQLCxx-TestSQLiteDatabase "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOSQLCxxTests" "TestSQLiteDatabase" "-D" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/VTK-Release-build/Testing/Temporary")
set_tests_properties(vtkIOSQLCxx-TestSQLiteDatabase PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSQL" RUN_SERIAL "1" SKIP_RETURN_CODE "125")
add_test(vtkIOSQLCxx-TestSQLiteTableReadWrite "/home/fenics/shared/VTK-build/VTK-Release-build/bin/vtkIOSQLCxxTests" "TestSQLiteTableReadWrite" "/home/fenics/shared/VTK-build/VTK-Release-build/ExternalData/IO/SQL/Testing/Data/Input/simple_table.vtk")
set_tests_properties(vtkIOSQLCxx-TestSQLiteTableReadWrite PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOSQL" RUN_SERIAL "1" SKIP_RETURN_CODE "125")
