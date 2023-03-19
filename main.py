import logging

from calendar_data.data import get_calendar_data, get_future_events
from telegram_bot.bot import send_message_to_prague_channel

PYVO_EVENTS_URL = "https://pyvo.cz/api/series/praha-pyvo.ics"

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    data = get_calendar_data(PYVO_EVENTS_URL)
    events = get_future_events(data=data)
    send_message_to_prague_channel(events=events)


if __name__ == "__main__":
    main()
