import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    def Prepare_To_Act(self):
        self.amplitude = c.FrontLegAmplitude
        self.offset = c.FrontLegPhaseOffset
        self.motorValues = np.zeros(c.simulationCycles)

        if self.jointName == b'Torso_BackLeg':
            self.frequency = 0.05
        else:
            self.frequency = 0.1
        for i in range(c.simulationCycles):
            self.motorValues[i] = self.amplitude*np.sin(self.frequency*i+self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot.robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValues[t],

            maxForce=c.torque)

    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "MotorValues.npy", self.motorValues)