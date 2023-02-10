# Day 2
# Updated 2023, Jarid Prince

from days.day_002.files.helpers import *

def day_002():
	title("BILL SPLITTER")
	# Numbers appropriately cast for each variable
	bill = float(nli("What was your total bill?"))
	tip_percentage = int(nli("What percentage would you like to tip?\n0, 10, 12, or 15?"))
	amount_of_people = int(nli("How many people are splitting the bill?"))
	# Adds the tip to the bill
	total_bill = (bill * (tip_percentage/100)) + bill 
	# Sets the payment pp as a 2 decimal floating number (as string)
	payment_per_person = "{:.2f}".format(total_bill/amount_of_people)
	nls(f'Each person should pay: ${payment_per_person}')