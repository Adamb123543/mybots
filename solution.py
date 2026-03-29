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
        self.weights = np.random.rand(3,2)
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
        pyrosim.Send_Cube("Torso", [1.5, 0, 1.5], [length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube("BackLeg", [-0.5, 0, -0.5], [length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube("FrontLeg", [0.5, 0, -0.5], [length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
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
