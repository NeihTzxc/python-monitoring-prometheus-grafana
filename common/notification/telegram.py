import os

import dotenv
import requests

dotenv.load_dotenv("common/notification/.env")


class Telegram:
    def __init__(self):
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.api_key = os.getenv("TELEGRAM_API_KEY")

    def send_message(self, message):
        api_url = f'https://api.telegram.org/bot{self.api_key}/sendMessage'
        try:
            response = requests.post(api_url, json={'chat_id': self.chat_id, 'text': message})
            print(response.text)
        except Exception as e:
            print(e)
