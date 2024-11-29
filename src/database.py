import configparser
from src.lib.list_wdget import ListWidget
from src.debug_logger import DebugLogger as log

DEBUG_CALLING_CLASS = 'database_manager'


class DatabaseManager:
    car_data = configparser.ConfigParser()

    @staticmethod
    def add_car_data(new_car_data: ListWidget): #This should append new car data to car_data, then write it
        section_name = new_car_data.ids['nickname'].text
        DatabaseManager.car_data.add_section(section_name)

        for key, value in new_car_data.ids.items():
            DatabaseManager.car_data[section_name][key] = value.text
            print(f'{key} = {new_car_data.ids[key].text}')

        with open('data.ini', 'w') as configfile:
            DatabaseManager.car_data.write(configfile)
            configfile.close()

    @staticmethod
    def read_car_data():
        DatabaseManager.car_data.read('data.ini')
        log.write_debug(DEBUG_CALLING_CLASS, message=f'loaded from database: {DatabaseManager.car_data.sections()}')
