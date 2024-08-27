from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from datetime import time
import src.enums as enums
import src.colors as colors

COLOR_SELECTION = [
    # colors.LIGHTER_DAY_WIDGET_COLOR,
    # colors.DARKER_DAY_WIDGET_COLOR
    (.4, .3, .3),
    (.7, .4, .5)
]

class BlankCalendarDay(BoxLayout):
    def __init__(self, **kwargs):
        super(BlankCalendarDay, self).__init__(**kwargs)
        # Make this a blank square.
        # Figure out how to make square blank


class CalendarDay(BoxLayout):
    def __init__(self, day_number: int, **kwargs):
        super(CalendarDay, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.event_list: [(time, enums.CarServiceType, str)] = None

        with self.canvas.before:
            Color(*COLOR_SELECTION[day_number % 2])
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.day_index_label = Label(text=str(day_number))
        self.day_index_label.valign = 'top'
        self.day_index_label.size_hint = (.25, .5)
        self.add_widget(self.day_index_label)

        self.event_text = Label()
        self.add_widget(self.event_text)

    def on_touch_down(self, touch):  # Overrides Widget.on_touch_down
        if self.collide_point(*touch.pos):
            print(f'{self.day_index_label.text} clicked')

    def on_touch_move(self, touch):
        pass

    def update_event_list(self, events: [(time, enums.CarServiceType, str)]):
        #use icons
        pass

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

