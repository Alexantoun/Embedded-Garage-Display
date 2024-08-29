from kivy.uix.gridlayout import GridLayout
from src.lib.colored_label_widget import ColoredLabel
import src.colors as colors
from src.lib.calendar_day_widget import CalendarDay

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

# To get the number of days in a month and the day of the week that the first of the month starts on, you can use the calendar and datetime modules in Python.
# Here's how you can do it:
# Get the Number of Days in a Month:
#     Use calendar.monthrange(year, month) to get a tuple where the first element
#     is the weekday of the first day of the month (0 = Monday, 6 = Sunday),
#     and the second element is the number of days in the month.
# Get the Day of the Week for the First of the Month:
#     The first element of the tuple returned by calendar.monthrange(year, month)
#     gives you the day of the week for the first of the month.

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
