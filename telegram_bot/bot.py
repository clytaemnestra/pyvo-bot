import logging
import os
from datetime import date
from typing import Any, Dict, Generator

import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
PRAGUE_CHAT_ID = "-1001168385726"

logger = logging.getLogger(__name__)


def send_message(chat_id: str, text: str) -> Dict[str, str]:
    token = TELEGRAM_TOKEN
    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat_id, "text": text},
    )
    response.raise_for_status()
    return response.json()


def send_notification(event: Dict[str, Any], days: int) -> None:
    summary = event["summary"]
    event_date = event["dtstart"].dt.date()
    output_event_date = event_date.strftime("%d.%m.%Y")
    date_difference = (event_date - date.today()).days
    if date_difference == days:
        message_text = (
            f"Tonight! {output_event_date}, {summary}"
            if days == 0
            else f"{days} days! {output_event_date}, {summary}"
        )
        send_message(chat_id=PRAGUE_CHAT_ID, text=message_text)
        logging.info(f"Message {message_text} sent!")


def send_message_to_prague_channel(
    events: Generator[Dict[str, Any], None, None]
) -> None:
    for event in events:
        send_notification(event, 6)
        send_notification(event, 3)
        send_notification(event, 0)
