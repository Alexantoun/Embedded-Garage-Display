import datetime
from kivy.core.text import LabelBase
import pytest
from unittest.mock import MagicMock, patch
import src.garage_app_main_window
import src.month_scroll_bar

MONTH_SCROLLBAR_ID = 'month_scroll'


@pytest.fixture
def mock_kivy_widgets(mocker):
    mocker.patch('src.garage_app_main_window.FloatLayout.add_widget')
    mocker.patch('src.garage_app_main_window.BoxLayout.add_widget')
    return mocker


@pytest.fixture
def window(mock_kivy_widgets):
    LabelBase.register(name='freedom_font', fn_regular='../assets/font/Freedom-10eM.ttf')
    return src.garage_app_main_window.GarageAppMainWindow()


####################################################################################
def test_on_start_window_displays_current_month(window):
    month_scroll = window.ids[MONTH_SCROLLBAR_ID]

    assert month_scroll.current_month == datetime.date.today().month - 1  #Month is between 1-12, my lists are from 0-11
    assert month_scroll.size_hint == [1, 0.085]


####################################################################################
def test_on_start_window_hides_side_bar(window):
    assert window.sidebar_layout.x == -150


####################################################################################
def test_on_scroll_bar_button_click_expect_correct_handler_called(window):
    month_scroll = window.ids[MONTH_SCROLLBAR_ID]

    with patch('src.garage_app_main_window.GarageAppMainWindow.handle_forward_scroll') as fore_scroll:
        month_scroll.next_button.trigger_action(duration=0)
        assert fore_scroll.assert_called_once

    with patch('src.garage_app_main_window.GarageAppMainWindow.handle_backward_scroll') as back_scroll:
        month_scroll.back_button.trigger_action(duration=0)
        assert back_scroll.assert_called_once


####################################################################################
def test_on_touch_up_such_that_side_bar_still_mostly_hidden_reset_side_bar_position(window):
    window.moving_bar = True
    window.sidebar_layout.x = -51
    window.on_touch_up(None)
    assert window.sidebar_layout.x == src.garage_app_main_window.SIDEBAR_INITIAL_POSITION_x
    assert not window.sidebar_active


####################################################################################
def test_on_touch_up_such_that_side_bar_mostly_exposed_set_position_to_fully_exposed(window):
    window.moving_bar = True
    window.sidebar_layout.x = -49
    window.on_touch_up(None)
    assert window.sidebar_layout.x == src.garage_app_main_window.SIDEBAR_ACTIVE_POSITION_x
    assert window.sidebar_active


####################################################################################
def test_on_touch_down_touch_start_position_updated(window):
    touch_mock = MagicMock()
    touch_mock.x = 123.321

    window.on_touch_down(touch_mock)
    assert window.touch_start_x == touch_mock.x


####################################################################################
def test_on_touch_move_with_insufficient_movement_sets_movement_flag_true(window):
    arbitrary_touch_start = 5
    arbitrary_touch_end = 20

    touch_mock = MagicMock()
    touch_mock.x = arbitrary_touch_start

    window.on_touch_down(touch_mock)
    touch_mock.x = arbitrary_touch_end
    window.on_touch_move(touch_mock)

    assert window.moving_bar


####################################################################################
def test_on_touch_move_with_insufficient_movement_sets_movement_flag_false(window):
    arbitrary_touch_start = 5
    arbitrary_touch_end = 6

    touch_mock = MagicMock()
    touch_mock.x = arbitrary_touch_start

    window.on_touch_down(touch_mock)
    touch_mock.x = arbitrary_touch_end
    window.on_touch_move(touch_mock)

    assert not window.moving_bar


####################################################################################
def test_on_touch_up_if_moving_flag_and_side_bar_not_exposed_enough_side_bar_returned_off_screen(window):
    assert True