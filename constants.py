import numpy as np

FrontLegAmplitude = -np.pi/8
FrontLegFrequency = 5
FrontLegPhaseOffset = np.pi*1.5

BackLegAmplitude = np.pi/8
BackLegFrequency = 5
BackLegPhaseOffset = 0

torque = 100

gravity = -9.8

simulationCycles = 400

cycleTimeSleep = 1/60 #originally 1/60

FrontLegTargetAngles = np.linspace(-np.pi, np.pi, simulationCycles)
BackLegTargetAngles = np.linspace(-np.pi, np.pi, simulationCycles)

backLegSensorValues = np.zeros(simulationCycles) #for storing sensor data
frontLegSensorValues = np.zeros(simulationCycles) #for storing sensor data

numberOfGenerations = 10

populationSize = 2

for i in range(simulationCycles):
    FrontLegTargetAngles[i] = FrontLegAmplitude*(-np.sin(FrontLegFrequency*FrontLegTargetAngles[i]+FrontLegPhaseOffset))
    BackLegTargetAngles[i] = BackLegAmplitude*(-np.sin(BackLegFrequency*BackLegTargetAngles[i]+BackLegPhaseOffset))
