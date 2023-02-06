# Copyright (c) 2023 Jarid Prince

import os
from misc import program_names
import time

root_path = "./"
folders = []

# Appends a series of strings to the folders array
# which are to be used for the folder names for each day's program
for x in range(1, 101):
    if x < 10:
        folders.append("day_00" + str(x))
    elif x >= 10 and x != 100:
        folders.append("day_0" + str(x))
    else:
        folders.append("day_" + str(x))


# Function which generates a folder called 'days' in the root directory
def make_days_folder():
    os.mkdir(os.path.join(root_path, "days"))


# Function which makes a directory for each string in the 'folders' array
# under the 'days' folder. Then creates a subdirectory for day-specific files.
# Finally, creates a main.py file which imports tools and creates a day funciton.
def make_folders_and_py_files():
    num = 0
    prepend_string = ""

    for folder in folders:
        if (num + 1) < 10:
            prepend_string = "00"
        elif (num + 1) < 100:
            prepend_string = "0"
        else:
            prepend_string = ""
        os.mkdir(os.path.join(f"{root_path}/days", folder))
        new_root = f"./days/{folder}"
        os.mkdir(os.path.join(new_root, "files"))
        with open(f"days/{folder}/main.py", "w+") as f:
            f.write(
                f'from days.{folder}.files.helpers import *\n\ndef day_{prepend_string}{num+1}():\n\ttitle("{program_names[num]}")'
            )
            # f.close() # Using with open, file is automatically closed after exiting indent
            print(program_names[num])
        with open(f"days/{folder}/files/helpers.py", "w+") as f:
            f.write("from misc import nls, nli, title, cls")
            # f.close() # Using with open, file is automatically closed after exiting indent

        num += 1


# from tools.misc import *\n

# Runs the above functions, creating base files and folders for 100 days.
def run():
    t_s = time.time()
    make_days_folder()
    make_folders_and_py_files()
    t_e = time.time()
    print(f"Time taken: {t_e - t_s} seconds")


run()
