# Copyright (c) 2023 Jarid Prince

import sys
from misc import cls

# Class definition
# Purpose is to display the names of programs based on misc.py program_names var
class ProgramViewer:
    def __init__(self, misc):
        self.misc = misc
        self.programs = misc.program_names
        self.program_view_choice = None
        self.start_range = None
        self.end_range = None
        self.programs_in_range = []
        self.selected_program = None

    # Presents user with a selection of 4 choices (ie Op1: Days 1-25) which upon input
    # will display programs in that range.
    def check_view_input(self):
        program_view_choice = ""
        while (
            not type(program_view_choice) is int
            or type(program_view_choice) is int
            and program_view_choice > 4
            or type(program_view_choice) is int
            and program_view_choice < 1
        ):
            try:
                program_view_choice = self.misc.nli(
                    f"(1) Days 1-25 (BEGINNER)\n(2) Days 26-50 (INTERMEDIATE)\n(3) Days 51-75 (ADVANCED)\n(4) Days 76-100 (PROFESSIONAL)\n\n{self.misc.bcolors.OKBLUE}Select a range to view programs.\nType 1, 2, 3 or 4:\n{self.misc.bcolors.ENDC}"
                )
            except KeyboardInterrupt:
                self.misc.nls("Exiting...")
                sys.exit()
            if program_view_choice == "q":
                sys.exit()
            try:
                program_view_choice = int(program_view_choice)
            except:
                self.misc.cls()
                self.misc.nls(
                    "You must type a number in the range 1-4. Try again or q to quit."
                )
                program_view_choice = ""
        self.program_view_choice = program_view_choice

        if self.program_view_choice == 1:
            self.start_range = 1
        elif self.program_view_choice == 2:
            self.start_range = 26
        elif self.program_view_choice == 3:
            self.start_range = 51
        elif self.program_view_choice == 4:
            self.start_range = 76
        self.end_range = self.start_range + 25

    # Displays programs available in the range selected by the user
    def display_programs_in_range(self):
        start = self.start_range
        end = self.end_range
        programs_in_range = [
            f"({day}) {self.programs[day-1]}" for day in range(start, end)
        ]
        self.misc.cls()
        self.kawaii_print(programs_in_range)
        try:
            self.selected_program = self.misc.nli(
                f"To select program 3: Type 3 and press enter.\nTo change range: Press enter.\n"
            )
        except KeyboardInterrupt:
            self.misc.nls("Exiting...")
            sys.exit()
        while self.selected_program == "" or self.selected_program == None:
            cls()
            self.program_view_choice == self.check_view_input()
            self.display_programs_in_range()

    # Neatly presents the program names in columns/rows by assessing the length of words to determine padding
    def kawaii_print(self, list):
        new_list = [
            [
                list[num],
                list[(num + (5 * 1))],
                list[(num + (5 * 2))],
                list[(num + (5 * 3))],
                list[(num + (5 * 4))],
            ]
            for num in range(0, len(list))
            if num < 5
        ]
        col_width = max(len(word) for row in new_list for word in row) + 2  # padding
        self.misc.nls(
            f"{self.misc.bcolors.OKGREEN}PROGRAMS AVAILABLE IN RANGE:{self.misc.bcolors.ENDC}"
        )
        print(
            f"\n{self.misc.bcolors.OKBLUE}Select a program from below.\n{self.misc.bcolors.ENDC}"
        )
        for row in new_list:
            print(
                f"{self.misc.bcolors.OKCYAN}{''.join(word.ljust(col_width) for word in row)}{self.misc.bcolors.ENDC}"
            )
