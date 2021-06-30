from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.bk(MOVE_DISTANCE)