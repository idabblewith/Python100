## PythonSensei

![PythonSensei](https://github.com/jprincedev/PythonSensei/blob/main/tools/sensei.jpg?raw=true)

### Welcome to 100 Days of Python.

## Introduction

PythonSensei is a program that runs 100 Python projects which were created over the course of 100 Days.<br>The 100 programs that PythonSensei can run are primarily based on [Angela Yu's 100 Days of Code Udemy Course](https://www.udemy.com/course/100-days-of-code), range from beginner to professional, and are optomised to be run via selection via CLI. As some require protected information such as passwords and emails, they have either been swapped out or cannot be run from the console (The code can still be viewed).


## How it works

The program uses three main classes to access files for each day in the 
Python 100 Bootcamp: PythonSensei, PythonViewer, PythonLauncher

## Additional Setup

### Running locally
You must create a virtual environment, enter it, and return to original directory:
   - Navigate to file directory of start.py via console
   - Run the following code:
      python -m venv && cd "${PWD}/venv/Scripts" && source activate && cd "../.."
   
You must pip install requirements.txt: 
   pip install -r requirements.txt

   This will install the following libraries & their dependencies:
   - Scapy (pip install scapy)
   - Colorgram (pip install colorgram.py)
   - Pandas (pip install pandas)
   - Pyperclip (pip install pyperclip)
   - Python Dotenv (pip install python_dotenv)
   - Requests (pip install requests)
   - Twilio (pip install twilio)

You must run start.py via the virtual machine.
   py start.py

PROGRAM SPECIFIC (OS):
   - P13: Install [Npcap](https://npcap.com/dist/npcap-1.72.exe)/NMap to your OS.

<!-- ### Credentials
Many programs require credentials. You will be prompted for credentials
if you have not already provided them. The following programs will require
credentials to run:
32, 33 (REWORK EMAIL)
35 (TWILIO, OPENWEATHER)

 -->

<!-- You can prefill these credentials in the .env file -->

<!-- 
NOTES/BUGS:
GENERAL CREATE A CHECK TO SEE IF CREDENTIAL FOR SELECTED DAY IS AVAILABLE
IF NOT ASK USER FOR IT, INPUT IT, AND RERUN THE DAY. IF ERROR CRED, INFORM USER ON ATTEMPT & RETURN (Create error message in misc).
OTHERWISE RETURN TO SELECTION (if user does not provide).

Day 13 - TO PREVENT ERROR, FIND A WAY TO CHECK IF NPCAP INSTALLED AND EXIT IF NOT
Day 17 - Goes until Q50, need to add quit button and show how many q left
All tkinter (D19, 20, 21, 22, 25, 27, 28, 29, 30) - focus no longer set to new open window
Day 22 - Error shown on close (tclerror), and strange speed up of ball
Day 23 - Error on close
Day 25 - Error shown on close


Day 13 - Scapy Not working - DAY REMOVED FOR NOW AND SCAPY UNINSTALLED
D32 - secrets
D33 - Secrets Day
D35 - Secrets day
D36 - Secrets Day
D37 - Secrets Day
D38 - Secrets Day
D39 - Secrets Day (files dm)
D40 - Secrets Day
NEED CHROME INSTALLED 
D46 - Secrets Day
D48 - Chrome Driver error


To run the program launcher locally, you must have Python installed and type 'python start.py' from the root directory (where start.py is located).

Here is a demo of how the program works:

_STARTING PYTHONSENSEI_
![Screenshot 1](https://github.com/jprincedev/PythonSensei/blob/main/tools/ss1.png?raw=true)

_SELECTING PROGRAM_
![Screenshot 2](https://github.com/jprincedev/PythonSensei/blob/main/tools/ss2.png?raw=true)

_RUNNING PROGRAM_
![Screenshot 3](https://github.com/jprincedev/PythonSensei/blob/main/tools/ss3.png?raw=true)

## List of Projects

Use the table below to develop an understanding of the projects.<br>The last twenty projects are intended to be a culmination of the skills learned throughout Angela's course and are thus marked 'Portfolio'. <br>

| DAY     | PROJECT                                                                                                | SKILL LEVEL  | NOTABLE TECH                               |
| ------- | ------------------------------------------------------------------------------------------------------ | ------------ | ------------------------------------------ |
| Day 1   | [BAND NAME GENERATOR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_001/main.py)       | BEGINNER     |                                            |
| Day 2   | [BILL SPLITTER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_002/main.py)             | BEGINNER     |                                            |
| Day 3   | [TREASURE HUNT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_003/main.py)             | BEGINNER     |                                            |
| Day 4   | [ROCK PAPER SCISSORS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_004/main.py)       | BEGINNER     |                                            |
| Day 5   | [PASSWORD GENERATOR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_005/main.py)        | BEGINNER     |                                            |
| Day 6   | [BMI CHECKER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_006/main.py)               | BEGINNER     |                                            |
| Day 7   | [HANGMAN](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_007/main.py)                   | BEGINNER     |                                            |
| Day 8   | [CAESAR'S CIPHER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_008/main.py)           | BEGINNER     |                                            |
| Day 9   | [SILENT BID](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_009/main.py)                | BEGINNER     |                                            |
| Day 10  | [BASIC CALCULATOR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_010/main.py)          | BEGINNER     |                                            |
| Day 11  | [BLACKJACK CAPSTONE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_011/main.py)        | BEGINNER     |                                            |
| Day 12  | [NUMBER GUESSING GAME](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_012/main.py)      | BEGINNER     |                                            |
| Day 13  | [MULTIPROCESS PORT SCANNER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_013/main.py) | BEGINNER     | SCAPY, SUBPROCESS                          |
| Day 14  | [HIGHER LOWER GAME](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_014/main.py)         | BEGINNER     |                                            |
| Day 15  | [COFFEE MACHINE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_015/main.py)            | BEGINNER     |                                            |
| Day 16  | [OOP COFFEE MACHINE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_016/main.py)        | BEGINNER     |                                            |
| Day 17  | [QUIZ](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_017/main.py)                      | BEGINNER     | REQUESTS                                   |
| Day 18  | [TURTLE ART](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_018/main.py)                | BEGINNER     | TKINTER, TURTLE                            |
| Day 19  | [TURTLE RACE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_019/main.py)               | BEGINNER     | TKINTER, TURTLE                            |
| Day 20  | [SNAKE GAME P1](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_020/main.py)             | BEGINNER     | TKINTER, TURTLE                            |
| Day 21  | [SNAKE GAME P2](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_021/main.py)             | BEGINNER     | TKINTER, TURTLE                            |
| Day 22  | [PONG](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_022/main.py)                      | BEGINNER     | TKINTER, TURTLE                            |
| Day 23  | [TURTLE CROSSING CAPSTONE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_023/main.py)  | BEGINNER     | TKINTER, TURTLE                            |
| Day 24  | [MAIL MERGER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_024/main.py)               | BEGINNER     |                                            |
| Day 25  | [US STATES GAME](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_025/main.py)            | INTERMEDIATE | PANDAS                                     |
| Day 26  | [NATO ALPHABET](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_026/main.py)             | INTERMEDIATE | PANDAS                                     |
| Day 27  | [MILES TO KM](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_027/main.py)               | INTERMEDIATE | TKINTER                                    |
| Day 28  | [POMODORO](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_028/main.py)                  | INTERMEDIATE | TKINTER                                    |
| Day 29  | [PASS MANAGER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_029/main.py)              | INTERMEDIATE | TKINTER                                    |
| Day 30  | [PASS MANAGER PRO](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_030/main.py)          | INTERMEDIATE | TKINTER                                    |
| Day 31  | [FLASH CARDS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_031/main.py)               | INTERMEDIATE | TKINTER                                    |
| Day 32  | [BIRTHDAY WISHER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_032/main.py)           | INTERMEDIATE | TKINTER, PANDAS                            |
| Day 33  | [ISS TRACKER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_033/main.py)               | INTERMEDIATE | SMTPLIB                                    |
| Day 34  | [QUIZZLER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_034/main.py)                  | INTERMEDIATE | REQUESTS                                   |
| Day 35  | [RAIN ALERT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_035/main.py)                | INTERMEDIATE | REQUESTS, TWILIO                           |
| Day 36  | [STOCK NOTIFIER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_036/main.py)            | INTERMEDIATE | REQUESTS, TWILIO                           |
| Day 37  | [PIXELA TRACKER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_037/main.py)            | INTERMEDIATE | REQUESTS                                   |
| Day 38  | [NLP WORKOUT TRACKER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_038/main.py)       | INTERMEDIATE | REQUESTS                                   |
| Day 39  | [FLIGHT SCANNER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_039/main.py)            | INTERMEDIATE | REQUESTS, TWILIO                           |
| Day 40  | [FLIGHT CLUB](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_040/main.py)               | INTERMEDIATE | REQUESTS, SMTPLIB, TWILIO                  |
| Day 41  | [HTML CV](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_041/main.py)                   | INTERMEDIATE |                                            |
| Day 42  | [HTML CV +](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_042main.py)                  | INTERMEDIATE |                                            |
| Day 43  | [HTML/CSS CV](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_043/main.py)               | INTERMEDIATE |                                            |
| Day 44  | [PERSONAL SITE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_044/main.py)             | INTERMEDIATE |                                            |
| Day 45  | [MUST WATCH LIST](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_045/main.py)           | INTERMEDIATE | BEAUTIFUL SOUP                             |
| Day 46  | [SPOTIFY TIME MACHINE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_046/main.py)      | ADVANCED     | SPOTIPY, BEAUTIFUL SOUP                    |
| Day 47  | [AUTOMATED PRICE TRACKER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_047/main.py)   | ADVANCED     | BEAUTIFUL SOUP                             |
| Day 48  | [SELENIUM GAME BOT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_048/main.py)         | ADVANCED     | SELENIUM                                   |
| Day 49  | [AUTOMATED JOB APPLICATION](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_049/main.py) | ADVANCED     | SELENIUM                                   |
| Day 50  | [TINDER SWIPING BOT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_050/main.py)        | ADVANCED     | SELENIUM                                   |
| Day 51  | [TWITTER COMPLAINT BOT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_051/main.py)     | ADVANCED     | SELENIUM                                   |
| Day 52  | [INSTAGRAM BOT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_052/main.py)             | ADVANCED     | SELENIUM                                   |
| Day 53  | [AUTOMATED REAL ESTATE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_053/main.py)     | ADVANCED     | SELENIUM, BEAUTIFUL SOUP                   |
| Day 54  | [FUNC SPEED DECORATOR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_054/main.py)      | ADVANCED     |                                            |
| Day 55  | [FLASK: GUESSING GAME](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_055/main.py)      | ADVANCED     | FLASK, TORNADO                             |
| Day 56  | [FLASK: NAMECARD](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_056/main.py)           | ADVANCED     | FLASK, TORNADO                             |
| Day 57  | [FLASK: BASIC BLOG](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_057/main.py)         | ADVANCED     | FLASK, TORNADO                             |
| Day 58  | [FLASK: TINDOG](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_058/main.py)             | ADVANCED     | FLASK, TORNADO                             |
| Day 59  | [FLASK: BASIC BLOG 2](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_059/main.py)       | ADVANCED     | FLASK, TORNADO                             |
| Day 60  | [FLASK: FORMS AND REQUESTS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_060/main.py) | ADVANCED     | FLASK, TORNADO                             |
| Day 61  | [FLASK: ADVANCED FORMS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_061/main.py)     | ADVANCED     | FLASK, TORNADO, WTFORMS                    |
| Day 62  | [FLASK: COFFEE AND WIFI](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_062/main.py)    | ADVANCED     | FLASK, TORNADO, WTFORMS                    |
| Day 63  | [VIRTUAL BOOKSHELF](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_063/main.py)         | ADVANCED     | FLASK, TORNADO, WTFORMS                    |
| Day 64  | [TOP 10 MOVIES](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_064/main.py)             | ADVANCED     | FLASK, TORNADO, WTFORMS, SQLITE3           |
| Day 65  | [UNSET](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_065/main.py)                     | ADVANCED     | UNSET                                      |
| Day 66  | [REST API](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_066/main.py)                  | ADVANCED     |                                            |
| Day 67  | [BLOG: REST API/CKEDITOR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_067/main.py)   | ADVANCED     | FLASK, CKEDITOR                            |
| Day 68  | [BLOG: AUTHENTICATION](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_068/main.py)      | PROFESSIONAL | FLASK_LOGIN                                |
| Day 69  | [BLOG: ADDING USERS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_069/main.py)        | PROFESSIONAL | SQL_ALCHEMY                                |
| Day 70  | [BLOG: DEPLOYMENT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_070/main.py)          | PROFESSIONAL | HEROKU                                     |
| Day 71  | [PANDAS DATA EXPLORATION](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_071/main.py)   | PROFESSIONAL | PANDAS                                     |
| Day 72  | [MATPLOTLIB](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_072/main.py)                | PROFESSIONAL | PANDAS, MATPLOTLIB                         |
| Day 73  | [LEGO PANDAS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_073/main.py)               | PROFESSIONAL | PANDAS, MATPLOTLIB                         |
| Day 74  | [GTRENDS AND MATPLOTLIB](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_074/main.py)    | PROFESSIONAL | PANDAS, MATPLOTLIB                         |
| Day 75  | [PLOTTING APP STORE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_075/main.py)        | PROFESSIONAL | PLOTLY, PANDAS, MATPLOTLIB                 |
| Day 76  | [NUMPY](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_076/main.py)                     | PROFESSIONAL | NUMPY, MATPLOTLIB, SCIPY, PIL              |
| Day 77  | [LINEAR REG. & SEABORN](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_077/main.py)     | PROFESSIONAL | SEABORN, SKLEARN, PLOTLY, MATPLOTLIB       |
| Day 78  | [NOBEL PRIZE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_078/main.py)               | PROFESSIONAL | SEABORN, MATPLOTLIB, PLOTLY, SCIPY         |
| Day 79  | [KERNEL DENSITY EST.](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_079/main.py)       | PROFESSIONAL | PANDAS, SEABORN, MATPLOTLIB, PLOTLY, SCIPY |
| Day 80  | [PROPERTY VALUATION](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_080/main.py)        | PROFESSIONAL | PANDAS, SEABORN, MATPLOTLIB, PLOTLY, SCIPY |
| Day 81  | [TEXT TO MORSE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_081/main.py)             | PORTFOLIO    |                                            |
| Day 82  | [PORTFOLIO WEBSITE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_082/main.py)         | PORTFOLIO    | UNSET                                      |
| Day 83  | [TIC TAC TOE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_083/main.py)               | PORTFOLIO    | UNSET                                      |
| Day 84  | [IMAGE WATERMARKING](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_084/main.py)        | PORTFOLIO    | UNSET                                      |
| Day 85  | [TYPING SPEED](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_085/main.py)              | PORTFOLIO    | UNSET                                      |
| Day 86  | [BREAKOUT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_086/main.py)                  | PORTFOLIO    | UNSET                                      |
| Day 87  | [CAFE AND WIFI](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_087/main.py)             | PORTFOLIO    | UNSET                                      |
| Day 88  | [TODO LIST](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_088/main.py)                 | PORTFOLIO    | UNSET                                      |
| Day 89  | [DISAPPEARING TEXT](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_089/main.py)         | PORTFOLIO    | UNSET                                      |
| Day 90  | [PDF TO AUDIOBOOK](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_090/main.py)          | PORTFOLIO    | UNSET                                      |
| Day 91  | [COLOR-PAL GEN](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_091/main.py)             | PORTFOLIO    | UNSET                                      |
| Day 92  | [CUSTOM WEB SCRAPER](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_092/main.py)        | PORTFOLIO    | UNSET                                      |
| Day 93  | [GOOGLE DINOSAUR](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_093/main.py)           | PORTFOLIO    | UNSET                                      |
| Day 94  | [SPACE INVADERS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_094/main.py)            | PORTFOLIO    | UNSET                                      |
| Day 95  | [CUSTOM API SITE](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_095/main.py)           | PORTFOLIO    | UNSET                                      |
| Day 96  | [ONLINE SHOP](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_096/main.py)               | PORTFOLIO    | UNSET                                      |
| Day 97  | [LIFE AUTOMATION](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_097/main.py)           | PORTFOLIO    | UNSET                                      |
| Day 98  | [SPACE RACE DATA](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_098/main.py)           | PORTFOLIO    | UNSET                                      |
| Day 99  | [POLICE DEATHS](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_099/main.py)             | PORTFOLIO    | UNSET                                      |
| Day 100 | [PREDICT SALARIES](https://github.com/jprincedev/PythonSensei/blob/main/tools/days/day_100/main.py)          | PORTFOLIO    | UNSET                                      |

## Tech Stack

The Tech Stack for PythonSensei is rather broad as the project covers various topics.
To name a few key components:

### General

- **Git Bash** as terminal
- **Python3** as primary language
- **Javascript** as additional language

### Webapp Development

- **Flask** as server framework
- **Request** as primary python API library
- **PostgreSQL** as our primary database
- **SQLite** as our secondary database
- **SQLAlchemy ORM** as ORM library
- **HTML5** to develop skeleton of websites
- **CSS3** to style website
- **Bootstrap 5** to style websites faster
- **WTForms** to create forms with flask

### Data Science

- **NumPy** as our database of choice
- **Plotly** as our database of choice
- **Scikit Learn** as our database of choice
- **Pandas** as our database of choice
- **Matplotlib** as our database of choice
- **Seaborn** as our database of choice

### GUI, Automation and Scraping

- **Selenium** as our database of choice
- **Beautiful Soup** as our database of choice
- **TKinter** as primary python API library
- **Turtle** as primary python API library

## Local Development Setup

To locally run the programs in PythonSensei, you require a total of 36 credential files. For obvious security reasons, these files have been gitignored and will not be made publicly available.

You must fill out a file with your own credentials for each program to work locally.
I am currently implementing a fix so that you can still run other programs that do not require credentials. You will be alerted if your credentials are missing.
You must also install Ncap for Scapy.

1. Generate and Fill Missing Files

   A bit of a gargantuan task, but if you're suurrreee...

   - Under the folder 'tools', there is a 'secret_creator.py' file which you should run to create the secret files.
   - Once you have run that file, you must use the below table to create the required credentials and paste them in the newly created files.

   Here is a table on the missing files:

   | FILE                         | TYPE         | DESCRIPTION                                                                                       | LINK FOR CREDENTIAL |
   | ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------- | ------------------- |
   | email.secret                 | EMAIL        | Your primary email (gmail used for SMTP)                                                          | gmail.com           |
   | email_password.secret        | PASSWORD     | Password for your primary email                                                                   | gmail.com           |
   | flight_app.secret            | API          |
   | insta_pass.secret            | PASSWORD     |
   | insta_user.secret            | USERNAME     |
   | linked_search.secret         | MISC         |
   | linkedin_email.secret        | EMAIL        |
   | linkedin_pass.secret         | PASSWORD     |
   | my_num.secret                | PHONE NUMBER |
   | newsapikey.secret            | API          |
   | nutritionix_api.secret       | API          |
   | nutritionix_app.secret       | API          |
   | open_weather_api.secret      | API          |
   | other_email.secret           | EMAIL        |
   | pixela_user.secret           | USERNAME     |
   | pixela.secret                | API          |
   | secret_key.secret            | SECRET KEY   |
   | sheety_bearer.secret         | TOKEN        |
   | sheety_flight_api.secret     | API          |
   | sheety_flight_user.secret    | LINK         |
   | spotify_client_id.secret     | API          |
   | spotify_client_secret.secret | API          |
   | stock_api.secret             | API          |
   | tequila_api.secret           | API          |
   | tinder_email.secret          | EMAIL        |
   | tinder_password.secret       | PASSWORD     |
   | tmdb_api.secret              | API          |
   | twilio_id.secret             | USERNAME     |
   | twilio_num.secret            | PHONE NUMBER |
   | twilio_password.secret       | PASSWORD     |
   | twilio_recovery.secret       | MISC         |
   | twilio_token.secret          | TOKEN        |
   | twitter_pass.secret          | PASSWORD     | Your Twitter Account Password                                                                     |
   | twitter_user.secret          | EMAIL        | Your Twitter Account Email                                                                        |
   | twitter_username.secret      | USERNAME     | Your Twitter Account Username                                                                     |
   | zillow_form.secret           | LINK         | A Link to your Zillow Form containing a questionairre which a program fills with real-estate data |

2. Install Dependencies

   - Navigate to the folder and create a virtual environment. `cd Python100 && mkvenv`

3. Launch the virtual environment

   - `cd venv/Scripts && source activate && cd .. && cd ..`

4. Install the required packages

   - While in the main directory: `pip install -r program_requirements.txt`
   - NOTE: if you are running from VSCode, you may need to change your interpreter to the `venv/Scripts/python.exe` file. This can be done at the bottom left of your screen.

5. Run

   - Run the `start.py` file in vs code and click run OR `python start.py`
   - NOTE: you must use the venv python (venv/Scripts/python.exe start.py). The command will look more like this: `c:/downloads/Python100/venv/Scripts/python.exe c:/downloads/Python100/start.py`

6. Follow the prompts and select a program.

   - If all is well, you will see a greeting and be prompted to select a program.

Have fun!~

idabblewith -->
