from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, alignment):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(alignment)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)
