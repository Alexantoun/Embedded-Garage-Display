from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import src.constants as const


class MonthScroll(BoxLayout):
    def __init__(self, current_month: int, **kwargs):
        super(MonthScroll, self).__init__(**kwargs)
        self.current_month = current_month - 1
        print(f'\treceived month: {const.MONTH_TO_STRING[self.current_month]}')

        self.orientation = 'horizontal'
        self.back_button, self.current_label, self.next_button = self.make_widgets()
        self.add_widget(self.back_button)
        self.add_widget(self.current_label)
        self.add_widget(self.next_button)

    def make_widgets(self):
        back = Button(text=const.MONTH_TO_STRING[self.current_month - 1])
        forward = Button(text=const.MONTH_TO_STRING[self.current_month + 1])
        current = Label(text=const.MONTH_TO_STRING[self.current_month])

        back.bind(on_release=self.go_to_previous_month)
        forward.bind(on_release=self.go_to_next_month)

        return back, current, forward

    def go_to_previous_month(self, unused):
        print('\t Going back a month')
        self.current_month = (self.current_month - 1) % const.MONTHS
        self.update_text()

    def go_to_next_month(self, unused):
        print('\t Going forward a month')
        self.current_month = (self.current_month + 1) % const.MONTHS
        self.update_text()

    def update_text(self):
        self.back_button.text = const.MONTH_TO_STRING[(self.current_month - 1) % const.MONTHS]
        self.current_label.text = const.MONTH_TO_STRING[self.current_month]
        self.next_button.text = const.MONTH_TO_STRING[(self.current_month + 1) % const.MONTHS]




