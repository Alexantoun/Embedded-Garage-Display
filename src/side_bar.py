from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import src.colors as colors


class SideBar(BoxLayout):
    def __init__(self, **kwargs):
        print('Set background color such that user cannot see inbetween the buttons on the side bar')
        super(SideBar, self).__init__(**kwargs)
        self.orientation = 'vertical'

        #create buttons
        self.add_car_button = Button(text='Add\nCar',
                                     size_hint=(1,1),
                                     halign='center',
                                     valign='middle',
                                     background_color=colors.SIDEBAR_BUTTON_COLOR,
                                     font_name='freedom_font')
        self.add_car_button.text_size = self.add_car_button.size
        self.add_car_button.font_size = 18
        self.add_car_button.bind(on_release=self.add_car_button_clicked)

        self.car_details_button = Button(text='Car\nDetails',
                                         size_hint=(1,1),
                                         halign='center', valign='middle',
                                         background_color=colors.SIDEBAR_BUTTON_COLOR,
                                         font_name='freedom_font')
        self.car_details_button.text_size = self.car_details_button.size
        self.car_details_button.font_size = 18
        self.car_details_button.bind(on_release=self.car_details_button_clicked)

        self.delete_car_button = Button(text='Delete\nCar',
                                        size_hint=(1, 1),
                                        halign='center',
                                        valign='middle',
                                        background_color=colors.SIDEBAR_BUTTON_COLOR,
                                        font_name='freedom_font')
        self.delete_car_button.text_size = self.delete_car_button.size
        self.delete_car_button.font_size = 18
        self.delete_car_button.bind(on_release=self.delete_car_button_clicked)

        self.settings_button = Button(text='Settings',
                                      size_hint=(1, 1),
                                      halign='center',
                                      valign='middle',
                                      background_color=colors.SIDEBAR_BUTTON_COLOR,
                                      font_name='freedom_font')
        self.settings_button.text_size = self.settings_button.size
        self.settings_button.font_size = 18
        self.settings_button.bind(on_release=self.settings_button_clicked)
        self.spacing = -3

        self.add_widget(self.add_car_button)
        self.add_widget(self.car_details_button)
        self.add_widget(self.delete_car_button)
        self.add_widget(self.settings_button)

    @staticmethod
    def settings_button_clicked(unused):
        print('settings clicked')

    @staticmethod
    def delete_car_button_clicked(unused):
        print('delete car clicked')

    @staticmethod
    def car_details_button_clicked(unused):
        print('car details clicked')
    @staticmethod
    def add_car_button_clicked(unused):
        print('add car clicked')