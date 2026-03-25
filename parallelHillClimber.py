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
        self.parent = self.parents[0]
    def Evolve(self):

        #self.parent.Evaluate('DIRECT')
        self.Evaluate(self.parents)
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}  # ADDED: empty dictionary
        for i in self.parents:  # ADDED: iterate over each parent
            self.children[i] = copy.deepcopy(self.parents[i])  # ADDED: deepcopy ith parent into ith child
            self.children[i].Set_ID(self.nextAvailableID)  # ADDED: assign unique ID
            self.nextAvailableID += 1  # ADDED: increment next available ID
        #print(self.children)  # ADDED: temporarily print children
        #exit()



    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()


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
        leastFit = min(self.parents, key = lambda i: self.parents[i].fitness)
        self.parents[leastFit].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
