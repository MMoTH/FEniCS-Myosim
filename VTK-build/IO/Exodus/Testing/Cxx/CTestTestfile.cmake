# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Exodus/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/Exodus/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOExodusCxx-TestExodusAttributes "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestExodusAttributes" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOExodusCxx-TestExodusAttributes PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExodus" SKIP_RETURN_CODE "125")
add_test(vtkIOExodusCxx-TestExodusIgnoreFileTime "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestExodusIgnoreFileTime" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOExodusCxx-TestExodusIgnoreFileTime PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExodus" SKIP_RETURN_CODE "125")
add_test(vtkIOExodusCxx-TestExodusSideSets "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestExodusSideSets" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOExodusCxx-TestExodusSideSets PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExodus" SKIP_RETURN_CODE "125")
add_test(vtkIOExodusCxx-TestMultiBlockExodusWrite "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestMultiBlockExodusWrite" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Exodus/Testing/Data/Baseline/TestMultiBlockExodusWrite.png")
set_tests_properties(vtkIOExodusCxx-TestMultiBlockExodusWrite PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOExodus" SKIP_RETURN_CODE "125")
add_test(vtkIOExodusCxx-Tetra15 "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestExodusTetra15" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Exodus/Testing/Data/Baseline/TestExodusTetra15.png" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/tetra15.g")
add_test(vtkIOExodusCxx-Wedge21 "/home/fenics/shared/VTK-build/bin/vtkIOExodusCxxTests" "TestExodusWedge21" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Exodus/Testing/Data/Baseline/TestExodusWedge21.png" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/wedge21.g")
