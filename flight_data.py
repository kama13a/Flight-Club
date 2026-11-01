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
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
