from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import src.constants as const
from src.debug_logger import DebugLogger as Log
from src.lib.colored_label_widget import ColoredLabel

DEBUG_CALLING_CLASS = 'month_scroll_bar'


class MonthScroll(BoxLayout):
    def __init__(self, current_month: int, **kwargs):
        super(MonthScroll, self).__init__(**kwargs)
        self.current_month = current_month - 1
        Log.write_debug(DEBUG_CALLING_CLASS, f'Creating month scroll bar starting at '
                                             f'month:{const.MONTH_TO_STRING[self.current_month]}')

        self.orientation = 'horizontal'
        self.back_button, self.current_label, self.next_button = self.make_widgets()
        self.add_widget(self.back_button)
        self.add_widget(self.current_label)
        self.add_widget(self.next_button)

        self.register_event_type('on_selected_month_back')
        self.register_event_type('on_selected_month_fore')

    def make_widgets(self):
        back = Button(text=const.MONTH_TO_STRING[self.current_month - 1], background_color=const.SCROLL_BUTTON_BG_COLOR,
                      font_name='freedom_font')
        back.font_size = 18
        forward = Button(text=const.MONTH_TO_STRING[self.current_month + 1], background_color=const.SCROLL_BUTTON_BG_COLOR,
                         font_name='freedom_font')
        current = ColoredLabel(text=const.MONTH_TO_STRING[self.current_month], bg_color=const.CURRENT_MONTH_BG_COLOR,
                               font_name='freedom_font')

        back.bind(on_release=self.go_to_previous_month)
        forward.bind(on_release=self.go_to_next_month)

        return back, current, forward

    def go_to_previous_month(self, unused):
        self.current_month = (self.current_month - 1) % const.MONTHS_IN_YEAR
        Log.write_debug(DEBUG_CALLING_CLASS, f'Going back to month{const.MONTH_TO_STRING[self.current_month]}')
        self.dispatch('on_selected_month_back')
        self.update_text()

    def go_to_next_month(self, unused):
        self.current_month = (self.current_month + 1) % const.MONTHS_IN_YEAR
        Log.write_debug(DEBUG_CALLING_CLASS, f'Going forward to month{const.MONTH_TO_STRING[self.current_month]}')
        self.dispatch('on_selected_month_fore')
        self.update_text()

    def update_text(self):
        self.back_button.text = const.MONTH_TO_STRING[(self.current_month - 1) % const.MONTHS_IN_YEAR]
        self.current_label.text = const.MONTH_TO_STRING[self.current_month]
        self.next_button.text = const.MONTH_TO_STRING[(self.current_month + 1) % const.MONTHS_IN_YEAR]

    def on_selected_month_fore(self):
        pass

    def on_selected_month_back(self):
        pass
