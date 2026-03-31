import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:

    def __init__(self, solutionID):
        self.motors = {}
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")  # adds floor plane
        pyrosim.Prepare_To_Simulate(self.robotId)  # additional setup for sensors with Pyrosim
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f'del brain{self.solutionID}.nndf')

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self,t):
        for LinkName in self.sensors:
            self.sensors[LinkName].Get_Value(t)

    def Prepare_To_Act(self):
        self.joints = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.joints[jointName] = MOTOR(jointName)

    def Act(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.joints[jointName].Set_Value(self, desiredAngle)

                #print(neuronName, jointName, desiredAngle)

            #for jointName in self.joints:
            #    self.joints[jointName].Set_Value(self,t)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionofLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionofLinkZero[0]
        #print(xCoordinateOfLinkZero)

        with open(f"tmp{self.solutionID}.txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))
        if os.path.exists(f"fitness{self.solutionID}.txt"):
            os.remove(f"fitness{self.solutionID}.txt")
        os.rename(f"tmp{self.solutionID}.txt", f"fitness{self.solutionID}.txt")

        #os.system(f"rename tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        exit()
