import os
import numpy as np
from parallelHillClimber import *
import constants as c
from solution import SOLUTION

os.makedirs("data", exist_ok=True)
os.makedirs("data/best_robots", exist_ok=True)

# count existing trials
existing_sym = len([f for f in os.listdir("data") if f.startswith("symmetric_trial") and f.endswith(".npy")])
existing_unsym = len([f for f in os.listdir("data") if f.startswith("unsymmetric_trial") and f.endswith(".npy")])

print(f"Found {existing_sym} symmetric trials, {existing_unsym} unsymmetric trials")

for trial in range(existing_sym):
    print(f"Extending Symmetric Trial {trial + 1} of {existing_sym}")
    s = SOLUTION(0)
    s.Create_World()
    phc = PARALLEL_HILL_CLIMBER()

    prevFile = f"data/best_robots/symmetric_trial{trial}"
    if os.path.exists(f"{prevFile}_weights.npy"):
        print(f"  Loading best robot from trial {trial}")
        for i in phc.parents:
            phc.parents[i].Load_Leg_Values(prevFile)

    phc.Evolve(symmetric=True)

    newFitness = np.array(phc.fitnessOverTime)
    existingFile = f"data/symmetric_trial{trial}.npy"
    existing = np.load(existingFile)
    combined = np.concatenate([existing, newFitness])
    np.save(existingFile, combined)

    phc.Save_Best(f"data/best_robots/symmetric_trial{trial}")

for trial in range(existing_unsym):
    print(f"Extending Unsymmetric Trial {trial + 1} of {existing_unsym}")
    s = SOLUTION(0)
    s.Create_World()
    phc = PARALLEL_HILL_CLIMBER()

    prevFile = f"data/best_robots/unsymmetric_trial{trial}"
    if os.path.exists(f"{prevFile}_weights.npy"):
        print(f"  Loading best robot from trial {trial}")
        for i in phc.parents:
            phc.parents[i].Load_Leg_Values(prevFile)

    phc.Evolve(symmetric=False)

    newFitness = np.array(phc.fitnessOverTime)
    existingFile = f"data/unsymmetric_trial{trial}.npy"
    existing = np.load(existingFile)
    combined = np.concatenate([existing, newFitness])
    np.save(existingFile, combined)

    phc.Save_Best(f"data/best_robots/unsymmetric_trial{trial}")