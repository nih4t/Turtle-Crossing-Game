from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.update_level()

    def update_level(self):
        # Clear the previous level text, increment the level, and display the updated level
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, align="left", font=("Arial", 16, "normal"))

    def game_over(self):
        # Display the "GAME OVER" message at the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 16, "normal"))
