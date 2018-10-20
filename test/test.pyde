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
    rect(100, 250, 400, 10)
    
    fill(0, 0, 255)
    rect(0, 125, 250, 10)


    if(test.allDotsDead()):
        test.calculateFitness()
        test.naturalSelection()
        test.mutateChildren()
        print(len(test.dots))
        print(test.minStep)
    else:
        test.update()
        test.show()
