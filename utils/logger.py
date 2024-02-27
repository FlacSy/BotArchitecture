import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config.config_manager import ConfigManager

class Logger:
    def __init__(self, log_file_name='log.log', log_level=logging.INFO):
        """
        - log_file_name принимает тип данных str, отвечает за имя файла с логами, по умолчанию "log.log"
        - log_level определяет уровень логированания, по умолчанию "INFO"
        """
        config_manager = ConfigManager()
        log_dir = config_manager.get_config_value('Logging', 'LoggingDir')
        self.log_file_path = os.path.join(log_dir, log_file_name)
        
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = TimedRotatingFileHandler(self.log_file_path, when='midnight', interval=2, backupCount=5, encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_exception(self, exception, extra_info=''):
        self.logger.exception(f'{extra_info}Exception: {exception}')
