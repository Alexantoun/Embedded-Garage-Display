
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from src.lib.colored_label import ColoredLabel
import src.colors as colors

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
            coloredLabel.size_hint = (1, 0.1)


        self.add_widget(ColoredLabel(bg_color=colors.SCROLL_BUTTON_BG_COLOR, text='nil'))



class CalendarDayTitleWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CalendarDayTitleWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        for day in DAY_TO_STRING:
            self.add_widget(ColoredLabel(bg_color=colors.DAY_LABEL_BG_COLOR, text=day))


