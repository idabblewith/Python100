# Copyright (c) 2023 Jarid Prince

# Class definition which runs the ProgramViewer and ProgramLauncher classes
# Purpose is to delegate input from user to determine whether or not another
# program should be run, and to clean up programs that have been run.
class PythonSensei:
    def __init__(self):
        self.cont = True
        self.program_names = misc.program_names

    def select_program(self):
        program_viewer = ProgramViewer(misc)
        program_viewer.check_view_input()
        program_viewer.display_programs_in_range()

        if program_viewer.selected_program == "q":
            sys.exit()

        if (
            type(program_viewer.program_view_choice) == None
            or type(program_viewer.program_view_choice) == ""
        ):
            return self.select_program()

        else:
            launcher = ProgramLauncher(misc)
            print(program_viewer.program_view_choice)
            launcher.set_program(program_viewer.selected_program)
            launcher.launch()
            del launcher
            del program_viewer
            gc.collect()


# Instantiates PythonSensei and allows users to select a program
# (If run directly)
if __name__ == "__main__":
    import misc
    from ProgramViewer import ProgramViewer
    from ProgramLauncher import ProgramLauncher
    import sys, gc

    sensei = PythonSensei()
    sensei.select_program()

# (If run via start.py or another program)
else:
    from tools.misc import *
    from tools.ProgramViewer import ProgramViewer
    from tools.ProgramLauncher import ProgramLauncher
    import sys, gc

    sensei = PythonSensei()
    sensei.select_program()
