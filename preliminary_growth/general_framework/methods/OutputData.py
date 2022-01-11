# @Author: charlesmann
# @Date:   2022-01-10T16:55:56-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-11T13:05:42-05:00

import SavedParaviewObjects
from dolfin import *
import numpy as np
import os

class OutputData():

    def __init__(self,params):

        # Initialize some output information
        self.output_path = params["output_path"][0]

        # Initialize some output files. These will eventually come from the instruction
        # file?

        self.ref_mesh_file = SavedParaviewObjects.SavedParaviewObjects(self.output_path,"reference_mesh.pvd")
        self.total_sol_file = SavedParaviewObjects.SavedParaviewObjects(self.output_path,"total_displacement.pvd")
        self.p_f_file = SavedParaviewObjects.SavedParaviewObjects(self.output_path,"passive_force.pvd")
        self.dev_file = SavedParaviewObjects.SavedParaviewObjects(self.output_path,"deviation.pvd")
        self.theta_file = SavedParaviewObjects.SavedParaviewObjects(self.output_path,"theta_ff.pvd")

        self.paraview_objects_to_save = [self.total_sol_file,self.p_f_file,self.dev_file,self.theta_file]

        growth_iter = 0 # will increment if there is growth
        try:
            os.mkdir(self.output_path + "iter_"+str(growth_iter))
        except:
            print "iter_0 directory already exists"
        self.fdataPV = open(self.output_path + "iter_"+str(growth_iter)+"/"+"PV_.txt", "w+", 0)

        #self.dev_txt_file = open('./fc_output/average_deviation.txt','w')

    def save_ref_mesh(self, object_to_save):
        self.ref_mesh_file << object_to_save

    def save_paraview_objects(self, objects_to_save):

        # For now, objects_to_save is a list of objects corresponding to the order
        # of self.paraview_objects_to_save. I want to code up a general way
        # to specify what to save in instruction file, and assemble the objects
        # to pass into this function on the fly

        for i in np.arange(np.shape(self.paraview_objects_to_save)):

            self.paraview_objects_to_save[i].save_pvd_object(object_to_save[i])

    def save_grown_mesh(self, object_to_save, growth_iteration):

        # set up new directory
        os.mkdir(self.output_path + "iter_" + str(growth_iteration))
        grown_mesh_file = File(self.output_path + "iter_" + str(growth_iteration) + "/" + "grown_mesh.pvd")
        grown_mesh_file << object_to_save
