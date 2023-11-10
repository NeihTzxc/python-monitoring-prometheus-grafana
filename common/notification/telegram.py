import os
import time

import dotenv
import requests

dotenv.load_dotenv("common/notification/.env")
disable_preview = True

class Telegram:
    def __init__(self):
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.api_key = os.getenv("TELEGRAM_API_KEY")

    def send_message(self, message):
        api_url = f'https://api.telegram.org/bot{self.api_key}/sendMessage'
        try:
            start_time = time.time()
            response = requests.post(api_url, json={'chat_id': self.chat_id, 'text': message, 'disable_web_page_preview': disable_preview})
            print(f"Execution Time: {time.time() - start_time} seconds")
            print(response.text)
        except Exception as e:
            print(e)
