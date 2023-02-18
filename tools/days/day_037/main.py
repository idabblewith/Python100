# Day 37
# Updated 2023, Jarid Prince

from days.day_037.files.helpers import *


def day_037():
    title("PIXELA TRACKER")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nPIXELA_TOKEN and PIXELA_USER values."
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
        PIXELA_TOKEN = os.getenv(
            "PIXELA_TOKEN"
        )  # Self generated between 8-128 characters
        PIXELA_USER = os.getenv(
            "PIXELA_USER"
        )  # Self generated (must be available username)
        creds.append(PIXELA_TOKEN)
        creds.append(PIXELA_USER)
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
        # Create a user with API params
        pixela_endpoint = "https://pixe.la/v1/users"
        user_params = {
            "token": PIXELA_TOKEN,
            "username": PIXELA_USER,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

        # #Check that user is created
        # response = requests.post(url=pixela_endpoint, json=user_params)
        # print(response.text)

        # Create an endpoint for tracking food/calories consumed
        graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs"
        graph_config = {
            "id": "calories",
            "name": "Food",
            "unit": "calory",
            "type": "float",
            "color": "momiji",
        }
        # Required when authenticating request. Uses same token for creation of account.
        headers = {"X-USER-TOKEN": PIXELA_TOKEN}

        # #Check that graph created with headers -> https://pixe.la/v1/users/[USER]/graphs/[GRAPHID].html
        # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        # print(response.text)

        # ---------------- Adding a pixel to the graph for today's date ----------------
        pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/calories"
        today = dt.now()
        print(f'Date: {today.strftime("%Y,%m,%d")}')
        pixel_data = {
            "date": today.strftime("%Y%m%d"),
            "quantity": input("How many calories did you eat today?\n"),
        }

        # Sending request
        response = requests.post(
            url=pixel_creation_endpoint, json=pixel_data, headers=headers
        )
        print(
            f"{response.text}\n Navigate to https://pixe.la/@{PIXELA_USER} to see your charts."
        )

        # ---------------- Updating a pixel on a given date ----------------
        # update_endpoint = f"{pixela_endpoint}/{USER}/graphs/calories/{today.strftime('%Y%m%d')}"
        # new_pixel_data = {
        #     "quantity": input("How many calories did you eat?")
        # }
        # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
        # print(response.text)

        # ---------------- Deleting pixel on a given date ----------------
        # delete_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/calories/{today.strftime('%Y%m%d')}"
        # response = requests.delete(url=delete_endpoint, headers=headers)
        # print(response.text)
