from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest
from datetime import datetime, timedelta
import requests_cache
from notification_manager import NotificationManager


requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

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
    try:
        search_data = fs.search_flight(
            origin='TAS',
            destination=city_code,
            out_date=out_date,
            return_date=return_date,
            is_direct=True
        )

        flight = find_cheapest(search_data, return_date)
        if flight.price == "N/A":
            print(f"No direct flight to {dest['city']}. Looking for indirect flights ...")


            search_data = fs.search_flight(
                origin='TAS',
                destination=city_code,
                out_date=out_date,
                return_date=return_date,
                is_direct=False
            )
            flight = find_cheapest(search_data, return_date)

    except Exception as e:
        print(f"❌ Error searching for {dest['city']} ({city_code}): {e}")
        continue


    if flight.price != "N/A" and flight.price <= dest["lowestPrice"]:
        stops_text = "Direct" if flight.stops == 0 else f"{flight.stops} stop(s)"
        message = f"🔥 CHEAPER FLIGHT to {dest['city']}! Only {flight.price}$ (Target: {dest['lowestPrice']}$) \n{stops_text}"
        print(message)
        nm.send_message(message)  # Sends to Telegram

    elif flight.price != "N/A":
        print(f"✈️ {dest['city']} : Flight is {flight.price}")

    else:
        print(f"❌ No flights found to {dest['city']}")