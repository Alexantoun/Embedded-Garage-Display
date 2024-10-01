import pytest
from unittest.mock import MagicMock, patch
from kivy.core.text import LabelBase
import src.month_scroll_bar

ARBITRARY_TEST_MONTH = 6  #June


@pytest.fixture
def mock_kivy(mocker):
    mocker.patch('src.month_scroll_bar.BoxLayout.add_widget')
    return mocker


@pytest.fixture
def scroll_bar(mock_kivy):
    LabelBase.register(name='freedom_font', fn_regular='../assets/font/Freedom-10eM.ttf')
    return src.month_scroll_bar.MonthScroll(ARBITRARY_TEST_MONTH)


####################################################################################
def test_on_init_scroll_bar_created_with_two_buttons_and_text_label_with_current_month(scroll_bar):
    assert scroll_bar.back_button is not None
    assert scroll_bar.current_month is not None
    assert scroll_bar.next_button is not None

    assert scroll_bar.back_button.text == 'May'
    assert scroll_bar.current_label.text == 'June'
    assert scroll_bar.next_button.text == 'July'


####################################################################################
def test_on_previous_month_scroll_button_and_label_text_updated_accurately(scroll_bar):
    scroll_bar.go_to_previous_month(None)
    assert scroll_bar.back_button.text == 'April'
    assert scroll_bar.current_label.text == 'May'
    assert scroll_bar.next_button.text == 'June'

    scroll_bar.go_to_previous_month(None)
    assert scroll_bar.back_button.text == 'March'
    assert scroll_bar.current_label.text == 'April'
    assert scroll_bar.next_button.text == 'May'


####################################################################################
def test_on_next_month_scroll_button_and_label_text_updated_accurately(scroll_bar):
    scroll_bar.go_to_next_month(None)
    assert scroll_bar.back_button.text == 'June'
    assert scroll_bar.current_label.text == 'July'
    assert scroll_bar.next_button.text == 'August'

    scroll_bar.go_to_next_month(None)
    assert scroll_bar.back_button.text == 'July'
    assert scroll_bar.current_label.text == 'August'
    assert scroll_bar.next_button.text == 'September'


####################################################################################
def test_scrolling_past_december_shows_january_as_current_month(scroll_bar):
    for month in range(0, 6):
        scroll_bar.go_to_next_month(None)

    assert scroll_bar.current_label.text == 'December'
    assert scroll_bar.next_button.text == 'January'

    scroll_bar.go_to_next_month(None)
    assert scroll_bar.back_button.text == 'December'
    assert scroll_bar.current_label.text == 'January'
    assert scroll_bar.next_button.text == 'February'


####################################################################################
def test_scrolling_before_january_shows_december_as_current_month(scroll_bar):
    for month in range(0, 5):
        scroll_bar.go_to_previous_month(None)

    assert scroll_bar.back_button.text == 'December'
    assert scroll_bar.current_label.text == 'January'

    scroll_bar.go_to_previous_month(None)
    assert scroll_bar.back_button.text == 'November'
    assert scroll_bar.current_label.text == 'December'
    assert scroll_bar.next_button.text == 'January'


####################################################################################
def test_on_back_button_pushed_selected_month_back_signal_evoked(scroll_bar):
    selected_month_back_handler = MagicMock()
    scroll_bar.bind(on_selected_month_back=selected_month_back_handler)

    scroll_bar.back_button.trigger_action(0)
    selected_month_back_handler.assert_called_once()


####################################################################################
def test_on_forward_button_pushed_selected_month_fore_evoked(scroll_bar):
    selected_month_fore_handler = MagicMock()
    scroll_bar.bind(on_selected_month_fore=selected_month_fore_handler)

    scroll_bar.next_button.trigger_action(0)
    selected_month_fore_handler.assert_called_once()
