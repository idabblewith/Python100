from days.day_021.files.helpers import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(
            f"Score: {self.score}", align="center", font=("Courier", 24, "normal")
        )

    def updatescore(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}", align="center", font=("Courier", 24, "normal")
        )
        print(self.score)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over!", align="center", font=("Arial", 24, "normal"))
