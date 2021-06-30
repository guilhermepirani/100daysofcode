from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.level = 1
            self.up()
            self.hideturtle()
            self.goto(-240, 270)
            self.write_level()
        
        def write_level(self):
            self.write(f'Level: {self.level}', align='center', font=FONT)

        def increment_level(self):
            self.level += 1
            self.clear()
            self.write_level()

        def game_over(self):
            self.goto(0, 0)
            self.write('GAME OVER', align='center', font=FONT)