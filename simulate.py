from simulation import SIMULATION

'''
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,c.gravity) #sets gravity
planeId = p.loadURDF("plane.urdf") #adds floor plane
robotId = p.loadURDF("body.urdf") #adds floor plane

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId) #additional setup for sensors with Pyrosim
backLegSensorValues = np.zeros(c.simulationCycles) #for storing sensor data
frontLegSensorValues = np.zeros(c.simulationCycles) #for storing sensor data

#np.save("data/FrontLegTargetAngles.npy",FrontLegTargetAngles)
#np.save("data/BackLegTargetAngles.npy",BackLegTargetAngles)

#exit()
for i in range(c.simulationCycles):
    #print(i)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #touch sensors
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") #touch sensors
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_BackLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=c.BackLegTargetAngles[i],

        maxForce=c.torque)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_FrontLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=c.FrontLegTargetAngles[i],

        maxForce=c.torque)
    time.sleep(c.cycleTimeSleep)
#np.save("backLegSensorValues.npy",backLegSensorValues)
p.disconnect()
np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)

print(backLegSensorValues)

'''

simulation = SIMULATION()