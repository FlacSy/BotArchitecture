import configparser

config = configparser.ConfigParser()

config.read('config\settings.ini')

LOG_DIR = config.get('Loging', 'LOG_DIR')