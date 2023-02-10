# Day 3
# Updated 2023, Jarid Prince

from days.day_003.files.helpers import *

def day_003():
	title("TREASURE HUNT")
	treasure_intro()
	direction1 = nli("You're at a crossroad, where do you want to go?\nLeft or right?")
	if direction1 not in left:
		cls()
		msg = "You fell into a hole!"
		gg(msg)
	else:
		cls()
		direction2 = nli("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.")
		if direction2 not in wait:
			cls()
			msg = "You got eaten by sharks!"
			gg(msg)
		else:
			cls()
			direction3 = nli("You arrive at the island unharmed.\nThere is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\nType 'red', 'blue' or 'yellow'.")
			if direction3 not in yellow:
				if direction3 in blue:
					msg = "You entered a room full of beasts!"
				elif direction3 in red:
					msg = "You entered a room smelling of gas.\nThe doors locked shut and someone threw a match in!"
				else:
					msg = "You didn't pick one of the doors before you!\nInstead, you slipped on a banana and died!"
				cls()
				gg(msg)
			else:
				cls()
				msg = "You found the treasure! You win!"
				nls(f"{msg}")