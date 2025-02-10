from calendar import monthrange
from kivy.uix.gridlayout import GridLayout

import src.constants as const
from src.debug_logger import DebugLogger as Log
from src.lib.colored_label_widget import ColoredLabel
from src.lib.day_widget import CalendarDay

DEBUG_CALLING_CLASS = 'calendar_widget'


class CalendarWidget(GridLayout):
    def __init__(self, today=0, month=0, year=0, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, f'initializing calendar widget, month={month}, year={year}')
        super(CalendarWidget, self).__init__(**kwargs)
        self.cols = const.DAYS_IN_WEEK
        starting_day, num_days = monthrange(year=year, month=month)
        self.spacing = .5

        Log.write_debug(DEBUG_CALLING_CLASS, f'Starting day={const.DAY_TO_STRING[starting_day]}, number of days={num_days}')

        for day in const.DAY_TO_STRING:
            colored_label = ColoredLabel(bg_color=const.DAY_LABEL_BG_COLOR, text=day)
            self.add_widget(colored_label)
            colored_label.size_hint = (1, 0.25)

        for preamble_day_spaces in range(0, starting_day):
            colored_label = ColoredLabel(bg_color=const.NON_DAY_WIDGET_COLOR, text='')
            self.add_widget(colored_label)

        color_index = 0
        day: int
        for day in range(1, num_days + 1):
            day_widget = CalendarDay(day_number=day)
            self.add_widget(day_widget)
            color_index = (color_index + 1) % 2
            if day == today:
                day_widget.draw_highlight_square()
                day_widget.selected = True

        trailing_day_spaces = (starting_day + num_days) % 7
        if trailing_day_spaces > 0:
            for day in range(trailing_day_spaces, 7):
                colored_label = ColoredLabel(bg_color=const.NON_DAY_WIDGET_COLOR, text='')
                self.add_widget(colored_label)

