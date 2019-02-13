#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "vtkTestDriver.h"



/* Forward declare test functions. */
int TestHyperTreeGridBinary2D(int, char*[]);
int TestHyperTreeGridBinary2DAxisClipBox(int, char*[]);
int TestHyperTreeGridBinary2DAxisClipEllipse(int, char*[]);
int TestHyperTreeGridBinary2DAxisClipPlanes(int, char*[]);
int TestHyperTreeGridBinary2DAxisReflectionXCenter(int, char*[]);
int TestHyperTreeGridBinary2DAxisReflectionXCenterMaterial(int, char*[]);
int TestHyperTreeGridBinary2DAxisReflectionYCenter(int, char*[]);
int TestHyperTreeGridBinary2DAxisReflectionYCenterMaterial(int, char*[]);
int TestHyperTreeGridBinary2DIJK(int, char*[]);
int TestHyperTreeGridBinary2DCellCenters(int, char*[]);
int TestHyperTreeGridBinary2DCellCentersMaterial(int, char*[]);
int TestHyperTreeGridBinary2DContour(int, char*[]);
int TestHyperTreeGridBinary2DContourMaterial(int, char*[]);
int TestHyperTreeGridBinary2DDepthLimiter(int, char*[]);
int TestHyperTreeGridBinary2DDepthLimiterMaterial(int, char*[]);
int TestHyperTreeGridBinary2DInterfaceMaterial(int, char*[]);
int TestHyperTreeGridBinary2DMaterial(int, char*[]);
int TestHyperTreeGridBinary2DMaterialIJK(int, char*[]);
int TestHyperTreeGridBinary2DThreshold(int, char*[]);
int TestHyperTreeGridBinary2DThresholdMaterial(int, char*[]);
int TestHyperTreeGridBinary2DVector(int, char*[]);
int TestHyperTreeGridBinary2DVectorAxisReflectionXCenter(int, char*[]);
int TestHyperTreeGridBinary2DVectorAxisReflectionYCenter(int, char*[]);
int TestHyperTreeGridBinary3DContour(int, char*[]);
int TestHyperTreeGridBinary3DGeometry(int, char*[]);
int TestHyperTreeGridBinaryClipPlanes(int, char*[]);
int TestHyperTreeGridBinaryEllipseMaterial(int, char*[]);
int TestHyperTreeGridBinaryHyperbolicParaboloidMaterial(int, char*[]);
int TestHyperTreeGridTernary2D(int, char*[]);
int TestHyperTreeGridTernary2DMaterial(int, char*[]);
int TestHyperTreeGridTernary2DMaterialBits(int, char*[]);
int TestHyperTreeGridTernary2DFullMaterialBits(int, char*[]);
int TestHyperTreeGridTernary2DBiMaterial(int, char*[]);
int TestHyperTreeGridTernary3DAxisClipBox(int, char*[]);
int TestHyperTreeGridTernary3DAxisClipCylinder(int, char*[]);
int TestHyperTreeGridTernary3DAxisClipPlanes(int, char*[]);
int TestHyperTreeGridTernary3DAxisCut(int, char*[]);
int TestHyperTreeGridTernary3DAxisCutMaterial(int, char*[]);
int TestHyperTreeGridTernary3DAxisReflectionXCenter(int, char*[]);
int TestHyperTreeGridTernary3DAxisReflectionXCenterMaterial(int, char*[]);
int TestHyperTreeGridTernary3DAxisReflectionYZCenter(int, char*[]);
int TestHyperTreeGridTernary3DAxisReflectionYZCenterMaterial(int, char*[]);
int TestHyperTreeGridTernary3DCellCenters(int, char*[]);
int TestHyperTreeGridTernary3DCellCentersMaterial(int, char*[]);
int TestHyperTreeGridTernary3DContour(int, char*[]);
int TestHyperTreeGridTernary3DContourMaterial(int, char*[]);
int TestHyperTreeGridTernary3DClip(int, char*[]);
int TestHyperTreeGridTernary3DDualContour(int, char*[]);
int TestHyperTreeGridTernary3DDualContourMaterial(int, char*[]);
int TestHyperTreeGridTernary3DGeometry(int, char*[]);
int TestHyperTreeGridTernary3DGeometryMaterial(int, char*[]);
int TestHyperTreeGridTernary3DGeometryMaterialBits(int, char*[]);
int TestHyperTreeGridTernary3DGeometryLargeMaterialBits(int, char*[]);
int TestHyperTreeGridTernary3DPlaneCutter(int, char*[]);
int TestHyperTreeGridTernary3DPlaneCutterDual(int, char*[]);
int TestHyperTreeGridTernary3DThreshold(int, char*[]);
int TestHyperTreeGridTernary3DThresholdMaterial(int, char*[]);
int TestHyperTreeGridTernary3DUnstructured(int, char*[]);
int TestHyperTreeGridTernary3DUnstructuredMaterial(int, char*[]);
int TestHyperTreeGridTernaryHyperbola(int, char*[]);
int TestHyperTreeGridTernarySphereMaterial(int, char*[]);
int TestHyperTreeGridTernarySphereMaterialReflections(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "TestHyperTreeGridBinary2D",
    TestHyperTreeGridBinary2D
  },
  {
    "TestHyperTreeGridBinary2DAxisClipBox",
    TestHyperTreeGridBinary2DAxisClipBox
  },
  {
    "TestHyperTreeGridBinary2DAxisClipEllipse",
    TestHyperTreeGridBinary2DAxisClipEllipse
  },
  {
    "TestHyperTreeGridBinary2DAxisClipPlanes",
    TestHyperTreeGridBinary2DAxisClipPlanes
  },
  {
    "TestHyperTreeGridBinary2DAxisReflectionXCenter",
    TestHyperTreeGridBinary2DAxisReflectionXCenter
  },
  {
    "TestHyperTreeGridBinary2DAxisReflectionXCenterMaterial",
    TestHyperTreeGridBinary2DAxisReflectionXCenterMaterial
  },
  {
    "TestHyperTreeGridBinary2DAxisReflectionYCenter",
    TestHyperTreeGridBinary2DAxisReflectionYCenter
  },
  {
    "TestHyperTreeGridBinary2DAxisReflectionYCenterMaterial",
    TestHyperTreeGridBinary2DAxisReflectionYCenterMaterial
  },
  {
    "TestHyperTreeGridBinary2DIJK",
    TestHyperTreeGridBinary2DIJK
  },
  {
    "TestHyperTreeGridBinary2DCellCenters",
    TestHyperTreeGridBinary2DCellCenters
  },
  {
    "TestHyperTreeGridBinary2DCellCentersMaterial",
    TestHyperTreeGridBinary2DCellCentersMaterial
  },
  {
    "TestHyperTreeGridBinary2DContour",
    TestHyperTreeGridBinary2DContour
  },
  {
    "TestHyperTreeGridBinary2DContourMaterial",
    TestHyperTreeGridBinary2DContourMaterial
  },
  {
    "TestHyperTreeGridBinary2DDepthLimiter",
    TestHyperTreeGridBinary2DDepthLimiter
  },
  {
    "TestHyperTreeGridBinary2DDepthLimiterMaterial",
    TestHyperTreeGridBinary2DDepthLimiterMaterial
  },
  {
    "TestHyperTreeGridBinary2DInterfaceMaterial",
    TestHyperTreeGridBinary2DInterfaceMaterial
  },
  {
    "TestHyperTreeGridBinary2DMaterial",
    TestHyperTreeGridBinary2DMaterial
  },
  {
    "TestHyperTreeGridBinary2DMaterialIJK",
    TestHyperTreeGridBinary2DMaterialIJK
  },
  {
    "TestHyperTreeGridBinary2DThreshold",
    TestHyperTreeGridBinary2DThreshold
  },
  {
    "TestHyperTreeGridBinary2DThresholdMaterial",
    TestHyperTreeGridBinary2DThresholdMaterial
  },
  {
    "TestHyperTreeGridBinary2DVector",
    TestHyperTreeGridBinary2DVector
  },
  {
    "TestHyperTreeGridBinary2DVectorAxisReflectionXCenter",
    TestHyperTreeGridBinary2DVectorAxisReflectionXCenter
  },
  {
    "TestHyperTreeGridBinary2DVectorAxisReflectionYCenter",
    TestHyperTreeGridBinary2DVectorAxisReflectionYCenter
  },
  {
    "TestHyperTreeGridBinary3DContour",
    TestHyperTreeGridBinary3DContour
  },
  {
    "TestHyperTreeGridBinary3DGeometry",
    TestHyperTreeGridBinary3DGeometry
  },
  {
    "TestHyperTreeGridBinaryClipPlanes",
    TestHyperTreeGridBinaryClipPlanes
  },
  {
    "TestHyperTreeGridBinaryEllipseMaterial",
    TestHyperTreeGridBinaryEllipseMaterial
  },
  {
    "TestHyperTreeGridBinaryHyperbolicParaboloidMaterial",
    TestHyperTreeGridBinaryHyperbolicParaboloidMaterial
  },
  {
    "TestHyperTreeGridTernary2D",
    TestHyperTreeGridTernary2D
  },
  {
    "TestHyperTreeGridTernary2DMaterial",
    TestHyperTreeGridTernary2DMaterial
  },
  {
    "TestHyperTreeGridTernary2DMaterialBits",
    TestHyperTreeGridTernary2DMaterialBits
  },
  {
    "TestHyperTreeGridTernary2DFullMaterialBits",
    TestHyperTreeGridTernary2DFullMaterialBits
  },
  {
    "TestHyperTreeGridTernary2DBiMaterial",
    TestHyperTreeGridTernary2DBiMaterial
  },
  {
    "TestHyperTreeGridTernary3DAxisClipBox",
    TestHyperTreeGridTernary3DAxisClipBox
  },
  {
    "TestHyperTreeGridTernary3DAxisClipCylinder",
    TestHyperTreeGridTernary3DAxisClipCylinder
  },
  {
    "TestHyperTreeGridTernary3DAxisClipPlanes",
    TestHyperTreeGridTernary3DAxisClipPlanes
  },
  {
    "TestHyperTreeGridTernary3DAxisCut",
    TestHyperTreeGridTernary3DAxisCut
  },
  {
    "TestHyperTreeGridTernary3DAxisCutMaterial",
    TestHyperTreeGridTernary3DAxisCutMaterial
  },
  {
    "TestHyperTreeGridTernary3DAxisReflectionXCenter",
    TestHyperTreeGridTernary3DAxisReflectionXCenter
  },
  {
    "TestHyperTreeGridTernary3DAxisReflectionXCenterMaterial",
    TestHyperTreeGridTernary3DAxisReflectionXCenterMaterial
  },
  {
    "TestHyperTreeGridTernary3DAxisReflectionYZCenter",
    TestHyperTreeGridTernary3DAxisReflectionYZCenter
  },
  {
    "TestHyperTreeGridTernary3DAxisReflectionYZCenterMaterial",
    TestHyperTreeGridTernary3DAxisReflectionYZCenterMaterial
  },
  {
    "TestHyperTreeGridTernary3DCellCenters",
    TestHyperTreeGridTernary3DCellCenters
  },
  {
    "TestHyperTreeGridTernary3DCellCentersMaterial",
    TestHyperTreeGridTernary3DCellCentersMaterial
  },
  {
    "TestHyperTreeGridTernary3DContour",
    TestHyperTreeGridTernary3DContour
  },
  {
    "TestHyperTreeGridTernary3DContourMaterial",
    TestHyperTreeGridTernary3DContourMaterial
  },
  {
    "TestHyperTreeGridTernary3DClip",
    TestHyperTreeGridTernary3DClip
  },
  {
    "TestHyperTreeGridTernary3DDualContour",
    TestHyperTreeGridTernary3DDualContour
  },
  {
    "TestHyperTreeGridTernary3DDualContourMaterial",
    TestHyperTreeGridTernary3DDualContourMaterial
  },
  {
    "TestHyperTreeGridTernary3DGeometry",
    TestHyperTreeGridTernary3DGeometry
  },
  {
    "TestHyperTreeGridTernary3DGeometryMaterial",
    TestHyperTreeGridTernary3DGeometryMaterial
  },
  {
    "TestHyperTreeGridTernary3DGeometryMaterialBits",
    TestHyperTreeGridTernary3DGeometryMaterialBits
  },
  {
    "TestHyperTreeGridTernary3DGeometryLargeMaterialBits",
    TestHyperTreeGridTernary3DGeometryLargeMaterialBits
  },
  {
    "TestHyperTreeGridTernary3DPlaneCutter",
    TestHyperTreeGridTernary3DPlaneCutter
  },
  {
    "TestHyperTreeGridTernary3DPlaneCutterDual",
    TestHyperTreeGridTernary3DPlaneCutterDual
  },
  {
    "TestHyperTreeGridTernary3DThreshold",
    TestHyperTreeGridTernary3DThreshold
  },
  {
    "TestHyperTreeGridTernary3DThresholdMaterial",
    TestHyperTreeGridTernary3DThresholdMaterial
  },
  {
    "TestHyperTreeGridTernary3DUnstructured",
    TestHyperTreeGridTernary3DUnstructured
  },
  {
    "TestHyperTreeGridTernary3DUnstructuredMaterial",
    TestHyperTreeGridTernary3DUnstructuredMaterial
  },
  {
    "TestHyperTreeGridTernaryHyperbola",
    TestHyperTreeGridTernaryHyperbola
  },
  {
    "TestHyperTreeGridTernarySphereMaterial",
    TestHyperTreeGridTernarySphereMaterial
  },
  {
    "TestHyperTreeGridTernarySphereMaterialReflections",
    TestHyperTreeGridTernarySphereMaterialReflections
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
