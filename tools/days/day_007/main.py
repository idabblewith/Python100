# Day 7
# Updated 2023, Jarid Prince

from days.day_007.files.helpers import *

def day_007():
	title("HANGMAN")
	nls(hangman_logo)
	lives = 6
	word = random.choice(hangman_words)
	display = ["_" for character in word]
	guesses = []
	
	# Function for assessing each letter in random word against user's guess
	# Updates the blank (_) to be the guess if correct
	def game_loop(guess):
		for position in range(0, len(word)):
			for letter in word[position]:
				if word[position] == guess:
					display[position] = letter

	end_of_game = False
	won = False

	# Runs until the word is known or lives are 0
	while "_" in display and lives > 0:
		guess = nli("Guess a letter.").lower()
		cls()
		if len(guess) != 1:
			guess = nli("Guess a letter. One letter only").lower()
		if guess in guesses:
			nls(hangman_stages[lives])
			nls(f"You have already tried that one!\nLives: {lives}")
		else:
			# Set _ to guessed letter if correct
			game_loop(guess)
			# Display hangman stage and let user know guess was correct
			if guess in word:
				nls(hangman_stages[lives])
				nls(f"Well done! '{guess}' is in the word!\nLives: {lives}")
			# Update hangman stages if incorrect, display new lives 
			else:
				lives-=1
				nls(hangman_stages[lives])
				nls(f"Nope! '{guess}' is not in the word! You lose a life!\nLives: {lives}")
			# Add guess to list and display it
			guesses.append(guess)
			nls(f"You've already tried these:\n{guesses}")
			# If lives reaches 0, set game over
			if lives == 0:
				end_of_game = True
				won = False
			# Display mystery word with remaining blank slots
			nls(display)

	# Set won to true, and end game if no more blanks
	if "_" not in display:
		won = True

	end_of_game = True
	# Based on won variable, determine end game message
	if end_of_game: 
		if won:
			msg = "You win!"
		else:
			msg = f"You lose!\nThe words was {word}!"
		print("Game Over")
		nls(msg)