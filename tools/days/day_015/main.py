# Day 15
# Updated 2023, Jarid Prince

from days.day_015.files.helpers import *

# Provides user with a choice of drinks
def ask_drink():
    choice = nli(
        'What would you like? "espresso", "latte", or "cappuccino"?\nType \'report\' to see resources.'
    ).lower()
    while choice not in COFFEE_CHOICES:
        choice = ask_drink()

    return choice


# Checks User input regarding payment
def check_input(denomination):
    isNumber = []
    while True not in isNumber:
        prompt = nli(f"How many {denomination}?\n")
        for character in prompt:
            if character not in numbers:
                isNumber.append(False)
        if False in isNumber:
            nls("That's not a number. Whole numbers only, please.\nTry again.\n")
            isNumber = []
        else:
            isNumber.append(True)
    converted = int(prompt)
    return converted


# Checks resources (milk, water, coffee)
def check_resources(drink):
    are_sufficient = True
    item = COFFEE_MENU[drink]
    if item["ingredients"]["water"] > resources["water"]:
        ingredient = "water"
        are_sufficient = False
    elif item["ingredients"]["coffee"] > resources["coffee"]:
        ingredient = "coffee"
        are_sufficient = False
    elif item["ingredients"]["milk"] > resources["milk"]:
        ingredient = "milk"
        are_sufficient = False
    else:
        ingredient = "none"
    return are_sufficient, ingredient


# Asks user for payment in 4 denominations
def ask_payment():
    quarters = check_input("quarters")
    dimes = check_input("dimes")
    nickels = check_input("nickels")
    pennies = check_input("pennies")
    total_paid = (
        (quarters * COFFEE_DENOMINATIONS["quarter"])
        + (dimes * COFFEE_DENOMINATIONS["dime"])
        + (nickels * COFFEE_DENOMINATIONS["nickel"])
        + (pennies * COFFEE_DENOMINATIONS["penny"])
    )
    return total_paid


# Checks payment against price of selected item
def check_payment(total_paid, choice):
    run_again = False
    profits = 0
    cls()
    nls(f"Total is ${total_paid}.")

    if total_paid < COFFEE_CHOICES[choice]:
        nls(
            f"You are ${round(COFFEE_CHOICES[choice] - total_paid, 2)} short.\nYou've been refunded. Please try again."
        )
        run_again = True
    elif total_paid > COFFEE_CHOICES[choice]:
        change = round(total_paid - COFFEE_CHOICES[choice], 2)
        nls(f"You are ${change} over.\nHere is your change.")
        profits += total_paid - change
    else:
        nls(f"Perfect. Here's your coffee!")
        profits += total_paid
    return profits, run_again


# After selection, ties in the above functions to run the machine
def on_selection(choice, out_of_order):
    cls()
    register = []
    nls(f"You selected {choice}.")
    resource, missing_resource = check_resources(choice)
    if resource == True:
        item = COFFEE_MENU[choice]
        msub = item["ingredients"]["milk"]
        csub = item["ingredients"]["coffee"]
        wsub = item["ingredients"]["water"]
        resources["milk"] -= msub
        resources["water"] -= wsub
        resources["coffee"] -= csub
        nls(f"The price is: ${COFFEE_CHOICES[choice]} Please insert coins.\n")
        total_paid = ask_payment()

        profits, run_again = check_payment(total_paid, choice)
        while run_again == True:
            total_paid = ask_payment()
            profits, run_again = check_payment(total_paid, choice)
        register.append(profits)
        b = sum(register)
    else:
        nls(f"Sorry we are out of {missing_resource}!")
        out_of_order = True
        nls("No can do.")
        b = sum(register)
    return b, out_of_order


# Main logic which calls above function and is recursively run if more coffee requested.
def coffee():
    out_of_order = False
    total_profits = 0
    msg = ""
    choice = ask_drink()
    while choice == "report":
        nls(f'Water levels are {resources["water"]}mls')
        nls(f'Milk levels are {resources["milk"]}mls')
        nls(f'Coffee levels are {resources["coffee"]}grams')
        choice = ask_drink()
    if choice == "off":
        sys.exit()
    else:
        profits, out_of_order = on_selection(choice, out_of_order)

    if out_of_order == True:
        msg = "Out of order"
    else:
        again = nli("Do you want more coffee?")
        cls()
        if again == "y":
            second_msg, second_seq = coffee()
            profits += second_seq
        else:
            msg = "finished"
        total_profits = profits

    return msg, total_profits


# Runner
def day_015():
    title("COFFEE MACHINE")
    msg, total_profits = coffee()
    profit = 0
    profit += round((total_profits), 2)
    nls(f"Profit: ${profit}")
