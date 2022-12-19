import os
import requests

API_KEY = os.environ.get("API_KEY")

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
LOCATIONS_ENDPOINT = f"{TEQUILA_ENDPOINT}/locations/query?"

tequila_headers = {
    "apikey": API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.search_params = {
            "term": city_name,
        }
        self.city_data = {}
        self.get_iata()

    def get_iata(self):
        # GET REQUEST
        # search iata and return it
        response = requests.get(url=LOCATIONS_ENDPOINT, params=self.search_params, headers=tequila_headers)
        response.raise_for_status()
        self.city_data = response.json()["locations"][0]
        city_iata = self.city_data["code"]
        # return the iatacode to the main function
        return city_iata

