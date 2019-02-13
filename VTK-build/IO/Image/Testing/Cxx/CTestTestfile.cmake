# CMake generated Testfile for 
# Source directory: /home/fenics/shared/VTK/IO/Image/Testing/Cxx
# Build directory: /home/fenics/shared/VTK-build/IO/Image/Testing/Cxx
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(vtkIOImageCxx-TestNrrdReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestNrrdReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestNrrdReader.png")
set_tests_properties(vtkIOImageCxx-TestNrrdReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestNIFTIReaderWriter "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestNIFTIReaderWriter" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestNIFTIReaderWriter.png")
set_tests_properties(vtkIOImageCxx-TestNIFTIReaderWriter PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestNIFTIReaderAnalyze "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestNIFTIReaderAnalyze" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestNIFTIReaderAnalyze.png")
set_tests_properties(vtkIOImageCxx-TestNIFTIReaderAnalyze PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestNIFTI2 "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestNIFTI2" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-T" "/home/fenics/shared/VTK-build/Testing/Temporary" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestNIFTI2.png")
set_tests_properties(vtkIOImageCxx-TestNIFTI2 PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestDataObjectIO "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestDataObjectIO")
set_tests_properties(vtkIOImageCxx-TestDataObjectIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestMetaIO "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestMetaIO" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/HeadMRVolume.mhd")
set_tests_properties(vtkIOImageCxx-TestMetaIO PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestImportExport "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestImportExport")
set_tests_properties(vtkIOImageCxx-TestImportExport PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestJPEGReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestJPEGReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/beach.jpg" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestJPEGReader.png")
set_tests_properties(vtkIOImageCxx-TestJPEGReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestDICOMImageReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestDICOMImageReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/dicom/prostate.IMG" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestDICOMImageReader.png")
set_tests_properties(vtkIOImageCxx-TestDICOMImageReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestDICOMImageReaderFileCollection "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestDICOMImageReaderFileCollection" "collection" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestDICOMImageReaderFileCollection.png")
set_tests_properties(vtkIOImageCxx-TestDICOMImageReaderFileCollection PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestBMPReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestBMPReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/masonry.bmp" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestBMPReader.png")
set_tests_properties(vtkIOImageCxx-TestBMPReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestBMPReaderDoNotAllow8BitBMP "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestBMPReaderDoNotAllow8BitBMP" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/masonry.bmp" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestBMPReaderDoNotAllow8BitBMP.png")
set_tests_properties(vtkIOImageCxx-TestBMPReaderDoNotAllow8BitBMP PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestSEPReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestSEPReader" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestSEPReader.png")
set_tests_properties(vtkIOImageCxx-TestSEPReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderMultipleMulti "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReaderMultiple" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/multipage_tiff_example.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderMultipleMulti PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderMultipleNormal "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReaderMultiple" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/test.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderMultipleNormal PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderMultipleTiled "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReaderMultiple" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/tiled_10x30_tiff_example.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderMultipleTiled PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderMulti "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/multipage_tiff_example.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestTIFFReaderMulti.png")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderMulti PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderTiled "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/tiled_64x64_tiff_example.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestTIFFReaderTiled.png")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderTiled PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestTIFFReaderTiledRGB "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestTIFFReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/libtiff/gourds_tiled_200x300.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestTIFFReaderTiledRGB.png")
set_tests_properties(vtkIOImageCxx-TestTIFFReaderTiledRGB PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestCompressedTIFFReader "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestCompressedTIFFReader" "/home/fenics/shared/VTK-build/ExternalData/Testing/Data/al_foam_smallest.0.tif" "-D" "/home/fenics/shared/VTK-build/ExternalData//Testing" "-V" "/home/fenics/shared/VTK-build/ExternalData/IO/Image/Testing/Data/Baseline/TestCompressedTIFFReader.png")
set_tests_properties(vtkIOImageCxx-TestCompressedTIFFReader PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestWriteToMemoryPNG "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestWriteToMemory" "test.png")
set_tests_properties(vtkIOImageCxx-TestWriteToMemoryPNG PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestWriteToMemoryJPEG "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestWriteToMemory" "test.jpeg")
set_tests_properties(vtkIOImageCxx-TestWriteToMemoryJPEG PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
add_test(vtkIOImageCxx-TestWriteToMemoryBMP "/home/fenics/shared/VTK-build/bin/vtkIOImageCxxTests" "TestWriteToMemory" "test.bmp")
set_tests_properties(vtkIOImageCxx-TestWriteToMemoryBMP PROPERTIES  FAIL_REGULAR_EXPRESSION "(
|^)ERROR: ;instance(s)? still around" LABELS "vtkIOImage" SKIP_RETURN_CODE "125")
