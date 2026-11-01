# TODO 3: flight_search.py
    # Responsibility: ONLY talking to the SerpApi (Flight Search API).
    # What to do:
        # Take the origin, destination, and date.
        # Send the request to SerpApi.
        # Return the raw JSON (messy data).
    # Methods:
        # search(origin, destination, out_date) -> returns raw JSON.
    # Connections:
        # Called by main.py.
import os
import requests
from dotenv import load_dotenv

load_dotenv()
FLIGHT_URL="https://serpapi.com/search"

class FlightSearch:
    def __init__(self):
        self.API_KEY = os.environ["API_KEY"]
        self.url = FLIGHT_URL

    def search_fight(self, origin, destination, out_date):

        params = {
            "engine" : "google_flights",
            "departure_id" : origin,
            "arrival_id" : destination,
            "outbound_date" : out_date,
            "type" : "2",
            "api_key" : self.API_KEY
        }
        response = requests.get(self.url, params=params)
        response.raise_for_status()
        data = response.json()

        return data

