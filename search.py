import os
from parallelHillClimber import *
import constants
import simulation
import time
import constants as c

s = SOLUTION(0)
s.Create_World()

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

phc.Show_Best()

