import datetime
from kivy.core.text import LabelBase
import pytest
from unittest.mock import patch
import src.garage_app_main_window
import src.month_scroll_bar

LabelBase.register(name='freedom_font', fn_regular='../assets/font/Freedom-10eM.ttf')
MONTH_SCROLLBAR_ID = 'month_scroll'

@pytest.fixture
def mock_kivy_widgets(mocker):
    mocker.patch('src.garage_app_main_window.FloatLayout.add_widget')
    mocker.patch('src.garage_app_main_window.BoxLayout.add_widget')
    return mocker

@pytest.fixture
def window(mock_kivy_widgets):
    return src.garage_app_main_window.GarageAppMainWindow()


def test_on_start_window_displays_current_month(window):
    monthScroll = window.ids[MONTH_SCROLLBAR_ID]

    assert monthScroll.current_month == datetime.date.today().month - 1 #Month is between 1-12, my lists are from 0-11
    assert monthScroll.size_hint == [1, 0.085]


def test_on_start_window_hides_side_bar(window):
    assert window.sidebar_layout.x == -100


def test_on_scroll_bar_button_click_expect_correct_handler_called(window):
    monthScroll = window.ids[MONTH_SCROLLBAR_ID]

    with patch('src.garage_app_main_window.GarageAppMainWindow.handle_forward_scroll') as fore_scroll:
        monthScroll.next_button.trigger_action(duration=0)
        assert fore_scroll.assert_called_once

    with patch('src.garage_app_main_window.GarageAppMainWindow.handle_backward_scroll') as back_scroll:
        monthScroll.back_button.trigger_action(duration=0)
        assert back_scroll.assert_called_once


def test_on_touch_slide_such_that_scroll_bar_still_mostly_hidden_reset_side_bar_position(window):

    assert True
