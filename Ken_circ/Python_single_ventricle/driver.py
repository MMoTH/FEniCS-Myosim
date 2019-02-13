# Code for driving simulations
import untangle as ut
from . import single_circulation as sc


def return_sim_struct_from_xml_file(xml_file_string):
    xml_struct = ut.parse(xml_file_string)
    sim_struct = xml_struct.single_circulation_simulation
    return sim_struct

def run_simulation_from_xml_file(xml_file_string):
    # First get the data struct for the model
    sim_struct = return_sim_struct_from_xml_file(xml_file_string)
    
    # Now create a single circulation object
    sim_object = sc.single_circulation(sim_struct, xml_file_string)

    # Now run the simulation
    sim_object.run_simulation()






