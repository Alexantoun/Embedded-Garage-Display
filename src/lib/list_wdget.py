from src.debug_logger import DebugLogger as Log

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

LIST_WIDGET_VERTICAL_PADDING = [0, 20, 0, 20]
DEBUG_CALLING_CLASS = 'ListWidget'
class ListWidget(ScrollView):
    def __init__(self, called_from: str, **kwargs):
        super(ListWidget, self).__init__(**kwargs)
        self.called_from = called_from
        self.orientation = 'vertical'
        self.bar_width = 15
        Log.write_debug(DEBUG_CALLING_CLASS+called_from, message='Initializing ListWidget')
        layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5, padding=LIST_WIDGET_VERTICAL_PADDING)

        layout.bind(minimum_height=layout.setter('height')) #allows layout to grow as widgets are added
        self.layout = layout
        self.add_widget(layout)
        self.widget_count = 0

    def add_list_widget_item(self, new_widget):
        Log.write_debug(DEBUG_CALLING_CLASS+self.called_from, message=f'Added widget. Widget count = {self.widget_count}')
        self.layout.add_widget(new_widget)
        self.widget_count += 1
