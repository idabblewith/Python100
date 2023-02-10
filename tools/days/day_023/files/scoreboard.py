from days.day_023.files.helpers import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(120, 260)
        self.write(f"Score: {self.score}", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
