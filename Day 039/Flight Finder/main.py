from datetime import *
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_dest_info()
flight_search = FlightSearch()
notification = NotificationManager()

update_needed = False
for dest in sheet_data:
    if dest["iataCode"] == "":
        dest["iataCode"] = flight_search.get_iata(dest["city"])
        update_needed = True

if update_needed:
    data_manager.dest_info = sheet_data
    data_manager.update_dest_info_iata()

DEPARTURE_IATA = "POZ"
tomorrow = datetime.now() + timedelta(days=1)
six_months_later = tomorrow + timedelta(days=180)

for dest in sheet_data:
    # search flights
    flight = flight_search.search_flights(
        fly_from=DEPARTURE_IATA,
        fly_to=dest["iataCode"],
        date_from=tomorrow,
        date_to=six_months_later
    )
    # send notification
    if flight is not None and flight.lowestPrice < dest["lowestPrice"]:
        notification.send_notification(
            message=f"Low Price Alert! Only {flight.lowestPrice} PLN to fly from "
                    f"{flight.departure_city} | {flight.departure_airport_code} "
                    f"to {flight.dest_city} | {flight.dest_airport_code}, "
                    f"from {flight.outbound_date} to {flight.inbound_date}."
        )
