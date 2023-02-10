# Day 14
# Updated 2023, Jarid Prince

from days.day_014.files.helpers import *

# Gets/sets/displays a and b
def new_sequence(previous_array, b_array):
    # get data
    if len(previous_array) == 0:
        a = random.choice(hl_gdata)
    else:
        a = previous_array[-1]
    aname = a["name"]
    adesc = a["description"]
    acountry = a["country"]

    b = random.choice(hl_gdata)
    if len(b_array) != 0:
        while b_array[-1] == b:
            b = random.choice(hl_gdata)
    b_array.append(b)
    bname = b["name"]
    bdesc = b["description"]
    bcountry = b["country"]

    # display data & vs
    print(f"Compare A: {aname}, a {adesc} from {acountry}.")
    vs()
    print(f"Against B: {bname}, a {bdesc} from {bcountry}.")
    return a, b


# Compares a and b follower count
def compare(previous_array, a, b):
    draw = False
    if a["follower_count"] > b["follower_count"]:
        atop = True
    elif a["follower_count"] == b["follower_count"]:
        draw = True
    elif a["follower_count"] < b["follower_count"]:
        atop = False
    previous_array.append(b)
    return atop, draw


# Checks answer
def check_answer(atop, draw, score, gg):
    answer = nli("Who has more followers? Type 'A' or 'B':\n")

    cls()
    if ((answer == "b" or answer == "B") and atop == True) or (
        (answer == "a" or answer == "A") and atop == False
    ):
        gg = True
        nls(f"Sorry that's wrong. Final Score: {score}")
        previous_array = []
        score = 0
    elif draw == True:
        nls("They're actually the same! Who'd have thunk it!")
        gg = False
    elif ((answer == "b" or answer == "B") and atop == False) or (
        (answer == "a" or answer == "A") and atop == True
    ):
        # higher_or_lower()
        score += 1
        nls(f"You're right! Current score: {score}")
        gg = False
    return score, gg


# Loops if not incorrect, ending if incorrect
def day_014():
    title("HIGHER LOWER GAME")
    higher_or_lower()
    nls("Guess who has more followers!")

    previous_array = []
    b_array = []
    score = 0
    gg = False

    while gg == False:
        a, b = new_sequence(previous_array, b_array)
        atop, draw = compare(previous_array, a, b)
        (
            score,
            gg,
        ) = check_answer(atop, draw, score, gg)
