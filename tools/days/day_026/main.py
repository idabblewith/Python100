# Day 26
# Updated 2023, Jarid Prince

from days.day_026.files.helpers import *


def day_026():
    title("NATO ALPHABET")
    # Reads the csv with pandas
    natos = pandas.read_csv("./tools/days/day_026/files/nato_phonetic_alphabet.csv")
    # Creates a dictionary with key as letter and value as phonetic name for each
    # row in natos csv
    phonetic_dict = {row.letter: row.code for (index, row) in natos.iterrows()}
    # Prompts user for name, uses list comprehension to generate list
    # of phonetic names and displays the list
    name = nli("Type your name: ").upper()
    result = [phonetic_dict[letter] for letter in name]
    nls(result)
