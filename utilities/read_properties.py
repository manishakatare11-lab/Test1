## read data from config.ini file

import configparser
import os

config = configparser.RawConfigParser()
# Project root tak jao (LearnProject)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

config_path = os.path.join(BASE_DIR, "config.ini")

print("Config Path:", config_path)       # debug
print("File Exists:", os.path.exists(config_path))  # debug

config.read(config_path)

print("Sections:", config.sections())

#


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_login():
        invalid_login = config.get('admin login info', 'invalid_password')
        return invalid_login

    


