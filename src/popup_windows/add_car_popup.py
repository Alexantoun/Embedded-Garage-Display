from src.debug_logger import DebugLogger as Log
from src.lib.list_wdget import ListWidget
from kivy.uix.popup import Popup

from kivy.uix.label import Label  # used for testing Delete

DEBUG_CALLING_CLASS = "AddCarPage"
class AddCarPage(Popup):
    def __init__(self, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, message="Creating AddCar popup page")
        super(AddCarPage, self).__init__(**kwargs)
        self.setup_title()
        self.size_hint = (0.5, 1)

        self.list_widget = ListWidget(called_from='AddCarPage')
        self.add_widget(self.list_widget)

        # placeholder for widget
        for i in range(0, 100):
            self.list_widget.add_list_widget_item(Label(text=str(i), height=25))

    def setup_title(self):
        self.title = "Enter Car Details"
        self.title_font = 'freedom_font'
        self.title_size = 18
        self.title_align = 'center'