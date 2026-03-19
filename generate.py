import pyrosim.pyrosim as pyrosim
import random
length = 1
width = 1
height = 1
x = -2
y = 2
z = 0.5




def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()



def Create_Robot(X,Y,Z):
    pass
    #pyrosim.Start_URDF("body.urdf")
    #pyrosim.Send_Cube("Torso", [1.5,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
    #pyrosim.Send_Cube("BackLeg", [-0.5,0,-0.5], [length, width, height])
    #pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2,0,1])
    #pyrosim.Send_Cube("FrontLeg", [0.5,0,-0.5], [length, width, height])
    #pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube("Torso", [1.5, 0, 1.5], [length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube("BackLeg", [-0.5, 0, -0.5], [length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube("FrontLeg", [0.5, 0, -0.5], [length, width, height])

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=  -1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)

    for i in range(0,3):
        for j in range(3,5):
            weight = random.random()*2-1
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=weight)


    pyrosim.End()
Generate_Body()
Generate_Brain()


Create_World()
Create_Robot(0,0,3)

