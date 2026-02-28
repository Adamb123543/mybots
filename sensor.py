import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = np.zeros(c.simulationCycles)
        #print(self.values)
    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #if t == c.simulationCycles - 1:
            #print(self.values)