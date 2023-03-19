from unittest.mock import patch

import pytest
from freezegun import freeze_time
from icalendar import Calendar

from telegram_bot.bot import send_notification

TEST_CHAT_ID = "-1001837942773"

event_data_three = """BEGIN:VEVENT
SUMMARY:Test event
DTSTART:20220318T180000Z
END:VEVENT"""

event_data_six = """BEGIN:VEVENT
SUMMARY:Test event
DTSTART:20220321T180000Z
END:VEVENT"""

event_data_zero = """BEGIN:VEVENT
SUMMARY:Test event
DTSTART:20220315T180000Z
END:VEVENT"""


def parse_event_data(event_data):
    cal = Calendar.from_ical(event_data)
    event = cal.walk("VEVENT")[0]
    return {
        "summary": event["SUMMARY"],
        "dtstart": event["DTSTART"],
    }


@pytest.mark.parametrize(
    "event_data, days, expected_text",
    [
        (event_data_zero, 0, "Tonight! 15.03.2022, Test event"),
        (event_data_three, 3, "3 days! 18.03.2022, Test event"),
        (event_data_six, 6, "6 days! 21.03.2022, Test event"),
    ],
)
@freeze_time("2022-03-15 12:00:00")
def test_send_notification(event_data, days, expected_text):
    event_dict = parse_event_data(event_data)

    with patch("telegram_bot.bot.send_message") as mock_send_message:
        send_notification(event_dict, days)
        mock_send_message.assert_called_once_with(
            chat_id=TEST_CHAT_ID, text=expected_text
        )
