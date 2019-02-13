#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#if defined(_MSC_VER)
# pragma warning(disable:4996) /* deprecation */
#endif

#include "/home/fenics/shared/VTK/Testing/Rendering/vtkTestingObjectFactory.h"



/* Forward declare test functions. */
int TestAdjustLowerBoundForLogPlot(int, char*[]);
int TestContextScene(int, char*[]);
int TestControlPointsItem(int, char*[]);
int TestControlPointsItemEvents(int, char*[]);
int TestAreaPlot(int, char*[]);
int TestAxes(int, char*[]);
int TestAxes2(int, char*[]);
int TestBagPlot(int, char*[]);
int TestBarGraph(int, char*[]);
int TestBarGraphHorizontal(int, char*[]);
int TestBarGraphSelection(int, char*[]);
int TestBoxPlot(int, char*[]);
int TestBoxPlot2(int, char*[]);
int TestCategoryLegend(int, char*[]);
int TestColorTransferFunction(int, char*[]);
int TestChartBadPoints(int, char*[]);
int TestChartDouble(int, char*[]);
int TestChartDoubleColors(int, char*[]);
int TestChartMatrix(int, char*[]);
int TestChartTileScaling(int, char*[]);
int TestChartUnicode(int, char*[]);
int TestChartsOn3D(int, char*[]);
int TestChartXYInvertedAxis(int, char*[]);
int TestChartXYZ(int, char*[]);
int TestContext(int, char*[]);
int TestContextArea(int, char*[]);
int TestContextAreaFixedAspect(int, char*[]);
int TestContextAreaFixedMargins(int, char*[]);
int TestContextAreaFixedRect(int, char*[]);
int TestContextImage(int, char*[]);
int TestContextItemStacking(int, char*[]);
int TestContextUnicode(int, char*[]);
int TestControlPointsHandleItem(int, char*[]);
int TestDiagram(int, char*[]);
int TestFunctionalBagPlot(int, char*[]);
int TestHistogram2D(int, char*[]);
int TestInteractiveChartXYZ(int, char*[]);
int TestLegendHiddenPlots(int, char*[]);
int TestLinePlot(int, char*[]);
int TestLinePlotDouble(int, char*[]);
int TestLinePlotDouble2(int, char*[]);
int TestLinePlot3D(int, char*[]);
int TestLinePlotAxisFonts(int, char*[]);
int TestLinePlot2(int, char*[]);
int TestLinePlotInteraction(int, char*[]);
int TestLinePlotSelection(int, char*[]);
int TestLinePlotSelection2(int, char*[]);
int TestMultipleChartRenderers(int, char*[]);
int TestMultipleRenderers(int, char*[]);
int TestMultipleScalarsToColors(int, char*[]);
int TestParallelCoordinates(int, char*[]);
int TestParallelCoordinatesDouble(int, char*[]);
int TestPieChart(int, char*[]);
int TestPlotMatrix(int, char*[]);
int TestPropItem(int, char*[]);
int TestScalarsToColors(int, char*[]);
int TestScatterPlot(int, char*[]);
int TestScatterPlotMatrix(int, char*[]);
int TestScatterPlotMatrixVehicles(int, char*[]);
int TestScatterPlotMatrixVisible(int, char*[]);
int TestScientificPlot(int, char*[]);
int TestStackedBarGraph(int, char*[]);
int TestStackedPlot(int, char*[]);
int TestSurfacePlot(int, char*[]);
int TestZoomAxis(int, char*[]);


/* Create map.  */

typedef int (*MainFuncPointer)(int , char*[]);
typedef struct
{
  const char* name;
  MainFuncPointer func;
} functionMapEntry;

static functionMapEntry cmakeGeneratedFunctionMapEntries[] = {
    {
    "TestAdjustLowerBoundForLogPlot",
    TestAdjustLowerBoundForLogPlot
  },
  {
    "TestContextScene",
    TestContextScene
  },
  {
    "TestControlPointsItem",
    TestControlPointsItem
  },
  {
    "TestControlPointsItemEvents",
    TestControlPointsItemEvents
  },
  {
    "TestAreaPlot",
    TestAreaPlot
  },
  {
    "TestAxes",
    TestAxes
  },
  {
    "TestAxes2",
    TestAxes2
  },
  {
    "TestBagPlot",
    TestBagPlot
  },
  {
    "TestBarGraph",
    TestBarGraph
  },
  {
    "TestBarGraphHorizontal",
    TestBarGraphHorizontal
  },
  {
    "TestBarGraphSelection",
    TestBarGraphSelection
  },
  {
    "TestBoxPlot",
    TestBoxPlot
  },
  {
    "TestBoxPlot2",
    TestBoxPlot2
  },
  {
    "TestCategoryLegend",
    TestCategoryLegend
  },
  {
    "TestColorTransferFunction",
    TestColorTransferFunction
  },
  {
    "TestChartBadPoints",
    TestChartBadPoints
  },
  {
    "TestChartDouble",
    TestChartDouble
  },
  {
    "TestChartDoubleColors",
    TestChartDoubleColors
  },
  {
    "TestChartMatrix",
    TestChartMatrix
  },
  {
    "TestChartTileScaling",
    TestChartTileScaling
  },
  {
    "TestChartUnicode",
    TestChartUnicode
  },
  {
    "TestChartsOn3D",
    TestChartsOn3D
  },
  {
    "TestChartXYInvertedAxis",
    TestChartXYInvertedAxis
  },
  {
    "TestChartXYZ",
    TestChartXYZ
  },
  {
    "TestContext",
    TestContext
  },
  {
    "TestContextArea",
    TestContextArea
  },
  {
    "TestContextAreaFixedAspect",
    TestContextAreaFixedAspect
  },
  {
    "TestContextAreaFixedMargins",
    TestContextAreaFixedMargins
  },
  {
    "TestContextAreaFixedRect",
    TestContextAreaFixedRect
  },
  {
    "TestContextImage",
    TestContextImage
  },
  {
    "TestContextItemStacking",
    TestContextItemStacking
  },
  {
    "TestContextUnicode",
    TestContextUnicode
  },
  {
    "TestControlPointsHandleItem",
    TestControlPointsHandleItem
  },
  {
    "TestDiagram",
    TestDiagram
  },
  {
    "TestFunctionalBagPlot",
    TestFunctionalBagPlot
  },
  {
    "TestHistogram2D",
    TestHistogram2D
  },
  {
    "TestInteractiveChartXYZ",
    TestInteractiveChartXYZ
  },
  {
    "TestLegendHiddenPlots",
    TestLegendHiddenPlots
  },
  {
    "TestLinePlot",
    TestLinePlot
  },
  {
    "TestLinePlotDouble",
    TestLinePlotDouble
  },
  {
    "TestLinePlotDouble2",
    TestLinePlotDouble2
  },
  {
    "TestLinePlot3D",
    TestLinePlot3D
  },
  {
    "TestLinePlotAxisFonts",
    TestLinePlotAxisFonts
  },
  {
    "TestLinePlot2",
    TestLinePlot2
  },
  {
    "TestLinePlotInteraction",
    TestLinePlotInteraction
  },
  {
    "TestLinePlotSelection",
    TestLinePlotSelection
  },
  {
    "TestLinePlotSelection2",
    TestLinePlotSelection2
  },
  {
    "TestMultipleChartRenderers",
    TestMultipleChartRenderers
  },
  {
    "TestMultipleRenderers",
    TestMultipleRenderers
  },
  {
    "TestMultipleScalarsToColors",
    TestMultipleScalarsToColors
  },
  {
    "TestParallelCoordinates",
    TestParallelCoordinates
  },
  {
    "TestParallelCoordinatesDouble",
    TestParallelCoordinatesDouble
  },
  {
    "TestPieChart",
    TestPieChart
  },
  {
    "TestPlotMatrix",
    TestPlotMatrix
  },
  {
    "TestPropItem",
    TestPropItem
  },
  {
    "TestScalarsToColors",
    TestScalarsToColors
  },
  {
    "TestScatterPlot",
    TestScatterPlot
  },
  {
    "TestScatterPlotMatrix",
    TestScatterPlotMatrix
  },
  {
    "TestScatterPlotMatrixVehicles",
    TestScatterPlotMatrixVehicles
  },
  {
    "TestScatterPlotMatrixVisible",
    TestScatterPlotMatrixVisible
  },
  {
    "TestScientificPlot",
    TestScientificPlot
  },
  {
    "TestStackedBarGraph",
    TestStackedBarGraph
  },
  {
    "TestStackedPlot",
    TestStackedPlot
  },
  {
    "TestSurfacePlot",
    TestSurfacePlot
  },
  {
    "TestZoomAxis",
    TestZoomAxis
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
 
    // Set defaults
    vtkTestingInteractor::ValidBaseline = "Use_-V_for_Baseline";
    vtkTestingInteractor::TempDirectory =
      std::string("/home/fenics/shared/VTK-build/Testing/Temporary");
    vtkTestingInteractor::DataDirectory = std::string("Use_-D_for_Data");

    int interactive = 0;
    for (int ii = 0; ii < ac; ++ii)
      {
      if (strcmp(av[ii], "-I") == 0)
        {
        interactive = 1;
        continue;
        }
      if (ii < ac-1 && strcmp(av[ii], "-V") == 0)
        {
        vtkTestingInteractor::ValidBaseline = std::string(av[++ii]);
        continue;
        }
      if (ii < ac-1 && strcmp(av[ii], "-T") == 0)
        {
        vtkTestingInteractor::TempDirectory = std::string(av[++ii]);
        continue;
        }
      if (ii < ac-1 && strcmp(av[ii], "-D") == 0)
        {
        vtkTestingInteractor::DataDirectory = std::string(av[++ii]);
        continue;
        }
      if (ii < ac-1 && strcmp(av[ii], "-E") == 0)
        {
        vtkTestingInteractor::ErrorThreshold =
            static_cast<double>(atof(av[++ii]));
        continue;
        }
      }
    vtkSmartPointer<vtkTestingObjectFactory> factory = vtkSmartPointer<vtkTestingObjectFactory>::New();
    if (!interactive)
      {
      // Disable any other overrides before registering our factory.
      vtkObjectFactoryCollection *collection = vtkObjectFactory::GetRegisteredFactories();
      collection->InitTraversal();
      vtkObjectFactory *f = collection->GetNextItem();
      while (f)
        {
        f->Disable("vtkRenderWindowInteractor");
        f = collection->GetNextItem();
        }
      vtkObjectFactory::RegisterFactory(factory);
      }

    if (testToRun < 0 || testToRun >= NumTests)
      {
      printf(
        "testToRun was modified by TestDriver code to an invalid value: %3d.\n",
        testNum);
      return -1;
      }
    result = (*cmakeGeneratedFunctionMapEntries[testToRun].func)(ac, av);

   if (result == VTK_SKIP_RETURN_CODE)
     {
     printf("Unsupported runtime configuration: Test returned "
            "VTK_SKIP_RETURN_CODE. Skipping test.\n");
     return result;
     }

   if (!interactive)
     {
     if (vtkTestingInteractor::TestReturnStatus != -1)
        {
        if (vtkTestingInteractor::TestReturnStatus != vtkTesting::PASSED)
          {
          result = EXIT_FAILURE;
          }
        else
          {
          result = EXIT_SUCCESS;
          }
        }
      vtkObjectFactory::UnRegisterFactory(factory);
      }

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
