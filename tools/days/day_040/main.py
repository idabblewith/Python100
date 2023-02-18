# Day 40
# Updated 2023, Jarid Prince

from days.day_040.files.helpers import *
from days.day_040.files.data_manager import DataManager
from days.day_040.files.flight_search import FlightSearch
from days.day_040.files.notification_manager import NotificationManager


def day_040():
    title("FLIGHT CLUB")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nSHEETY_FLIGHT_URL, TEQUILA_API, SHEETY_FLIGHT_USER_ENDPOINT values."
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
        SHEETY_FLIGHT_USER_ENDPOINT = os.getenv("SHEETY_FLIGHT_USER_ENDPOINT")
        MY_EMAIL = os.getenv("MY_EMAIL")
        MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
        creds.append(MY_EMAIL)
        creds.append(MY_EMAIL_PASSWORD)
        creds.append(SHEETY_FLIGHT_URL)
        creds.append(TEQUILA_API_KEY)
        creds.append(SHEETY_FLIGHT_USER_ENDPOINT)
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
            MY_EMAIL=MY_EMAIL, MY_PASSWORD=MY_EMAIL_PASSWORD
        )

        # Given Destination, and prokmpt user for max stopovers
        ORIGIN_CITY = "PER"
        MAX_STOPOVERS = flight_search.set_max_stopovers()
        ONE_WAY = flight_search.set_oneway()

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
        cheap = []
        for destination in sheet_data:
            flight = flight_search.check_flights(
                ORIGIN_CITY,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_later,
                destination_city=destination["city"],
                MAX_STOPOVERS=MAX_STOPOVERS,
                ONE_WAY=ONE_WAY,
            )
            # Send Email if lower than lowest price on spreadsheet
            if flight == None:
                nls(
                    f'{bcolors.WARNING}No flights found for {destination["iataCode"]}.{bcolors.ENDC}'
                )
            else:
                # Handle direct and connecting flights appendage to cheap array
                if MAX_STOPOVERS >= 1:
                    if flight.price < destination["lowestPrice"]:
                        cheap.append(
                            dict(
                                fromCity=flight.origin_city,
                                toCity=flight.destination_city,
                                price=flight.price,
                                fromDate=flight.out_date,
                                toDate=flight.return_date,
                                stops=flight.stop_overs,
                                viaCity=flight.via_city,
                            )
                        )
                else:
                    cheap.append(
                        dict(
                            fromCity=flight.origin_city,
                            toCity=flight.destination_city,
                            price=flight.price,
                            fromDate=flight.out_date,
                            toDate=flight.return_date,
                        )
                    )

        email_list = data_manager.get_email_list(SHEETY_FLIGHT_USER_ENDPOINT)
        # print(cheap)
        # print(email_list)

        # Email each user in list for each cheap flight found in sheet
        for user in email_list["users"]:
            message = ""
            for cheap_flight in cheap:
                if cheap_flight["stops"]:
                    message += f"\nLow price alert!\n{cheap_flight['fromCity']}-{cheap_flight['toCity']} | AUD${cheap_flight['price']}\n{cheap_flight['fromDate']}\nSTOPOVERS: {cheap_flight['stops']} via {cheap_flight['viaCity']}"
                else:
                    message += f"\nLow price alert!\n{cheap_flight['fromCity']}-{cheap_flight['toCity']} | AUD${cheap_flight['price']}\n{cheap_flight['fromDate']} to {cheap_flight['toDate']}\n"

            # Send email will print the email instead if there is an error with credentials (see notification_manager)
            notification_manager.send_emails(message=message, person=user["email"])

        # https://www.faredetective.com/farehistory/
