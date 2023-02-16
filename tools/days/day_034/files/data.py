from days.day_034.files.helpers import requests

# Pull data from online trivia database
def get_data():

    parameters = {"amount": 10, "type": "boolean"}

    response = requests.get("https://opentdb.com/api.php", parameters)
    response.raise_for_status()
    question_data = response.json()["results"]
    return question_data
