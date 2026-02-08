import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

print(backLegSensorValues)
plt.plot(backLegSensorValues,label="BackLeg",linewidth=3)
plt.plot(frontLegSensorValues,label="FrontLeg", linewidth=3)
plt.legend()
plt.show()