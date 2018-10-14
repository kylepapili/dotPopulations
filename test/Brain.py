import random as ra

goal = PVector(200, 10)

class Brain:
    step = 0
    directions = [PVector]
    def __init__(self):
        self.directions = [PVector(0, 0)]
        self.randomize()
        
    def randomize(self):
        for i in range(400):
            randomAngle = ra.uniform(0, 6.28)
            self.directions.append(PVector.fromAngle(randomAngle))
    
    def clone(self):
        clonedBrain = Brain()
        for i in range(len(self.directions)):
            clonedBrain.directions[i] = self.directions[i].copy()
        return clonedBrain
    
    def mutate(self):
        mutationRate = 0.01
        for i in range(len(self.directions)):
            rand = ra.uniform(0,1)
            if rand<mutationRate:
                randomAngle = ra.uniform(0, 6.28)
                self.directions[i] = PVector.fromAngle(randomAngle)
            
