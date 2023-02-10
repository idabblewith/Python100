from days.day_021.files.helpers import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_seg = []
        self.spawn()
        self.head = self.snake_seg[0]

    def spawn(self):
        for pos in STARTING_POSITIONS:
            self.add_seg(pos)

    def add_seg(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_seg.append(segment)

    def extend(self):
        self.add_seg(self.snake_seg[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_seg) - 1, 0, -1):
            newx = self.snake_seg[seg_num - 1].xcor()
            newy = self.snake_seg[seg_num - 1].ycor()
            self.snake_seg[seg_num].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
