"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Variable where random number from 0 to 5 is stored
random = randrange(0,4)
#Vector where the colors are declared"""
color_list = ['black','green','blue','purple','orange']
#The snake will take the color depending on the position of the random
color_snake = color_list[random]
#The color taken by random is removed so that it is not repeated
color_list.pop(random)
#The new random value is stored
random = randrange(0,3)
#The fruit will take the color depending on the position of the random
color_fruit = color_list[random]

"""Function to modify the position of the food at 2 seconds, the food only moves 1 pixel"""
def random_food():
    rand = randrange(0, 4)
    if rand == 0:
        if food.x == 190:
            food.x -= 10
        else:
            food.x += 10
    elif rand == 1:
        if food.x == -180:
            food.x += 10
        else:
            food.x -= 10
    elif rand == 2:
        if food.y == 190:
            food.y -= 10
        else:
            food.y += 10
    elif rand == 3:
        if food.y == -180:
            food.y += 10
        else:
            food.y -= 10
    ontimer(random_food, 2000)
    """Here you can select the time of that the food change"""

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def dibujo(x,y,size,name):
    """We store our snake's positions in an array with 'X' and 'Y'
    coordinates and loop to move the snake forward.
    """
    up()
    goto(x,y)
    down()
    color(name)
    begin_fill()

    for i in range (4):
        #by the value of the argument it takes, which depends on the length
        forward(size)
        #Change the viper's direction by 90 so it can only turn in those degrees
        left(90)

    end_fill()

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_fruit)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
random_food()
move()
done()
