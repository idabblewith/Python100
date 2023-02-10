# Day 1
# Updated 2023, Jarid Prince

from days.day_001.files.helpers import *

def day_001():
	title("BAND NAME GENERATOR")
	city = nli("What's the name of the city you grew up in?")
	pet = nli("What's your pet's name?")
	nls(f"Your band name is: {pet} {city}.")