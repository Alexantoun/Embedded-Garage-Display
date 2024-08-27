from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import src.colors as colors
from src.lib.colored_label_widget import ColoredLabel

MONTH_IN_YEAR = 12
MONTH_TO_STRING = [
    'JANUARY',
    'FEBRUARY',
    'MARCH',
    'APRIL',
    'MAY',
    'JUNE',
    'JULY',
    'AUGUST',
    'SEPTEMBER',
    'OCTOBER',
    'NOVEMBER',
    'DECEMBER'
]


class MonthScroll(BoxLayout):
    def __init__(self, current_month: int, **kwargs):
        super(MonthScroll, self).__init__(**kwargs)
        self.current_month = current_month - 1
        print(f'\treceived month: {MONTH_TO_STRING[self.current_month]}')

        self.orientation = 'horizontal'
        self.back_button, self.current_label, self.next_button = self.make_widgets()
        self.add_widget(self.back_button)
        self.add_widget(self.current_label)
        self.add_widget(self.next_button)

    def make_widgets(self):
        back = Button(text=MONTH_TO_STRING[self.current_month - 1], background_color=colors.SCROLL_BUTTON_BG_COLOR)
        forward = Button(text=MONTH_TO_STRING[self.current_month + 1], background_color=colors.SCROLL_BUTTON_BG_COLOR)
        current = ColoredLabel(text=MONTH_TO_STRING[self.current_month], bg_color=colors.CURRENT_MONTH_BG_COLOR)

        back.bind(on_release=self.go_to_previous_month)
        forward.bind(on_release=self.go_to_next_month)

        return back, current, forward

    def go_to_previous_month(self, unused):
        print('\tGoing back a month')
        self.current_month = (self.current_month - 1) % MONTH_IN_YEAR
        self.update_text()

    def go_to_next_month(self, unused):
        print('\tGoing forward a month')
        self.current_month = (self.current_month + 1) % MONTH_IN_YEAR
        self.update_text()

    def update_text(self):
        self.back_button.text = MONTH_TO_STRING[(self.current_month - 1) % MONTH_IN_YEAR]
        self.current_label.text = MONTH_TO_STRING[self.current_month]
        self.next_button.text = MONTH_TO_STRING[(self.current_month + 1) % MONTH_IN_YEAR]




