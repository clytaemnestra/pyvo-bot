from datetime import date
from typing import Any, Dict, Generator

import requests
from icalendar import Calendar


def get_calendar_data(pyvo_events_url: str) -> bytes:
    calendar_raw_data = requests.get(pyvo_events_url)
    return calendar_raw_data.content


def get_future_events(
    data: bytes,
) -> Generator[Dict[str, Any], None, None]:
    gcal = Calendar.from_ical(data)
    for event in gcal.walk():
        if event.name == "VEVENT" and event["dtstart"].dt.date() >= date.today():
            yield event
