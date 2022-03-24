"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
#Impoert turtle
from turtle import *


from freegames import vector


""" Function line; draw a line between two points """
def line(start, end):
    """Draw line from start to end and fill it with a color."""
    
    up() #Pull the pen up – no drawing when moving.
    goto(start.x, start.y)  #Move the pen to x,y position
    down() #Pull the pen down – drawing when moving.
    goto(end.x, end.y) 

""" Function square; Draw a square with a defined 
    length from start x to end x  
"""
def square(start, end):
    """Draw a square from start to end and fill it with a color."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill() #To be called just before drawing a shape to be filled.

    for count in range(4):
        forward(end.x - start.x) #Move the turtle forward 
        left(90) #Make de turtle rotate 

    end_fill() #filled all de figure

"""Function cric; Draw a circle calculating the radius, between two points"""
def circ(start, end):
    """Variable that calculates the radius of the circle 
    from the points in X and Y. 
    """
    import math
    rad = math.dist(start,end)
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Funcion de turtle para dibujar un circulo
    circle(rad)

    end_fill()

"""Function rectangle;Draw a rectangle with a defined 
    length from start x to end y   
    """
def rectangle(start, end):
    """Draw a rectangle from start to end and fill it with a color."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x - start.x)
        left(90)    
        forward(end.y - start.y)
        left(90)
        
    end_fill()

"""Function triangle;Draw a rectangle with a defined 
    length from start x to end y   
    """
def triangle(start, end):
    """Draw a triangle from start to end and fill it with a color."""
    pass  # TODO 
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    forward (end.x - start.x)
    left (120)
    forward (end.x - start.x)
    left (120)
    forward (end.x - start.x)

""" Call the function of the figure depending on which key you press."""
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

""" Stores in a dictionary the letter and function that it sends to call"""
def store(key, value):
    """Store value in state at key."""
    state[key] = value





state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circ), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
