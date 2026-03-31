import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as random
import time
import sys

length = 1
width = 1
height = 1
x = -2
y = 2
z = 0.5


class SOLUTION():
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights*2-1
    def Set_ID(self, myID):
        self.myID = myID

    def Evaluate(self, directOrGUI):
        self.Start_Simulation(directOrGUI)
        self.Wait_For_Simulation_To_End()

    def Start_Simulation(self, directOrGUI):
        #self.Create_World()
        self.Create_Brain()
        while not os.path.exists(f"brain{self.myID}.nndf"):
            time.sleep(0.01)
        self.Create_Body()
        os.system(f"start /B python simulate.py {directOrGUI} {self.myID} 2>nul") #added 2>nul


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{str(self.myID)}.txt"):
            time.sleep(0.01)
        fitnessFile = open(f"fitness{str(self.myID)}.txt", "r")
        self.fitness = float(fitnessFile.read())
        #print(self.fitness)
        fitnessFile.close()
        os.remove(f"fitness{self.myID}.txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube("Torso", [0,0,1], [length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube("BackLeg", [0,-0.5,0], [0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube("FrontLeg", [0,0.5,0], [0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",position=[-0.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube("LeftLeg", [-0.5, 0, 0], [1,0.2,0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube("RightLeg", [0.5, 0, 0], [1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",position=[0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube("FrontLowerLeg", [0,0,-0.5], [0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",position=[0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube("BackLowerLeg", [0,0,-0.5], [0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube("LeftLowerLeg", [0,0,-0.5], [0.2,0.2,1])

        pyrosim.Send_Joint(name="Torso_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube("RightLowerLeg", [0,0,-0.5], [0.2,0.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        #pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")

        #pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        #pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        #pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        #pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLowerLeg")
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=  -1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                weight = random.random() * 2 - 1
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()


    def Mutate(self):
        #randomRow = random.randint(0,2)
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        #randomColumn = random.randint(0,1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randomRow, randomColumn] = random.random()*2-1
