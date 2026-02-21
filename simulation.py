from robot import ROBOT
from world import WORLD
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

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
            print(i)
            self.robot.Sense(i)
            p.stepSimulation()
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")  # touch sensors
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")  # touch sensors
            pyrosim.Set_Motor_For_Joint(

                bodyIndex=self.robot.robotId,

                jointName=b'Torso_BackLeg',

                controlMode=p.POSITION_CONTROL,

                targetPosition=c.BackLegTargetAngles[i],

                maxForce=c.torque)

            pyrosim.Set_Motor_For_Joint(

                bodyIndex=self.robot.robotId,

                jointName=b'Torso_FrontLeg',

                controlMode=p.POSITION_CONTROL,

                targetPosition=c.FrontLegTargetAngles[i],

                maxForce=c.torque)

            time.sleep(c.cycleTimeSleep)

    def __del__(self):

        p.disconnect()

