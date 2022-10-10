import os
from datetime import date

import requests

from calendar_data.data import get_future_events
from typing import Dict

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
PRAGUE_CHAT_ID = "-1001168385726"


def send_message(chat_id: str, text: str) -> Dict[str, str]:
    token = TELEGRAM_TOKEN
    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat_id, "text": text},
    )
    response.raise_for_status()
    return response.json()


def send_message_to_prague_channel() -> None:
    events = get_future_events("https://pyvo.cz/api/series/praha-pyvo.ics")
    for event in events:
        summary = event["summary"]
        event_date = event["dtstart"].dt.date()
        output_event_date = event["dtstart"].dt.date().strftime("%d.%m.%Y")
        date_difference = (event_date - date.today()).days
        match date_difference:
            case 6:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"Next week! {output_event_date}, {summary}",
                )
            case 3:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"In three days! {output_event_date}, {summary}",
                )
            case 0:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"Tonight! {output_event_date}, {summary}",
                )
