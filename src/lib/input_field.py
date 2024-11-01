from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')  # Must be before importing anything else
import src.constants as const
from kivy.uix.textinput import TextInput


class InputField(TextInput):
    def __init__(self, hint_text: str
                 , font_size: int = 24
                 , allow_alphabetical: bool = True
                 , allow_numerical: bool = True
                 , **kwargs):

        super(InputField, self).__init__(**kwargs)
        self.multiline = False
        self.hint_text = hint_text
        self.size_hint_y = None
        self.height = 35
        self.font_size = font_size
        self.font_name = 'pricedown_bl'
        self.halign = 'center'
        self.background_color = const.LIGHTER_DAY_WIDGET_COLOR
        self.padding = [0, 3, 0, 3]

        self.allow_alphabetical = allow_alphabetical
        self.allow_numerical = allow_numerical

    def insert_text(self, substring, from_undo=False):
        if substring.isalpha() and self.allow_alphabetical:
            return super().insert_text(substring)

        if substring.isdigit() and self.allow_numerical:
            return super().insert_text(substring)
