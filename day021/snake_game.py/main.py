'''Classic snake game'''

from time import sleep
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SNAKE_SPEED = 0.1
WALLS = [280, -280]

# Setting up window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')
window.tracer(0)

food = Food()
scoreboard = Scoreboard()
snake = Snake()

window.listen()

# Snake turning movements
window.onkey(snake.up, 'Up')
window.onkey(snake.down, 'Down')
window.onkey(snake.right, 'Right')
window.onkey(snake.left, 'Left')

# Runs game
running = True
while running:
    window.update()
    sleep(SNAKE_SPEED)

    snake.move()
    snake_pos = [snake.head.xcor(), snake.head.ycor()]

    # Detect colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increment_score()

    # Detect colission with walls
    if snake_pos[0] > WALLS[0] or snake_pos[0] < WALLS[1] or snake_pos[1] > WALLS[0] or snake_pos[1] < WALLS[1]:
        running = False
        scoreboard.game_over()

    # Detect colission with tail
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            running = False
            scoreboard.game_over()

window.exitonclick()