'''Simple drawing board using turtle graphics'''

from turtle import Turtle, Screen

def move_forward():
    pen.fd(10)

def move_backward():
    pen.bk(10)

def turn_right():
    pen.rt(10)

def turn_left():
    pen.lt(10)

def clear():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()

pen = Turtle()
window = Screen()

# Make window object listen commands
window.listen()

# Call functions on key press
window.onkeypress(move_forward, 'w')
window.onkeypress(move_backward, 's')
window.onkeypress(turn_right, 'd')
window.onkeypress(turn_left, 'a')
window.onkeypress(clear, 'c')

window.exitonclick()