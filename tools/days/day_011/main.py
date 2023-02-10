# Day 11
# Updated 2023, Jarid Prince

from days.day_011.files.helpers import *


# Function to deal a card/number to a player
def deal(cards, player):
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for card in range(cards):
        card = random.choice(numbers)
        if card == 11 and sum(player) > 10:
            card = 1
        player.append(card)
    return card


# Function to calculate the sum of a given player's cards
def calculate_cards(player):
    score = sum(player)
    return score


# Main function. Runs game logic and resets if player chooses to play again
def day_011():
    title("BLACKJACK CAPSTONE")
    blackjack_logo()
    end = False
    msg = ""
    you = []
    pc = []
    deal(2, you)
    deal(2, pc)
    pc_firstcard = pc[0]
    current_score = calculate_cards(you)
    pc_current_score = calculate_cards(pc)

    if pc_current_score == 21 and current_score != 21 and len(pc) == 2:
        msg = "PC Blackjack! You lose!"
        end = True
    elif current_score == 21 and pc_current_score != 21 and len(you) == 2:
        msg = "Blackjack! You win!"
        end = True
    else:
        while end == False:
            if current_score > 21:
                msg = "Bust! You lose!"
                end = True
            else:
                nls(f"Your cards: {you}, Score: {current_score}")
                nls(f"Computer's first card: {pc_firstcard}")
                hitme = nli("Hit me?\ny or n.")
                cls()
                if hitme != "y":
                    end = True
                else:
                    card = deal(1, you)
                    current_score = calculate_cards(you)

        while pc_current_score < 16:
            deal(1, pc)
            pc_current_score = sum(pc)

        if pc_current_score == current_score:
            msg = "Tie!"
            end = True
        elif pc_current_score > 21:
            msg = "PC Bust! You win!"
            end = True
        elif pc_current_score <= 21 and pc_current_score > current_score:
            msg = "Computer has a higher score! You lose!"
            end = True
        elif current_score <= 21 and current_score > pc_current_score:
            msg = "You have a higher score! You win!"
            end = True

    if end == True:
        nls(f"{you}\nYour score: {current_score}")
        nls(f"{pc}\nPC score: {pc_current_score}")
        nls(msg)
        again = input("Play again?\n y or n.\n")
        if again == "y":
            cls()
            day_011()
