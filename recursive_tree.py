from random import randint
from typing import cast, List
import turtle

def setPenColor(branchLen:int, t:turtle.Turtle) -> None:
    if branchLen > 15:
        t.color("brown")
    else: 
        t.color("green")

def tree(branchLen:int, t:turtle.Turtle) -> None:
    # Pen ends up in the same place where it started.

    # Base case: branchLen <= 5, in which case do nothing.
    if branchLen > 5: # Recursive case
        setPenColor(branchLen, t)
        t.width(round(branchLen / 15))
        t.forward(branchLen)
        #t.right(20)
        angleR:float = randint(15, 35)
        t.right(angleR) # Turn right a bit for the right-hand subtree
        tree(branchLen - randint(10, 20), t)
        angleL:float = randint(15, 35)
        t.left(angleR + angleL) # Turn left for the left-hand subtree
        #t.left(40)
        tree(branchLen - randint(10, 20),t)
        t.right(angleL) # Turn right to get back to the starting orientation

        setPenColor(branchLen, t)
        t.backward(branchLen)

def main(args:List[str]) -> int:
    t:turtle.Turtle = turtle.Turtle()
    myWin:turtle.TurtleScreen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick() # type: ignore
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
