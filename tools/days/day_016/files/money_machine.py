from days.day_016.files.helpers import *


class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        nls(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        nls("Please insert coins.")
        for coin in self.COIN_VALUES:
            user_input = ""
            while type(user_input) != int:
                user_input = input(f"How many {coin}?: ")
                try:
                    user_input = int(user_input)
                except:
                    nls("Must be an integer, try again.")
                    cls()
            value = float(user_input) * self.COIN_VALUES[coin]
            self.money_received += value
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        cls()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            nls(f"Here's your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            nls("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
