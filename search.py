import os
from parallelHillClimber import *
import constants
import simulation
import time
import constants as c


phc = PARALLEL_HILL_CLIMBER()
phc.Show_Best()

phc.Evolve()

phc.Show_Best()

#for i in range(5):
#
#    os.system(r"C:\Users\boyle\AppData\Local\Python\pythoncore-3.14-64\python.exe generate.py")
#    os.system(r"C:\Users\boyle\AppData\Local\Python\pythoncore-3.14-64\python.exe simulate.py")

