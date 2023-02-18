from days.day_040.files.helpers import requests, nls, JSONDecodeError, json

# This class is responsible for talking to the Google Sheet (must be passed in on instantiation).
class DataManager:
    def __init__(self, SHEETY_FLIGHT_URL):
        self.destination_data = {}
        self.sheet = SHEETY_FLIGHT_URL

    # Uses Sheety endpointed (connected to google sheet) to get data
    def get_destination_data(self):
        response = requests.get(url=f"{self.sheet}")
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # Provides Iata codes for given cities
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{self.sheet}/{city['id']}", json=new_data)
            print(response.text)

    def get_email_list(self, SHEETY_FLIGHT_USER_ENDPOINT):
        user_data = requests.get(url=SHEETY_FLIGHT_USER_ENDPOINT)
        list = user_data.json()
        return list
