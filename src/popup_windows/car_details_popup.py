from src.debug_logger import DebugLogger as Log

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

DEBUG_CALLING_CLASS = "CarDetailsPage"

class CarDetailsPage(Popup):
    def __init__(self, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, message='Creating Car Details page')
        super(CarDetailsPage, self).__init__(**kwargs)
        self.setup_title()
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {'top': 1}
        layout = BoxLayout(orientation='vertical')

    def setup_title(self):
        self.title = "Select Car to View Details"
        self.title_font = 'pricedown_bl'
        self.title_size = 22
        self.title_align = 'center'
