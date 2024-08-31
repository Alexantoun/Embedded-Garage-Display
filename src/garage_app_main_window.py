from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

import datetime

from src.month_scroll_bar import MonthScroll
from src.lib.calendar_widget import CalendarWidget
from src.side_bar import SideBar


SIDEBAR_INITIAL_POSITION_x = -100
SIDEBAR_ACTIVE_POSITION_x = -1

MONTH_TO_STRING = [  # for debugging
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

class GarageAppMainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(GarageAppMainWindow, self).__init__(**kwargs)
        self.calendar_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.sidebar_layout = SideBar()
        self.sidebar_active: bool
        self.setup_sidebar()

        self.add_widget(self.calendar_layout)
        self.add_widget(self.sidebar_layout)

        self.selected_date = datetime.date.today()
        print(self.selected_date)
        month = self.selected_date.month
        year = self.selected_date.year

        month_scroll_bar = MonthScroll(month, size_hint=(1, .085))
        month_scroll_bar.bind(on_selected_month_fore=self.handle_forward_scroll)
        month_scroll_bar.bind(on_selected_month_back=self.handle_backward_scroll)

        self.calendar_layout.add_widget(month_scroll_bar)
        self.calendar_widget = CalendarWidget(month=month, year=year)
        self.calendar_layout.add_widget(self.calendar_widget)

        self.touch_start_x = None
        self.moving_bar = False

    def on_touch_down(self, touch):
        self.touch_start_x = touch.x
        if self.sidebar_active:
            self.sidebar_layout.on_touch_down(touch)
            return True  # Returning true means that the touch event has been completely handled by this widget
            # Returning false would mean that the touch event wasnt completely handled, and allows propagation of the event to child widgets
        return super(GarageAppMainWindow, self).on_touch_down(touch)  # This means to let the base class handle what to do with event

    def on_touch_move(self, touch):
        delta_x = touch.x - self.touch_start_x
        new_x_position = self.sidebar_layout.x + delta_x
        self.sidebar_layout.x = min(new_x_position, SIDEBAR_ACTIVE_POSITION_x)
        self.moving_bar = abs(delta_x) > 1
        return True

    def on_touch_up(self, touch):
        if self.moving_bar:
            if self.sidebar_layout.x < -25:  # if sidebar not exposed enough, hide it again
                self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x
                print('re-hiding side bar due to not being pulled enough')
            else:
                self.sidebar_layout.x = SIDEBAR_ACTIVE_POSITION_x
                self.sidebar_active = True
                print('fully exposing side bar due to being pulled enough')

            self.moving_bar = False
            return True

        elif self.sidebar_active and not self.sidebar_layout.collide_point(*touch.pos):
            self.sidebar_active = False
            # Have the sidebar 'slide' back to its hidden position
            animation = Animation(x=SIDEBAR_INITIAL_POSITION_x, duration=0.15)
            animation.bind()
            animation.start(self.sidebar_layout)

            return True

        elif not self.sidebar_active:
            return super(GarageAppMainWindow, self).on_touch_up(touch)

    def handle_forward_scroll(self, unused):
        if self.selected_date.month == 12:
            self.selected_date = datetime.datetime(year=self.selected_date.year + 1, month=1, day=1)
        else:
            self.selected_date = datetime.datetime(year=self.selected_date.year, month=self.selected_date.month + 1, day=1)

        self.calendar_layout.remove_widget(self.calendar_widget)
        self.calendar_widget = CalendarWidget(self.selected_date.month, self.selected_date.year)
        self.calendar_layout.add_widget(self.calendar_widget)
        print(f'Date goes on to: {MONTH_TO_STRING[self.selected_date.month - 1]}, {self.selected_date.year}')

    def handle_backward_scroll(self, unused):
        if self.selected_date.month == 1:
            self.selected_date = datetime.datetime(year=self.selected_date.year - 1, month=12, day=1)
        else:
            self.selected_date = datetime.datetime(year=self.selected_date.year, month=self.selected_date.month - 1, day=1)

        self.calendar_layout.remove_widget(self.calendar_widget)
        self.calendar_widget = CalendarWidget(self.selected_date.month, self.selected_date.year)
        self.calendar_layout.add_widget(self.calendar_widget)
        print(f'Date goes back to: {MONTH_TO_STRING[self.selected_date.month - 1]}, {self.selected_date.year}')

    def setup_sidebar(self):
        self.sidebar_layout = SideBar(size_hint=(0.125, 1))
        self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x
        self.sidebar_layout.y = -1
        self.sidebar_active = False
