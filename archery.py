# Draw an archery target

from graphics import *
from typing import List, Tuple

def drawRings(w:GraphWin, center:Point, radius:float) -> None:
    # Pre: w is not closed, center is in w, and...
    assert radius > 0     
    # Returning None is often a tipoff that there are side effects going on
    colors:Tuple[str, ...] = ('white', 'black', 'blue', 'red', 'yellow')

    for i in range(5):
        r:float = radius * (1 - (0.2*i))
        circ:Circle = Circle(center, r)
        circ.setFill(colors[i])
        circ.draw(w)
        # Loop invariant: circ has been drawn and...
        assert 0 <= i < 5 and 0 < r <= radius and circ.getRadius() == r and \
            circ.getCenter().getX() == center.getX() and circ.getCenter().getY() == center.getY()

    # Post: precondition and the target got drawn (side effect)

def drawTarget() -> GraphWin:
    # Pre: none
    w:GraphWin = GraphWin('Archery target', 350, 350) # Not a side effect: this is the return value
    w.setCoords(-1, -1, 1, 1)

    drawRings(w, Point(0, 0), 1)
    # Post: w exists, is drawn, has 2x2 coordinates with Y increasing upwards, and has a target drawn
    return w

def main(args:List[str]) -> int:
    # Pre: none
    w:GraphWin = drawTarget()

    # Wait for a mouse click
    w.getMouse()
    w.close()
    # Post: w is closed
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)