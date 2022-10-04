import os
from datetime import date

import requests

from calendar_data.data import get_future_events

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
PRAGUE_CHAT_ID = "-1001837942773"  # test chat


def send_message(chat_id, text):
    token = TELEGRAM_TOKEN
    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat_id, "text": text},
    )
    response.raise_for_status()
    return response.json()


def send_message_to_prague_channel():
    events = get_future_events("https://pyvo.cz/api/series/praha-pyvo.ics")
    for event in events:
        summary = event["summary"]
        # fix for https://github.com/pyvec/pyvo.cz/issues/161
        output_summary = summary[1:-1]
        event_date = event["dtstart"].dt.date()
        output_event_date = event["dtstart"].dt.date().strftime("%d.%m.%Y")
        date_difference = (event_date - date.today()).days
        match date_difference:
            case 7:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"Next week! {output_event_date}, {output_summary}",
                )
            case 3:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"In three days! {output_event_date}, {output_summary}",
                )
            case 0:
                send_message(
                    PRAGUE_CHAT_ID,
                    f"Tonight! {output_event_date}, {output_summary}",
                )
