# Day 16
# Updated 2023, Jarid Prince

from days.day_016.files.helpers import *
from days.day_016.files.money_machine import MoneyMachine
from days.day_016.files.menu import Menu
from days.day_016.files.coffee_maker import CoffeeMaker


def day_016():
    title("OOP COFFEE MACHINE")
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    is_on = True

    # Keeps looping until user turns off or resources insufficient
    while is_on:
        # Provides list of options for user to choose from
        options = menu.get_items()
        choice = nli(f"What would you like?\n{options}\n")
        if choice == "off":
            is_on = False
        # Presents the money report and coffee report
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        # When chooseing coffee or anything else
        else:
            selectable = menu.menu_choices()
            while choice not in selectable:
                cls()
                nls("Sorry, that item is not available.")
                choice = nli(f"What would you like?\n{options}\n")
            drink = menu.find_drink(choice)

            # Checks if resources sufficient and payment made to make coffee
            if coffee_maker.is_resource_sufficient(
                drink
            ) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                # Asks user if they want more, if no quits, otherwise checks
                # resources and loops again if available.
                again = nli("Would you like more coffee?\n'y' or 'n'")
                if again == "n":
                    cls()
                    is_on = False
                else:
                    cls()
                    if not coffee_maker.is_resource_sufficient(drink):
                        is_on = False
