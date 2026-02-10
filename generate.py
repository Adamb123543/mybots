import pyrosim.pyrosim as pyrosim
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
    #pyrosim.Send_Cube("Link0", [X,Y,Z], [length, width, height])
    #pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[-1,0,0])
    #pyrosim.Send_Cube("Link1", [1,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0,0,1])
    #pyrosim.Send_Cube("Link2", [1,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[1,0,0])
    #pyrosim.Send_Cube("Link3", [1,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[1,0,0])
    #pyrosim.Send_Cube("Link4", [1,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0,0,-1])
    #pyrosim.Send_Cube("Link5", [1,0,1.5], [length, width, height])
    #pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0,0,-1])
    #pyrosim.Send_Cube("Link6", [1,0,1.5], [length, width, height])

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube("Torso", [0,0,2], [length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0,0.5,-0.5])
    pyrosim.Send_Cube("BackLeg", [0,0.5,1.5], [length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0,-0.5,-0.5])
    pyrosim.Send_Cube("FrontLeg", [0,-0.5,1.5], [length, width, height])


    pyrosim.End()



Create_World()
Create_Robot(0,0,3)

