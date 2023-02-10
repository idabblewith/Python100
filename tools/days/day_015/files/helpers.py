from misc import nls, title, nli, numbers, cls, sys

COFFEE_CHOICES = {
    "espresso": 1.5,
    "latte": 2.0,
    "cappuccino": 2.5,
    "report": "Printing report...",
    "off": "Switching off...",
}

COFFEE_MENU = {
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}},
    "latte": {"ingredients": {"water": 250, "milk": 150, "coffee": 24}},
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18}},
}

COFFEE_DENOMINATIONS = {"penny": 0.01, "nickel": 0.05, "dime": 0.1, "quarter": 0.25}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
