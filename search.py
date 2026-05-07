import os
from parallelHillClimber import *
import constants
import simulation
import time
import constants as c


num_trials = 30
comp = 0

for trial in range(num_trials):
    print("symmetric Trial {}".format(trial))
    s = SOLUTION(0)
    s.Create_World()

    phc = PARALLEL_HILL_CLIMBER()

    phc.Evolve(symmetric = True)
    phc.Save_Fitness(f"data/symmetric_trial{trial+comp}")
    phc.Save_Best(f"data/best_robots/symmetric_trial{trial}")
    #phc.Show_Best()


for trial in range(num_trials):
    print("unsymmetric Trial {}".format(trial))
    s = SOLUTION(0)
    s.Create_World()

    phc = PARALLEL_HILL_CLIMBER()

    phc.Evolve(symmetric = False)
    phc.Save_Fitness(f"data/unsymmetric_trial{trial+comp}")
    phc.Save_Best(f"data/best_robots/unsymmetric_trial{trial}")
    #phc.Show_Best()

