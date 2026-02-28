import time
import sys
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
screen.onkey(player.up, "Up")
cars = CarManager()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car) <20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_check():
        player.reset_postition()
        cars.increase_speed()
        scoreboard.increase_level()
