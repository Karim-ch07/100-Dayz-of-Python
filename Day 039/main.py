# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from twilio.rest import Client

# Twilio Account Information
account_sid = ""
auth_token = ""

# Twilio send message
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="article",
    from_="+15108801602",
    to="+48729339635",
)
print(message.status)
