# Day 12
# Updated 2023, Jarid Prince

from days.day_012.files.helpers import *


# Function to set difficulty
def set_difficulty():
    difficulty = nli("Play 'easy' or 'hard' mode?")
    if difficulty in easy_array:
        attempts = 10
    elif difficulty in hard_array:
        attempts = 5
    return attempts


# Function to check user guess
def check_guess_int():
    guess = ""
    while type(guess) != int:
        try:
            guess = int(input("Your guess: "))
        except:
            nls("You must type a number. Try again.")
    return guess


# Main function, selects a random number up to 100 and runs user input logic
def day_012():
    title("NUMBER GUESSING GAME")
    guessing_game()
    win = False
    attempts = set_difficulty()
    nls("I'm thinking of a number between 1 and 100")
    the_number = random.choice(range(1, 101))

    while attempts != 0 and win != True:
        nls(f"You have {attempts} guesses remaining.")

        guess = check_guess_int()

        if guess != the_number:
            attempts -= 1
            if guess > the_number:
                msg = "Too high!"
            else:
                msg = "Too low!"
            nls(msg)
        else:
            win = True

    if attempts == 0:
        nls("You lose!")
    if win == True:
        nls("Correct! You win!")
    again = nli("Play again? y or n.")
    cls()
    if again in yes_array:
        day_012()
    else:
        nls("Goodbye!")
