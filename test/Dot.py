import Brain

class Dot:
    fitness = 0
    reachedGoal = bool(0)
    dead = bool(0)
    def __init__(self):
        self.pos = PVector(400/2, 400-100)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.brain = Brain.Brain()
    
    def show(self):
        fill(0)
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
            elif (dist(self.pos.x, self.pos.y, Brain.goal.x, Brain.goal.y) < 5):
                self.reachedGoal = bool(1)
                
    def calculateFitness(self):
        distanceToGoal = dist(self.pos.x, self.pos.y, Brain.goal.x, Brain.goal.y)
        self.fitness = 1/ (distanceToGoal*distanceToGoal)
        
    def spawnChild(self):
        child = Dot()
        child.brain = self.brain.clone()
        return child
