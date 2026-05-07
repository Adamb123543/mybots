import numpy as np
import matplotlib.pyplot as plt
import os

print("Files in data/:")
print(os.listdir("data"))

def Plot_Fitness(filePrefix, label, color):
    allTrials = []
    i = 0
    while os.path.exists(f"{filePrefix}{i}.npy"):
        data = np.load(f"{filePrefix}{i}.npy")
        allTrials.append(data)
        i += 1

    if not allTrials:
        print(f"No files found for {label}")
        return

    print(f"Loaded {len(allTrials)} trials for {label}")

    minLength = min(len(t) for t in allTrials)
    allTrials = [t[:minLength] for t in allTrials]

    generations = np.arange(minLength)

    for trial in allTrials:
        plt.plot(generations, trial, color=color, alpha=0.15, linewidth=1)

    mean = np.array(allTrials).mean(axis=0)
    plt.plot(generations, mean, label=f"{label} (n={len(allTrials)})", color=color, linewidth=2.5)

plt.figure(figsize=(12, 6))

Plot_Fitness("data/symmetric_trial", "Symmetric", "blue")
Plot_Fitness("data/unsymmetric_trial", "Asymmetric", "red")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Symmetric vs Asymmetric Body Evolution")
plt.legend()
plt.show()