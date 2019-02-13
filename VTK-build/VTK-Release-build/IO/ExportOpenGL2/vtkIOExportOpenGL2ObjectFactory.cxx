/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkIOExportOpenGL2ObjectFactory.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/

#include "vtkIOExportOpenGL2ObjectFactory.h"
#include "vtkVersion.h"

// Include all of the classes we want to create overrides for.

#include "vtkOpenGLGL2PSExporter.h"

vtkStandardNewMacro(vtkIOExportOpenGL2ObjectFactory)

// Now create the functions to create overrides with.

  VTK_CREATE_CREATE_FUNCTION(vtkOpenGLGL2PSExporter)

vtkIOExportOpenGL2ObjectFactory::vtkIOExportOpenGL2ObjectFactory()
{

    this->RegisterOverride("vtkGL2PSExporter",
                           "vtkOpenGLGL2PSExporter",
                           "Override for vtkIOExportOpenGL2 module", 1,
                           vtkObjectFactoryCreatevtkOpenGLGL2PSExporter);
}

const char * vtkIOExportOpenGL2ObjectFactory::GetVTKSourceVersion()
{
  return VTK_SOURCE_VERSION;
}

void vtkIOExportOpenGL2ObjectFactory::PrintSelf(ostream &os, vtkIndent indent)
{
  this->Superclass::PrintSelf(os, indent);
}

// Registration of object factories.
static unsigned int vtkIOExportOpenGL2Count;

VTKIOEXPORTOPENGL2_EXPORT void vtkIOExportOpenGL2_AutoInit_Construct()
{
  if(++vtkIOExportOpenGL2Count == 1)
    {
    
    vtkIOExportOpenGL2ObjectFactory* factory = vtkIOExportOpenGL2ObjectFactory::New();
    if (factory)
      {
      // vtkObjectFactory keeps a reference to the "factory",
      vtkObjectFactory::RegisterFactory(factory);
      factory->Delete();
      }
    }
}

VTKIOEXPORTOPENGL2_EXPORT void vtkIOExportOpenGL2_AutoInit_Destruct()
{
  if(--vtkIOExportOpenGL2Count == 0)
    {
    // Do not call vtkObjectFactory::UnRegisterFactory because
    // vtkObjectFactory.cxx statically unregisters all factories.
    }
}
