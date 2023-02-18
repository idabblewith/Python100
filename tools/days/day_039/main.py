# Day 39
# Updated 2023, Jarid Prince

from days.day_039.files.helpers import *
from days.day_039.files.data_manager import DataManager
from days.day_039.files.flight_search import FlightSearch
from days.day_039.files.notification_manager import NotificationManager


def day_039():
    title("FLIGHT SCANNER")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nSHEETY_FLIGHT_URL, TEQUILA_API, TWILIO_ID, TWILIO_TOKEN, TWILIO_NUMBER, MY_PHONE_NUMBER values."
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
        SHEETY_FLIGHT_URL = os.getenv("SHEETY_FLIGHT_URL")
        TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
        TWILIO_ID = os.getenv("TWILIO_ID")
        TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
        TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
        MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
        creds.append(SHEETY_FLIGHT_URL)
        creds.append(TEQUILA_API_KEY)
        creds.append(TWILIO_ID)
        creds.append(TWILIO_TOKEN)
        creds.append(TWILIO_NUMBER)
        creds.append(MY_PHONE_NUMBER)
    except Exception as e:
        error_env_msg(e)
        env_error = True
    else:
        for cred in creds:
            if cred == None or cred == "":
                error_env_msg(f"Error with credential: {cred}")
                env_error = True

    # RUN ONLY IF NO ERROR WITH KEYS
    if not env_error:
        # Instantiate relevant classes with API Keys
        data_manager = DataManager(SHEETY_FLIGHT_URL)
        sheet_data = data_manager.get_destination_data()
        flight_search = FlightSearch(TEQUILA_API_KEY)
        notification_manager = NotificationManager(
            TWILIO_ID, TWILIO_TOKEN, TWILIO_NUMBER, MY_PHONE_NUMBER
        )

        # Given Destination, and prokmpt user for max stopovers
        ORIGIN_CITY = "PER"
        MAX_STOPOVERS = flight_search.set_max_stopovers()

        # Update Sheet if no iataCode
        if sheet_data[0]["iataCode"] == "":
            for row in sheet_data:
                row["iataCode"] = flight_search.get_destination_code(row["city"])
            data_manager.destination_data = sheet_data
            data_manager.update_destination_codes()

        # Set relevant time variables from tomorrow to 6 months later
        tomorrow_base = dt.now() + timedelta(1)
        tomorrow = tomorrow_base.strftime("%d/%m/%Y")
        six_later_base = tomorrow_base + timedelta((6 * 30))
        six_later = six_later_base.strftime("%d/%m/%Y")

        # Read sheet to check flights from origin to locations in sheet
        for destination in sheet_data:
            flight = flight_search.check_flights(
                ORIGIN_CITY,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_later,
                destination_city=destination["city"],
                MAX_STOPOVERS=MAX_STOPOVERS,
            )
            # Send SMS if lower than lowest price on spreadsheet
            if flight == None:
                continue
            elif flight.price < destination["lowestPrice"]:
                # Handler to check if there is a connecting flight, or direct
                if flight.final_city != flight.destination_city:
                    notification_manager.send_sms(
                        message=f"CONNECTING FLIGHT FOUND:\n{flight.origin_city} -> {flight.destination_city} -> {flight.final_city}: ${flight.price} AUD, dates: {flight.out_date} to {flight.return_date}."
                    )

                else:
                    notification_manager.send_sms(
                        message=f"DIRECT FLIGHT FOUND:\n{flight.origin_city} -> {flight.final_city}: ${flight.price} AUD, dates: {flight.out_date} to {flight.return_date}."
                    )
