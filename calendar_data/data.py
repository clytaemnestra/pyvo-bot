from datetime import date

import requests
from icalendar import Calendar


def get_calendar_data(pyvo_events_url):
    calendar_raw_data = requests.get(pyvo_events_url)
    return calendar_raw_data.content


def get_future_events(pyvo_events_url):
    data = get_calendar_data(pyvo_events_url)
    gcal = Calendar.from_ical(data)
    for event in gcal.walk():
        if (
            event.name == "VEVENT"
            and event["dtstart"].dt.date() > date.today()
        ):
            yield event
