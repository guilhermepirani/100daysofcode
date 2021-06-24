from turtle import Turtle, Screen

# Create object
pen = Turtle()
dashes = 10

# Draw a dashed line
for _ in range(dashes):
    pen.fd(30)
    pen.up()
    pen.fd(10)
    pen.down()

# Keep window open
window = Screen()
window.exitonclick()