import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
#pyrosim.Send_Cube(name="Box", pos=[x,y,z],size=[length, width, height])
#x = x+1
#z = z+1
#pyrosim.Send_Cube(name="Box2", pos=[x,y,z],size=[length, width, height])
for j in range(5): #rows
    y+=1
    x = 0
    for k in range(4): #columns
        x+=1
        length = 1
        width = 1
        height = 1
        for i in range(10): #height
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
            z+=1
            length = length*0.9
            width = length
            height = length
pyrosim.End()