# Day 4
# Updated 2023, Jarid Prince

from days.day_004.files.helpers import *

def day_004():
	title("ROCK PAPER SCISSORS")
	options = [rock, paper, scissors]
	def newseq():
		nls("New Game:")
		user_choice = int(nli("What do you choose?\nType '1' for Rock, '2' for Paper, or '3' for Scissors.")) -1
		if user_choice >= 3 or user_choice < 0:
			nls("You typed an invalid number. You lose!")
			newseq()
			cls()
		else:
			pc_choice =  random.randint(0, len(options)-1)

			nls(f"You chose:\n{options[user_choice]}")
			nls(f"Computer chose:\n{options[pc_choice]}")

			if user_choice == pc_choice -1:
				nls("You lose!")
			elif user_choice == pc_choice:
				nls("It's a draw!")
			else:
				nls("You win!")
			restart = nli("Type y and enter to go again.")
			if restart in yes_array:
				cls()
				newseq()
	newseq()