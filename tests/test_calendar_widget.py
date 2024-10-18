import pytest
from unittest.mock import MagicMock
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
import src.lib.calendar_widget

ARBITRARY_TEST_MONTH = 10
ARBITRARY_TEST_YEAR = 2024
# October 2024 starts on Tuesday, and ends on Thursday. It has 31 days
DAYS_LABEL_STARTING_INDEX: int = -7

@pytest.fixture
def calendar_widget():
    LabelBase.register(name='freedom_font', fn_regular='../assets/font/Freedom-10eM.ttf')
    calendar_widget = src.lib.calendar_widget.CalendarWidget(ARBITRARY_TEST_MONTH, ARBITRARY_TEST_YEAR)
    return calendar_widget


####################################################################################
def test_on_construction_topmost_row_shows_names_of_days_of_week(calendar_widget):
    days_label = []
    for column in reversed(calendar_widget.children[DAYS_LABEL_STARTING_INDEX:]):
        days_label.append(column)

    assert days_label[0].text == 'Monday'
    assert days_label[1].text == 'Tuesday'
    assert days_label[2].text == 'Wednesday'
    assert days_label[3].text == 'Thursday'
    assert days_label[4].text == 'Friday'
    assert days_label[5].text == 'Saturday'
    assert days_label[6].text == 'Sunday'


####################################################################################
def test_on_construction_calendar_widget_contains_one_widget_per_day_in_month():
    number_of_column_identifiers = 7
    days_in_october_2024, oct_preamble_days_count, oct_trailing_day_count = 31, 1, 3
    days_in_may_2025, may_preamble_days_count, may_trailing_day_count = 30, 3, 2
    days_in_december_2023, dec_preamble_days_count, dec_trailing_day_count = 29, 4, 2

    calendar_widget = src.lib.calendar_widget.CalendarWidget(10, 2024)
    assert ((len(calendar_widget.children)
            - (number_of_column_identifiers + oct_preamble_days_count + oct_trailing_day_count))
            == days_in_october_2024)

    calendar_widget = src.lib.calendar_widget.CalendarWidget(5, 2025)
    assert ((len(calendar_widget.children)
            - (number_of_column_identifiers + may_preamble_days_count + may_trailing_day_count))
            == days_in_may_2025)

    calendar_widget = src.lib.calendar_widget.CalendarWidget(12, 2023)
    assert ((len(calendar_widget.children)
            - (number_of_column_identifiers + dec_preamble_days_count + dec_trailing_day_count))
            == days_in_december_2023)
