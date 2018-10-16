import Brain
import Dot
import random as ra


DotObj = Dot.Dot()  # get an instance of the class

class Population:
    dots = []
    fitnessSum = 0
    generation = 1
    bestDot = 0
    minStep = 400
    
    
    def __init__(self):
        for i in range(1000):
            self.dots.append((Dot.Dot()))

    def show(self):
        for i in range(len(self.dots)):
            self.dots[i].show()

    def update(self):
        for i in range(len(self.dots)):
            if self.dots[i].brain.step > self.minStep:
                self.dots[i].dead = bool(1)
            self.dots[i].update()
    
    def calculateFitness(self):
        for i in range(len(self.dots)):
            self.dots[i].calculateFitness()
            
    def allDotsDead(self):
        for i in range(len(self.dots)):
            if not self.dots[i].dead and not self.dots[i].reachedGoal:
                return bool(0)
        return bool(1)
            
    def naturalSelection(self):
        newDots = []
        self.establishBestDot()
        self.calculateMinStep()
        newDots.append(self.dots[self.bestDot].spawnChild())
        newDots[0].isBestDot = bool(1)
        self.calculateFitnessSum()
        for i in range(len(self.dots[1:])):
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
            
    def establishBestDot(self):
        maxDot = 0
        maxIndex = 0
        for i in range(len(self.dots)):
            if self.dots[i].fitness > maxDot:
                maxDot = self.dots[i].fitness
                maxIndex = i
        self.bestDot = maxIndex
        
    def calculateMinStep(self):
        minStep = self.minStep
        for i in range(len(self.dots)):
            if self.dots[i].brain.step < minStep:
                if self.dots[i].reachedGoal:
                    minStep = self.dots[i].brain.step
        self.minStep = minStep
            
