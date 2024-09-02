#! /usr/bin/python3

from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.app import App
from src.garage_app_main_window import GarageAppMainWindow
from src.debug_logger import DebugLogger

# https://www.amazon.com/Raspberry-Pi-Official-Touch-Screen/dp/B073S3LQ6Q/ref=nav_ya_signin?crid=2MMGMIDHX3QRQ&dib=eyJ2IjoiMSJ9.bBQEIyGCJnigb0-6D3mskXNURpBTy7_AjTA94il-czdRckylDn1-irdO6G1WFiOQ2hQ5xAD6CclYepvAJypf-BoyxBKBQ8Bxrs9wYWOK7z3iSDkE09JUCA_P6MKDqaEoHocEhJ1n470jKKF4D4y2B4_V5yKU9JyEsBeiu_DlaoMN6I-qxc_reJAdROMl_7sU7KTfUY7y6jjT-qf3OMJ5RJBGJDmJEerzt7zosT8jIZE.Em3QXw_dBLfUh05jauV6tnR-l5a2cfXpOstFY4wcKak&dib_tag=se&keywords=raspberry+pi+touch+screen&qid=1724555264&sprefix=raspberry+pi+touch+screen%2Caps%2C105&sr=8-9

RBPi_SCREEN_WIDTH_px: int = 800
RBPi_SCREEN_HEIGHT_px: int = 480


class GarageAppEntryPoint(App):
    def build(self):
        DebugLogger.write_debug('garage_app_entry_point', 'Program started')

        Config.set('graphics', 'width', RBPi_SCREEN_WIDTH_px)
        Config.set('graphics', 'height', RBPi_SCREEN_HEIGHT_px)
        Config.set('graphics', 'fullscreen', '0')
        Config.set('graphics', 'borderless', '0')

        LabelBase.register(name='freedom_font', fn_regular='assets/font/Freedom-10eM.ttf')

        Config.write()
        return GarageAppMainWindow()


if __name__ == '__main__':
    try:
        GarageAppEntryPoint().run()
        print('TODO:\n\tDay_widget should contain its own day to search for the data table\n\t'
              'The font sucks on a small screen\n\t'
              'Sidebar widgets can start being made\n\t'
              'Design + implement database for events\n\t'
              'day_widgets should show any events on that day\n\t'
              'day_widgets on click should show the events details for that day')
    except Exception as exception:
        DebugLogger.write_debug('garage_app_entry_point', f'Fatal error encountered:\n\t{exception}')
    finally:
        DebugLogger.write_debug('garage_app_entry_point', 'Program closed')
        DebugLogger.close()
