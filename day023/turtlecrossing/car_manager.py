import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(300, 900), random.randint(-240, 240))
        self.setheading(180)
        self.showturtle()

    def move(self, level):
        self.fd(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))
