import datetime
import src.enums as enums

from kivy.uix.gridlayout import GridLayout
from src.lib.colored_label_widget import ColoredLabel
import src.colors as colors
from src.calendar_day_widget import CalendarDay

from datetime import time
DAYS_IN_WEEK = 7
DAY_TO_STRING = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


class CalendarWidget(GridLayout):
    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)
        self.cols = DAYS_IN_WEEK
        coloredLabel: ColoredLabel
        for day in DAY_TO_STRING:
            coloredLabel = ColoredLabel(bg_color=colors.DAY_LABEL_BG_COLOR, text=day)
            self.add_widget(coloredLabel)
            coloredLabel.size_hint = (1, 0.25)

        color_index = 0
        for i in range(1, 32):
            self.add_widget(CalendarDay(day_number=i))
            color_index = (color_index + 1) % 2
