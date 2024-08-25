from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color


class ColoredLabel(Label):
    def __init__(self, bg_color, text, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        self.text = text
        self.color = (0, 0, 0)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)
        print(bg_color)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

