# Draw an archery target

from graphics import *
from typing import List, Tuple

def drawRings(w:GraphWin, center:Point, radius:float) -> None: 
    # Returning None is often a tipoff that there are side effects going on
    colors:Tuple[str, ...] = ('white', 'black', 'blue', 'red', 'yellow')

    for i in range(5):
        r:float = radius * (1 - (0.2*i))
        circ:Circle = Circle(center, r)
        circ.setFill(colors[i])
        circ.draw(w)
    # Side effect: the target got drawn

def drawTarget() -> GraphWin:
    w:GraphWin = GraphWin('Archery target', 350, 350) # Not a side effect: this is the return value
    w.setCoords(-1, -1, 1, 1)

    drawRings(w, Point(0, 0), 1)

    return w

def main(args:List[str]) -> int:
    w:GraphWin = drawTarget()

    # Wait for a mouse click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)