import Brain
import Dot
import random as ra


DotObj = Dot.Dot()  # get an instance of the class

class Population:
    dots = [DotObj]
    fitnessSum = 0
    generation = 1
    
    
    def __init__(self):
        for i in range(100):
            self.dots.append((Dot.Dot()))

    def show(self):
        for i in range(len(self.dots)):
            self.dots[i].show()

    def update(self):
        for i in range(len(self.dots)):
            self.dots[i].update()
    
    def calculateFitness(self):
        for i in range(len(self.dots)):
            self.dots[i].calculateFitness()
            
    def allDotsDead(self):
        for i in range(len(self.dots)):
            if not self.dots[i].dead and not self.dots[i].reachedGoal:
                return bool(0)
            else:
                return bool(1)
            
    def naturalSelection(self):
        newDots = []
        self.calculateFitnessSum()
        for i in range(len(self.dots)):
            #Select Parent based on fitness
            parent = self.selectParent()
            #Get Baby
            newDots.append(parent.spawnChild())
            
        self.dots = newDots
        self.generation = self.generation + 1
            
    def calculateFitnessSum(self):
        fitnessSum = 0
        for i in range(len(self.dots)):
            fitnessSum = fitnessSum + self.dots[i].fitness
        self.fitnessSum = fitnessSum
            
    def selectParent(self):
        randomNum = ra.uniform(0, self.fitnessSum)
        runningSum = 0
        for i in range(len(self.dots)):
            runningSum = runningSum + self.dots[i].fitness
            if (runningSum > randomNum):
                return self.dots[i]
    
    def mutateChildren(self):
        for i in range(len(self.dots)):
            self.dots[i].brain.mutate()
            
            
