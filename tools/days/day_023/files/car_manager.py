from days.day_023.files.helpers import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
START_POS = 300


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn(self):
        spawn_control = random.randint(1, 5)
        if spawn_control == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            rand_y = random.randint(-250, 250)
            new_car.goto(START_POS, rand_y)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def drive(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
