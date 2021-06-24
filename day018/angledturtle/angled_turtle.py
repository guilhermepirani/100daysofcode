from turtle import Turtle, Screen, colormode
from random import randint

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pen.color(r, g, b)

# Create object
pen = Turtle()
colormode(255)

sides = 3
final_sides = 12

# Draw shapes given sides variables
while sides < final_sides:
    random_rgb()    
    for _ in range(sides):
        pen.fd(100)
        pen.rt(360 / sides)
    sides += 1

# Keep window open
window = Screen()
window.exitonclick()