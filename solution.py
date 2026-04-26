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

Max_Mutation = 0.2 #percentage a child's limb can be different than the parents

class SOLUTION():
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)

        self.weights = self.weights*2-1
        self.frontLegSize = [0.2,2,0.2]
        self.backLegSize = [0.2,2,0.2]
        self.leftLegSize = [2, 0.2, 0.2]
        self.rightLegSize = [2, 0.2, 0.2]
        self.backLowerLegSize = [0.2,0.2,1]
        self.frontLowerLegSize = [0.2,0.2,1]
        self.rightLowerLegSize = [0.2,0.2,1]
        self.leftLowerLegSize = [0.2,0.2,1]
        '''
        self.frontLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 2), random.uniform(0.1, 1)]
        self.backLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 2), random.uniform(0.1, 1)]
        self.leftLegSize = [random.uniform(0.1, 2), random.uniform(0.1, 1), random.uniform(0.1, 1)]
        self.rightLegSize = [random.uniform(0.1, 2), random.uniform(0.1, 1), random.uniform(0.1, 1)]
        self.backLowerLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 1), random.uniform(0.1, 2)]
        self.frontLowerLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 1), random.uniform(0.1, 2)]
        self.rightLowerLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 1), random.uniform(0.1, 2)]
        self.leftLowerLegSize = [random.uniform(0.1, 1), random.uniform(0.1, 1), random.uniform(0.1, 2)]
        #lowerLegSize = [length, width, height
        '''

    def Save_Leg_Values(self, filename = "best_robot"):
        np.save(f"{filename}_weights.npy", self.weights)
        np.save(f"{filename}_frontLeg.npy", self.frontLegSize)
        np.save(f"{filename}_backLeg.npy", self.backLegSize)
        np.save(f"{filename}_leftLeg.npy", self.leftLegSize)
        np.save(f"{filename}_rightLeg.npy", self.rightLegSize)
        np.save(f"{filename}_frontLowerLeg.npy", self.frontLowerLegSize)
        np.save(f"{filename}_backLowerLeg.npy", self.backLowerLegSize)
        np.save(f"{filename}_leftLowerLeg.npy", self.leftLowerLegSize)
        np.save(f"{filename}_rightLowerLeg.npy", self.rightLowerLegSize)

    def Load_Leg_Values(self, filename = "best_robot"):
        self.weights = np.load(f"{filename}_weights.npy")
        self.frontLegSize = list(np.load(f"{filename}_frontLeg.npy"))
        self.backLegSize = list(np.load(f"{filename}_backLeg.npy"))
        self.leftLegSize = list(np.load(f"{filename}_leftLeg.npy"))
        self.rightLegSize = list(np.load(f"{filename}_rightLeg.npy"))
        self.frontLowerLegSize = list(np.load(f"{filename}_frontLowerLeg.npy"))
        self.backLowerLegSize = list(np.load(f"{filename}_backLowerLeg.npy"))
        self.leftLowerLegSize = list(np.load(f"{filename}_leftLowerLeg.npy"))
        self.rightLowerLegSize = list(np.load(f"{filename}_rightLowerLeg.npy"))

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
        while not os.path.exists(f"body{self.myID}.urdf"):
            time.sleep(0.01)
        os.system(f"start /B python simulate.py {directOrGUI} {self.myID} 2>nul")


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{str(self.myID)}.txt"):
            time.sleep(0.01)

        fitnessFile = None
        while fitnessFile is None:
            try:
                fitnessFile = open(f"fitness{str(self.myID)}.txt", "r")
            except PermissionError:
                time.sleep(0.01)
        self.fitness = float(fitnessFile.read())
        #print(self.fitness)
        fitnessFile.close()
        os.remove(f"fitness{self.myID}.txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        heightComp = 1.5
        pyrosim.Start_URDF(f"body{self.myID}.urdf")
        pyrosim.Send_Cube("Torso", [0, 0, 1 + heightComp], [length, width, height])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1 + heightComp], jointAxis="1 0 0")
        pyrosim.Send_Cube("BackLeg", [0, -self.backLegSize[1] / 2, 0], self.backLegSize)

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1 + heightComp], jointAxis="1 0 0")
        pyrosim.Send_Cube("FrontLeg", [0, self.frontLegSize[1] / 2, 0], self.frontLegSize)

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1 + heightComp], jointAxis="0 1 0")
        pyrosim.Send_Cube("LeftLeg", [-self.leftLegSize[0] / 2, 0, 0], self.leftLegSize)

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1 + heightComp], jointAxis="0 1 0")
        pyrosim.Send_Cube("RightLeg", [self.rightLegSize[0] / 2, 0, 0], self.rightLegSize)

        pyrosim.Send_Joint(name="Torso_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, self.frontLegSize[1], 0], jointAxis="1 0 0")
        pyrosim.Send_Cube("FrontLowerLeg", [0, 0, -self.frontLowerLegSize[2] / 2], self.frontLowerLegSize)

        pyrosim.Send_Joint(name="Torso_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -self.backLegSize[1], 0], jointAxis="1 0 0")
        pyrosim.Send_Cube("BackLowerLeg", [0, 0, -self.backLowerLegSize[2] / 2], self.backLowerLegSize)

        pyrosim.Send_Joint(name="Torso_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-self.leftLegSize[0], 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube("LeftLowerLeg", [0, 0, -self.leftLowerLegSize[2] / 2], self.leftLowerLegSize)

        pyrosim.Send_Joint(name="Torso_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[self.rightLegSize[0], 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube("RightLowerLeg", [0, 0, -self.rightLowerLegSize[2] / 2], self.rightLowerLegSize)

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
        minimum = 0.1
        maximum = 4
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

        for i in range(3): #front leg
            self.frontLegSize[i] = max(minimum, min(maximum, self.frontLegSize[i] + random.uniform(-Max_Mutation, Max_Mutation)))
            self.backLegSize[i] = self.frontLegSize[i]

        for i in range(3): #left leg
            self.leftLegSize[i] = max(minimum, min(maximum, self.leftLegSize[i] + random.uniform(-Max_Mutation, Max_Mutation)))
            self.rightLegSize[i] = self.leftLegSize[i]

        for i in range(3): #front lower leg
            self.frontLowerLegSize[i] = max(minimum, min(maximum, self.frontLowerLegSize[i] + random.uniform(-Max_Mutation, Max_Mutation)))
            self.backLowerLegSize[i] = self.frontLowerLegSize[i]

        for i in range(3): #left lower leg
            self.leftLowerLegSize[i] = max(minimum, min(maximum, self.leftLowerLegSize[i] + random.uniform(-Max_Mutation, Max_Mutation)))
            self.rightLowerLegSize[i] = self.leftLowerLegSize[i]


