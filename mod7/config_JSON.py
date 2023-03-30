from LevelsToFileHandler import LevelsToFileHandler
from logging.handlers import TimedRotatingFileHandler
from ASCII_Filter import ASCIIFilter
config_by_levels = {
    "version": 1,
    "filters": {
        "ASCIIFilter": {
            "()": ASCIIFilter,
        }
    },
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "http_handler": {
            "()": "logging.handlers.HTTPHandler",
            "host": "localhost:5000",
            "url": "/logs",
            "method": "POST"
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "level": "DEBUG"
        },
        "file": {
            "()": LevelsToFileHandler,
            "level":"DEBUG",
            "formatter":"default",
            "mode":"a"
        },
        "rotating": {
            "()": "logging.handlers.TimedRotatingFileHandler",
            "filename":"utils.log",
            "when":"h",
            "interval": 10,
            "backupCount": 5,
            "level": "INFO",
            "filters": ['ASCIIFilter'],
            "formatter":"default",
        }
    },
    "loggers":{
            "appLogger" :{
                "level": "DEBUG",
                "handlers":["console", "file"]
            },
            "utilsLogger" :{
                "level": "DEBUG",
                "handlers":["console", "file"]
            },
            "unitsFileLogger": {
                "level": "INFO",
                "handlers": ['rotating']
            },
            "httpLogger": {
                "level": "DEBUG",
                "handlers": ['http_handler']
            }
    }
}