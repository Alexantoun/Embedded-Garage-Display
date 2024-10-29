import src.constants as const
from src.debug_logger import DebugLogger as Log
from src.lib.input_field import InputField
from src.lib.list_wdget import ListWidget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


DEBUG_CALLING_CLASS = "AddCarPage"
class AddCarPage(Popup):
    def __init__(self, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, message="Creating AddCar popup page")
        super(AddCarPage, self).__init__(**kwargs)
        self.setup_title()
        self.size_hint = (0.5, 0.6)
        self.pos_hint = {'top': 1}

        layout = BoxLayout(orientation='vertical')
        self.list_widget = self.create_list_widget()
        layout.add_widget(self.list_widget)
        layout.add_widget(self.create_button_layout())

        self.add_widget(layout)

    def create_list_widget(self):
        list_widget = ListWidget(called_from='AddCarPage')
        list_widget.add_list_widget_item(InputField(hint_text="Hello"))
        return list_widget

    def create_button_layout(self):
        layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        layout.padding = [0, 0, 0, 0]

        cancel_button = Button(text='cancel', size_hint_y=1, font_size=24, font_name='freedom_font')
        cancel_button.background_color = const.SCROLL_BUTTON_BG_COLOR
        cancel_button.bind(on_press=self.on_cancel_pressed)
        layout.add_widget(cancel_button)

        add_button = Button(text='add car', size_hint_y=1, font_size=24, font_name='freedom_font')
        add_button.background_color = const.SCROLL_BUTTON_BG_COLOR
        add_button.bind(on_press=self.on_add_car_pressed)
        layout.add_widget(add_button)

        return layout

    def setup_title(self):
        self.title = "Enter Car Details"
        self.title_font = 'freedom_font'
        self.title_size = 18
        self.title_align = 'center'

    def on_cancel_pressed(self, unused):
        Log.write_debug(DEBUG_CALLING_CLASS, message="cancel clicked")
        self.dismiss()

    def on_add_car_pressed(self, unused):
        Log.write_debug(DEBUG_CALLING_CLASS, message="ok clicked")
        self.dismiss()