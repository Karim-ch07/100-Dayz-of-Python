from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

sheet_data = DataManager()

for dest in sheet_data.dest_info:
    if dest["iataCode"] == "":
        flight_search = FlightSearch(dest["city"])
        dest["iataCode"] = flight_search.get_iata()
        sheet_data.update_dest_info_iata(dest)

flights = FlightData(sheet_data)
notifications = NotificationManager(flights)
