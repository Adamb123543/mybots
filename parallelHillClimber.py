import constants
import copy
from solution import *
import constants as c
class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()

    def Evolve(self):
        #self.parent.Evaluate('DIRECT')
        #for currentGeneration in range(constants.numberOfGenerations):
        #    self.Evolve_For_One_Generation()
        for parent in self.parents:
            self.parents[parent].Evaluate('GUI')

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass