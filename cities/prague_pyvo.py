from datetime import datetime

from calendar_data.data import get_future_events
from telegram_bot.bot import send_message

PRAGUE_CHAT_ID = "-1001837942773"  # test chat


def send_message_to_prague_channel():
    events = get_future_events("https://pyvo.cz/api/series/praha-pyvo.ics")
    for event in events:
        summary = event["summary"].replace("(", "").replace(")", "")
        event_date = event["dtstart"].dt.replace(tzinfo=None).date()
        output_event_date = event["dtstart"].dt.date().strftime("%d.%m.%Y")
        date_difference = (event_date - datetime.today().date()).days
        match date_difference:
            case 7:
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
