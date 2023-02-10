from days.day_022.files.helpers import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slow")
        self.xmove = 7
        self.ymove = 7
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self, axis):
        self.axis = axis
        if self.axis == "x":
            self.xmove *= -1

        elif self.axis == "y":
            self.ymove *= -1

        self.move_speed *= 0.2

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce("x")
