#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "vtkTestDriver.h"



/* Forward declare test functions. */
int TestBlockOpacity(int, char*[]);
int TestBlockVisibility(int, char*[]);
int TestCompositeDataPointGaussian(int, char*[]);
int TestCompositeDataPointGaussianSelection(int, char*[]);
int TestCompositePolyDataMapper2(int, char*[]);
int TestCompositePolyDataMapper2Picking(int, char*[]);
int TestCompositePolyDataMapper2Scalars(int, char*[]);
int TestCompositePolyDataMapper2CellScalars(int, char*[]);
int TestCompositePolyDataMapper2MixedGeometryCellScalars(int, char*[]);
int TestCompositePolyDataMapper2MixedGeometryEdges(int, char*[]);
int TestGlyph3DMapperTreeIndexingCompositeGlyphs(int, char*[]);
int TestMultiBlockPartialArrayPointData(int, char*[]);
int TestMultiBlockPartialArrayFieldData(int, char*[]);
int TestTranslucentLUTAlphaBlending(int, char*[]);
int TestTranslucentLUTTextureAlphaBlending(int, char*[]);
int TestAreaSelections(int, char*[]);
int TestValuePassFloatingPoint(int, char*[]);
int TestToggleOSWithInteractor(int, char*[]);
int otherCoordinate(int, char*[]);
int FrustumClip(int, char*[]);
int Mace(int, char*[]);
int RGrid(int, char*[]);
int TestActor2D(int, char*[]);
int TestActor2DTextures(int, char*[]);
int TestActorLightingFlag(int, char*[]);
int TestAnimationScene(int, char*[]);
int TestAssemblyBounds(int, char*[]);
int TestBackfaceCulling(int, char*[]);
int TestBareScalarsToColors(int, char*[]);
int TestColorByCellDataStringArray(int, char*[]);
int TestColorByPointDataStringArray(int, char*[]);
int TestColorByStringArrayDefaultLookupTable(int, char*[]);
int TestColorByStringArrayDefaultLookupTable2D(int, char*[]);
int TestColorTransferFunction(int, char*[]);
int TestColorTransferFunctionStringArray(int, char*[]);
int TestDirectScalarsToColors(int, char*[]);
int TestDiscretizableColorTransferFunction(int, char*[]);
int TestDiscretizableColorTransferFunctionStringArray(int, char*[]);
int TestDiscretizableColorTransferFunctionOpacity(int, char*[]);
int TestEdgeFlags(int, char*[]);
int TestFollowerPicking(int, char*[]);
int TestGlyph3DMapper(int, char*[]);
int TestGlyph3DMapper2(int, char*[]);
int TestGlyph3DMapperArrow(int, char*[]);
int TestGlyph3DMapperIndexing(int, char*[]);
int TestGlyph3DMapperMasking(int, char*[]);
int TestGlyph3DMapperOrientationArray(int, char*[]);
int TestGlyph3DMapperQuaternionArray(int, char*[]);
int TestGlyph3DMapperPicking(int, char*[]);
int TestGlyph3DMapperTreeIndexing(int, char*[]);
int TestGradientBackground(int, char*[]);
int TestHiddenLineRemovalPass(int, char*[]);
int TestHomogeneousTransformOfActor(int, char*[]);
int TestImageAndAnnotations(int, char*[]);
int TestInteractorStyleImageProperty(int, char*[]);
int TestInteractorTimers(int, char*[]);
int TestLabeledContourMapper(int, char*[]);
int TestLabeledContourMapperWithActorMatrix(int, char*[]);
int TestPickingManager(int, char*[]);
int TestManyActors(int, char*[]);
int TestMapVectorsAsRGBColors(int, char*[]);
int TestMapVectorsToColors(int, char*[]);
int TestOffAxisStereo(int, char*[]);
int TestOrderedTriangulator(int, char*[]);
int TestOpacity(int, char*[]);
int TestStereoBackgroundLeft(int, char*[]);
int TestStereoBackgroundRight(int, char*[]);
int TestOSConeCxx(int, char*[]);
int TestOnAndOffScreenConeCxx(int, char*[]);
int TestPickTextActor(int, char*[]);
int TestPointSelection(int, char*[]);
int TestPointSelectionWithCellData(int, char*[]);
int TestPolygonSelection(int, char*[]);
int TestResetCameraVerticalAspectRatio(int, char*[]);
int TestResetCameraVerticalAspectRatioParallel(int, char*[]);
int TestSplitViewportStereoHorizontal(int, char*[]);
int TestTexturedBackground(int, char*[]);
int TestTextureSize(int, char*[]);
int TestTextureRGBA(int, char*[]);
int TestTextureRGBADepthPeeling(int, char*[]);
int TestTilingCxx(int, char*[]);
int TestTransformCoordinateUseDouble(int, char*[]);
int TestTranslucentImageActorAlphaBlending(int, char*[]);
int TestTranslucentImageActorDepthPeeling(int, char*[]);
int TestTranslucentLUTDepthPeeling(int, char*[]);
int TestTranslucentLUTTextureDepthPeeling(int, char*[]);
int TestTStripsColorsTCoords(int, char*[]);
int TestTStripsNormalsColorsTCoords(int, char*[]);
int TestTStripsNormalsTCoords(int, char*[]);
int TestTStripsTCoords(int, char*[]);
int TestWindowToImageFilter(int, char*[]);
int otherLookupTable(int, char*[]);
int otherLookupTableWithEnabling(int, char*[]);
int RenderNonFinite(int, char*[]);
int SurfacePlusEdges(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "TestBlockOpacity",
    TestBlockOpacity
  },
  {
    "TestBlockVisibility",
    TestBlockVisibility
  },
  {
    "TestCompositeDataPointGaussian",
    TestCompositeDataPointGaussian
  },
  {
    "TestCompositeDataPointGaussianSelection",
    TestCompositeDataPointGaussianSelection
  },
  {
    "TestCompositePolyDataMapper2",
    TestCompositePolyDataMapper2
  },
  {
    "TestCompositePolyDataMapper2Picking",
    TestCompositePolyDataMapper2Picking
  },
  {
    "TestCompositePolyDataMapper2Scalars",
    TestCompositePolyDataMapper2Scalars
  },
  {
    "TestCompositePolyDataMapper2CellScalars",
    TestCompositePolyDataMapper2CellScalars
  },
  {
    "TestCompositePolyDataMapper2MixedGeometryCellScalars",
    TestCompositePolyDataMapper2MixedGeometryCellScalars
  },
  {
    "TestCompositePolyDataMapper2MixedGeometryEdges",
    TestCompositePolyDataMapper2MixedGeometryEdges
  },
  {
    "TestGlyph3DMapperTreeIndexingCompositeGlyphs",
    TestGlyph3DMapperTreeIndexingCompositeGlyphs
  },
  {
    "TestMultiBlockPartialArrayPointData",
    TestMultiBlockPartialArrayPointData
  },
  {
    "TestMultiBlockPartialArrayFieldData",
    TestMultiBlockPartialArrayFieldData
  },
  {
    "TestTranslucentLUTAlphaBlending",
    TestTranslucentLUTAlphaBlending
  },
  {
    "TestTranslucentLUTTextureAlphaBlending",
    TestTranslucentLUTTextureAlphaBlending
  },
  {
    "TestAreaSelections",
    TestAreaSelections
  },
  {
    "TestValuePassFloatingPoint",
    TestValuePassFloatingPoint
  },
  {
    "TestToggleOSWithInteractor",
    TestToggleOSWithInteractor
  },
  {
    "otherCoordinate",
    otherCoordinate
  },
  {
    "FrustumClip",
    FrustumClip
  },
  {
    "Mace",
    Mace
  },
  {
    "RGrid",
    RGrid
  },
  {
    "TestActor2D",
    TestActor2D
  },
  {
    "TestActor2DTextures",
    TestActor2DTextures
  },
  {
    "TestActorLightingFlag",
    TestActorLightingFlag
  },
  {
    "TestAnimationScene",
    TestAnimationScene
  },
  {
    "TestAssemblyBounds",
    TestAssemblyBounds
  },
  {
    "TestBackfaceCulling",
    TestBackfaceCulling
  },
  {
    "TestBareScalarsToColors",
    TestBareScalarsToColors
  },
  {
    "TestColorByCellDataStringArray",
    TestColorByCellDataStringArray
  },
  {
    "TestColorByPointDataStringArray",
    TestColorByPointDataStringArray
  },
  {
    "TestColorByStringArrayDefaultLookupTable",
    TestColorByStringArrayDefaultLookupTable
  },
  {
    "TestColorByStringArrayDefaultLookupTable2D",
    TestColorByStringArrayDefaultLookupTable2D
  },
  {
    "TestColorTransferFunction",
    TestColorTransferFunction
  },
  {
    "TestColorTransferFunctionStringArray",
    TestColorTransferFunctionStringArray
  },
  {
    "TestDirectScalarsToColors",
    TestDirectScalarsToColors
  },
  {
    "TestDiscretizableColorTransferFunction",
    TestDiscretizableColorTransferFunction
  },
  {
    "TestDiscretizableColorTransferFunctionStringArray",
    TestDiscretizableColorTransferFunctionStringArray
  },
  {
    "TestDiscretizableColorTransferFunctionOpacity",
    TestDiscretizableColorTransferFunctionOpacity
  },
  {
    "TestEdgeFlags",
    TestEdgeFlags
  },
  {
    "TestFollowerPicking",
    TestFollowerPicking
  },
  {
    "TestGlyph3DMapper",
    TestGlyph3DMapper
  },
  {
    "TestGlyph3DMapper2",
    TestGlyph3DMapper2
  },
  {
    "TestGlyph3DMapperArrow",
    TestGlyph3DMapperArrow
  },
  {
    "TestGlyph3DMapperIndexing",
    TestGlyph3DMapperIndexing
  },
  {
    "TestGlyph3DMapperMasking",
    TestGlyph3DMapperMasking
  },
  {
    "TestGlyph3DMapperOrientationArray",
    TestGlyph3DMapperOrientationArray
  },
  {
    "TestGlyph3DMapperQuaternionArray",
    TestGlyph3DMapperQuaternionArray
  },
  {
    "TestGlyph3DMapperPicking",
    TestGlyph3DMapperPicking
  },
  {
    "TestGlyph3DMapperTreeIndexing",
    TestGlyph3DMapperTreeIndexing
  },
  {
    "TestGradientBackground",
    TestGradientBackground
  },
  {
    "TestHiddenLineRemovalPass",
    TestHiddenLineRemovalPass
  },
  {
    "TestHomogeneousTransformOfActor",
    TestHomogeneousTransformOfActor
  },
  {
    "TestImageAndAnnotations",
    TestImageAndAnnotations
  },
  {
    "TestInteractorStyleImageProperty",
    TestInteractorStyleImageProperty
  },
  {
    "TestInteractorTimers",
    TestInteractorTimers
  },
  {
    "TestLabeledContourMapper",
    TestLabeledContourMapper
  },
  {
    "TestLabeledContourMapperWithActorMatrix",
    TestLabeledContourMapperWithActorMatrix
  },
  {
    "TestPickingManager",
    TestPickingManager
  },
  {
    "TestManyActors",
    TestManyActors
  },
  {
    "TestMapVectorsAsRGBColors",
    TestMapVectorsAsRGBColors
  },
  {
    "TestMapVectorsToColors",
    TestMapVectorsToColors
  },
  {
    "TestOffAxisStereo",
    TestOffAxisStereo
  },
  {
    "TestOrderedTriangulator",
    TestOrderedTriangulator
  },
  {
    "TestOpacity",
    TestOpacity
  },
  {
    "TestStereoBackgroundLeft",
    TestStereoBackgroundLeft
  },
  {
    "TestStereoBackgroundRight",
    TestStereoBackgroundRight
  },
  {
    "TestOSConeCxx",
    TestOSConeCxx
  },
  {
    "TestOnAndOffScreenConeCxx",
    TestOnAndOffScreenConeCxx
  },
  {
    "TestPickTextActor",
    TestPickTextActor
  },
  {
    "TestPointSelection",
    TestPointSelection
  },
  {
    "TestPointSelectionWithCellData",
    TestPointSelectionWithCellData
  },
  {
    "TestPolygonSelection",
    TestPolygonSelection
  },
  {
    "TestResetCameraVerticalAspectRatio",
    TestResetCameraVerticalAspectRatio
  },
  {
    "TestResetCameraVerticalAspectRatioParallel",
    TestResetCameraVerticalAspectRatioParallel
  },
  {
    "TestSplitViewportStereoHorizontal",
    TestSplitViewportStereoHorizontal
  },
  {
    "TestTexturedBackground",
    TestTexturedBackground
  },
  {
    "TestTextureSize",
    TestTextureSize
  },
  {
    "TestTextureRGBA",
    TestTextureRGBA
  },
  {
    "TestTextureRGBADepthPeeling",
    TestTextureRGBADepthPeeling
  },
  {
    "TestTilingCxx",
    TestTilingCxx
  },
  {
    "TestTransformCoordinateUseDouble",
    TestTransformCoordinateUseDouble
  },
  {
    "TestTranslucentImageActorAlphaBlending",
    TestTranslucentImageActorAlphaBlending
  },
  {
    "TestTranslucentImageActorDepthPeeling",
    TestTranslucentImageActorDepthPeeling
  },
  {
    "TestTranslucentLUTDepthPeeling",
    TestTranslucentLUTDepthPeeling
  },
  {
    "TestTranslucentLUTTextureDepthPeeling",
    TestTranslucentLUTTextureDepthPeeling
  },
  {
    "TestTStripsColorsTCoords",
    TestTStripsColorsTCoords
  },
  {
    "TestTStripsNormalsColorsTCoords",
    TestTStripsNormalsColorsTCoords
  },
  {
    "TestTStripsNormalsTCoords",
    TestTStripsNormalsTCoords
  },
  {
    "TestTStripsTCoords",
    TestTStripsTCoords
  },
  {
    "TestWindowToImageFilter",
    TestWindowToImageFilter
  },
  {
    "otherLookupTable",
    otherLookupTable
  },
  {
    "otherLookupTableWithEnabling",
    otherLookupTableWithEnabling
  },
  {
    "RenderNonFinite",
    RenderNonFinite
  },
  {
    "SurfacePlusEdges",
    SurfacePlusEdges
  },

  {0,0}
};

/* Allocate and create a lowercased copy of string
   (note that it has to be free'd manually) */

static char* lowercase(const char *string)
{
  char *new_string, *p;

#ifdef __cplusplus
  new_string = static_cast<char *>(malloc(sizeof(char) *
    static_cast<size_t>(strlen(string) + 1)));
#else
  new_string = (char *)(malloc(sizeof(char) * (size_t)(strlen(string) + 1)));
#endif

  if (!new_string)
    {
    return 0;
    }
  strcpy(new_string, string);
  p = new_string;
  while (*p != 0)
    {
#ifdef __cplusplus
    *p = static_cast<char>(tolower(*p));
#else
    *p = (char)(tolower(*p));
#endif

    ++p;
    }
  return new_string;
}

int main(int ac, char *av[])
{
  int i, NumTests, testNum = 0, partial_match;
  char *arg, *test_name;
  int count;
  int testToRun = -1;

  

  for(count =0; cmakeGeneratedFunctionMapEntries[count].name != 0; count++)
    {
    }
  NumTests = count;
  /* If no test name was given */
  /* process command line with user function.  */
  if (ac < 2)
    {
    /* Ask for a test.  */
    printf("Available tests:\n");
    for (i =0; i < NumTests; ++i)
      {
      printf("%3d. %s\n", i, cmakeGeneratedFunctionMapEntries[i].name);
      }
    printf("To run a test, enter the test number: ");
    fflush(stdout);
    if( scanf("%d", &testNum) != 1 )
      {
      printf("Couldn't parse that input as a number\n");
      return -1;
      }
    if (testNum >= NumTests)
      {
      printf("%3d is an invalid test number.\n", testNum);
      return -1;
      }
    testToRun = testNum;
    ac--;
    av++;
    }
  partial_match = 0;
  arg = 0;
  /* If partial match is requested.  */
  if(testToRun == -1 && ac > 1)
    {
    partial_match = (strcmp(av[1], "-R") == 0) ? 1 : 0;
    }
  if (partial_match && ac < 3)
    {
    printf("-R needs an additional parameter.\n");
    return -1;
    }
  if(testToRun == -1)
    {
    arg = lowercase(av[1 + partial_match]);
    }
  for (i =0; i < NumTests && testToRun == -1; ++i)
    {
    test_name = lowercase(cmakeGeneratedFunctionMapEntries[i].name);
    if (partial_match && strstr(test_name, arg) != NULL)
      {
      testToRun = i;
      ac -=2;
      av += 2;
      }
    else if (!partial_match && strcmp(test_name, arg) == 0)
      {
      testToRun = i;
      ac--;
      av++;
      }
    free(test_name);
    }
  if(arg)
    {
    free(arg);
    }
  if(testToRun != -1)
    {
    int result;
    vtksys::SystemInformation::SetStackTraceOnError(1);
 
    if (testToRun < 0 || testToRun >= NumTests)
      {
      printf(
        "testToRun was modified by TestDriver code to an invalid value: %3d.\n",
        testNum);
      return -1;
      }
    result = (*cmakeGeneratedFunctionMapEntries[testToRun].func)(ac, av);

    return result;
    }


  /* Nothing was run, display the test names.  */
  printf("Available tests:\n");
  for (i =0; i < NumTests; ++i)
    {
    printf("%3d. %s\n", i, cmakeGeneratedFunctionMapEntries[i].name);
    }
  printf("Failed: %s is an invalid test name.\n", av[1]);

  return -1;
}
