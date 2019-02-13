# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/ExportPDF
# Build directory: /home/fenics/shared/VTK-build/IO/ExportPDF
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOExportPDF-HeaderTest "/usr/bin/python2" "/home/fenics/shared/VTK/Testing/Core/HeaderTesting.py" "/home/fenics/shared/VTK/IO/ExportPDF" "VTKIOEXPORTPDF_EXPORT")
set_tests_properties(vtkIOExportPDF-HeaderTest PROPERTIES  LABELS "vtkIOExportPDF")
