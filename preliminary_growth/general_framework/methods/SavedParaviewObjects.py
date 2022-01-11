# @Author: charlesmann
# @Date:   2022-01-10T18:10:49-05:00
# @Last modified by:   charlesmann
# @Last modified time: 2022-01-10T18:24:57-05:00
from dolfin import *

class SavedParaviewObjects():

    def __init__(self,output_path,file_name):

        self.output_path = output_path
        self.file_name = file_name
        self.f = File(output_path + file_name)

    def save_pvd_object(self,object_to_save):
        self.f << object_to_save
