from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.label import Label

from datetime import time

import src.constants as const
from src.debug_logger import DebugLogger as Log
import src.enums as enums

DEBUG_CALLING_CLASS = 'day_widget'

COLOR_SELECTION = [
    const.LIGHTER_DAY_WIDGET_COLOR,
    const.DARKER_DAY_WIDGET_COLOR
]


class CalendarDay(BoxLayout):
    def __init__(self, day_number: int, **kwargs):
        super(CalendarDay, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.event_list: [(time, enums.CarServiceType, str)] = None
        self.selected: bool = False
        self.border: Line = None

        with self.canvas.before:
            Color(*COLOR_SELECTION[day_number % 2])
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.day_index_label = Label(text=str(day_number), color=(0.1, 0, 0.05), valign='top', size_hint=(0.25, .5))
        self.add_widget(self.day_index_label)

        self.event_text = Label()
        self.add_widget(self.event_text)

    def on_touch_up(self, touch):  # Overrides Widget.on_touch_down
        if self.collide_point(*touch.pos):
            if not self.selected:
                self.draw_highlight_square()
                self.selected = True
                Log.write_debug(DEBUG_CALLING_CLASS, f'Day {self.day_index_label.text} checked')

        elif self.selected:
            self.remove_highlight_square()
            self.selected = False

    def remove_highlight_square(self):
        self.canvas.after.remove(self.border)
        self.border = None

    def draw_highlight_square(self):
        with self.canvas.after:
            Color(*const.SIDEBAR_BUTTON_COLOR)
            self.border = Line(rectangle=(self.x, self.y + 1, self.width - 2, self.height - 2), width=2)

    def update_event_list(self, events: [(time, enums.CarServiceType, str)]):
        #use icons
        pass

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        if self.selected:
            self._update_border()

    def _update_border(self):
        self.border.rectangle = (self.x, self.y, self.width, self.height)
