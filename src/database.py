import configparser

from src.lib.list_wdget import ListWidget

class DatabaseManager:
    @staticmethod
    def write_car_data(car_data: ListWidget):
        config = configparser.ConfigParser()
        data_to_save = {}
        for key, value in car_data.ids.items():
            data_to_save[key] = value.text
            print(f'{key} = {value.text}')

        config[data_to_save['nickname']] = data_to_save
        with open('data.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
