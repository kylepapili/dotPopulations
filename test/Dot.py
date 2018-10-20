import Brain

class Dot:
    fitness = 0
    reachedGoal = bool(0)
    dead = bool(0)
    isBestDot = bool(0)
    
    def __init__(self):
        self.pos = PVector(400/2, 390)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.brain = Brain.Brain()
    
    def show(self):
        if self.isBestDot:
            fill(0,250,0)
            ellipse(self.pos.x, self.pos.y, 8, 8)
        else:
            fill(250,250,250)
            ellipse(self.pos.x, self.pos.y, 4, 4)
        
    def move(self):
        if(len(self.brain.directions) > self.brain.step):
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step = self.brain.step + 1
        else:
            self.dead = bool(1)
        
        self.vel.add(self.acc)
        self.vel.limit(5)
        self.pos.add(self.vel)
            
    def update(self):
        if not self.dead and not self.reachedGoal:
            #Not Dead
            self.move()
            if self.pos.x < 2 or self.pos.y < 2 or self.pos.x > width-2 or self.pos.y > height-2:
                self.dead = bool(1)
            elif(self.pos.x > 100 and self.pos.x < 400 and self.pos.y > 250 and self.pos.y < 260): #rectangle
                self.dead = bool(1)
            elif(self.pos.x > 0 and self.pos.x < 250 and self.pos.y > 125 and self.pos.y < 135):
                self.dead = bool(1)
            #elif(self.pos.x > 150 and self.pos.x < 160 and self.pos.y > 0 and self.pos.y < 160):
                #self.dead = bool(1)
            elif (dist(self.pos.x, self.pos.y, Brain.goal.x, Brain.goal.y) < 5):
                self.reachedGoal = bool(1)
                
    def calculateFitness(self):
        if self.reachedGoal:
            self.fitness = 1 + 10000/(self.brain.step * self.brain.step)
        elif self.dead:
            distanceToGoal = dist(self.pos.x, self.pos.y, Brain.goal.x, Brain.goal.y)
            self.fitness = 100 / ((distanceToGoal*distanceToGoal))
        else:
            distanceToGoal = dist(self.pos.x, self.pos.y, Brain.goal.x, Brain.goal.y)
            self.fitness = 1000 / (distanceToGoal*distanceToGoal)
        
    def spawnChild(self):
        child = Dot()
        child.brain = self.brain.clone()
        return child
