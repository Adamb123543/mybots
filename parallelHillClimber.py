import constants
import copy
from solution import *
import constants as c
import numpy as np
class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.parent = self.parents[0]
    def Evolve(self,symmetric):
        self.fitnessOverTime = [] #for data storage

        #self.parent.Evaluate('DIRECT')
        self.Evaluate(self.parents)
        bestInitialKey = max(self.parents, key=lambda i: self.parents[i].fitness)
        self.initialBest = copy.deepcopy(self.parents[bestInitialKey])
        for currentGeneration in range(constants.numberOfGenerations):
            print(f"Generation {currentGeneration + 1} of {constants.numberOfGenerations}")  # <-- here
            self.Evolve_For_One_Generation(symmetric)

    def Evolve_For_One_Generation(self, symmetric):
        self.Spawn()
        self.Mutate(symmetric)
        self.Evaluate(self.children, "DIRECT")
        self.Print()
        self.Select()
        bestFitness = min(self.parents[i].fitness for i in self.parents) #for data storage
        self.fitnessOverTime.append(-bestFitness)

    def Save_Fitness(self,filename): #for data storage
        np.save(f"{filename}.npy",np.array(self.fitnessOverTime))

    def Spawn(self):
        self.children = {}  # ADDED: empty dictionary
        for i in self.parents:  # ADDED: iterate over each parent
            self.children[i] = copy.deepcopy(self.parents[i])  # ADDED: deepcopy ith parent into ith child
            self.children[i].Set_ID(self.nextAvailableID)  # ADDED: assign unique ID
            self.nextAvailableID += 1  # ADDED: increment next available ID
        #print(self.children)  # ADDED: temporarily print children
        #exit()



    def Mutate(self,symmetric = True ):
        for i in self.children:
            if symmetric == True:
                self.children[i].Mutate_Symmetric()
            else:
                self.children[i].Mutate_Unsymmetric()


    def Select(self):
        #if self.parent.fitness > self.child.fitness:
         #   self.parent = self.child
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]
    def Print(self):
        print()
        for i in self.parents:
            print(self.parents[i].fitness, self.children[i].fitness)
        print()

    def Show_Best(self):
        #self.parent.Evaluate("GUI")

        print('First Robot Showing')
        self.initialBest.Evaluate("GUI")
        print('Final Evolved Robot Showing')
        leastFit = min(self.parents, key = lambda i: self.parents[i].fitness)
        best_robot = self.parents[leastFit]
        best_robot.Save_Leg_Values('best_robot')
        self.parents[leastFit].Start_Simulation("GUI")

    def Save_Best(self, filename):
        bestKey = min(self.parents, key = lambda i: self.parents[i].fitness)
        self.parents[bestKey].Save_Leg_Values(filename)


    def Evaluate(self, solutions, directOrGUI = "DIRECT"):
        for i in solutions:
            solutions[i].Start_Simulation(directOrGUI)
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
