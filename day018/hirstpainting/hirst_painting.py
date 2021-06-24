import colorgram
from random import choice
from turtle import Turtle, Screen, colormode

# Get colors from image
colors = colorgram.extract('day018/hirstpainting/image.jpg', 10)

# Get rgb values from colors
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # Exclude whites
    if (r + g + b) < 665:
        rgb_colors.append((r, g, b))

# Pen starting settings
pen = Turtle()
pen.speed('fastest')
pen.up()
pen.setheading(225)
pen.fd(300)
pen.down()
pen.setheading(0)
colormode(255)

# Drawing loop
n_dots = 100
for dots in range(1, n_dots + 1):
    pen.dot(20, choice(rgb_colors))
    pen.up()
    pen.fd(50)
    pen.down()

    if dots % 10 == 0:
        pen.up()
        for _ in range(2):
            pen.lt(90)
            pen.fd(50)
        pen.fd(450)
        pen.setheading(0)

# Keep window open
window = Screen()
window.exitonclick()