from src.debug_logger import DebugLogger as Log
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label  #For testing
from src.database import DatabaseManager

DEBUG_CALLING_CLASS = "CarDetailsPage"

MAX_CARS_IN_ROW = 4

# class CarSelectionIconLabel(BoxLayout):
#     def __init__(self, image=None, text=""):
#         self.orientation = 'vertical'
#         self.text = text
#         self.image = image
        # self.add_widget() #Make an image widget or something to show an icon

        # self.add_widget() #Make a text widget or something to show text

    # def on_touch_up(self, touch):
    #     print(f'{self.text} was clicked')

class CarDetailsPage(Popup):
    def __init__(self, **kwargs):
        Log.write_debug(DEBUG_CALLING_CLASS, message='Creating Car Details page')
        super(CarDetailsPage, self).__init__(**kwargs)
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {'top': 1}

        self.setup_title()
        self.rows = BoxLayout(orientation='vertical')
        self.add_widget(self.rows)
        self.populate_car_details()

    def populate_car_details(self):
        cars_count = 0
        for car in DatabaseManager.car_data.sections():
            if cars_count % MAX_CARS_IN_ROW == 0:
                print("adding row")
                layout = BoxLayout(orientation='horizontal')
                self.rows.add_widget(layout)

            print("Adding label", car.title())
            layout.add_widget(Label(text=car.title(), font_size=22))
            cars_count += 1
            self.ids[car.title()] = ""

    def setup_title(self):
        self.title = "Select Car to View Details"
        self.title_font = 'pricedown_bl'
        self.title_size = 22
        self.title_align = 'center'