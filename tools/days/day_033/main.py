# Day 33
# Updated 2023, Jarid Prince

from days.day_033.files.helpers import *


def day_033():
    title("ISS TRACKER")
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

    # Attempt to extract secrets, only run rest of code if successful
    try:
        load_dotenv(ENV_FILE)
        MY_EMAIL = os.getenv("MY_EMAIL")
        MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
        MY_OTHER_EMAIL = os.getenv("MY_OTHER_EMAIL")
    except:
        error_env_msg()
        env_error = True
    else:
        if (
            MY_EMAIL_PASSWORD == None
            or MY_EMAIL_PASSWORD == ""
            or MY_EMAIL == None
            or MY_EMAIL == ""
        ):
            error_env_msg()
            env_error = True

    # Default values for latitude and longditude
    MY_LAT = -31.981800
    MY_LONG = 115.863708

    # Your position is within +5 or -5 degrees of the ISS position.
    def iss_overhead():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        if (
            MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
            and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        ):
            nls("ISS IS OVERHEAD")
            return True
        else:
            nls("ISS is NOT overhead")

    def is_night():
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get(
            "https://api.sunrise-sunset.org/json", params=parameters
        )
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 8
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 8
        if sunrise >= 24:
            sunrise = sunrise - 24
        if sunset >= 24:
            sunset = sunset - 24

        now = dt.now()

        if now.hour >= sunset or now.hour <= sunrise:
            print(f"Current time: {now}")
            print(f"Sunrise: {sunrise}")
            print(f"Sunset: {sunset}")
            print("It is currently dark outside at the given position.")
            return True

    def convert_to_float(prompt):
        while type(prompt) == float:
            try:
                RETURN_VALUE = float(prompt)
            except:
                nls("There was an error converting that value into a float.")
            else:
                return RETURN_VALUE

    if not env_error:
        nls(
            f"This program will send you an email if the ISS is close to your position and it is dark outside."
        )
        lat_prompt = nli(
            f"Current latitude:{MY_LAT}. Press enter if this is okay, or type a new latitude."
        )
        if lat_prompt != "":
            MY_LAT = convert_to_float(lat_prompt)
        long_prompt = nli(
            f"Current longditude:{MY_LONG}. Press enter if this is okay, or type a new longditude."
        )
        if long_prompt != "":
            MY_LONG = convert_to_float(long_prompt)

        while True:
            if is_night() and iss_overhead():
                try:
                    # Potentially rework for user choice of SMTP provider
                    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls()
                        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
                        connection.send_message(
                            from_addr=MY_EMAIL,
                            to_addrs=MY_OTHER_EMAIL,
                            msg="Subject: ISS Overhead!\n\n Look up! The ISS is above your location!",
                        )
                except SMTPAuthenticationError as e:
                    nls(
                        f"Unfortunately, there was an error with your credentials or the SMTP service.\nIf you are certain your credentials are correct, you may need to configure SMTP for your email account or allow less secure apps.\nIf you are using gmail, please note that they no longer allows less secure apps:\n\nError: {e}"
                    )
            nls("Waiting 60 seconds to try again...")
            time.sleep(60)
