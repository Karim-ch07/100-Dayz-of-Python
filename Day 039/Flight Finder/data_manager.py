import os
import requests

USER_ID = os.environ.get("USER_IDENTIFICATION")
TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

SHEETY_ENDPOINT = f"https://api.sheety.co/{USER_ID}/flightDeals/prices"

sheety_headers = {
    "Authorization": TOKEN,
}


class DataManager:

    def __init__(self):
        self.dest_info = []

    def get_dest_info(self):
        # GET REQUEST
        # get info from Google sheet
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        self.dest_info = data["prices"]
        return self.dest_info

    def update_dest_info_iata(self):
        # PUT REQUEST
        # update info in the Google sheet
        for dest in self.dest_info:
            SHEETY_PUT_ENDPOINT = f"{SHEETY_ENDPOINT}/{dest['id']}"
            dest_update = {
                "price": {
                    "iataCode": dest["iataCode"],
                }
            }
            response = requests.put(url=SHEETY_PUT_ENDPOINT, json=dest_update, headers=sheety_headers)
            response.raise_for_status()
