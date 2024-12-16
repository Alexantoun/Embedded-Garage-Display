import src.constants as const
from src.database import DatabaseManager
from src.debug_logger import DebugLogger as Log
from src.lib.input_field import InputField
from src.lib.list_wdget import ListWidget

from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import threading

DEBUG_CALLING_CLASS = "AddCarPage"

class AddCarPage(Popup):
    def __init__(self, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, message="Creating AddCar popup page")
        super(AddCarPage, self).__init__(**kwargs)
        self.setup_title()
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {'top': 1}

        layout = BoxLayout(orientation='vertical')
        self.list_widget = AddCarPage.create_list_widget()
        layout.add_widget(self.list_widget)
        layout.add_widget(self.create_button_layout())

        self.add_widget(layout)
        self.close_touch_debounce = False

####################################################################################
    def create_button_layout(self):
        layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        layout.padding = [0, 0, 0, 0]

        cancel_button = Button(text='Cancel', size_hint_y=1, font_size=24, font_name='pricedown_bl')
        cancel_button.background_color = const.SCROLL_BUTTON_BG_COLOR
        cancel_button.bind(on_press=self.on_cancel_pressed)
        layout.add_widget(cancel_button)

        add_button = Button(text='Add car', size_hint_y=1, font_size=24, font_name='pricedown_bl')
        add_button.background_color = const.SCROLL_BUTTON_BG_COLOR
        add_button.bind(on_press=self.on_add_car_pressed)
        layout.add_widget(add_button)

        return layout

####################################################################################
    def setup_title(self):
        self.title = "Enter Car Details"
        self.title_font = 'pricedown_bl'
        self.title_size = 22
        self.title_align = 'center'

####################################################################################
    def on_cancel_pressed(self, unused):
        if not self.close_touch_debounce:
            self.close_touch_debounce = True
            Clock.schedule_once(lambda dt: self.on_touch_debounce_timer(), const.TOUCH_DEBOUNCE_TIMEOUT)
            Log.write_debug(DEBUG_CALLING_CLASS, message="cancel clicked")

####################################################################################
    def on_add_car_pressed(self, unused):
        if not self.close_touch_debounce:
            self.close_touch_debounce = True
            Clock.schedule_once(lambda dt: self.on_touch_debounce_timer(), const.TOUCH_DEBOUNCE_TIMEOUT)
            Log.write_debug(DEBUG_CALLING_CLASS, message="ok clicked")
            save_thread = threading.Thread(target=DatabaseManager.add_car_data, args=(self.list_widget,))
            save_thread.start()

####################################################################################
    def on_touch_debounce_timer(self):
        self.close_touch_debounce = False
        self.dismiss()

####################################################################################
    @staticmethod
    def create_list_widget() -> ListWidget:
        list_widget = ListWidget(called_from='AddCarPage')

        car_make_field = InputField(hint_text="Make", allow_numerical=False)
        list_widget.add_list_widget_item(car_make_field)
        list_widget.ids['make'] = car_make_field

        car_model_field = InputField(hint_text="Model")
        list_widget.add_list_widget_item(car_model_field)
        list_widget.ids['model'] = car_model_field

        car_date_field = InputField(hint_text="Year", allow_alphabetical=False)
        list_widget.add_list_widget_item(car_date_field)
        list_widget.ids['date'] = car_date_field

        car_mileage_field = InputField(hint_text="Mileage", allow_alphabetical=False)
        list_widget.add_list_widget_item(car_mileage_field)
        list_widget.ids['mileage'] = car_mileage_field

        car_recent_oil_change = InputField(hint_text="Miles @ most recent oil change", allow_alphabetical=False)
        list_widget.add_list_widget_item(car_recent_oil_change)
        list_widget.ids['oil_change'] = car_recent_oil_change

        car_oil_change_frequency = InputField(hint_text="Miles between oil changes", allow_alphabetical=False)
        list_widget.add_list_widget_item(car_oil_change_frequency)
        list_widget.ids['oil_freq'] = car_oil_change_frequency

        car_nickname_field = InputField(hint_text="Nickname for car")
        list_widget.add_list_widget_item(car_nickname_field)
        list_widget.ids['nickname'] = car_nickname_field

        return list_widget
