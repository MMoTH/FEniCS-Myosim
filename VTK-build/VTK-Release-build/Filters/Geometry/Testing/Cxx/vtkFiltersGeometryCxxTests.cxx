#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "vtkTestDriver.h"



/* Forward declare test functions. */
int TestExtractSurfaceNonLinearSubdivision(int, char*[]);
int TestDataSetSurfaceFieldData(int, char*[]);
int TestDataSetSurfaceFilterQuadraticTetsGhostCells(int, char*[]);
int TestDataSetSurfaceFilterWith1DGrids(int, char*[]);
int TestDataSetRegionSurfaceFilter(int, char*[]);
int TestImageDataToUniformGrid(int, char*[]);
int TestLinearToQuadraticCellsFilter(int, char*[]);
int TestProjectSphereFilter(int, char*[]);
int TestStructuredAMRNeighbor(int, char*[]);
int TestUniformGridGhostDataGenerator(int, char*[]);
int TestUnstructuredGridGeometryFilter(int, char*[]);
int TestUnstructuredGridGeometryFilterGhostCells(int, char*[]);
int TestGeometryFilterCellData(int, char*[]);
int TestStructuredAMRGridConnectivity(int, char*[]);
int TestStructuredGridConnectivity(int, char*[]);
int TestStructuredGridGhostDataGenerator(int, char*[]);
int UnitTestDataSetSurfaceFilter(int, char*[]);
int UnitTestProjectSphereFilter(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "TestExtractSurfaceNonLinearSubdivision",
    TestExtractSurfaceNonLinearSubdivision
  },
  {
    "TestDataSetSurfaceFieldData",
    TestDataSetSurfaceFieldData
  },
  {
    "TestDataSetSurfaceFilterQuadraticTetsGhostCells",
    TestDataSetSurfaceFilterQuadraticTetsGhostCells
  },
  {
    "TestDataSetSurfaceFilterWith1DGrids",
    TestDataSetSurfaceFilterWith1DGrids
  },
  {
    "TestDataSetRegionSurfaceFilter",
    TestDataSetRegionSurfaceFilter
  },
  {
    "TestImageDataToUniformGrid",
    TestImageDataToUniformGrid
  },
  {
    "TestLinearToQuadraticCellsFilter",
    TestLinearToQuadraticCellsFilter
  },
  {
    "TestProjectSphereFilter",
    TestProjectSphereFilter
  },
  {
    "TestStructuredAMRNeighbor",
    TestStructuredAMRNeighbor
  },
  {
    "TestUniformGridGhostDataGenerator",
    TestUniformGridGhostDataGenerator
  },
  {
    "TestUnstructuredGridGeometryFilter",
    TestUnstructuredGridGeometryFilter
  },
  {
    "TestUnstructuredGridGeometryFilterGhostCells",
    TestUnstructuredGridGeometryFilterGhostCells
  },
  {
    "TestGeometryFilterCellData",
    TestGeometryFilterCellData
  },
  {
    "TestStructuredAMRGridConnectivity",
    TestStructuredAMRGridConnectivity
  },
  {
    "TestStructuredGridConnectivity",
    TestStructuredGridConnectivity
  },
  {
    "TestStructuredGridGhostDataGenerator",
    TestStructuredGridGhostDataGenerator
  },
  {
    "UnitTestDataSetSurfaceFilter",
    UnitTestDataSetSurfaceFilter
  },
  {
    "UnitTestProjectSphereFilter",
    UnitTestProjectSphereFilter
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
