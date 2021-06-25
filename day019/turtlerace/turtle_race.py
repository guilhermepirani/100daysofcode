'''Simple turtle race with betting'''

import random
from turtle import Turtle, Screen

def start_turtle(name, color, x, y, speed='slowest'):
    name = Turtle(shape='turtle')
    name.color(color)
    name.up()
    name.goto(x, y)
    name.down()
    name.speed(speed)
    turtles.append(name)


window = Screen()
window.title("Turtle Race")
window.setup(width=500, height=400)

race_on = False
turtles = []

# Set turtles
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'gray']
y_pos = -150
for color in colors:
    start_turtle(f'{color}_turtle', color, -230, y_pos)
    y_pos += 50

# Popup to enter bet
user_bet = window.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Starts race after user enters bet
if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            race_on = False
            turtle_color = turtle.pencolor()
            if user_bet == turtle_color:
                print(f"Congratulations! {turtle_color.capitalize()} is the first to cross the finishing line!")
            else:
                print(f"You've lost! {turtle_color.capitalize()} is the first to cross the finishing line!")

        turtle.fd(random.randint(1, 10))

window.exitonclick()