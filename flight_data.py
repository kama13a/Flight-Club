# TODO 2: flight_data.py
    # Responsibility: Act as a clean container (a box) for ONE flight's information.
    # What to do:
        # Take the values passed to it and store them as attributes.
    # Attributes:
        # self.price
        # self.origin_airport
        # self.destination_airport
        # self.out_date
        # self.return_date
    # Methods:
        # Only __init__ (the constructor).
    # Connection:
        # Created by main.py (main.py gets the data and passes it in).

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")


    all_flights = data["best_flights"] + data["other_flights"]
    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin_airport = first_flight["flights"][0]["departure_airport"]["id"]
    destination_airport = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    stops = len(first_flight["flights"]) - 1
    cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date, stops)

    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            continue
        if price < cheapest_flight.price:
            lowest_price = price
            origin_airport = flight["flights"][0]["departure_airport"]["id"]
            destination_airport = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            stops = len(flight["flights"]) - 1
            cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport,out_date, return_date, stops)

            print(f"Lowest price to {destination_airport} is GBP {lowest_price}")

    return cheapest_flight