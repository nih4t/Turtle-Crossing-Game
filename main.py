from turtle import Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle Crossing")

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")

car_manager.generate_traffic_jam(20)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # collision with car
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.increase_speed()
        scoreboard.update_level()


    if car_manager.player_car_collision(player.xcor(), player.ycor()):
        game_is_on = False
        scoreboard.level = 1



