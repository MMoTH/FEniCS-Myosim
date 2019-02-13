set(vtkCommonMath_HEADERS_LOADED 1)
set(vtkCommonMath_HEADERS "vtkAmoebaMinimizer;vtkFunctionSet;vtkInitialValueProblemSolver;vtkMatrix3x3;vtkMatrix4x4;vtkPolynomialSolversUnivariate;vtkQuaternionInterpolator;vtkRungeKutta2;vtkRungeKutta4;vtkRungeKutta45;vtkQuaternion;vtkTuple")

foreach(header ${vtkCommonMath_HEADERS})
  set(vtkCommonMath_HEADER_${header}_EXISTS 1)
endforeach()
