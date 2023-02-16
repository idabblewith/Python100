# Day 18
# Updated 2023, Jarid Prince

from days.day_018.files.helpers import *

# Main logic - creates screen with Turtle
def day_018():
    title("TURTLE ART")
    nls("Watch the art! :)")
    nls(f"{bcolors.FAIL}DO NOT CLOSE WINDOW UNTIL COMPLETE{bcolors.ENDC}")
    # Remedy issue caused by running file through PythonSensei.py
    try:
        screen = Screen()
        screen = setup_screen(screen)
        timmy = Turtle()
        timmy = setup_timmy(timmy)
        set_timmy_movement(timmy)
        go(timmy, 10)
        cleanup(timmy, screen)

    except Exception as e:
        screen = Screen()
        screen = setup_screen(screen)
        timmy = Turtle()
        timmy = setup_timmy(timmy)
        set_timmy_movement(timmy)
        go(timmy, 10)
        cleanup(timmy, screen)


# Creates a turtle named Timmy
def setup_timmy(timmy):
    timmy.hideturtle()
    timmy.speed("fastest")
    timmy.pencolor("white")
    timmy.penup()
    return timmy


# Sets the screen parameters
def setup_screen(screen):
    screen.title("Turtle Art")
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    screen.colormode(255)
    return screen


# Sets Timmy's movement
def set_timmy_movement(timmy):
    timmy.setheading(225)
    timmy.forward(320)
    timmy.setheading(360)


# Selects a random color from colors variable
def set_new_color(colors):
    a = random.choice(colors)
    return a


# Begins Timmy's movement
def go(timmy, times):
    for _ in range(0, times):
        for _ in range(10):
            timmy.dot(20, set_new_color(COLORS_IN_IMAGE))
            timmy.forward(50)
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


# Cleanup function when program has ended
def cleanup(timmy, screen):
    timmy.clear()
    screen.clear()
    screen.bye()
    del timmy
    del screen
