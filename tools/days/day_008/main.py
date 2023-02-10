# Day 8
# Updated 2023, Jarid Prince

from days.day_008.files.helpers import *

# Note, text files are removed by default

# Creating variables based on characters in string.printable
AVAIL_CHAR = [char for char in string.printable]
NUMBERS = AVAIL_CHAR[:10]
ALPHAS_LOWER = AVAIL_CHAR[10:36]
ALPHAS_CAPS = AVAIL_CHAR[36:62]
SYMBOLS = AVAIL_CHAR[62:-6]
LEAVE_BE = SYMBOLS + NUMBERS

# Handler for direction (encrypt/decrypt) attempts. 
direction_attempts = []


# Function which asks direction, and appends choice to above handler
def ask_direction():
    directions = ["encrypt", "e", "decrypt", "d"]
    direction = nli("Would you like to decrypt or encrypt?\nType 'decrypt' or 'd' for decrypt.\nType 'encrypt' or 'e' for encrypt.\n")
    direction_attempts.append(direction)
    if direction_attempts[-1] not in directions:
        cls()
        nls("You must either type 'encrypt', 'e', 'decrypt', or 'd'!\nTry again.")
        ask_direction()
    return direction_attempts[-1]


# Function which asks message to encrypt
def ask_msg():
    msg = nli("Write a message to encrypt:")
    return msg


# Function which asks rotation key
def ask_rotation():
    rotation_key = ""
    ready = False
    
    while ready == False:
        try:
            rotation_key = nli("What is the rotation key?")
            rotation_key = int(rotation_key)
        except ValueError:
            cls()
            nls(f"You must only enter a number!\nTry again.")
        else:
            if rotation_key > 25 or rotation_key < 0:
                cls()
                nls("Number must be between 0 and 25! Try again!")
            else:
                ready = True
    return rotation_key


# Function which runs the cipher and inverts rotation value if decrypting
def cipher(direction, msg, rotation, change_text_file):
    altered = ""
    if direction == "decrypt" or direction == "d" and change_text_file == False:
        rotation*=-1

    for character in msg:
        if character == " ":
            altered += " "
        elif character in ALPHAS_LOWER:
            norm_index = ALPHAS_LOWER.index(character)
            new_index = int(norm_index) + int(rotation)
            if new_index > 25:
                new_index -= len(ALPHAS_LOWER)
            altered+=ALPHAS_LOWER[new_index]
        elif character in ALPHAS_CAPS:
            norm_index = ALPHAS_CAPS.index(character)
            new_index = int(norm_index) + int(rotation) 
            if new_index > 25:
                new_index -= len(ALPHAS_CAPS)
            altered+=ALPHAS_CAPS[new_index]
        elif character in LEAVE_BE:
            altered+= character
    return altered


# Function which writes given text to a file. The name of the file is based
# on the rotation direction 
def write_to_file(altered_text, direction, change_text_file):
    if direction == "encrypt" or direction == "e" :
        file_name = "./tools/days/day_008/files/EncryptedText.txt"
    elif direction == "decrypt" or direction == "d":
        if change_text_file == True:
            file_name = "./tools/days/day_008/files/EncryptedText.txt"
        else:
            file_name = "./tools/days/day_008/files/DecryptedText.txt"
    with open(file_name, 'w') as f:
        f.write(altered_text)
        f.close()
        nls(f"Successfully wrote to file: '{file_name}'")


# Main function to run above logic
def day_008():
	title("CAESAR'S CIPHER")
	cipher_logo()
	direction = ask_direction()
	change_text_file = False                                              
	if direction == "encrypt" or direction == "e":
		msg = ask_msg()
	elif direction == "decrypt" or direction == "d":
		file_to_decrypt = "./tools/days/day_008/files/EncryptedText.txt"
		if os.path.exists(file_to_decrypt):
			f = open(file_to_decrypt, "r")
			msg = f.read()
			nls(f"Encrypted Text: {msg}")
			a = nli("Press enter to continue.")
		else:
			cls()
			nls("No file to decrypt. Please first encrypt a message.")
			msg = ask_msg()
			change_text_file = True
	rotation = int(ask_rotation())
	altered_msg = cipher(direction, msg, rotation, change_text_file)
	write_to_file(altered_msg, direction, change_text_file)