from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f'score: {self.score}', align='center', font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)