import os
from dotenv import load_dotenv
import requests
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.BOT_TOKEN = os.environ["TELEGRAM_TOKEN"]
        self.CHAT_ID = os.environ["CHAT_ID"]

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id" : self.CHAT_ID,
            "text" : message
        }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to send message: {response.status_code}")
            return False
