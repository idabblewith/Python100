from days.day_039.files.helpers import requests, nls, nli, bcolors
from days.day_039.files.flight_data import FlightData

# Class responsible for handling Kiwi API flight searching

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def __init__(self, TEQUILA_API_KEY):
        self.tequila_api = TEQUILA_API_KEY

    def get_destination_code(self, city_name):
        # print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": self.tequila_api}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def set_max_stopovers(self):
        stopovers = int(
            nli(
                "How many stopovers are you willing to accept?\nType 0 for direct flights."
            )
        )
        return stopovers

    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time,
        destination_city,
        MAX_STOPOVERS,
    ):
        headers = {"apikey": self.tequila_api}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": MAX_STOPOVERS,
            "curr": "AUD",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(
                f"\n{bcolors.FAIL}No flights found{bcolors.ENDC} for {destination_city} with {MAX_STOPOVERS} max stopover{'' if MAX_STOPOVERS < 2 else 's'} between {from_time} and {to_time}."
            )
            return None
        # else:
        #     nls(data)

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            final_city=destination_city,
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        # Checks for stopovers
        if flight_data.final_city != flight_data.destination_city:
            print(
                f"\n{bcolors.OKCYAN}CONNECTING FLIGHT FOUND:{bcolors.ENDC}\n{flight_data.origin_city} -> {flight_data.destination_city} -> {flight_data.final_city}: ${flight_data.price} AUD"
            )
        else:
            print(
                f"\n{bcolors.OKBLUE}DIRECT FLIGHT FOUND:{bcolors.ENDC}\n({flight_data.final_city}) {flight_data.origin_city} -> {flight_data.destination_city}: ${flight_data.price} AUD"
            )
        return flight_data
