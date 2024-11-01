from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.clock import Clock
import datetime

import src.constants as const
from src.debug_logger import DebugLogger as log
from src.lib.calendar_widget import CalendarWidget
from src.month_scroll_bar import MonthScroll
from src.side_bar import SideBar

SIDEBAR_INITIAL_POSITION_x = -150
SIDEBAR_ACTIVE_POSITION_x = 0
MINIMUM_TOUCH_MOVEMENT = 5
MOVEMENT_DELTA_DIVISOR = 25

DEBUG_CALLING_CLASS = 'garage_app_main_window'


class GarageAppMainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(GarageAppMainWindow, self).__init__(**kwargs)
        self.selected_date = datetime.date.today()
        month = self.selected_date.month
        year = self.selected_date.year
        log.write_debug(DEBUG_CALLING_CLASS, message=f'Starting app. starting date = {self.selected_date}')

        self.calendar_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        self.sidebar_layout = SideBar(size_hint=(0.125, 1))
        self.ids['side_bar'] = self.sidebar_layout
        self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x
        self.sidebar_active = False

        self.add_widget(self.calendar_layout)
        self.add_widget(self.sidebar_layout)
        month_scroll_bar = MonthScroll(month, size_hint=(1, .085))
        self.ids['month_scroll'] = month_scroll_bar
        month_scroll_bar.bind(on_selected_month_fore=self.handle_forward_scroll)
        month_scroll_bar.bind(on_selected_month_back=self.handle_backward_scroll)

        self.calendar_layout.add_widget(month_scroll_bar)

        self.calendar_widget = CalendarWidget(month=month, year=year)
        self.ids['calendar_widget'] = self.calendar_widget
        self.calendar_layout.add_widget(self.calendar_widget)

        self.touch_start_x = None
        self.moving_bar = False

        self.touch_up_debounce: bool = False
        self.touch_down_debounce: bool = False

####################################################################################
    def on_touch_down(self, touch):
        if not self.touch_down_debounce:
            self.touch_down_debounce = True
            Clock.schedule_once(lambda dt: self.on_touch_down_debounce_timer(), const.TOUCH_DEBOUNCE_TIMEOUT)

            log.write_debug(DEBUG_CALLING_CLASS, message=f'touch_down')
            self.touch_start_x = touch.x
            if self.sidebar_active:
                self.sidebar_layout.on_touch_down(touch)
                return True  # Returning true means that the touch event has been completely handled by this widget
                # Returning false would mean that the touch event wasn't completely handled, and
                # allows propagation of the event to child widgets

            return super(GarageAppMainWindow, self).on_touch_down(
                touch)  # This means to let the base class handle what to do with event
        else:
            return True

####################################################################################
    def on_touch_move(self, touch):
        delta_x = touch.x - self.touch_start_x
        self.moving_bar = abs(delta_x) > MINIMUM_TOUCH_MOVEMENT
        if self.moving_bar:
            new_x_position = self.sidebar_layout.x + (delta_x / MOVEMENT_DELTA_DIVISOR)
            self.sidebar_layout.x = min(new_x_position, SIDEBAR_ACTIVE_POSITION_x)
        return True

####################################################################################
    def on_touch_up(self, touch):
        if not self.touch_up_debounce:
            self.touch_up_debounce = True
            Clock.schedule_once(lambda dt: self.on_touch_up_debounce_timer(), const.TOUCH_DEBOUNCE_TIMEOUT)

            log.write_debug(DEBUG_CALLING_CLASS, message=f'touch_up')
            if self.moving_bar:
                if self.sidebar_layout.x < -50:  # if sidebar not exposed enough, hide it again
                    log.write_debug(DEBUG_CALLING_CLASS,
                                    message=f'Re-hiding side bar, pos_x={self.sidebar_layout.x}')
                    self.sidebar_layout.x = SIDEBAR_INITIAL_POSITION_x

                else:
                    log.write_debug(DEBUG_CALLING_CLASS,
                                    message=f'Fully exposing side bar, pos_x={self.sidebar_layout.x}')
                    self.sidebar_layout.x = SIDEBAR_ACTIVE_POSITION_x
                    self.sidebar_active = True

                self.moving_bar = False
                return True

            elif self.sidebar_active and not self.sidebar_layout.collide_point(*touch.pos):
                self.sidebar_active = False
                animation = Animation(x=SIDEBAR_INITIAL_POSITION_x, duration=0.15)
                animation.start(self.sidebar_layout)
                log.write_debug(DEBUG_CALLING_CLASS, message='Re-hiding side bar due to click away')

                return True

            elif not self.sidebar_active:
                return super(GarageAppMainWindow, self).on_touch_up(touch)
        else:
            return True

####################################################################################
    def handle_forward_scroll(self, unused):
        if self.selected_date.month == 12:
            self.selected_date = datetime.datetime(year=self.selected_date.year + 1, month=1, day=1)
        else:
            self.selected_date = datetime.datetime(year=self.selected_date.year, month=self.selected_date.month + 1,
                                                   day=1)

        self.calendar_layout.remove_widget(self.calendar_widget)
        self.calendar_widget = CalendarWidget(self.selected_date.month, self.selected_date.year)
        self.calendar_layout.add_widget(self.calendar_widget)
        log.write_debug(DEBUG_CALLING_CLASS,
                        message=f'change month to: {const.MONTH_TO_STRING[self.selected_date.month - 1]}, {self.selected_date.year}')

####################################################################################
    def handle_backward_scroll(self, unused):
        if self.selected_date.month == 1:
            self.selected_date = datetime.datetime(year=self.selected_date.year - 1, month=12, day=1)
        else:
            self.selected_date = datetime.datetime(year=self.selected_date.year, month=self.selected_date.month - 1,
                                                   day=1)

        self.calendar_layout.remove_widget(self.calendar_widget)
        self.calendar_widget = CalendarWidget(self.selected_date.month, self.selected_date.year)
        self.calendar_layout.add_widget(self.calendar_widget)
        log.write_debug(DEBUG_CALLING_CLASS,
                        message=f'change month to: {const.MONTH_TO_STRING[self.selected_date.month - 1]}, {self.selected_date.year}')

####################################################################################
    def on_touch_up_debounce_timer(self):
        self.touch_up_debounce = False

####################################################################################
    def on_touch_down_debounce_timer(self):
        self.touch_down_debounce = False
