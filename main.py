from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
import requests_cache
from notification_manager import NotificationManager


requests_cache.install_cache('flight_cache', expire_after=3600)

today = datetime.now()
out_date = "2026-12-15"
until = today + timedelta(days=14)
return_date = "2026-12-22"

dm = DataManager()
destinations = dm.get_destination_data()

fs = FlightSearch()
nm = NotificationManager()

for dest in destinations:
    city_code = dest["iataCode"]

    search_data = fs.search_flight(
        origin='TAS',
        destination=city_code,
        out_date=out_date,
        return_date=return_date
    )

    if "best_flights" in search_data and len(search_data["best_flights"]) > 0:
        cheapest = search_data["best_flights"][0]

        price = cheapest["price"]
        origin_airport = cheapest["flights"][0]["departure_airport"]["id"]
        destination_airport = cheapest["flights"][-1]["arrival_airport"]["id"]

        flight = FlightData(
            price=price,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            out_date=out_date,
            return_date=return_date
        )

        if flight.price <= dest["lowestPrice"]:
            message = f"Cheaper flight to {dest['city']}! Only {flight.price} (Targeted was {dest['lowestPrice']})"
            nm.send_message(message)
            print(message)
        else:
            print(f"{dest['city']} : Flight is {flight.price}")

    else:
        print(f"x No flights found to {dest['city']}")