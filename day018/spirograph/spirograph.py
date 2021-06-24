from turtle import Turtle, Screen, colormode
from random import randint

def random_rgb():
    '''Generate random rgb color'''
    
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pen.color(r, g, b)

# Create object
pen = Turtle()
pen.speed('fastest')
colormode(255)

n_circles = 100

# Draw a spirograph
for _ in range(n_circles):
    random_rgb()
    pen.circle(100)
    pen.setheading(pen.heading() + (360 / n_circles))


# Keep window open
window = Screen()
window.exitonclick()