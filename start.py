# Copyright (c) 2023 Jarid Prince
#############################################
#                 Imports
#############################################

# Used to create folders and files quickly
# tools/importer.py && create_files.py
from tools.misc import *
import sys, subprocess


#############################################
# 					Code
#############################################

# Run each program as a subprocess of this program
def start_process():
    try:
        args = [sys.executable or "python", "./tools/PythonSensei.py"]
        p = subprocess.call(args)  # non-blocking
    except KeyboardInterrupt:
        sys.exit()


# Launch this code on run
if __name__ == "__main__":
    cont = True
    first = True
    cls()
    title(f"{bcolors.WARNING}100 Days Of\n\n\t\t\t  Python!{bcolors.ENDC}")
    print(
        f"{bcolors.HEADER}IMPORTANT: Please make sure you are in the correct directory for this file.{bcolors.ENDC}"
    )

    # Handlers and Output between programs
    while cont == True:
        if first == True:
            start_process()
            first = False
            nls(
                f"{bcolors.OKGREEN} {'*'*20} {bcolors.ENDC} PROGRAM COMPLETE! {bcolors.OKGREEN} {'*'*20} {bcolors.ENDC} "
            )
        else:
            try:
                go_again = nli(
                    "If you would like to try another program press enter.\nTo exit type any other character and press enter.\n"
                )
                cls()

                if go_again != "":
                    nls(f"Exiting...")
                    cont = False
                else:
                    start_process()
                    nls(
                        f"{bcolors.OKGREEN} {'*'*20} {bcolors.ENDC} PROGRAM COMPLETE! {bcolors.OKGREEN} {'*'*20} {bcolors.ENDC} "
                    )
            except KeyboardInterrupt:
                nls("Exiting...")
                sys.exit()
