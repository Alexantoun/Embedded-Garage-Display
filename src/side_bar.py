import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import src.constants as const
from src.debug_logger import DebugLogger as log

DEBUG_CALLING_CLASS = 'side_bar'

from kivy.app import App

class SideBar(BoxLayout):
    def __init__(self, **kwargs):
        log.write_debug(DEBUG_CALLING_CLASS, 'initializing sidebar')
        super(SideBar, self).__init__(**kwargs)
        self.orientation = 'vertical'

        with self.canvas.before:
            Color(*const.SIDEBAR_BUTTON_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_car_button = SideBar.create_button('Add\nCar')
        self.add_car_button.bind(on_release=self.add_car_button_clicked)

        self.car_details_button = SideBar.create_button('Car\nDetails')
        self.car_details_button.bind(on_release=self.car_details_button_clicked)

        self.delete_car_button = SideBar.create_button('Delete\nCar')
        self.delete_car_button.bind(on_release=self.delete_car_button_clicked)

        self.settings_button = SideBar.create_button('Settings')
        self.settings_button.bind(on_release=self.settings_button_clicked)

        self.add_widget(self.add_car_button)
        self.add_widget(self.car_details_button)
        self.add_widget(self.delete_car_button)
        self.add_widget(self.settings_button)

    def _update_rect(self, *unused):
        self.rect.pos = self.pos
        self.rect.size = self.size

    @staticmethod
    def create_button(text) -> Button:
        button = Button(text=text,
                        size_hint=(1, 1),
                        halign='center',
                        valign='middle',
                        background_color=const.SIDEBAR_BUTTON_COLOR,
                        font_name='freedom_font')
        button.font_size = 18
        return button

    @staticmethod
    def settings_button_clicked(unused):
        log.write_debug(DEBUG_CALLING_CLASS, 'Settings clicked')
        print('settings clicked')
        app = App.get_running_app()
        app.stop()


    @staticmethod
    def delete_car_button_clicked(unused):
        log.write_debug(DEBUG_CALLING_CLASS, 'Delete clicked')
        print('delete car clicked')

    @staticmethod
    def car_details_button_clicked(unused):
        log.write_debug(DEBUG_CALLING_CLASS, 'Details clicked')
        print('car details clicked')

    @staticmethod
    def add_car_button_clicked(unused):
        log.write_debug(DEBUG_CALLING_CLASS, 'Add clicked')
        print('add car clicked')
