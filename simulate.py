import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8) #sets gravity
planeId = p.loadURDF("plane.urdf") #adds floor plane
robotId = p.loadURDF("body.urdf") #adds floor plane

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId) #additional setup for sensors with Pyrosim
backLegSensorValues = np.zeros(1000) #for storing sensor data
frontLegSensorValues = np.zeros(1000) #for storing sensor data

for i in range(1000):
    #print(i)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #touch sensors
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") #touch sensors

    time.sleep(1/60)
#np.save("backLegSensorValues.npy",backLegSensorValues)
p.disconnect()
np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)

print(backLegSensorValues)


