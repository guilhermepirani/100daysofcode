from turtle import Turtle, Screen, colormode
from random import randint, choice

def random_rgb():
    '''Generate random rgb color'''
    
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pen.color(r, g, b)

# Create object
pen = Turtle()
colormode(255)
pen.pensize(10)
pen.speed('fastest')

directions = [0, 90, 180, 270]

# Draw random lines  
for _ in range(200):
    random_rgb()  
    pen.fd(30)
    pen.setheading(choice(directions))


# Keep window open
window = Screen()
window.exitonclick()