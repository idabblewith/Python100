# Class responsible for formatting responses of flight data
class FlightData:
    def __init__(
        self,
        price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        final_city,
        out_date,
        return_date=None,
        stop_overs=None,
        via_city=None,
    ):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.final_city = final_city
        self.out_date = out_date
        self.return_date = None if return_date == None else return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
