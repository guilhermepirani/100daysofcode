'''A classic pong game'''

from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


GAME_SPEED = 0.03


# Window setup
window = Screen()
window.setup(width=800, height=600)
window.bgcolor('black')
window.title('Pong')
window.tracer()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

window.textinput(title='Ready, set', prompt='Press enter to start game')

window.listen()

# Movement
window.onkeypress(right_paddle.go_up, 'Up')
window.onkeypress(right_paddle.go_down, 'Down')
window.onkeypress(left_paddle.go_up, 'w')
window.onkeypress(left_paddle.go_down, 's')

# Runs game
running = True
while running:
    window.update()

    ball.move()
    sleep(GAME_SPEED)

    # Detect colission with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect colission with paddles
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50:
            ball.x_bounce()

    # Detect goal
    if ball.xcor() > 360:
        scoreboard.increment_score_left()
        ball.reset_position()
    elif ball.xcor() < -360:
        scoreboard.increment_score_right()
        ball.reset_position()

    if scoreboard.right_score == 3 or scoreboard.left_score == 3:
        running = False
        scoreboard.game_over()

window.exitonclick()