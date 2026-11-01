# TODO 1: data_manager.py
    # Responsible for talking to the Google Sheet
    # API :
        #1. Google Sheet Data Management - https://sheety.co/
    # What to do :
        #1. create new project in google sheets and connect to the sheety
    # methods:
        #1. add_row() -- creating a row for the new travel

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
class DataManager:
    def __init__(self):
        self.ENDPOINT = os.environ["SHEETY_URL"]
        self.BEARER = os.environ["BEARER_TOKEN"]

        self.headers = {
            "Authorization" : f"Bearer {self.BEARER}"
        }

    def get_destination_data(self):
        response = requests.get(url=self.ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

