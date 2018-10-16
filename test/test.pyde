import Dot
import Brain
import Population

test = Population.Population()

def setup():
    size(400, 400)
    frameRate(240)

def draw():
    background(0)
    fill(255, 0, 0)
    ellipse(Brain.goal.x, Brain.goal.y, 10, 10)
    
    fill(0, 0, 255)
    rect(100, 250, 250, 10)
    
    fill(0, 0, 255)
    rect(50, 125, 300, 10)
    
    fill(0, 0, 255)
    rect(350, 100, 10, 100)
    
    rect(150, 0, 10, 150)

    if(test.allDotsDead()):
        test.calculateFitness()
        test.naturalSelection()
        test.mutateChildren()
        print(len(test.dots))
        print(test.minStep)
    else:
        test.update()
        test.show()
