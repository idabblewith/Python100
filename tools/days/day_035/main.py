# Day 35
# Updated 2023, Jarid Prince

from days.day_035.files.helpers import *


def day_035():
    title("RAIN ALERT")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file'\nOPEN_WEATHER_API, TWILIO_ID, TWILIO_TOKEN, TWILIO_NUMBER & MY_PHONE_NUMBER values."
    )

    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    ENV_FILE = os.path.join(BASE_DIR, ".env")
    env_error = False

    def error_env_msg(e):
        nls(
            f"It seems that you do not have an environment variable for a required file!\n{e}"
        )

    creds = []
    try:
        load_dotenv(ENV_FILE)
        TWILIO_ID = os.getenv("TWILIO_ID")
        TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
        TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
        MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
        OPEN_WEATHER_API = os.getenv("OPEN_WEATHER_API")
        creds.append(TWILIO_ID)
        creds.append(TWILIO_TOKEN)
        creds.append(TWILIO_NUMBER)
        creds.append(MY_PHONE_NUMBER)
        creds.append(OPEN_WEATHER_API)
    except Exception as e:
        error_env_msg(e)
        env_error = True
    else:
        for cred in creds:
            if cred == None or cred == "":
                error_env_msg(f"Error with credential: {cred}")
                env_error = True

    # RUN ONLY IF NO ERRORS WITH ENV KEYS
    if not env_error:
        nls("Credentials are present. Checking Weather API for Perth...")
        # Preparing API parameters for request & sending, raising error if one present
        params = {
            "lat": -31.9333,
            "lon": 115.8333,
            "exclude": "alerts,daily,minutely,current",
            "appid": OPEN_WEATHER_API,
        }

        response = requests.get(
            url="https://api.openweathermap.org/data/3.0/onecall", params=params
        )
        response.raise_for_status()
        # Format to JSON and determine wheteher it will rain in the next 12 hours (code less than 700 means rain)
        data = response.json()
        will_rain = False
        next_12 = data["hourly"][:12]
        for hour in next_12:
            weather_code = hour["weather"][0]["id"]
            if weather_code < 700:
                will_rain = True
        # Create a Twilio client and determine message based on whether it will rain
        nls("Checking Twilio details...")
        if will_rain:
            client = Client(TWILIO_ID, TWILIO_TOKEN)
            message = client.messages.create(
                body="It's going to rain today within the next 12 hours. Bring an umbrella.",
                from_=TWILIO_NUMBER,
                to=MY_PHONE_NUMBER,
            )
            print(message.status)
        else:
            client = Client(TWILIO_ID, TWILIO_TOKEN)
            message = client.messages.create(
                body="It's going to rain today within the next 12 hours. Bring an umbrella.",
                from_=TWILIO_NUMBER,
                to=MY_PHONE_NUMBER,
            )
            print(message.status)
            nls("An SMS will be sent to your phone number in the next few minutes.")
