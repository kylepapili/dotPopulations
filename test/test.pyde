import Dot
import Brain
import Population

test = Population.Population()

def setup():
    size(400, 400)
    test = Population.Population()

def draw():
    background(255)
    fill(255, 0, 0)
    ellipse(Brain.goal.x, Brain.goal.y, 10, 10)

    if(test.allDotsDead()):
        test.calculateFitness()
        test.naturalSelection()
        test.mutateChildren()
    else:
        test.update()
        test.show()
