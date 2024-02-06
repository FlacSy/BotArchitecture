import configparser

config = configparser.ConfigParser()

config.read('config\secrets.ini')

BOT_TOKEN = config.get('Bot', 'BOT_TOKEN')