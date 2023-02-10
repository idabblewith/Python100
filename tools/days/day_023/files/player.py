from days.day_023.files.helpers import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(
        self,
    ):
        super().__init__()
        self.start = STARTING_POSITION
        self.move_distance = MOVE_DISTANCE
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.back_to_start()

    def move(self):
        self.goto(0, self.ycor() + self.move_distance)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def back_to_start(self):
        self.goto(self.start)
