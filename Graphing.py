import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def Plot_Fitness(filePrefix, numTrials, label, color):
    allTrials = []
    for i in range(numTrials):
        data = np.load(f"{filePrefix}{i}.npy")
        allTrials.append(data)

    allTrials = np.array(allTrials)
    generations = np.arange(allTrials.shape[1])

    finalFitnesses = allTrials[:, -1]
    ranks = np.argsort(np.argsort(finalFitnesses))
    colormap = cm.get_cmap("coolwarm")

    for i, trial in enumerate(allTrials):
        c = colormap(ranks[i] / (numTrials - 1))
        plt.plot(generations, trial, color=c, alpha=0.3, linewidth=1)

    mean = allTrials.mean(axis=0)
    plt.plot(generations, mean, label=label, color=color, linewidth=2.5)

num_trials = 10

plt.figure(figsize=(12, 6))

Plot_Fitness("symmetric_trial", num_trials, "Symmetric (mean)", "blue")
Plot_Fitness("unsymmetric_trial", num_trials, "Unsymmetric (mean)", "red")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Symmetric vs Unsymmetric Body Evolution")
plt.legend()
plt.show()