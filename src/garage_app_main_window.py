from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

import datetime

from src.month_scroll_bar import MonthScroll
from src.calendar_widget import CalendarWidget
from src.side_bar import SideBar

#Temp imports
from kivy.uix.label import Label

SIDEBAR_INITIAL_POSITION_x = -100
SIDEBAR_ACTIVE_POSITION_x = -1
# class GarageAppMainWindow(BoxLayout):
#     def __init__(self, **kwargs):
#         super(GarageAppMainWindow, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.date_today = datetime.date.today()
#         print(self.date_today)
#         month = self.date_today.month
#
#         self.add_widget(MonthScroll(month, size_hint=(1, .085)))
#         self.add_widget(CalendarWidget())

class GarageAppMainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(GarageAppMainWindow, self).__init__(**kwargs)
        calendar_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.sidebar_layout = BoxLayout()
        self.setup_sidebar()

        self.add_widget(calendar_layout)
        self.add_widget(self.sidebar_layout)
        # calendar_layout.size = self.size

        # self.orientation = 'vertical'
        self.date_today = datetime.date.today()
        print(self.date_today)
        month = self.date_today.month

        calendar_layout.add_widget(MonthScroll(month, size_hint=(1, .085)))
        calendar_layout.add_widget(CalendarWidget())

        self.bind(on_touch_down=self.on_clicked)

    def on_clicked(self, unused, alsoUnused):
        if self.sidebar_layout.x == SIDEBAR_INITIAL_POSITION_x:
            self.sidebar_layout.x = SIDEBAR_ACTIVE_POSITION_x
        elif self.sidebar_layout.x == SIDEBAR_ACTIVE_POSITION_x:
            self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x

        print('clicked')
    def setup_sidebar(self):
        self.sidebar_layout = SideBar(size_hint=(0.125, 1))
        self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x
        self.sidebar_layout.y = -1
        self.sidebar_layout.active = False