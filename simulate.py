import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8) #sets gravity
planeId = p.loadURDF("plane.urdf") #adds floor plane
p.loadSDF("boxes.sdf")

for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()

