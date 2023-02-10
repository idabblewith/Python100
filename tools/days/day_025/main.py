# Day 25
# Updated 2023, Jarid Prince

from days.day_025.files.helpers import *


def day_025():
    title("US STATES GAME")
    # Creates screen
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    rootwindow.call("wm", "attributes", ".", "-topmost", "0")
    image = "./tools/days/day_025/files/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Reads data from CSV to generate a states list
    data = pandas.read_csv("./tools/days/day_025/files/50_states.csv")
    states_list = data.state.to_list()

    # Logic runs while guesses is less than 50
    guesses = []
    while len(guesses) < 50:
        answer_state = screen.textinput(
            title=f"{len(guesses)}/50 States Correct", prompt="Guess another."
        ).title()
        # Breaks the loop on typing exit, creates a states to learn csv file based on remainder
        if answer_state == "Exit":
            missing_states = []
            for state in states_list:
                if state not in guesses:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        # Appends guessed state if correct and writes the name on the location
        # based on csv data
        if answer_state in states_list and answer_state not in guesses:
            guesses.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
    # Clean up
    screen.clear()
    screen.bye()
