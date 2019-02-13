#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "vtkTestDriver.h"



/* Forward declare test functions. */
int LagrangeHexahedron(int, char*[]);
int TestAngularPeriodicDataArray(int, char*[]);
int TestColor(int, char*[]);
int TestVector(int, char*[]);
int TestVectorOperators(int, char*[]);
int TestAMRBox(int, char*[]);
int TestBiQuadraticQuad(int, char*[]);
int TestCompositeDataSets(int, char*[]);
int TestComputeBoundingSphere(int, char*[]);
int TestDataArrayDispatcher(int, char*[]);
int TestDataObject(int, char*[]);
int TestDispatchers(int, char*[]);
int TestFieldList(int, char*[]);
int TestGenericCell(int, char*[]);
int TestGraph(int, char*[]);
int TestGraph2(int, char*[]);
int TestGraphAttributes(int, char*[]);
int TestHigherOrderCell(int, char*[]);
int TestImageDataFindCell(int, char*[]);
int TestImageDataInterpolation(int, char*[]);
int TestImageIterator(int, char*[]);
int TestInterpolationDerivs(int, char*[]);
int TestInterpolationFunctions(int, char*[]);
int TestMappedGridDeepCopy(int, char*[]);
int TestPath(int, char*[]);
int TestPentagonalPrism(int, char*[]);
int TestPiecewiseFunctionLogScale(int, char*[]);
int TestPixelExtent(int, char*[]);
int TestPointLocators(int, char*[]);
int TestPolyDataRemoveCell(int, char*[]);
int TestPolygon(int, char*[]);
int TestPolygonBoundedTriangulate(int, char*[]);
int TestPolyhedron0(int, char*[]);
int TestPolyhedron1(int, char*[]);
int TestPolyhedron3(int, char*[]);
int TestPolyhedronCombinatorialContouring(int, char*[]);
int TestPolyhedronConvexity(int, char*[]);
int TestQuadraticPolygon(int, char*[]);
int TestRect(int, char*[]);
int TestSelectionExpression(int, char*[]);
int TestSelectionSubtract(int, char*[]);
int TestSortFieldData(int, char*[]);
int TestTable(int, char*[]);
int TestTreeBFSIterator(int, char*[]);
int TestTreeDFSIterator(int, char*[]);
int TestTriangle(int, char*[]);
int TimePointLocators(int, char*[]);
int otherCellArray(int, char*[]);
int otherCellBoundaries(int, char*[]);
int otherCellPosition(int, char*[]);
int otherCellTypes(int, char*[]);
int otherColorTransferFunction(int, char*[]);
int otherEmptyCell(int, char*[]);
int otherFieldData(int, char*[]);
int otherImageData(int, char*[]);
int otherRectilinearGrid(int, char*[]);
int otherStructuredGrid(int, char*[]);
int otherUniformGrid(int, char*[]);
int quadCellConsistency(int, char*[]);
int quadraticEvaluation(int, char*[]);
int TestBoundingBox(int, char*[]);
int TestPlane(int, char*[]);
int TestStaticCellLinks(int, char*[]);
int TestStructuredData(int, char*[]);
int TestDataObjectTypes(int, char*[]);
int TestPolyDataRemoveDeletedCells(int, char*[]);
int UnitTestCells(int, char*[]);
int UnitTestImplicitDataSet(int, char*[]);
int UnitTestImplicitVolume(int, char*[]);
int UnitTestLine(int, char*[]);
int UnitTestPlanesIntersection(int, char*[]);
int UnitTestTriangleIntersection(int, char*[]);
int TestLagrangeTriangle(int, char*[]);
int TestLagrangeTetra(int, char*[]);
int TestLagrangeWedge(int, char*[]);
int quadraticIntersection(int, char*[]);
int TestCellIterators(int, char*[]);
int TestCellLocator(int, char*[]);
int TestMeanValueCoordinatesInterpolation1(int, char*[]);
int TestMeanValueCoordinatesInterpolation2(int, char*[]);
int TestPolyhedron4(int, char*[]);
int TestSmoothErrorMetric(int, char*[]);
int TestQuadraticPolygonFilters(int, char*[]);
int TestPolyhedron2(int, char*[]);
int TestPolyhedronContouring(int, char*[]);
int TestPolyhedronCutter(int, char*[]);
int TestKdTreeRepresentation(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "LagrangeHexahedron",
    LagrangeHexahedron
  },
  {
    "TestAngularPeriodicDataArray",
    TestAngularPeriodicDataArray
  },
  {
    "TestColor",
    TestColor
  },
  {
    "TestVector",
    TestVector
  },
  {
    "TestVectorOperators",
    TestVectorOperators
  },
  {
    "TestAMRBox",
    TestAMRBox
  },
  {
    "TestBiQuadraticQuad",
    TestBiQuadraticQuad
  },
  {
    "TestCompositeDataSets",
    TestCompositeDataSets
  },
  {
    "TestComputeBoundingSphere",
    TestComputeBoundingSphere
  },
  {
    "TestDataArrayDispatcher",
    TestDataArrayDispatcher
  },
  {
    "TestDataObject",
    TestDataObject
  },
  {
    "TestDispatchers",
    TestDispatchers
  },
  {
    "TestFieldList",
    TestFieldList
  },
  {
    "TestGenericCell",
    TestGenericCell
  },
  {
    "TestGraph",
    TestGraph
  },
  {
    "TestGraph2",
    TestGraph2
  },
  {
    "TestGraphAttributes",
    TestGraphAttributes
  },
  {
    "TestHigherOrderCell",
    TestHigherOrderCell
  },
  {
    "TestImageDataFindCell",
    TestImageDataFindCell
  },
  {
    "TestImageDataInterpolation",
    TestImageDataInterpolation
  },
  {
    "TestImageIterator",
    TestImageIterator
  },
  {
    "TestInterpolationDerivs",
    TestInterpolationDerivs
  },
  {
    "TestInterpolationFunctions",
    TestInterpolationFunctions
  },
  {
    "TestMappedGridDeepCopy",
    TestMappedGridDeepCopy
  },
  {
    "TestPath",
    TestPath
  },
  {
    "TestPentagonalPrism",
    TestPentagonalPrism
  },
  {
    "TestPiecewiseFunctionLogScale",
    TestPiecewiseFunctionLogScale
  },
  {
    "TestPixelExtent",
    TestPixelExtent
  },
  {
    "TestPointLocators",
    TestPointLocators
  },
  {
    "TestPolyDataRemoveCell",
    TestPolyDataRemoveCell
  },
  {
    "TestPolygon",
    TestPolygon
  },
  {
    "TestPolygonBoundedTriangulate",
    TestPolygonBoundedTriangulate
  },
  {
    "TestPolyhedron0",
    TestPolyhedron0
  },
  {
    "TestPolyhedron1",
    TestPolyhedron1
  },
  {
    "TestPolyhedron3",
    TestPolyhedron3
  },
  {
    "TestPolyhedronCombinatorialContouring",
    TestPolyhedronCombinatorialContouring
  },
  {
    "TestPolyhedronConvexity",
    TestPolyhedronConvexity
  },
  {
    "TestQuadraticPolygon",
    TestQuadraticPolygon
  },
  {
    "TestRect",
    TestRect
  },
  {
    "TestSelectionExpression",
    TestSelectionExpression
  },
  {
    "TestSelectionSubtract",
    TestSelectionSubtract
  },
  {
    "TestSortFieldData",
    TestSortFieldData
  },
  {
    "TestTable",
    TestTable
  },
  {
    "TestTreeBFSIterator",
    TestTreeBFSIterator
  },
  {
    "TestTreeDFSIterator",
    TestTreeDFSIterator
  },
  {
    "TestTriangle",
    TestTriangle
  },
  {
    "TimePointLocators",
    TimePointLocators
  },
  {
    "otherCellArray",
    otherCellArray
  },
  {
    "otherCellBoundaries",
    otherCellBoundaries
  },
  {
    "otherCellPosition",
    otherCellPosition
  },
  {
    "otherCellTypes",
    otherCellTypes
  },
  {
    "otherColorTransferFunction",
    otherColorTransferFunction
  },
  {
    "otherEmptyCell",
    otherEmptyCell
  },
  {
    "otherFieldData",
    otherFieldData
  },
  {
    "otherImageData",
    otherImageData
  },
  {
    "otherRectilinearGrid",
    otherRectilinearGrid
  },
  {
    "otherStructuredGrid",
    otherStructuredGrid
  },
  {
    "otherUniformGrid",
    otherUniformGrid
  },
  {
    "quadCellConsistency",
    quadCellConsistency
  },
  {
    "quadraticEvaluation",
    quadraticEvaluation
  },
  {
    "TestBoundingBox",
    TestBoundingBox
  },
  {
    "TestPlane",
    TestPlane
  },
  {
    "TestStaticCellLinks",
    TestStaticCellLinks
  },
  {
    "TestStructuredData",
    TestStructuredData
  },
  {
    "TestDataObjectTypes",
    TestDataObjectTypes
  },
  {
    "TestPolyDataRemoveDeletedCells",
    TestPolyDataRemoveDeletedCells
  },
  {
    "UnitTestCells",
    UnitTestCells
  },
  {
    "UnitTestImplicitDataSet",
    UnitTestImplicitDataSet
  },
  {
    "UnitTestImplicitVolume",
    UnitTestImplicitVolume
  },
  {
    "UnitTestLine",
    UnitTestLine
  },
  {
    "UnitTestPlanesIntersection",
    UnitTestPlanesIntersection
  },
  {
    "UnitTestTriangleIntersection",
    UnitTestTriangleIntersection
  },
  {
    "TestLagrangeTriangle",
    TestLagrangeTriangle
  },
  {
    "TestLagrangeTetra",
    TestLagrangeTetra
  },
  {
    "TestLagrangeWedge",
    TestLagrangeWedge
  },
  {
    "quadraticIntersection",
    quadraticIntersection
  },
  {
    "TestCellIterators",
    TestCellIterators
  },
  {
    "TestCellLocator",
    TestCellLocator
  },
  {
    "TestMeanValueCoordinatesInterpolation1",
    TestMeanValueCoordinatesInterpolation1
  },
  {
    "TestMeanValueCoordinatesInterpolation2",
    TestMeanValueCoordinatesInterpolation2
  },
  {
    "TestPolyhedron4",
    TestPolyhedron4
  },
  {
    "TestSmoothErrorMetric",
    TestSmoothErrorMetric
  },
  {
    "TestQuadraticPolygonFilters",
    TestQuadraticPolygonFilters
  },
  {
    "TestPolyhedron2",
    TestPolyhedron2
  },
  {
    "TestPolyhedronContouring",
    TestPolyhedronContouring
  },
  {
    "TestPolyhedronCutter",
    TestPolyhedronCutter
  },
  {
    "TestKdTreeRepresentation",
    TestKdTreeRepresentation
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
