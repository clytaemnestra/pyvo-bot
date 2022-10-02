from datetime import datetime

from calendar_data.data import parse_calendar_data
from telegram_bot.bot import send_message


def send_message_to_prague_channel():
    events = parse_calendar_data("https://pyvo.cz/api/series/praha-pyvo.ics")
    prague_chat_id = "-1001837942773"  # test chat
    for event in events:
        summary = event.get("summary").replace("(", "").replace(")", "")
        event_date = event.get("dtstart").dt.replace(tzinfo=None).date()
        output_event_date = event.get("dtstart").dt.date().strftime("%d.%m.%Y")
        date_difference = abs(event_date - datetime.today().date()).days
        match date_difference:
            case 7:
                send_message(
                    prague_chat_id,
                    f"Next week! {output_event_date}, {summary}",
                )
            case 3:
                send_message(
                    prague_chat_id,
                    f"In three days! {output_event_date}, {summary}",
                )
            case 0:
                send_message(
                    prague_chat_id,
                    f"Tonight! {output_event_date}, {summary}",
                )
