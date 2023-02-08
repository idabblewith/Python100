# Day 5 - idabblewith

from days.day_005.files.helpers import *

def day_005():
	title("PASSWORD GENERATOR")
	# Sets available characters to list of printable characters in built-in string var
	AVAIL_CHAR = [char for char in string.printable]
	# Sets subsets based on each type of character in string.printable
	NUMBER = AVAIL_CHAR[:10]
	ALPHA = AVAIL_CHAR[10:62]
	SYMBOL = AVAIL_CHAR[62:-6]
	# Asks user for input regarding amount of numbers, alphabet, symbol characters
	numbers_amount = int(nli("How many numbers would you like in your password?")) + 1
	alphabet_amount = int(nli("How many letters would you like in your password?")) + 1
	symbols_amount = int(nli("How many symbols would you like in your password?")) + 1
	new_pass_array = []
	# Adds a letter, symbol, number to new_pass array based on user input
	for each_number in range(1,numbers_amount):
		new_pass_array.append(random.choice(NUMBER))	
	for each_letter in range(1,alphabet_amount):
		new_pass_array.append(random.choice(ALPHA))	
	for each_symbol in range(1,symbols_amount):
		new_pass_array.append(random.choice(SYMBOL))
	# Shuffles array and prepares new_pass string for returning to user
	random.shuffle(new_pass_array)
	new_pass =""
	# Adds each character from shuffled array to string and returns it
	for character in new_pass_array:
		new_pass+=character
	nls(f"Here is your new password: {new_pass}")
	