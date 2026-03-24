import os
from hillclimber import *
import constants
import simulation
import time
import constants as c


hc = HILL_CLIMBER()
hc.Show_Best()

hc.Evolve()

hc.Show_Best()

#for i in range(5):
#
#    os.system(r"C:\Users\boyle\AppData\Local\Python\pythoncore-3.14-64\python.exe generate.py")
#    os.system(r"C:\Users\boyle\AppData\Local\Python\pythoncore-3.14-64\python.exe simulate.py")

