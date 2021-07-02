from turtle import Turtle

FONT = ('Courier', 10, 'normal')

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self, x, y):
        self.goto(x, y)

    def fill(self, name):
        self.write(name, font=FONT)

