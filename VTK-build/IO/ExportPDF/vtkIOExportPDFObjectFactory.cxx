/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkIOExportPDFObjectFactory.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/

#include "vtkIOExportPDFObjectFactory.h"
#include "vtkVersion.h"

// Include all of the classes we want to create overrides for.


vtkStandardNewMacro(vtkIOExportPDFObjectFactory)

// Now create the functions to create overrides with.


vtkIOExportPDFObjectFactory::vtkIOExportPDFObjectFactory()
{

}

const char * vtkIOExportPDFObjectFactory::GetVTKSourceVersion()
{
  return VTK_SOURCE_VERSION;
}

void vtkIOExportPDFObjectFactory::PrintSelf(ostream &os, vtkIndent indent)
{
  this->Superclass::PrintSelf(os, indent);
}

// Registration of object factories.
static unsigned int vtkIOExportPDFCount;

VTKIOEXPORTPDF_EXPORT void vtkIOExportPDF_AutoInit_Construct()
{
  if(++vtkIOExportPDFCount == 1)
    {
    
    vtkIOExportPDFObjectFactory* factory = vtkIOExportPDFObjectFactory::New();
    if (factory)
      {
      // vtkObjectFactory keeps a reference to the "factory",
      vtkObjectFactory::RegisterFactory(factory);
      factory->Delete();
      }
    }
}

VTKIOEXPORTPDF_EXPORT void vtkIOExportPDF_AutoInit_Destruct()
{
  if(--vtkIOExportPDFCount == 0)
    {
    // Do not call vtkObjectFactory::UnRegisterFactory because
    // vtkObjectFactory.cxx statically unregisters all factories.
    }
}
