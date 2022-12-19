import os
from twilio.rest import Client
from flight_data import FlightData

SID = os.environ.get("ACCOUNT_SID")
TOKEN = os.environ.get("AUTH_TOKEN")
MY_NUMBER = os.environ.get("MY_NUMBER")
# Twilio Account Information
account_sid = SID
auth_token = TOKEN


class NotificationManager:
    def __init__(self, flight_data: FlightData):
        for search_result in flight_data.search_results:
            if search_result["cheaper"]:
                # Twilio send message
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    # body to be modified accordingly
                    body=f"Low Price Alert! Only {search_result['lowestPrice']} PLN to fly from "
                         f"{search_result['departure_city']}|{search_result['departure_airport_code']} to "
                         f"{search_result['dest_city']}|{search_result['dest_airport_code']},"
                         f" from {search_result['outbound_date']} to {search_result['inbound_date']}.",
                    from_="+15108801602",
                    to=MY_NUMBER,
                )
                print(message.status)
