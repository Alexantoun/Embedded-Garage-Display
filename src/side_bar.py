from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class SideBar(BoxLayout):
    def __init__(self, **kwargs):
        super(SideBar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_car_button = Button(text='Add\nCar', size_hint=(1,1))
        self.car_details_button = Button(text='Car\nDetails', size_hint=(1,1))
        self.delete_car_button = Button(text='delete\nCar', size_hint=(1,1))
        self.settings_button = Button(text='Settings', size_hint=(1,1))
        self.spacing = -10

        self.add_widget(self.add_car_button)
        self.add_widget(self.car_details_button)
        self.add_widget(self.delete_car_button)
        self.add_widget(self.settings_button)

        self.active: bool = False
