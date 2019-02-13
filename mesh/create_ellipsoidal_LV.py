########################################################################
import vtk
import numpy as np
import sys
import inspect
import os
from readUGrid import readUGrid
########################################################################

def create_ellipsoidal_LV(casename="ellipsoidal", meshsize=0.3, gmshcmd="gmsh", iswritemesh=False, verbose=True):


        if (verbose): print '*** create_ellipsoidal_LV ***'

        cur_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 

	geofile = cur_dir + "/ellipsoidal.geo"
	tempgeofile = "ellipsoidal_temp.geo"
	print geofile
	print tempgeofile
	print os.getcwd()

	meshfilename = casename+".vtk"

        cmd = "cp " + geofile + " " + tempgeofile
	os.system(cmd)
	
        cmd = "sed -i.bak s/'<<Meshsize>>'/'" + str(meshsize) + "'/g " + tempgeofile
	os.system(cmd)
	cmd = gmshcmd+" -3 ellipsoidal_temp.geo -o " + meshfilename
	os.system(cmd)
	cmd = "rm ellipsoidal_temp.geo"
	os.system(cmd)

	ugrid = readUGrid(meshfilename)

	return ugrid





