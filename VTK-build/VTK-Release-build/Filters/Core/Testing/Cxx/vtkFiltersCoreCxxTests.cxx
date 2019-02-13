#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "vtkTestDriver.h"



/* Forward declare test functions. */
int TestAppendArcLength(int, char*[]);
int TestAppendFilter(int, char*[]);
int TestAppendMolecule(int, char*[]);
int TestAppendPolyData(int, char*[]);
int TestAppendSelection(int, char*[]);
int TestArrayCalculator(int, char*[]);
int TestAssignAttribute(int, char*[]);
int TestBinCellDataFilter(int, char*[]);
int TestCategoricalPointDataToCellData(int, char*[]);
int TestCategoricalResampleWithDataSet(int, char*[]);
int TestCellDataToPointData(int, char*[]);
int TestCenterOfMass(int, char*[]);
int TestCleanPolyData(int, char*[]);
int TestCleanPolyData2(int, char*[]);
int TestClipPolyData(int, char*[]);
int TestConnectivityFilter(int, char*[]);
int TestCutter(int, char*[]);
int TestDecimatePolylineFilter(int, char*[]);
int TestDecimatePro(int, char*[]);
int TestDelaunay2D(int, char*[]);
int TestDelaunay2DBestFittingPlane(int, char*[]);
int TestDelaunay2DFindTriangle(int, char*[]);
int TestDelaunay2DMeshes(int, char*[]);
int TestDelaunay3D(int, char*[]);
int TestExecutionTimer(int, char*[]);
int TestFeatureEdges(int, char*[]);
int TestFlyingEdges(int, char*[]);
int TestGlyph3D(int, char*[]);
int TestHedgeHog(int, char*[]);
int TestImplicitPolyDataDistance(int, char*[]);
int TestMaskPoints(int, char*[]);
int TestNamedComponents(int, char*[]);
int TestPointDataToCellData(int, char*[]);
int TestPolyDataConnectivityFilter(int, char*[]);
int TestProbeFilter(int, char*[]);
int TestProbeFilterImageInput(int, char*[]);
int TestProbeFilterOutputAttributes(int, char*[]);
int TestResampleToImage(int, char*[]);
int TestResampleToImage2D(int, char*[]);
int TestResampleWithDataSet(int, char*[]);
int TestResampleWithDataSet2(int, char*[]);
int TestResampleWithDataSet3(int, char*[]);
int TestRemoveDuplicatePolys(int, char*[]);
int TestSmoothPolyDataFilter(int, char*[]);
int TestSMPPipelineContour(int, char*[]);
int TestStripper(int, char*[]);
int TestStructuredGridAppend(int, char*[]);
int TestThreshold(int, char*[]);
int TestThresholdPoints(int, char*[]);
int TestTransposeTable(int, char*[]);
int TestTriangleMeshPointNormals(int, char*[]);
int TestTubeFilter(int, char*[]);
int TestUnstructuredGridQuadricDecimation(int, char*[]);
int UnitTestMaskPoints(int, char*[]);
int UnitTestMergeFilter(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "TestAppendArcLength",
    TestAppendArcLength
  },
  {
    "TestAppendFilter",
    TestAppendFilter
  },
  {
    "TestAppendMolecule",
    TestAppendMolecule
  },
  {
    "TestAppendPolyData",
    TestAppendPolyData
  },
  {
    "TestAppendSelection",
    TestAppendSelection
  },
  {
    "TestArrayCalculator",
    TestArrayCalculator
  },
  {
    "TestAssignAttribute",
    TestAssignAttribute
  },
  {
    "TestBinCellDataFilter",
    TestBinCellDataFilter
  },
  {
    "TestCategoricalPointDataToCellData",
    TestCategoricalPointDataToCellData
  },
  {
    "TestCategoricalResampleWithDataSet",
    TestCategoricalResampleWithDataSet
  },
  {
    "TestCellDataToPointData",
    TestCellDataToPointData
  },
  {
    "TestCenterOfMass",
    TestCenterOfMass
  },
  {
    "TestCleanPolyData",
    TestCleanPolyData
  },
  {
    "TestCleanPolyData2",
    TestCleanPolyData2
  },
  {
    "TestClipPolyData",
    TestClipPolyData
  },
  {
    "TestConnectivityFilter",
    TestConnectivityFilter
  },
  {
    "TestCutter",
    TestCutter
  },
  {
    "TestDecimatePolylineFilter",
    TestDecimatePolylineFilter
  },
  {
    "TestDecimatePro",
    TestDecimatePro
  },
  {
    "TestDelaunay2D",
    TestDelaunay2D
  },
  {
    "TestDelaunay2DBestFittingPlane",
    TestDelaunay2DBestFittingPlane
  },
  {
    "TestDelaunay2DFindTriangle",
    TestDelaunay2DFindTriangle
  },
  {
    "TestDelaunay2DMeshes",
    TestDelaunay2DMeshes
  },
  {
    "TestDelaunay3D",
    TestDelaunay3D
  },
  {
    "TestExecutionTimer",
    TestExecutionTimer
  },
  {
    "TestFeatureEdges",
    TestFeatureEdges
  },
  {
    "TestFlyingEdges",
    TestFlyingEdges
  },
  {
    "TestGlyph3D",
    TestGlyph3D
  },
  {
    "TestHedgeHog",
    TestHedgeHog
  },
  {
    "TestImplicitPolyDataDistance",
    TestImplicitPolyDataDistance
  },
  {
    "TestMaskPoints",
    TestMaskPoints
  },
  {
    "TestNamedComponents",
    TestNamedComponents
  },
  {
    "TestPointDataToCellData",
    TestPointDataToCellData
  },
  {
    "TestPolyDataConnectivityFilter",
    TestPolyDataConnectivityFilter
  },
  {
    "TestProbeFilter",
    TestProbeFilter
  },
  {
    "TestProbeFilterImageInput",
    TestProbeFilterImageInput
  },
  {
    "TestProbeFilterOutputAttributes",
    TestProbeFilterOutputAttributes
  },
  {
    "TestResampleToImage",
    TestResampleToImage
  },
  {
    "TestResampleToImage2D",
    TestResampleToImage2D
  },
  {
    "TestResampleWithDataSet",
    TestResampleWithDataSet
  },
  {
    "TestResampleWithDataSet2",
    TestResampleWithDataSet2
  },
  {
    "TestResampleWithDataSet3",
    TestResampleWithDataSet3
  },
  {
    "TestRemoveDuplicatePolys",
    TestRemoveDuplicatePolys
  },
  {
    "TestSmoothPolyDataFilter",
    TestSmoothPolyDataFilter
  },
  {
    "TestSMPPipelineContour",
    TestSMPPipelineContour
  },
  {
    "TestStripper",
    TestStripper
  },
  {
    "TestStructuredGridAppend",
    TestStructuredGridAppend
  },
  {
    "TestThreshold",
    TestThreshold
  },
  {
    "TestThresholdPoints",
    TestThresholdPoints
  },
  {
    "TestTransposeTable",
    TestTransposeTable
  },
  {
    "TestTriangleMeshPointNormals",
    TestTriangleMeshPointNormals
  },
  {
    "TestTubeFilter",
    TestTubeFilter
  },
  {
    "TestUnstructuredGridQuadricDecimation",
    TestUnstructuredGridQuadricDecimation
  },
  {
    "UnitTestMaskPoints",
    UnitTestMaskPoints
  },
  {
    "UnitTestMergeFilter",
    UnitTestMergeFilter
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
