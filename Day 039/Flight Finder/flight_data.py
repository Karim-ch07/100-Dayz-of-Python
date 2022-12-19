
class FlightData:
    def __init__(self, departure_city, departure_airport_code, dest_city, dest_airport_code,
                 outbound_date, inbound_date, lowestPrice):
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code
        self.dest_city = dest_city
        self.dest_airport_code = dest_airport_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.lowestPrice = lowestPrice