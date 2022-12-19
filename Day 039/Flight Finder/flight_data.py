import requests
import os
from datetime import *
from data_manager import DataManager

API_KEY = os.environ.get("API_KEY")

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
SEARCH_ENDPOINT = f"{TEQUILA_ENDPOINT}/v2/search?"

tequila_headers = {
    "apikey": API_KEY,
}

tomorrow = datetime.now() + timedelta(days=1)
six_months_later = tomorrow + timedelta(days=180)

FLIGHT_TYPE = "round"
DEPARTURE_CITY = "Poznan"
DEPARTURE_IATA = "POZ"
DEPARTURE_START_DATE = tomorrow.strftime("%d/%m/%Y")
DEPARTURE_END_DATE = six_months_later.strftime("%d/%m/%Y")
RETURN_MIN_DATE = 7
RETURN_MAX_DATE = 28
STOPS = 0
CURRENCY = "PLN"
LIMIT_RESULTS = 10


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, sheet_data: DataManager):
        self.search_results = []
        for dest in sheet_data.dest_info:
            self.search_params = {
                "flight_type": FLIGHT_TYPE,
                "fly_from": DEPARTURE_IATA,
                "fly_to": dest["iataCode"],  # destination
                "date_from": DEPARTURE_START_DATE,  # set to tomorrow
                "date_to": DEPARTURE_END_DATE,  # set to 6 months later
                "nights_in_dst_from": RETURN_MIN_DATE,  # min stay set to 7
                "nights_in_dst_to": RETURN_MAX_DATE,  # max stay set to 28
                "max_stopovers": STOPS,  # direct flights only
                "curr": CURRENCY,  # zloty as a currency
                "limit": LIMIT_RESULTS,  # limit results to 10
            }
            self.search_result = {
                "departure_city": DEPARTURE_CITY,
                "departure_airport_code": DEPARTURE_IATA,
                "dest_city": dest["city"],
                "dest_airport_code": "",
                "outbound_date": "",
                "inbound_date": "",
                "lowestPrice": dest["lowestPrice"],
                "cheaper": False,
            }
            self.get_flight_data()

    def get_flight_data(self):
        # GET REQUEST
        # search flights | TEQUILA API
        response = requests.get(url=SEARCH_ENDPOINT, params=self.search_params, headers=tequila_headers)
        response.raise_for_status()
        try:
            result_data = response.json()["data"][0]
        except IndexError:
            pass
        else:
            if result_data["price"] < self.search_result["lowestPrice"]:
                inbound = result_data["route"][0]["utc_departure"].split("T")[0]
                outbound = result_data["route"][1]["utc_departure"].split("T")[0]
                self.search_result.update({
                    # "departure_city": DEPARTURE_CITY,
                    # "departure_airport_code": DEPARTURE_IATA,
                    # "dest_city": dest["city"],
                    "dest_airport_code": result_data["flyTo"],
                    "outbound_date": inbound,
                    "inbound_date": outbound,
                    "lowestPrice": result_data["price"],
                    "cheaper": True,
                })
        finally:
            self.search_results.append(self.search_result)
