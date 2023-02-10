# Day 24
# Updated 2023, Jarid Prince

from days.day_024.files.helpers import *


def day_024():
    title("MAIL MERGER")
    # Gets current working directory to display to user in file path
    import os

    cwd = os.getcwd()
    print(f"Operating in: {cwd}")
    PLACEHOLDER = "[name]"
    # Checks list of invited people and assigns it to a variable
    with open("./tools/days/day_024/files/Input/Names/invited_names.txt") as names_file:
        names_list = names_file.readlines()
    # Checks letter template and replaces placeholder with name from list for each name
    with open(
        "./tools/days/day_024/files/Input/Letters/starting_letter.txt"
    ) as letter_template:
        contents = letter_template.read()
        for name in names_list:
            naked_name = name.strip()
            new_letter = contents.replace(PLACEHOLDER, naked_name)
            # Saves the new letter to a file
            with open(
                f"./tools/days/day_024/files/Output/ReadyToSend/{naked_name}_letter.txt",
                "w",
            ) as complete_l:
                complete_l.write(new_letter)
            print(f"Successfully wrote to file for: {naked_name}")
    print(
        f"\nSee '{cwd}\\tools\\days\\day_024\\files\\Output\\ReadyToSend' for files.\n"
    )
