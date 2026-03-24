from simulation import SIMULATION
import sys

import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import random
from simulation import SIMULATION
import simulation

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run(directOrGUI)
simulation.Get_Fitness()