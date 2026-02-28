from robot import ROBOT
from world import WORLD
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK




class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0, 0, c.gravity)  # sets gravity

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.simulationCycles):
            #print(i)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            p.stepSimulation()
            time.sleep(c.cycleTimeSleep)

    def __del__(self):

        p.disconnect()

