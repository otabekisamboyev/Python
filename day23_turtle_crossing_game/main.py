import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_generator()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with wall
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        scoreboard.add_level()
        car_manager.level_up()


screen.exitonclick()
