from kivy.uix.boxlayout import BoxLayout
import datetime

from src.month_scroll_bar import MonthScroll

#Temp imports
from kivy.uix.label import Label


class GarageAppMainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(GarageAppMainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.date_today = datetime.date.today()
        print(self.date_today)
        month = self.date_today.month

        self.add_widget(MonthScroll(month, size_hint=(1, .075)))
        self.add_widget(Label(text='delete me'))
