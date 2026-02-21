import numpy as np

FrontLegAmplitude = -np.pi/8
FrontLegFrequency = 5
FrontLegPhaseOffset = np.pi*1.5

BackLegAmplitude = np.pi/8
BackLegFrequency = 5
BackLegPhaseOffset = 0

torque = 25

gravity = -9.8

simulationCycles = 1000

cycleTimeSleep = 1/60

FrontLegTargetAngles = np.linspace(-np.pi, np.pi, simulationCycles)
BackLegTargetAngles = np.linspace(-np.pi, np.pi, simulationCycles)

backLegSensorValues = np.zeros(simulationCycles) #for storing sensor data
frontLegSensorValues = np.zeros(simulationCycles) #for storing sensor data


for i in range(simulationCycles):
    FrontLegTargetAngles[i] = FrontLegAmplitude*(-np.sin(FrontLegFrequency*FrontLegTargetAngles[i]+FrontLegPhaseOffset))
    BackLegTargetAngles[i] = BackLegAmplitude*(-np.sin(BackLegFrequency*BackLegTargetAngles[i]+BackLegPhaseOffset))
