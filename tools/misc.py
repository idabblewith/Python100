# Copyright (c) 2023 Jarid Prince

import os, sys

easy_array = ["easy", "Easy", "EASY", "e", "E"]
hard_array = ["hard", "Hard", "HARD", "h", "H"]
small_array = ["S", "s", "Small", "small", "Sm", "sm"]
medium_array = ["M", "m", "Medium", "medium", "Md", "md"]
large_array = ["L", "l", "Large", "large", "Lrg", "Lg", "lg"]
sizes_array = small_array + medium_array + large_array
right = ["Right", "right", "r", "R"]
left = ["Left", "left", "l", "L"]
yes_array = ["Yeah", "yeah", "Yea", "yea", "Ye", "ye", "Y", "y", "Yes", "yes"]
no_array = ["Nah", "nah", "Nay", "nay", "Na", "na", "N", "n", "No", "no"]
yesno_array = yes_array + no_array
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "`",
    "~",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
    "=",
    "{",
    "[",
    "}",
    "}",
    "|",
    ":",
    ";",
    '"',
    "'",
    "<",
    ",",
    ">",
    ".",
    "?",
    "/",
]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def nls(string_input):
    formatted_string = f"\n{string_input}\n"
    print(formatted_string)


def nli(string_input):
    fsi = input(f"\n{string_input}\n")
    return fsi


def title(string):
    ft = f'{bcolors.OKGREEN}\n{"*"*62}{bcolors.ENDC}\n\n\t\t\t{string}\n\n{bcolors.OKGREEN}\n{"*"*62}{bcolors.ENDC}\n'
    cls()
    print(ft)


def cls():
    os.system("clear")


def gg(msg):
    nls(f"{msg}\nGame Over.")


def press_start():
    a = input("Press enter to start.")
    return a


program_names = [
    "BAND NAME GENERATOR",
    "BILL SPLITTER",
    "TREASURE HUNT",
    "ROCK PAPER SCISSORS",
    "PASSWORD GENERATOR",
    "BMI CHECKER",
    "HANGMAN",
    "CAESAR'S CIPHER",
    "SILENT BID",
    "BASIC CALCULATOR",
    "BLACKJACK CAPSTONE",
    "NUMBER GUESSING GAME",
    "MULTIPROCESS PORT SCANNER",
    "HIGHER LOWER GAME",
    "COFFEE MACHINE",
    "OOP COFFEE MACHINE",
    "QUIZ",
    "TURTLE ART",
    "TURTLE RACE",
    "SNAKE GAME P1",
    "SNAKE GAME P2",
    "PONG",
    "TURTLE CROSSING CAPSTONE",
    "MAIL MERGER",
    "US STATES GAME",
    "NATO ALPHABET",
    "MILES TO KM",
    "POMODORO",
    "PASS MANAGER",
    "PASS MANAGER PRO",
    "FLASH CARDS",
    "BIRTHDAY WISHER",
    "ISS TRACKER",
    "QUIZZLER",
    "RAIN ALERT",
    "STOCK NOTIFIER",
    "PIXELA TRACKER",
    "NLP WORKOUT TRACKER",
    "FLIGHT SCANNER",
    "FLIGHT CLUB",
    "HTML CV",
    "HTML CV +",
    "HTML/CSS CV",
    "PERSONAL SITE",
    "MUST WATCH LIST",
    "SPOTIFY TIME MACHINE",
    "AUTOMATED PRICE TRACKER",
    "SELENIUM GAME BOT",
    "AUTOMATED JOB APPLICATION",
    "TINDER SWIPING BOT",
    "TWITTER COMPLAINT BOT",
    "INSTAGRAM BOT",
    "AUTOMATED REAL ESTATE",
    "FUNC SPEED DECORATOR",
    "FLASK: GUESSING GAME",
    "FLASK: NAMECARD",
    "FLASK: BASIC BLOG",
    "FLASK: TINDOG",
    "FLASK: BASIC BLOG 2",
    "FLASK: FORMS AND REQUESTS",
    "FLASK: ADVANCED FORMS",
    "FLASK: COFFEE AND WIFI",
    "VIRTUAL BOOKSHELF",
    "TOP 10 MOVIES",
    "FILLER WD FILLER",
    "REST API",
    "BLOG: REST API/CKEDITOR",
    "BLOG: AUTHENTICATION",
    "BLOG: ADDING USERS",
    "BLOG: DEPLOYMENT",
    "PANDAS DATA EXPLORATION",
    "MATPLOTLIB",
    "LEGO PANDAS",
    "GTRENDS AND MATPLOTLIB",
    "PLOTTING APP STORE",
    "NUMPY",
    "LINEAR REG. & SEABORN",
    "NOBEL PRIZE",
    "KERNEL DENSITY EST.",
    "PROPERTY VALUATION",
    "TEXT TO MORSE",
    "PORTFOLIO WEBSITE",
    "TIC TAC TOE",
    "IMAGE WATERMARKING",
    "TYPING SPEED",
    "BREAKOUT",
    "CAFE AND WIFI",
    "TODO LIST",
    "DISAPPEARING TEXT",
    "PDF TO AUDIOBOOK",
    "COLOR-PAL GEN",
    "CUSTOM WEB SCRAPER",
    "GOOGLE DINOSAUR",
    "SPACE INVADERS",
    "CUSTOM API SITE",
    "ONLINE SHOP",
    "LIFE AUTOMATION",
    "SPACE RACE DATA",
    "POLICE DEATHS",
    "PREDICT SALARIES",
]
