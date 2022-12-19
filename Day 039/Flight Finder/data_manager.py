import requests
import os

USER_ID = os.environ.get("USER_IDENTIFICATION")
TOKEN = os.environ.get("AUTH_TOKEN")

SHEETY_ENDPOINT = f"https://api.sheety.co/{USER_ID}/flightDeals/prices"

sheety_headers = {
    "Authorization": TOKEN,
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # GET REQUEST
        # get info from Google sheet
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        # initialize destinations info var
        self.dest_info = data["prices"]

    def get_dest_info(self):
        # return the data upon call list of dictionaries with all cities
        return self.dest_info

    def update_dest_info_iata(self, dest):
        # PUT REQUEST
        # update info in the Google sheet
        SHEETY_PUT_ENDPOINT = f"{SHEETY_ENDPOINT}/{dest['id']}"
        dest_update = {
            "price": {
                "iataCode": dest["iataCode"],
            }
        }
        response = requests.put(url=SHEETY_PUT_ENDPOINT, json=dest_update, headers=sheety_headers)
        response.raise_for_status()
