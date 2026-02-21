import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
from pyrosim.pyrosim import Prepare_To_Simulate


class ROBOT:
    def __init__(self):
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")  # adds floor plane
        pyrosim.Prepare_To_Simulate(self.robotId)  # additional setup for sensors with Pyrosim
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self,t):
        for LinkName in self.sensors:
            self.sensors[LinkName].Get_Value(t)
