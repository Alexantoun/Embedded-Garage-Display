from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock') #Must be before importing anything else
import src.constants as const
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

class InputField(TextInput):
    def __init__(self, hint_text: str, **kwargs):
        super(InputField, self).__init__(**kwargs)
        self.multiline = False
        self.hint_text = hint_text
        self.size_hint_y = None
        self.height = 30
        self.font_size = 24
        self.font_name = 'freedom_font'
        self.halign = 'center'
        self.padding = [0, 3, 0, 3]
        self.background_color = const.LIGHTER_DAY_WIDGET_COLOR

    def insert_text(self, substring, from_undo=False):
        return super().insert_text(substring if substring.isalpha() or substring == ' ' else '')