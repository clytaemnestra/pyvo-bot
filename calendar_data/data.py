from datetime import datetime

import requests
from icalendar import Calendar


def get_calendar_data(pyvo_events_url):
    calendar_raw_data = requests.get(pyvo_events_url)
    return calendar_raw_data.content


def get_future_events(pyvo_events_url):
    data = get_calendar_data(pyvo_events_url)
    gcal = Calendar.from_ical(data)
    future_events = []
    for event in gcal.walk():
        # tzinfo=None removes timezone information from events,
        # as both datetimes need to be either in the same timezone
        # or not to have any timezone information for the comparison to work
        if (
            event.name == "VEVENT"
            and event["dtstart"].dt.replace(tzinfo=None) > datetime.today()
        ):
            future_events.append(event)
    return future_events
