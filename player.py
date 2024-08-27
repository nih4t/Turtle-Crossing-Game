from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        # Move the player forward by 10 units in the direction it is facing
        self.forward(10)
