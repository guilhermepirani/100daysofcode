import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_list = []

screen.listen()

screen.onkey(turtle.move_up, 'Up')
screen.onkey(turtle.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars
    if len(car_list) < 20:
        car = CarManager()
        car_list.append(car)

    # Car behavior
    for car in car_list:
        car.move(scoreboard.level)

        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

        if car.xcor() < -320:
            car.hideturtle()
            car_list.remove(car)
            del car
    
    # Level Up
    if turtle.ycor() >= 280:
        scoreboard.increment_level()
        turtle.finish_line()
    



screen.exitonclick()