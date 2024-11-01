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
    LabelBase.register(name='pricedown_bl', fn_regular='../assets/font/Freedom-10eM.ttf')
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
def test_on_touch_move_with_sufficient_movement_sets_movement_flag_true(window):
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
    arbitrary_touch_start = 5
    arbitrary_touch_end = 20
    touch_mock = MagicMock()

    touch_mock.x = arbitrary_touch_start
    window.on_touch_down(touch_mock)

    touch_mock.x = arbitrary_touch_end
    window.on_touch_move(touch_mock)
    assert window.sidebar_layout.x > src.garage_app_main_window.SIDEBAR_INITIAL_POSITION_x

    window.on_touch_up(touch_mock)
    assert window.sidebar_layout.x == src.garage_app_main_window.SIDEBAR_INITIAL_POSITION_x


####################################################################################
def test_on_touch_up_if_moving_flag_and_side_bar_sufficiently_exposed_then_side_bar_fully_exposed(window):
    arbitrary_touch_start = 5
    arbitrary_touch_end = 200
    touch_mock = MagicMock()

    touch_mock.x = arbitrary_touch_start
    window.on_touch_down(touch_mock)

    touch_mock.x = arbitrary_touch_end
    for movement in range(0, 8):
        touch_mock.x += 50
        window.on_touch_move(touch_mock)

    assert window.sidebar_layout.x > src.garage_app_main_window.SIDEBAR_INITIAL_POSITION_x

    window.on_touch_up(touch_mock)
    assert window.sidebar_layout.x == src.garage_app_main_window.SIDEBAR_ACTIVE_POSITION_x


####################################################################################
def test_on_touch_up_and_touch_not_on_side_bar_then_side_bar_hidden(window):
    window.sidebar_layout.x = src.garage_app_main_window.SIDEBAR_ACTIVE_POSITION_x
    window.sidebar_active = True
    window.moving_bar = False
    non_colliding_touch_pos = (150, 300)

    touch_mock = MagicMock()
    touch_mock.pos = non_colliding_touch_pos

    with patch('src.garage_app_main_window.Animation') as animation:
        start_mock = MagicMock()
        animation.return_value.start = start_mock
        window.on_touch_up(touch_mock)
        start_mock.assert_called_once_with(window.sidebar_layout)


####################################################################################
def test_on_touch_down_debounce_prevents_multiple_calls_in_short_period_of_time(window):
    assert window.touch_down_debounce is False

    touch_mock = MagicMock()
    touch_mock.pos = (20, 20)

    with patch('src.garage_app_main_window.Clock') as clock_mock:
        clock_mock.schedule_once = MagicMock()
        window.on_touch_down(touch_mock)
        assert window.touch_down_debounce is True

        window.on_touch_down(touch_mock)
        window.on_touch_down(touch_mock)
        window.on_touch_down(touch_mock)

        assert 1 == clock_mock.schedule_once.call_count

        window.on_touch_down_debounce_timer()
        window.on_touch_down(touch_mock)

        assert 2 == clock_mock.schedule_once.call_count


####################################################################################
def test_on_touch_up_debounce_prevents_multiple_calls_in_short_period_of_time(window):
    assert window.touch_up_debounce is False

    touch_mock = MagicMock()
    touch_mock.pos = (20, 20)

    with patch('src.garage_app_main_window.Clock') as clock_mock:
        clock_mock.schedule_once = MagicMock()
        window.on_touch_up(touch_mock)
        assert window.touch_up_debounce is True

        window.on_touch_up(touch_mock)
        window.on_touch_up(touch_mock)

        assert 1 == clock_mock.schedule_once.call_count

        window.on_touch_up_debounce_timer()
        window.on_touch_up(touch_mock)

        assert 2 == clock_mock.schedule_once.call_count


####################################################################################
# To confirm that month(x) + 12 is equal to month(x)
def test_sanity_check_datetime_month_cycles(window):
    MONTHS_IN_YEAR = 12
    window.selected_date = datetime.datetime(year=2024, month=6, day=1)
    for month in range(0, MONTHS_IN_YEAR):
        window.handle_forward_scroll(None)

    assert window.selected_date == datetime.datetime(year=2025, month=6, day=1)

    for month in range(MONTHS_IN_YEAR, 0, -1):
        window.handle_backward_scroll(None)

    assert window.selected_date == datetime.datetime(year=2024, month=6, day=1)


####################################################################################
def test_on_month_scroll_then_calendar_widget_recreated_with_correct_data(window):
    with patch('src.garage_app_main_window.CalendarWidget') as calendar_widget_mock:
        window.selected_date = datetime.datetime(year=2024, month=6, day=1)
        window.handle_forward_scroll(None)
        calendar_widget_mock.assert_called_once_with(7, 2024)
        calendar_widget_mock.reset_mock()

        window.handle_backward_scroll(None)
        calendar_widget_mock.assert_called_once_with(6, 2024)

