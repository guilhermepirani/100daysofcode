from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
            new_seg = Turtle(shape='square')
            new_seg.color('white')
            new_seg.up()
            new_seg.goto(pos)
            self.snake_body.append(new_seg)

    def grow(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[seg - 1].xcor()
            y_cor = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x_cor, y_cor)
        self.head.fd(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)