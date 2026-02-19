import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
FrontLegTargetAngles = np.load('data/FrontLegTargetAngles.npy')
BackLegTargetAngles = np.load('data/BackLegTargetAngles.npy')
#plt.plot(backLegSensorValues,label="BackLeg",linewidth=3)
#plt.plot(frontLegSensorValues,label="FrontLeg", linewidth=3)
plt.plot(FrontLegTargetAngles,label="Target Angles", linewidth=1)
plt.plot(BackLegTargetAngles,label="Target Angles", linewidth=1)

plt.legend()
plt.show()
