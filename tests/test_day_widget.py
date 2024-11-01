from kivy.core.text import LabelBase
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.widget import Widget

import pytest
from unittest.mock import MagicMock, patch

import src.lib.day_widget
import src.constants as const

ARBITRARY_DAY_NUMBER = 27

@pytest.fixture
def mock_kivy_widgets(mocker):
    mocker.patch('src.lib.day_widget.CalendarDay.collide_point', return_value=True)

@pytest.fixture
def day_widget(mock_kivy_widgets):
    LabelBase.register(name='pricedown_bl', fn_regular='../assets/font/Freedom-10eM.ttf')
    return src.lib.day_widget.CalendarDay(ARBITRARY_DAY_NUMBER)


####################################################################################
def test_on_creation_widget_presented_correctly(day_widget):
    with patch('src.lib.day_widget.Color') as color_mock:
        day_widget = src.lib.day_widget.CalendarDay(ARBITRARY_DAY_NUMBER)
        color_mock.assert_called_once_with(*const.DARKER_DAY_WIDGET_COLOR)
        assert day_widget.day_index_label.text == str(ARBITRARY_DAY_NUMBER)


####################################################################################
def test_calendar_day_widgets_alternate_color():
    with patch('src.lib.day_widget.Color') as color_mock:
        day_1 = src.lib.day_widget.CalendarDay(1)
        color_mock.assert_called_once_with(*const.DARKER_DAY_WIDGET_COLOR)
        color_mock.reset_mock()

        day_2 = src.lib.day_widget.CalendarDay(2)
        color_mock.assert_called_once_with(*const.LIGHTER_DAY_WIDGET_COLOR)
        color_mock.reset_mock()

        day_3 = src.lib.day_widget.CalendarDay(3)
        color_mock.assert_called_once_with(*const.DARKER_DAY_WIDGET_COLOR)
        color_mock.reset_mock()

        day_4 = src.lib.day_widget.CalendarDay(4)
        color_mock.assert_called_once_with(*const.LIGHTER_DAY_WIDGET_COLOR)
        color_mock.reset_mock()


####################################################################################
def test_on_touch_up_and_day_not_selected_then_widget_will_highlight_itself(day_widget):
    kivy_touch_mock = MagicMock()
    kivy_touch_mock.pos = (12, 12)
    day_widget.selected = False

    with patch('src.lib.day_widget.Color') as color_mock, \
            patch('src.lib.day_widget.Line') as line_mock:

        day_widget.on_touch_up(kivy_touch_mock)

        color_mock.assert_called_with(*const.SIDEBAR_BUTTON_COLOR)
        line_mock.assert_called_once_with(rectangle=(day_widget.x, day_widget.y + 1, day_widget.width - 2, day_widget.height - 2), width=2)
        assert day_widget.selected


####################################################################################
def test_on_touch_up_on_different_day_widget_then_widget_will_remove_highlighting(day_widget):
    kivy_touch_mock = MagicMock()
    kivy_touch_mock.pos = (12, 12)
    day_widget.selected = False
    day_widget.on_touch_up(kivy_touch_mock)
    assert day_widget.border is not None

    with patch('src.lib.day_widget.CalendarDay.collide_point', return_value=False):
        day_widget.on_touch_up(kivy_touch_mock)

        assert not day_widget.selected
        assert day_widget.border is None