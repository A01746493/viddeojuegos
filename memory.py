"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

taps = 0

writer = Turtle(visible = False)

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    global mark,taps

    """Update mark and hidden tiles based on tap."""
    taps = taps + 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def win():
    clear()
    goto(0,0)
    shape(car)
    stamp()

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        """The if function is so that if it has a digit it is placed at x
        distance and if it has two digits it is placed at another x distance"""
        if tiles[mark] > 9:
            goto(x + 5, y)
        else:
            goto(x + 15, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal') )

    hidden = hide.count(True)
    found = 64 - hidden
    print("CARDS FOUND", found)

    if hidden ==0:
        win()
        up()
        goto(-100, 80)
        color('white')
        write('NAILED IT!', font=('Times New Roman', 30, 'normal'))
        goto(-140, -150)
        color('white')
        write(f'YOU MADE {taps} CLICS', font=('Arial', 20, 'normal'))
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
