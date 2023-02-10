# Day 10
# Updated 2023, Jarid Prince

from days.day_010.files.helpers import *


# Simple mathematical functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


# Representation in operation variable
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Main calculator
def day_010():
    title("BASIC CALCULATOR")
    calculator_logo()
    num1 = float(nli("What's the first number?"))
    print("\n")
    shouldcontinue = True

    while shouldcontinue:
        for symbol in operations:
            print(symbol)
        operation_symb = nli("Select an operator from above:")
        num2 = float(nli("What's the second number?"))
        calculation_func = operations[operation_symb]
        answer = calculation_func(num1, num2)

        nls(f"{num1} {operation_symb} {num2} = {answer}")

        continuep = nli(f"Keep going with current answer ({answer})?\ny or n?\n")
        if continuep in yes_array:
            num1 = float(answer)
        else:
            cls()
            shouldcontinue = False
