import os

import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]


def send_message(chat_id, text):
    token = TELEGRAM_TOKEN
    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat_id, "text": text},
    )
    response.raise_for_status()
    return response.json()
