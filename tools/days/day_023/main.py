# Day 23
# Updated 2023, Jarid Prince

from days.day_023.files.helpers import *
from days.day_023.files.player import Player
from days.day_023.files.car_manager import CarManager
from days.day_023.files.scoreboard import Scoreboard


def day_023():
    title("TURTLE CROSSING CAPSTONE")
    # Creates Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Instantiates Player, Carmanager & Score classes
    player = Player()
    car = CarManager()
    score = Scoreboard()

    # Listens to W key presses
    screen.listen()
    screen.onkeypress(player.move, "w")

    # Launches game
    gameon = True
    while gameon:
        # Prevent screen closure
        time.sleep(0.1)
        # Spawn cars and make them cross
        car.spawn()
        car.drive()
        # Kill turtle if too close
        screen.update()
        for item in car.cars:
            if player.distance(item) <= 25:
                print("you dead")
                score.game_over()
                gameon = False
        # If player reaches the end, update score, increase car speed, reset
        if player.finish() == True:
            score.update()
            player.back_to_start()
            car.level_up()
    # Clean up
    screen.clear()
    screen.bye()
