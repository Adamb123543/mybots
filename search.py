import os
from parallelHillClimber import *
import constants
import simulation
import time
import constants as c

s = SOLUTION(0)
s.Create_World()

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve(symmetric = True)
phc.Save_Fitness(f"symmetric_trial")
phc.Show_Best()
num_trials = 10
comp = 0

for trial in range(num_trials):
    print("symmetric Trial {}".format(trial))
    s = SOLUTION(0)
    s.Create_World()

    phc = PARALLEL_HILL_CLIMBER()

    phc.Evolve(symmetric = True)
    phc.Save_Fitness(f"symmetric_trial{trial+comp}")
    #phc.Show_Best()


for trial in range(num_trials):
    print("unsymmetric Trial {}".format(trial))
    s = SOLUTION(0)
    s.Create_World()

    phc = PARALLEL_HILL_CLIMBER()

    phc.Evolve(symmetric = False)
    phc.Save_Fitness(f"unsymmetric_trial{trial+comp}")
    #phc.Show_Best()

