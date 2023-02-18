from days.day_040.files.helpers import requests, nls, nli, bcolors, pprint
from days.day_040.files.flight_data import FlightData

# Class responsible for handling Kiwi API flight searching

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def __init__(self, TEQUILA_API_KEY):
        self.tequila_api = TEQUILA_API_KEY
        self.city_codes = []

    def get_destination_code(self, city_names):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        for city in city_names:
            query = {"term": city, "location_types": "city"}

            headers = {"apikey": self.tequila_api}
            response = requests.get(
                url=location_endpoint, headers=headers, params=query
            )
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)
        return code

    def set_max_stopovers(self):
        stopovers = int(
            nli(
                "How many stopovers are you willing to accept?\nType 0 for direct flights."
            )
        )
        return stopovers

    def set_oneway(self):
        oneway = True

        oneway = nli("Is it Oneway?\nType 'y' or 'n'.")
        if oneway == "y":
            oneway = False
        elif oneway != "n" and oneway != "y":
            oneway = True
            print("Error with input, setting oneway to true")
        else:
            oneway = True
        return oneway

    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time,
        destination_city,
        MAX_STOPOVERS,
        ONE_WAY,
    ):
        headers = {"apikey": self.tequila_api}

        # Prepare query based on whether or not one-way flight
        one_way = ONE_WAY
        if one_way == True:
            query = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time,
                "date_to": to_time,
                "flight_type": "oneway",
                "one_for_city": 1,
                "max_stopovers": MAX_STOPOVERS,
                "curr": "AUD",
            }
        else:
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

        # Feedback
        nls(f"{bcolors.OKCYAN}PREPARED:\n{response.json()}{bcolors.ENDC}")

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(
                f"\nNo flights found for {destination_city} with {MAX_STOPOVERS} max stopover{'' if MAX_STOPOVERS < 2 else 's'} between {from_time} and {to_time}."
            )
            return None
        except Exception as e:
            nls(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
            return None
        else:
            if one_way == False:
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
                        f"\nCONNECTING FLIGHT FOUND:\n{flight_data.origin_city} -> {flight_data.destination_city} -> {flight_data.final_city}: ${flight_data.price} AUD"
                    )
                else:
                    print(
                        f"\nDIRECT FLIGHT FOUND:\n({flight_data.final_city}) {flight_data.origin_city} -> {flight_data.destination_city}: ${flight_data.price} AUD"
                    )
                # pprint(f"{data}")
                return flight_data
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                )
                # Checks for stopovers
                if flight_data.final_city != flight_data.destination_city:
                    print(
                        f"\nCONNECTING FLIGHT FOUND:\n{flight_data.origin_city} -> {flight_data.destination_city} -> {flight_data.final_city}: ${flight_data.price} AUD"
                    )
                else:
                    print(
                        f"\nDIRECT FLIGHT FOUND:\n({flight_data.final_city}) {flight_data.origin_city} -> {flight_data.destination_city}: ${flight_data.price} AUD"
                    )
                # pprint(f"{data}")
                return flight_data
