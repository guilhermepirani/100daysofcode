from turtle import Turtle, Screen

# Create object
pen = Turtle()

# Draw a square
for _ in range(4):
    pen.fd(100)
    pen.lt(90)

# Keep window open
window = Screen()
window.exitonclick()