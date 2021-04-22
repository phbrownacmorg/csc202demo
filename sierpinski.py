from typing import List, Tuple
import turtle

def drawTriangle(t:turtle.Turtle, 
        vertex:Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]],
        color:str) -> None:
    """Draw a triangle with vertices VERTEX and background color COLOR, using turtle T."""
    t.fillcolor(color)
    t.up()
    t.goto(vertex[0][0], vertex[0][1])
    t.down()
    t.begin_fill()
    t.goto(vertex[1][0], vertex[1][1])
    t.goto(vertex[2][0], vertex[2][1])
    t.goto(vertex[0][0], vertex[0][1])
    t.end_fill()

def midPt(p0:Tuple[float, float], p1:Tuple[float, float]) -> Tuple[float, float]:
    """Find and return the midpoint of points P0 and P1."""
    return ((p0[0] + p1[0])/2, (p0[1] + p1[1])/2)

def sierpinski(t:turtle.Turtle, 
        vertex:Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]],
        degree:int) -> None:
    """Draw a Sierpinski triangle of degree DEGREE, with vertices VERTEX, using turtle T."""
    colormap:List[str] = ['blue','red','green','white','yellow', 'violet','orange']

    # Pre:
    assert degree < len(colormap)

    drawTriangle(t, vertex, colormap[degree])
    # Recursive case
    if degree > 0:
        sierpinski(t, (vertex[0], midPt(vertex[0], vertex[1]), midPt(vertex[0], vertex[2])),
            degree - 1)
        sierpinski(t, (vertex[1], midPt(vertex[1], vertex[0]), midPt(vertex[1], vertex[2])),
            degree - 1)
        sierpinski(t, (vertex[2], midPt(vertex[2], vertex[0]), midPt(vertex[2], vertex[1])),
            degree - 1)
    t.up()
    t.goto(vertex[0][0], vertex[0][1])

def main(args:List[str]) -> int:
    t:turtle.Turtle = turtle.Turtle()
    w:turtle.TurtleScreen = turtle.Screen()
    vertices:Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]] = \
        ((-200, -100), (0, 200), (200, -100))
    sierpinski(t, vertices, 3)
    w.exitonclick() # type: ignore
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)