import constants
import copy
from solution import *
import constants as c
class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):

        #self.parent.Evaluate('DIRECT')
        for parent in self.parents:
            self.parents[parent].Start_Simulation("DIRECT")
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1



    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()


    def Select(self):
        for i in self.parents:
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        for i in self.parents:
            print(f"[{i}] parent: {self.parents[i].fitness:.4f}  child: {self.children[i].fitness:.4f}")

    def Show_Best(self):
        best = max(self.parents.values(), key=lambda s: s.fitness)
        best.Evaluate("GUI")