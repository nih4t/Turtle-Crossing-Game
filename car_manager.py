COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MORE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def generate_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.penup()
        random_y = random.randint(-250, 250)
        random_x = random.randint(300, 800)
        car.goto(random_x, random_y)
        self.cars.append(car)

    def generate_traffic_jam(self, number_of_cars):
        for i in range(number_of_cars):
            self.generate_car()

    def increase_speed(self):
        self.move_distance += MORE_INCREMENT

    def move(self):
        for car in self.cars:
            car.backward(self.move_distance)

            if car.xcor() < -300:
                random_y = random.randint(-250, 250)
                car.goto(300, random_y)

    def player_car_collision(self, player_xcor, player_ycor):
        for car in self.cars:
            if car.distance(player_xcor, player_ycor) < 20:
                return True
        return False









