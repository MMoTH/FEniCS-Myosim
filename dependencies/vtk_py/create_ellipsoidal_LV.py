#######################################################################
import sys
sys.path.append("/home/fenics/shared/source_code/dependencies")
import vtk
import numpy as np
import vtk_py
import sys
import inspect
import os

########################################################################


def create_ellipsoidal_LV(casename="ellipsoidal", meshsize=0.05, gmshcmd="gmsh", iswritemesh=True, verbose=True):

    print "starting script"
    if verbose:
        print '*** create_ellipsoidal_LV ***'

        cur_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

	geofile = cur_dir + "/ellipsoidal.geo"
	tempgeofile = "ellipsoidal_temp.geo"
	print tempgeofile
	print os.getcwd()

	meshfilename = casename+".vtk"

        cmd = "cp " + geofile + " " + tempgeofile
	os.system(cmd)

        cmd = "sed -i.bak s/'<<Meshsize>>'/'" + str(meshsize) + "'/g " + tempgeofile
        #cmd = "sed 's/lz_i=lz_o-wt;/lz_i=lz_o-0.5*wt;/' ellipsoidal_temp.geo"
	os.system(cmd)
	cmd = gmshcmd+" -3 ellipsoidal_temp.geo -o " + meshfilename
	os.system(cmd)
	#cmd = "rm ellipsoidal_temp.geo"
	os.system(cmd)

	ugrid = vtk_py.readUGrid(meshfilename)

	return ugrid
#returned_grid = create_ellipsoidal_LV(casename="ellipsoidal", meshsize=0.05, gmshcmd="gmsh", iswritemesh=True, verbose=True)
