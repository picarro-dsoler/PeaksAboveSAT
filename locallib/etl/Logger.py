import logging

class Loggers:
    def __init__(self, logger_name='Logger', level=logging.INFO, keys=['File']):
        self.logger_name = logger_name
        self.loggers = {}
        for key in keys:
            self.add_logger(key, level)

    def add_logger(self, logger_subname, level=logging.INFO):
        self.loggers[logger_subname] = logging.getLogger( f'{self.logger_name}_{logger_subname}')
        self.loggers[logger_subname].setLevel(level)
        setattr(self, logger_subname, self.loggers[logger_subname])

    def add_handler(self, handler):
        self.logger.addHandler(handler)

    def remove_handler(self, handler):
        self.logger.removeHandler(handler)
        return self.logger

    def clear_handlers(self):
        for logger in self.loggers.values():
            logger.handlers.clear()
        return self

    def set_level(self, level):
        self.logger.setLevel(level)

    def get_logger(self):
        return self.logger
    
    def info(self, message):
        for logger in self.loggers.values():
            logger.info(message)
        return self
    def error(self, message):
        for logger in self.loggers.values():
            logger.error(message)
        return self
    def warning(self, message):
        for logger in self.loggers.values():
            logger.warning(message)
        return self