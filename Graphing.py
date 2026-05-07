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
    allTrials = np.array(allTrials)
    generations = np.arange(allTrials.shape[1])
    mean = allTrials.mean(axis=0)
    std = allTrials.std(axis=0)

    plt.plot(generations, mean, label=f"{label} (n={len(allTrials)})", color=color, linewidth=2)
    plt.fill_between(generations, mean - std, mean + std, color=color, alpha=0.2)

plt.figure(figsize=(12, 6))

Plot_Fitness("data/symmetric_trial", "Symmetric", "blue")
Plot_Fitness("data/unsymmetric_trial", "Unsymmetric", "red")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Symmetric vs Unsymmetric Body Evolution")
plt.legend()
plt.show()