# Day 32
# Updated 2023, Jarid Prince

from days.day_032.files.helpers import *


def day_032():
    title("BIRTHDAY WISHER")
    # Secrets now saved in one location - env
    nls(
        "NOTE: This file requires that you fill in the .env file's MY_EMAIL & MY_EMAIL_PASSWORD values."
    )

    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    ENV_FILE = os.path.join(BASE_DIR, ".env")
    env_error = False

    def error_env_msg():
        nls(
            "It seems that you do not have an environment variable for your email and its password. This information is privately stored on your local machine.\nYou must create an .env file and set the password and email variables to run this program.\n\nGo to the root directory of PythonSensei and create a .env file and open it.\nUse this format:\n\nMY_EMAIL=emailhere@email.com\nMY_EMAIL_PASSWORD=passwordhere"
        )

    try:
        load_dotenv(ENV_FILE)
        my_email = os.getenv("my_email")
        password = os.getenv("my_email_password")
    except:
        error_env_msg()
        env_error = True
    else:
        if password == None or password == "" or my_email == None or password == "":
            error_env_msg()
            env_error = True

    if not env_error:
        now = dt.datetime.now()
        today = str(now.date())
        a = pandas.read_csv("./tools/days/day_032/files/birthdays.csv")
        b = a.to_dict(orient="records")
        c = []

        try:
            for person in b:
                person["day"] = str(person["day"])
                person["month"] = str(person["month"])
                if len(person["day"]) == 1:
                    person["day"] = "0" + person["day"]
                if len(person["month"]) == 1:
                    person["month"] = "0" + person["month"]
                birthday = f'{person["year"]}-{person["month"]}-{person["day"]}'
                if birthday == today:
                    num = random.randint(1, 3)
                    file_path = (
                        f"./tools/days/day_032/files/letter_templates/letter_{num}.txt"
                    )
                    with open(file_path) as bday_msg_file:
                        contents = bday_msg_file.read()
                        bday_msg = contents.replace("[NAME]", person["name"])

                    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
                        conn.starttls()
                        conn.login(user=my_email, password=password)
                        conn.sendmail(
                            from_addr=my_email,
                            to_addrs=person["email"],
                            msg=f"Subject: Happy Birthday!!\n\n{bday_msg}",
                        )
        except SMTPAuthenticationError as e:
            nls(
                f"Unfortunately, there was an error with your credentials or the SMTP service.\nIf you are certain your credentials are correct, you may need to configure SMTP for your email account or allow less secure apps.\nIf you are using gmail, please note that they no longer allows less secure apps:\n\nError: {e}"
            )
