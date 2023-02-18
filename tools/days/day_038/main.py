# Day 38
# Updated 2023, Jarid Prince

from days.day_038.files.helpers import *


def day_038():
    title("NLP WORKOUT TRACKER")

    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nNUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY and SHEETY_BEARER values."
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
        NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
        NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
        SHEETY_BEARER = os.getenv(
            "SHEETY_BEARER"
        )  # User Generated and added to Sheety Authentication via project dashboard
        creds.append(NUTRITIONIX_APP_ID)
        creds.append(NUTRITIONIX_API_KEY)
        creds.append(SHEETY_BEARER)
    except Exception as e:
        error_env_msg(e)
        env_error = True
    else:
        for cred in creds:
            if cred == None or cred == "":
                error_env_msg(f"Error with credential: {cred}")
                env_error = True

    # RUN ONLY IF NO ERROR WITH ENV KEYS
    if not env_error:
        exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        # This will differ based on your connected account
        sheet_get_endpoint = (
            "https://api.sheety.co/15ae3c416bf45dc7d700adaa6ce50555/myWorkouts/workouts"
        )
        # (PUBLIC) Test and see results based on Google Sheet Inputs

        headers = {
            "x-app-id": NUTRITIONIX_APP_ID,
            "x-app-key": NUTRITIONIX_API_KEY,
        }

        # Ask user for information to be processed by Natural Language Algorithm
        exercise = nli("What exercise did you do and how many reps?")

        # Include personal body information
        params = {
            "query": exercise,
            "gender": "male",
            "weight_kg": "68",  # It's muscle, I promise :')
            "height_cm": "166",
            "age": 29,
        }

        response = requests.post(url=exercise_endpoint, json=params, headers=headers)
        result = response.json()

        today_date = dt.now().strftime("%d/%m/%Y")
        now_time = dt.now().strftime("%X")

        # Create Google/Sheety inputs based on response
        for exercise in result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"],
                }
            }

            # Authorise with Bearer token from Sheety Dashboard (Sheety must be authorised to access Google)
            bearer_headers = {"Authorization": f"Bearer {SHEETY_BEARER}"}
            sheet_response = requests.post(
                sheet_get_endpoint, json=sheet_inputs, headers=bearer_headers
            )

            nls("Natural Language Processing Complete! New Row Added.")
            print(
                f"{sheet_response.text}\nHead to {sheet_get_endpoint} to see exercises."
            )
