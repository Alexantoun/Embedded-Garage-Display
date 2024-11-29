#! /usr/bin/python3

import platform
import threading
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.app import App

from src.database import DatabaseManager
from src.garage_app_main_window import GarageAppMainWindow
from src.debug_logger import DebugLogger

# https://www.amazon.com/Raspberry-Pi-Official-Touch-Screen/dp/B073S3LQ6Q/ref=nav_ya_signin?crid=2MMGMIDHX3QRQ&dib=eyJ2IjoiMSJ9.bBQEIyGCJnigb0-6D3mskXNURpBTy7_AjTA94il-czdRckylDn1-irdO6G1WFiOQ2hQ5xAD6CclYepvAJypf-BoyxBKBQ8Bxrs9wYWOK7z3iSDkE09JUCA_P6MKDqaEoHocEhJ1n470jKKF4D4y2B4_V5yKU9JyEsBeiu_DlaoMN6I-qxc_reJAdROMl_7sU7KTfUY7y6jjT-qf3OMJ5RJBGJDmJEerzt7zosT8jIZE.Em3QXw_dBLfUh05jauV6tnR-l5a2cfXpOstFY4wcKak&dib_tag=se&keywords=raspberry+pi+touch+screen&qid=1724555264&sprefix=raspberry+pi+touch+screen%2Caps%2C105&sr=8-9

RBPi_SCREEN_WIDTH_px: int = 1024
RBPi_SCREEN_HEIGHT_px: int = 600


def is_running_on_rpi() -> str:
    info = platform.uname()
    return '1' if (('arm' in info.machine) or ('aarch' in info.machine)) \
        else '0'

class GarageAppEntryPoint(App):
    def build(self):
        DebugLogger.write_debug('garage_app_entry_point', 'Program started')

        load_database_thread = threading.Thread(target=DatabaseManager.read_car_data)
        load_database_thread.start()

        Config.set('graphics', 'width', RBPi_SCREEN_WIDTH_px)
        Config.set('graphics', 'height', RBPi_SCREEN_HEIGHT_px)

        config_borderless_fullscreen: str
        config_borderless_fullscreen = is_running_on_rpi()

        Config.set('graphics', 'fullscreen', config_borderless_fullscreen)
        Config.set('graphics', 'borderless', config_borderless_fullscreen)

        LabelBase.register(name='pricedown_bl', fn_regular='assets/font/pricedown bl.otf')

        Config.write()
        return GarageAppMainWindow()


if __name__ == '__main__':
    try:
        GarageAppEntryPoint().run()

        print('TODO:\n\tDay_widget should contain its own day to search for the data table\n\t'              
              'Sidebar widgets can start being made\n\t'
              'day_widgets should show any events on that day\n\t'
              'day_widgets on click should show the events details for that day\n\t')

    except Exception as exception:
        DebugLogger.write_debug('garage_app_entry_point', f'Fatal error encountered:\n\t{exception}')
    finally:
        DebugLogger.write_debug('garage_app_entry_point', 'Program closed')
        DebugLogger.close()
