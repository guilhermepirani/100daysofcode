from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.up()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f'{self.left_score} {self.right_score}', align='center', font=FONT)

    def increment_score_right(self):
        self.right_score += 1
        self.clear()
        self.write_score()

    def increment_score_left(self):
        self.left_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)