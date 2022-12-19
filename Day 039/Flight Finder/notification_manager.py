import os
from twilio.rest import Client

# Twilio Account Information
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.environ.get("MY_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, message):
        # Twilio send message
        notification = self.client.messages.create(
            body=message,
            from_="+15108801602",
            to=MY_NUMBER,
        )
        # print message status
        print(notification.status)
