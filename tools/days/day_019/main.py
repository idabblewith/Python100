# Day 19
# Updated 2023, Jarid Prince

from days.day_019.files.helpers import *

# Main logic
def day_019():
    title("TURTLE RACE")
    number_of_turtles = 6
    screen = Screen()
    screen, height, width, user_bet = setup_screen(screen)
    try:
        race_on = True
        race(user_bet, number_of_turtles, race_on, width, height, COLORS_IN_IMAGE)
        screen.bye()
    except:

        race_on = True
        race(user_bet, number_of_turtles, race_on, width, height, COLORS_IN_IMAGE)
        screen.bye()


# Creates the application window with Turtle
def setup_screen(screen):
    screen.title("Turtle Art")
    width = 1000
    height = 500
    screen.setup(width, height)
    screen.colormode(255)
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    rootwindow.call("wm", "attributes", ".", "-topmost", "0")
    user_bet = screen.textinput(
        "Make your bet",
        "There are 6 turtles. Which turtle will win the race?\nType a number between 1-6.",
    )
    return screen, height, width, user_bet


# Selects a random color from colors variable
def newcolor(colors):
    a = random.choice(colors)
    return a


# Basic means to spacing out turtle equally (startpoint & gap)
def spacing_handler(number_of_turtles, height):
    if number_of_turtles == 1:
        startpoint = 0
        gap = 0
    elif number_of_turtles >= 2:
        startpoint = (height / (height / 150)) * 1.1
        gap = startpoint / 2 + (startpoint * 1.1 - startpoint)
    return startpoint, gap


# Sets the startpoints for each turtle based on number of turtles/height
def set_turtles(number_of_turtles, height, colors):
    startpoint, gap = spacing_handler(number_of_turtles, height)
    turtles = {}

    for number in range(1, number_of_turtles + 1):
        turtle = Turtle(shape="turtle")
        turtle.color(newcolor(colors))
        turtle.penup()
        turtle.speed("fastest")
        turtle_number = int(f"{number}")
        turtles[turtle_number] = {}
        turtles[turtle_number]["name"] = turtle_number
        turtles[turtle_number]["x"] = int(-230)
        turtles[turtle_number]["y"] = int(startpoint + (number * 50 * -1))
        turtles[turtle_number]["turtle"] = turtle

    for number in turtles:
        turtlelol = turtles[number]["turtle"]
        x = turtles[number]["x"]
        y = turtles[number]["y"]
        turtlelol.goto(x=x, y=y)
    return turtles


# Begins random movement of turtles in forward direction
def move(width, turtles, race_on):
    # print(turtles)
    race_on = True
    while race_on == True:
        for number in turtles:
            turtlelol = turtles[number]
            turtlelol["turtle"].forward(random.randint(1, 10))
            if turtlelol["turtle"].xcor() > (width / 2) - 20:
                winner = turtlelol["name"]
                print(f"The winner is Turtle {winner}")
                race_on = False
    return winner


# Begins the race
def race(user_bet, number_of_turtles, race_on, width, height, colors):
    winners = []
    turtles = set_turtles(number_of_turtles, height, colors)
    winner = move(width, turtles, race_on)
    winners.append(str(winner))
    print(f"You bet on Turtle {str(user_bet)}")

    if user_bet in winners:
        print("You won your bet!")
    else:
        print("You lost your bet!")
    winners = []
